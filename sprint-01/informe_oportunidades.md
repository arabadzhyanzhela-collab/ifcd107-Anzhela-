# Informe de Oportunidades de Inteligencia Artificial

**Cliente:** TurisData Canarias  
**Elaborado por:** Consultora 5Green (Anzhela, Cristina, Miguel, Fran y Andrii)  
**Fecha:** 21 de octubre de 2026  
**Sprint:** 01 — Auditoría de Oportunidades de IA


## 1\. Resumen Ejecutivo

Tras analizar los procesos operativos y la problemática de negocio de TurisData Canarias, hemos identificado 5 oportunidades clave para la aplicación de inteligencia artificial y automatización. Recomendamos comenzar con un **piloto de predicción de cancelaciones de reservas (Caso 1\)**. Esta iniciativa aborda directamente la principal pérdida económica del cliente (21,25 % de cancelaciones generales), utiliza datos tabulares históricos ya existentes y requiere una inversión moderada con un riesgo ético controlable mediante intervención humana.


## 2\. Lo que hemos entendido del cliente

TurisData Canarias gestiona alojamientos y experiencias turísticas con un alto impacto de cancelaciones de última hora que dejan habitaciones vacías sin margen de reasignación. En la entrevista del 16/10, el Director General nos contó que tiene **2.400 cancelaciones** registradas, que sus **datos están incompletos y sin revisar** y que quiere «reducir las cancelaciones, agilizar los trabajos y ofrecer mejor atención al cliente». También propuso un **chat de voz** para automatizar las reservas; lo hemos tenido en cuenta, pero no reduce por sí solo las cancelaciones, por eso no es el piloto recomendado. A partir de los hallazgos del Sprint 0, abordamos nuestra pregunta estratégica priorizada (*How Might We*):

> **HMW Priorizada:** *¿Cómo podríamos anticipar qué reservas tienen un alto riesgo de cancelación para tomar medidas preventivas y proteger el margen de beneficio sin deteriorar la relación con el cliente?*

El cliente busca soluciones realistas con un presupuesto acotado a «15.000 euros» para la fase piloto, que estén listas «antes de la próxima temporada», sin comprometer los datos personales de los huéspedes (cumplimiento estricto de RGPD/AI Act) ni delegar decisiones críticas de forma 100 % autónoma.


## 3\. Tabla de 5 Casos de Uso Evaluados

| Caso de Uso | Problema de Negocio | Modalidad | Tipo de Aprendizaje | Familia de Algoritmos | Datos Necesarios (¿Existen?) | Métrica de Exito |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **1.Predicción de riesgo de cancelación** *(Tarjeta/Propio)* | Habitaciones vacías por cancelaciones imprevistas (pérdida de ingresos). | Tabular (Datos de reserva) | Supervisado | Clasificación (Árboles de decisión / Regresión Logística) | Histórico de reservas, antelación, canal, tarifa, noches . | Precisión y Recall en cancelaciones (F1-Score) / reducción de habitaciones vacías. |
| **2.Resumen y análisis de sentimiento de reseñas** *(Tarjeta)* | Imposibilidad de leer manualmente más de 1.500 reseñas para detectar fallos operativos. | Texto (Lenguaje) | Supervisado / Preentrenado | Procesamiento de Lenguaje Natural (NLP) / Modelos de Lenguaje (LLMs) | Texto de reseñas, puntuaciones pasadas, fecha y alojamiento (**Sí existe**). | Accuracy en detección de sentimiento / Tiempo ahorrado a dirección. |
| **3.Regla de notificación y recordatorios de cancelación gratuita** *(Sin IA / Reglas)* | Falta de contacto previo antes de vencer el plazo de cancelación gratuita, aumentando cancelaciones de última hora. | No aplica (Lógica de negocio) | No aplica (Basado en reglas determinísticas) | Sistema de reglas condicionales (`IF/THEN`) | Fecha de check-in, política de cancelación, email del cliente (**Sí existe**). | % de confirmación previa / Reducción de cancelaciones tras notificación. |
| **4.Agrupamiento y segmentación de huéspedes** *(Propio 1\)* | Desconocimiento del perfil de cliente para personalizar ofertas y promociones de fidelización. | Tabular | No Supervisado | Agrupamiento (Clustering \- K-Means / DBSCAN) | Histórico de consumo, duración de estancia, país/origen, tipo de viaje (**Sí existe**). | Coeficiente Silhouette / % de conversión de campañas dirigidas. |
| **5.Control automático de calidad de fotos de alojamientos** *(Propio 2\)* | Publicación de imágenes de mala calidad o desactualizadas en OTAs que reducen las reservas. | Imagen (Visión por computador) | Supervisado | Redes Convolucionales (CNN) / Clasificación de imagen | Fotografías del catálogo de alojamientos (**Requiere recopilar/etiquetar**). | Accuracy de clasificación de calidad visual / Incremento de clics en anuncios. |


*Nota metodológica:* Los 5 casos cubren 3 modalidades distintas (Tabular, Texto e Imagen) e incluyen 1 caso basado en reglas sin IA para maximizar el criterio técnico y la eficiencia de costes.

---

## 4\. Priorización (Matriz Impacto × Facilidad)

