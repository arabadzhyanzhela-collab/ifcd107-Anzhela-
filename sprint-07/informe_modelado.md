# Informe de modelado · Sprint 7 · «Precio y cancelación»

**Equipo 5 Green** · Cristina, Miguel, Fran, Andri y Anzhela · Cliente: TurisData
Cuaderno: `reto_S07.ipynb` · Semilla: `SEMILLA = 42` · Datos: `reservas_turisdata.csv` (6 000 reservas **sintéticas** de un solo hotel)

> **Cifras:** todas salen de `reto_S07.ipynb` (celda 5 las reúne en `cifras_informe.json`). Los costes en euros son **hipótesis del equipo** (apartado 5), no datos del hotel.

---

## 1 · Resumen para el gerente

1. **Tarifa de referencia.** Con solo el tipo de habitación y la época, el modelo acierta el precio por noche con un error medio de **6,76 €** (lo normal sin modelo sería equivocarse en 25,56 €). Una estándar cuesta ≈ **67 €** en temporada baja; la suite, unos **101 € más**; la temporada alta suma ≈ **22 €**.
2. **Aviso de cancelación.** Si dejamos todo como está («no hacer nada») y las cancelaciones que no vemos nos cuestan 150 € cada una, en 1 200 reservas perderíamos **82.650 €**. Con el aviso del modelo y el umbral elegido (0,32) el coste esperado baja a **38.775 €**: un ahorro de **43.875 €** (≈ **36.562 € por cada 1 000 reservas**).
3. **Qué hacer.** Usar el aviso para decidir cuántas reservas aceptar de más, **sin pasarse**: el aviso detecta el **85 %** de las cancelaciones, pero **43 % de las alarmas son falsas**, y cada falsa alarma puede acabar en un cliente reubicado (≈ 75 € esperados). Detalle y límites en los apartados 6 y 7.

---

## 2 · Variables usadas y excluidas (sin fuga de datos)

Solo se usan variables **conocidas en el momento de reservar**.

| Modelo | Variables usadas | Variables excluidas y por qué |
|---|---|---|
| **Precio** | `tipo_habitacion`, `temporada_alta` (derivada del mes de `fecha_llegada`) | `cancelada` (es el desenlace; **nunca** se usa para predecir el precio), `id_reserva`, fechas crudas, y el resto de columnas (el cliente pidió una tarifa por tipo y época) |
| **Cancelación** | `antelacion_dias`, `noches`, `adultos`, `ninos`, `precio_noche`, `peticiones_especiales`, `cliente_repetidor`, `cancelaciones_previas`, `temporada_alta`, `tipo_habitacion`, `regimen`, `canal`, `pais_origen`, `tarifa`, `deposito` | `cancelada` (objetivo), `id_reserva`, `fecha_reserva`, `fecha_llegada` |

**Aviso:** `peticiones_especiales` podría registrarse *después* de reservar. Se comprobó que quitarla casi no cambia el modelo (AUC en validación cruzada 0,758 con ella frente a 0,755 sin ella), así que el riesgo de fuga es pequeño; si el hotel confirma que no se conoce al reservar, se elimina.

---

## 3 · Modelo de precio (regresión)

Partición 80 % / 20 % (`random_state=42`). Máximo 3 modelos: referencia, lineal y una mejora.

| Modelo (test, 1 200 reservas) | MAE (€) | RMSE (€) | R² |
|---|---|---|---|
| Referencia: precio medio de entrenamiento | 25,56 | 33,33 | ≈ 0,00 |
| Regresión lineal | 7,24 | 9,70 | 0,915 |
| Lineal + interacciones | **6,76** | **8,94** | **0,928** |

- **Cómo se lee:** MAE = error medio en euros por noche; el RMSE castiga más los errores grandes (sobre todo en las suites).
- **¿Compensa la complejidad?** La mejora de las interacciones es modesta (**0,48 € por noche**, R² de validación cruzada 0,926 → 0,934), pero no cuesta nada explicarla (siguen siendo solo 2 variables), así que se usa para la tarifa. La lineal es igual de válida si se prefiere lo más simple.
- **Tarifa de referencia (€ por noche, modelo con interacciones):**

| Tipo | Temporada baja | Temporada alta | Recargo |
|---|---|---|---|
| Estándar | 70 | 87 | 17 |
| Superior | 95 | 119 | 24 |
| Familiar | 110 | 137 | 27 |
| Suite | 161 | 198 | 37 |

---

