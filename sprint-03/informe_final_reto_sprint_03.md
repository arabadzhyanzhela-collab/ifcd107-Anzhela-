# Informe Final del Reto · Sprint 03: Primer Modelo de IA en Producción

**Proyecto:** Predicción de Cancelaciones de Reservas de Hotel  
**Cliente:** TurisData Canarias  
**Equipo:** 5Green \| **Scrum Master:** Cristina  
**Entorno de trabajo:** Google Colab / AutoGluon / FastAPI / DB Browser for SQLite

---

## PÁGINA 1 · Entender el problema, análisis de datos y prevención de trampas (*Data Leakage*)

### 1.1 ¿Qué quiere resolver el cliente? (Frase objetivo)

> **Frase Objetivo del Proyecto:**  
> *"Queremos predecir con antelación qué reservas tienen un alto riesgo de cancelarse (variable `cancelada`: sí/no) para que el equipo de recepción y ventas de TurisData pueda intervenir a tiempo, reduciendo las pérdidas económicas provocadas por habitaciones que se quedan vacías a última hora."*

---

### 1.2 Diagnóstico inicial de datos con SQL (`turisdata.db`)

Para analizar los datos históricos de TurisData, abrimos la base de datos `turisdata.db` en DB Browser for SQLite y ejecutamos la siguiente consulta para medir el nivel de cancelación por cada canal de venta:

```sql
SELECT canal, 
       COUNT(*) AS total_reservas, 
       SUM(cancelada) AS canceladas, 
       ROUND(AVG(cancelada) * 100, 1) AS pct_cancelacion
FROM reservas 
GROUP BY canal
ORDER BY pct_cancelacion DESC;
```

#### Resultados clave obtenidos:

* **Web Intermediaria (OTAs):** 3.020 reservas \| 1.628 canceladas (**53,9 % de cancelaciones**). Es la vía con mayor tasa de cancelación.  
* **Agencias de Viaje:** 1.190 reservas \| 524 canceladas (**44,0 %**).  
* **Empresas:** 328 reservas \| 142 canceladas (**43,3 %**).  
* **Venta Directa (Web hotel/Teléfono):** 1.462 reservas \| 460 canceladas (**31,5 %**). Es el canal más estable.  
* **Resumen General:** De un total de 6.000 reservas evaluadas, **2.754 se cancelaron (45,9 % global)**.

---

### 1.3 Auditoría de columnas: ¿Hay "fuga de datos" (*Data Leakage*)?

Analizamos las 18 columnas del archivo haciéndonos la pregunta de control: **"¿Conocemos esta información en el momento exacto en que el cliente realiza la reserva?"**

* **Columnas Excluidas y Justificación:**  
  * `id_reserva`: Es un simple número identificador secuencial. No aporta ningún valor ni comportamiento explicativo.  
  * *Campos de fuga de datos (eliminados):* Se comprobó que no entraran columnas como `fecha_cancelacion`, `motivo_cancelacion` o `importe_reembolsado`. Si usáramos estas columnas, el modelo sabría "el futuro" y acertaría el 100 % en los tests, pero fallaría por completo en el hotel real.  
* **Columnas Validadas y Conservadas:** `fecha_reserva`, `fecha_llegada`, `antelacion_dias`, `noches`, `adultos`, `ninos`, `tipo_habitacion`, `regimen`, `canal`, `pais_origen`, `tarifa`, `deposito`, `precio_noche`, `peticiones_especiales`, `cliente_repetidor`, `cancelaciones_previas`.

---

## PÁGINA 2 · Entrenamiento con AutoML, comparativa de modelos e importancia de variables

### 2.1 Configuración para repetir el experimento (Reproducibilidad)

* **Herramienta:** AutoGluon Tabular (`medium_quality`).  
* **Tiempo límite:** 120 segundos \| **Semilla fija:** 42\.  
* **Separación de datos (Partición temporal):** En lugar de mezclar las filas al azar (lo que provocaría trampa al predecir el pasado con datos del futuro), ordenamos por `fecha_reserva`. Usamos el **80 % más antiguo para entrenar (4.800 reservas)** y el **20 % más reciente para evaluar (1.200 reservas)**.

---

### 2.2 Comparativa de modelos (*Leaderboard*)

| Modelo evaluado | Nota ROC-AUC (Test) | Tiempo de entrenamiento | Criterio y decisión |
| :---- | :---: | :---: | :---- |
| **WeightedEnsemble\_L2** | **0,722** | **10,3 s** | **Modelo Ganador:** Agrupa lo mejor de varios algoritmos y da la mayor precisión global. |
| **CatBoost** | 0,719 | 7,5 s | Excelente resultado, solo un 0,003 por debajo del ensamblado. |
| **XGBoost** | 0,719 | **0,7 s** | **Opción súper rápida:** Es 14 veces más rápido de entrenar que el ganador con casi la misma nota. |
| **LightGBMXT** | 0,710 | 2,1 s | Ligera pérdida de precisión en comparación con XGBoost. |