Evaluamos cada caso en una escala del 1 al 5 en dos ejes:

* **Impacto:** Reducción de costes, aumento de ingresos o mejora operativa directa.  
* **Facilidad:** Disponibilidad de datos, baja complejidad técnica y plazo de desarrollo corto.

```
       IMPACTO
          ^
        5 |               [Caso 1: Cancelaciones]
          |
        4 |  [Caso 2: Reseñas]          [Caso 3: Reglas Avisos]
          |
        3 |                             [Caso 4: Segmentación]
          |
        2 |               [Caso 5: Calidad Fotos]
          |
        1 └────────────────────────────────────────────> FACILIDAD
            1      2      3      4      5
```

### Criterio de Priorización:

1. **Caso 1 (Predicción de Cancelaciones) — Prioridad 1:** Alto Impacto (5), Alta Facilidad (4). Los datos ya están recopilados en `turisdata.db` y ataca el problema financiero directo de la empresa.  
2. **Caso 3 (Regla de Recordatorios) — Prioridad 2:** Impacto Medio-Alto (4), Facilidad Máxima (5). Solución rápida, sin coste de modelo de IA, que genera valor inmediato ("quick win").  
3. **Caso 2 (Análisis de Reseñas) — Prioridad 3:** Impacto Alto (4), Facilidad Media (3). Requiere procesamiento de texto y limpieza de PII.  
4. **Caso 4 (Segmentación de Huéspedes) — Prioridad 4:** Impacto Medio (3), Facilidad Alta (4). Útil para marketing, pero no urgente.  
5. **Caso 5 (Control de Fotos) — Prioridad 5:** Impacto Moderado (2), Facilidad Baja (2). Exige recopilar y etiquetar un dataset de imágenes inexistente actualmente.


## 5\. Riesgos y Checklist Ético (Semáforo Ético)

| Caso | Semáforo | Riesgo Principal Identificado | Medida Mitigadora Propuesta |
| :---- | :---- | :---- | :---- |
| **Caso 1: Cancelaciones** | **ÁMBAR** | **Sesgo indirecto:** Usar la nacionalidad o canal de origen podría discriminar indebidamente a ciertos colectivos. | Excluir datos sensibles del entrenamiento (país de origen sensible) y exigir validación humana antes de aplicar cobros o penalizaciones. |
| **Caso 2: Reseñas** | **ÁMBAR** | **Privacidad (RGPD):** Las reseñas libres pueden contener nombres de empleados o huéspedes. | Aplicar anonimización y filtrado de PII (Datos de Identificación Personal) antes del procesamiento NLP. |
| **Caso 3: Reglas Avisos** | **VERDE** | **Spam o molestia:** Enviar demasiados avisos. | Limitar las comunicaciones a 1 única notificación 48 h antes de la expiración del plazo. |
| **Caso 4: Segmentación** | **VERDE** | **Perfilado discriminatorio:** Descuentos desiguales según origen. | Agrupar únicamente por comportamiento de reserva (anticipación, noches), no por variables demográficas protegidas. |
| **Caso 5: Fotos** | **VERDE** | **Falsos positivos:** Descartar fotos válidas de propietarios locales. | Permitir revisión manual antes de despublicar cualquier imagen de la plataforma. |


## 6\. Recomendación y Siguientes Pasos

### Proyecto Piloto Propuesto:

Desarrollo de un **Modelo de Clasificación Predictiva de Cancelaciones (Caso 1\)** combinado con el **Sistema de Avisos Automáticos (Caso 3\)**.

* **Duración estimada:** 4 semanas.  
* **Presupuesto estimado:** 8.500 € (dentro del límite de 15.000 €).  
* **Datos necesarios del cliente:** Exportación limpia del histórico `reservas_turisdata.csv` del PMS.

### Siguientes Pasos Inmediatos:

1. Validar con el equipo de recepción/operaciones las variables que se utilizarán en el modelo.  
2. Definir el umbral de probabilidad para activar una acción (ej. si el riesgo de cancelación es \> 75 %, enviar recordatorio de confirmación).  
3. Establecer el protocolo de supervisión humana (Human-in-the-loop).


## 7\. Límites de este Informe

* No se ha realizado una auditoría directa sobre la calidad técnica y valores nulos del histórico de `turisdata.db`; el propio cliente reconoce que los datos están incompletos.  
* La tasa de cancelación del 21,25 % procede de los datos del cliente y está pendiente de verificar (se revisa en el Sprint 2).  
* No se ha evaluado la infraestructura de servidores de TurisData para determinar si el modelo se desplegará en la nube o en local.  
* *Advertencia normativa:* Las referencias al **AI Act** y legislación europea deben revisarse periódicamente según el calendario de entrada en vigor de la normativa aplicable (verificar calendario vigente).


### Declaración de uso de IA Generativa

Hemos utilizado asistentes de IA como apoyo en la generación de ideas iniciales de casos de uso y para la revisión de estilo y claridad del documento. Todo el contenido, clasificaciones técnicas, selección de casos y evaluaciones éticas han sido verificados y validados manualmente por el equipo de la consultora 5Green. Las frases del cliente proceden de nuestras notas de la entrevista del 16/10.