## 4 · Modelo de cancelación (clasificación)

Tasa de cancelación: **45,9 %**. Partición 80 % / 20 % estratificada. El modelo y el umbral se eligen **solo con validación cruzada en train**; el test se usa una vez (apartado 5).

| Modelo | AUC (validación cruzada) | AP (validación cruzada) | AUC test | AP test |
|---|---|---|---|---|
| Referencia: «siempre no cancela» | 0,500 | 0,459 | — | — |
| Regresión logística | **0,758** | **0,719** | 0,746 | 0,729 |
| k-NN (k = 201, extra) | 0,734 | 0,689 | 0,727 | 0,704 |

**Sin jerga:** el **AUC** responde «si cojo una reserva que cancela y otra que no, ¿cuántas veces el modelo da más riesgo a la que cancela?»: 75 % de las veces (50 % sería azar). La **AP** resume cuánto se mantiene la precisión al ir detectando más cancelaciones. La logística gana a k-NN y a la referencia y además se puede explicar.

**Por qué no basta la exactitud:** el modelo «siempre no cancela» acierta el 54,1 % de las reservas y **no detecta ninguna cancelación** (recall 0 %).

**Matriz de confusión en test (1 200 reservas, 551 canceladas):**

| Umbral | Cancelaciones detectadas (recall) | Alarmas acertadas (precisión) | No detectadas (FN) | Falsas alarmas (FP) |
|---|---|---|---|---|
| 0,50 | 62 % | 66 % | 211 | 178 |
| **0,32 (elegido)** | **85 %** | **57 %** | **81** | **355** |

---

## 5 · Hipótesis de coste, umbral y sensibilidad

**Hipótesis de coste (del equipo; referencia: precio medio ≈ 103 €/noche, estancia media ≈ 5,5 noches):**

- **`COSTE_FN` = 150 €** — *cancelación que no detectamos.* La habitación queda vacía y solo se logra revender una parte de las noches: ≈ 1,5 noches medias sin ingresar.
- **`COSTE_FP` = 75 €** — *falsa alarma.* Aceptamos una reserva de más y el cliente sí llega: reubicarlo cuesta ≈ 1,5 noches medias (≈ 150 €), pero solo ocurre si el hotel está realmente lleno; suponemos que la mitad de las veces → ≈ 75 € esperados.

**Umbral elegido: 0,32.** Se probaron umbrales de 0,05 a 0,95 con validación cruzada en train y se tomó el de menor `FN × COSTE_FN + FP × COSTE_FP`. Coincide con la regla teórica `COSTE_FP / (COSTE_FP + COSTE_FN)` = 0,33.

**Resultado en test (una sola vez, 1 200 reservas):**

| Escenario | Coste total | Coste por 1 000 reservas | Ahorro frente a no hacer nada |
|---|---|---|---|
| Sin modelo (no hacer nada) | 82.650 € | 68.875 € | — |
| Umbral 0,50 | 45.000 € | 37.500 € | 37.650 € |
| **Umbral 0,32** | **38.775 €** | **32.312 €** | **43.875 €** |

El umbral elegido ahorra además **6.225 €** frente al umbral por defecto (0,5).

**Análisis de sensibilidad** (validación cruzada en train; se repite la búsqueda del umbral con otros costes):

| Escenario | COSTE_FN | COSTE_FP | Umbral óptimo | Ahorro frente a no hacer nada (€ por 1 000 reservas) |
|---|---|---|---|---|
| Base | 150 | 75 | 0,32 | 38.281 |
| FN el doble | 300 | 75 | 0,17 | 101.641 |
| FN la mitad | 75 | 75 | 0,49 | 11.250 |
| FP el doble | 150 | 150 | 0,49 | 22.500 |
| FP la mitad | 150 | 37,5 | 0,17 | 50.820 |
| Ambos el doble | 300 | 150 | 0,32 | 76.563 |

**Cómo leerlo:** el umbral solo depende de la *proporción* entre los dos costes. Cuanto más cara es una cancelación no detectada frente a una falsa alarma, **más bajo** el umbral (se avisa más). Si ambas cuestan casi lo mismo (FN ≈ FP), el umbral vuelve a ≈ 0,5 y el ahorro cae a 11.250 €–22.500 € por 1 000 reservas. **En todos los escenarios el modelo sigue ahorrando dinero.**

---

## 6 · Recomendación de negocio