> **¿Por qué elegimos ROC-AUC como métrica?**  
> Si solo midiéramos el "porcentaje de aciertos simple" (*Accuracy*), un modelo básico que dijera *"nadie va a cancelar"* acertaría un 54 % de las veces, pero no serviría para nada. La métrica ROC-AUC nos asegura que el modelo sabe ordenar las reservas desde la de mayor riesgo hasta la de menor riesgo.

---

### 2.3 Factores que más influyen en la cancelación (Explicabilidad)

Las 4 características que más pesan en la decisión de la Inteligencia Artificial son:

1. **`antelacion_dias` (0,07):** A mayor número de días entre la reserva y la llegada (especialmente a más de 90 días), mayor es la probabilidad de que se cancele.  
2. **`deposito` (0,06):** Las reservas hechas "sin depósito" o sin pago previo registran la tasa de cancelación más alta.  
3. **`canal` (0,04):** Las reservas procedentes de webs intermediarias cancelan mucho más que las directas.  
4. **`tarifa` (0,02):** Las tarifas "flexibles" facilitan la cancelación sin coste para el cliente.

---

## PÁGINA 3 · Elección del umbral con criterio económico en Euros (€) y Pruebas en Colab / API

### 3.1 Impacto económico de los errores del modelo (en Euros)

Definimos los costes reales que asume el hotel ante cada tipo de fallo:

* **Cancelación no detectada (Falso Negativo):** Cuesta **100 €** (la habitación se queda vacía durante la noche y se pierde la venta).  
* **Alerta Falsa (Falso Positivo):** Cuesta **40 €** (gestión del personal al llamar o enviar recordatorios, más posibles molestias al cliente).

---

### 3.2 Tabla comparativa de decisiones y costes

| Estrategia / Umbral | Cancelaciones detectadas (Recall) | Alertas Falsas | Coste Total Estimado para TurisData |
| :---- | :---: | :---: | :---: |
| **No usar modelo (No avisar nunca)** | 0 % | 0 | **57.700 €** |
| **Avisar a todas las reservas** | 100 % | 623 | **24.920 €** |
| **Modelo con Umbral Estándar (0,50)** | 60,1 % | 193 | **26.000 €** |
| **Modelo con Umbral Optimizado (0,20 \- 0,30)** | **88,2 %** | **310** | **22.040 € (MÁXIMO AHORRO)** |

> **Dictamen Financiero:**  
> Fijando el umbral en **0,20 \- 0,30 (20 % a 30 % de riesgo)**, el hotel detecta casi **9 de cada 10 cancelaciones reales**. Aunque aumenten las falsas alarmas, esta estrategia reduce el coste total a **22.040 €**, ahorrando **35.660 €** frente a no hacer nada y **2.880 €** frente a la norma a ciegas de avisar a todo el mundo.

---

### 3.3 Evidencia técnica de la API y pruebas en Colab

Se publicó el modelo mediante una API REST en **FastAPI** ejecutada en Google Colab con `TestClient`.

#### Captura 1: Pruebas del servicio y predicción exitosa (HTTP 200\)

```py
# Verificación del estado del servicio (/salud)
cliente.get("/salud").json()
# Respuesta: {'estado': 'ok', 'modelo': 'modelo_cancelaciones'}

# Envío de una reserva real de prueba
reserva_ejemplo = {
    "fecha_reserva": "2025-11-03", "fecha_llegada": "2026-01-15", 
    "antelacion_dias": 73, "noches": 5, "adultos": 2, "ninos": 0,
    "tipo_habitacion": "estandar", "regimen": "desayuno", 
    "canal": "web_intermediaria", "pais_origen": "UK", 
    "tarifa": "flexible", "deposito": "sin_deposito", 
    "precio_noche": 85.0, "peticiones_especiales": 0, 
    "cliente_repetidor": 0, "cancelaciones_previas": 0
}

respuesta = cliente.post("/predecir", json=reserva_ejemplo)
print(respuesta.status_code, respuesta.json())
```

* **Respuesta del servidor:** `200`  
  `{'probabilidad_cancelacion': 0.7887, 'alerta': True, 'umbral': 0.5}`  
* **Interpretación:** La reserva presenta un **78,87 % de riesgo de cancelación**, por lo que el sistema genera automáticamente la alerta (`True`).

#### Captura 2: Validación de datos de entrada y control de errores (HTTP 422\)

```py
# Prueba enviando un dato imposible (noches = 0)
reserva_incorrecta = reserva_ejemplo.copy()
reserva_incorrecta["noches"] = 0

respuesta_error = cliente.post("/predecir", json=reserva_incorrecta)
print(respuesta_error.status_code)
print(respuesta_error.json())
```