**Acción:** usar el aviso de riesgo con el umbral **0,32** (marcar como «probable cancelación» toda reserva con riesgo ≥ 32 %) para decidir cuántas reservas se aceptan por encima de la capacidad, empezando con un **piloto prudente** (por ejemplo, en temporada alta).

**Cifras:**
- Ahorro estimado frente a no hacer nada: **43.875 € en 1 200 reservas** (≈ 36.562 € por 1 000). Con el ritmo del CSV (≈ 2 000 reservas al año) el orden de magnitud sería ≈ **70 000 € al año**.
- Por temporada, el aviso rinde más en **alta** (≈ 41.681 € por 1 000 reservas) que en **baja** (≈ 31.427 €), porque se cancela más y hay menos margen de error.
- Si el coste real de una cancelación no detectada **se acerca al de una falsa alarma**, el umbral correcto sube hacia 0,5 y el ahorro baja a ≈ 11 000–23 000 € por 1 000 reservas.

**La recomendación cambiaría si…** una reubicación costara mucho más de lo supuesto (> 150 € de coste esperado por falsa alarma): habría que subir el umbral y hacer menos overbooking. **Para afinarla haría falta:** el coste real de reubicar a un cliente, la proporción de noches que se logran revender tras una cancelación y la capacidad diaria del hotel.

**Límites:**
- Datos **sintéticos de un solo hotel**: las cifras sirven para decidir *cómo* trabajar, no como previsión financiera.
- Los costes son **hipótesis**; el ahorro depende directamente de ellas.
- Con el umbral 0,32 se marca como «cancelará» una parte muy grande de las reservas (el 70 % aprox.), porque la tasa base ya es del 46 %: el aviso sirve para **ordenar el riesgo** y calcular cuántas habitaciones sobrevender, no para actuar reserva a reserva.
- El AUC de 0,75 es útil pero no perfecto: seguirán existiendo errores en ambos sentidos.

---

## 7 · IA responsable

- **¿Quién sufre los falsos positivos?** El cliente que **sí viene** y es marcado como «probable cancelación»: con overbooking es quien puede quedarse sin habitación y ser **reubicado**. Con el umbral 0,32 hay 355 casos así en 1 200 reservas.
- **¿Se penaliza a algún canal o país?** Se midió con validación cruzada en train (celda 4.7). Entre los clientes que sí vienen, se marca por error al **71 %** de los de **web_intermediaria** frente al **29 %** de los de **directo** (brecha de 41,4 puntos). Por países la brecha es menor (de 43 % en FR a 64 % en las reservas sin país informado: 20,7 puntos). Parte de la diferencia es real (algunos canales cancelan más), pero el efecto práctico es que **unos grupos soportan más falsas alarmas que otros**.
- **¿Y si se piden depósitos solo a ciertos clientes?** No lo recomendamos: usar el aviso para exigir depósitos o penalizar a un canal o país concreto trasladaría el error del modelo al cliente. El aviso se usa a nivel de **habitaciones por fecha** (cuánto sobrevender), no para tratar peor a una persona.
- **Medidas propuestas:** (1) pactar de antemano una **compensación** para el cliente reubicado (hotel equivalente, transporte, descuento); (2) **monitorizar la tasa de falsos positivos por canal y país** cada trimestre; (3) reentrenar con datos reales del hotel; (4) no usar la nacionalidad como criterio de decisión.
- **Datos sintéticos:** estos riesgos se han medido sobre datos de prueba; con clientes reales habría que repetirlo antes de decidir nada.

---

## Revisión con la rúbrica

| Criterio | Nivel (1–4) | Prueba (una frase) | Revisó |
|---|---|---|---|
| Corrección técnica | 4 | `reto_S07.ipynb` aplica un pipeline sin data leakage y ajusta el umbral mediante validación cruzada en *train*. | Anzhela |
| Reproducibilidad | 4 | Al ejecutar "Reiniciar y ejecutar todo" en Google Colab se obtienen exactamente las mismas métricas y el archivo `cifras_informe.json`. | Fran |
| Análisis y comunicación al cliente | 4 | El informe traduce las métricas estadísticas a un ahorro económico concreto en euros (43.875 €) con un análisis de sensibilidad completo. | Miguel |
| IA responsable | 4 | Se cuantifica numéricamente la brecha de falsos positivos entre canales (41,4 puntos) y se argumenta éticamente no usar el país para tomar decisiones. | Cristina |

**Mejoras anotadas:** Para próximos entregables, se sugiere añadir una prueba visual interactiva de los costes en función del umbral para facilitar la presentación ejecutiva.