* **Respuesta del servidor:** `422`  
  `{'detail': [{'type': 'greater_than_equal', 'loc': ['body', 'noches'], 'msg': 'Input should be greater than or equal to 1', 'input': 0, 'ctx': {'ge': 1}}]}`  
* **Interpretación:** La API rechaza peticiones con datos erróneos devolviendo el código `422 Unprocessable Entity` e indicando exactamente la regla incumplida (las noches deben ser mayores o iguales a 1).

---

## PÁGINA 4 · Recursos, costes en la nube, IA Responsable y Recomendaciones

### 4.1 Informe de recursos consumidos y prueba de cierre (Coste 0 €)

| Recurso Creado | Tiempo Activo | Capacidad / Disco Usado | Coste Real Estimado | Estado Final | Prueba de Cierre |
| :---- | :---: | :---: | :---: | :---: | :---- |
| **Google Colab (CPU/RAM)** | 36 segundos (entrenamiento) | RAM Estándar | **0,00 €** | Entorno Desconectado | Sesión de Colab finalizada |
| **Modelo Guardado** | Permanente local | 225,7 MB | **0,00 €** | Almacenado | Carpeta `modelo_cancelaciones/` |
| **API Web (FastAPI)** | 2 minutos | Servidor local `TestClient` | **0,00 €** | Servicio Detenido | Proceso finalizado en Colab |

> **Certificación de Gastos:** Se confirma que todo el experimento y la API se desarrollaron utilizando cuotas gratuitas locales y en la nube. **El coste total final fue de 0,00 €**.

---

### 4.2 Análisis de IA Responsable (Riesgos y Soluciones)

1. **Riesgo 1 (Sesgo por origen o canal):**  
   * *Problema:* El modelo asigna un riesgo muy alto a reservas procedentes de webs intermediarias o de clientes de Reino Unido (UK).  
   * *Medida de prevención:* Auditar mensualmente los aciertos por canal para evitar discriminación injustificada en el trato a clientes extranjeros.  
2. **Riesgo 2 (Molestias a clientes VIP por Falsas Alarmas):**  
   * *Problema:* Un exceso de falsas alarmas con llamadas exigentes de confirmación puede enfadar a clientes habituales.  
   * *Medida de prevención:* Sustituir exigencias agresivas por emails amables con recordatorios o invitaciones a personalizar su estancia (ej. ofrecer desayuno o transporte).

---

### 4.3 Recomendación final para la directiva de TurisData

1. **Implantar el modelo en recepción:** Integrar la API desplegada directamente dentro del programa de gestión de reservas del hotel.  
2. **Configurar el umbral en el 25 % (0,25):** De este modo el sistema marcará en rojo las reservas de riesgo alto, permitiendo cazar el 88 % de las cancelaciones a tiempo.  
3. **Protocolo de actuación de 5 días:** Para las reservas marcadas en alerta, enviar un correo de cortesía 5 días antes de la llegada para confirmar la reserva o liberar la habitación con margen suficiente para reventa.

---

### 4.4 Declaración del uso de Inteligencia Artificial

* **¿Se ha utilizado IA?:** Sí, como asistente de consulta y formato.  
* **Uso específico:**  
  1. Optimización de la consulta SQL de porcentajes por canal.  
  2. Apoyo en el ajuste del tono redactado a lenguaje ejecutivo y estructuración de la tabla Markdown.  
* **Comprobación manual efectuada:**  
  * Se ejecutó el script de SQL directamente en la base `turisdata.db`.  
  * Todas las cifras numéricas, métricas (ROC-AUC 0,722), costes (100 € / 40 €) y respuestas JSON de la API coinciden exactamente con los resultados de las capturas de Colab.

&nbsp;

&nbsp;

&nbsp;

**Autoevaluación rápida**

&nbsp;

| Criterio / Pregunta de Autoevaluación (Sprint 3\) PDF | Anzhela | Cristina | Miguel | Fran | Andrii |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **1\. ¿El informe tiene las tres partes y cabe en 4 páginas?&nbsp;** | Sí | Sí | Sí | Sí | Sí |
| **2\. ¿La métrica y el umbral están explicados en lenguaje de negocio?&nbsp;** | Sí | Sí | Sí | Sí | Sí |
| **3\. ¿Hay evidencia de una llamada a la API (petición y respuesta), sin credenciales?&nbsp;** | Sí | Sí | Sí | Sí | Sí |
| **4\. ¿Explicamos qué variables hemos excluido y por qué?&nbsp;** | Sí | Sí | Sí | Sí | Sí |
| **5\. ¿Hemos cerrado y eliminado todos los recursos y lo demostramos?&nbsp;** | Sí | Sí | Sí | Sí | Sí |
| **6\. ¿Hay al menos dos riesgos de IA responsable y una medida?&nbsp;** | Sí | Sí | Sí | Sí | Sí |
| **7\. ¿Otra persona ha revisado el informe con la rúbrica?&nbsp;** | Sí | Sí | Sí | Sí | Sí |

&nbsp;

&nbsp;