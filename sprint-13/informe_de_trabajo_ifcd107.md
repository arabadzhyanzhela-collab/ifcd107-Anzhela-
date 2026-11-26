# Informe de Trabajo — S013

**Equipo:** `5_GREEN`

**Fecha:** 25/11/2026

## 1. Reto exprés de red neuronal (`tramposos_juego.csv`)

Se desarrolló y evaluó un modelo de red neuronal densa (1 capa oculta con activación ReLU, capa de salida sigmoide, optimizador Adam y *EarlyStopping*) para predecir la variable objetivo `tramposo` sobre un conjunto de **4.000 casos** y **8 variables de entrada** (5,9 % de positivos; línea base sin red del **94,1 %**).

* **Configuración elegida (en validación):** 8 neuronas en la capa oculta y umbral de decisión `0.5`.

* **Resultados en prueba (evaluación única):**

  * **Exactitud:** 97,4 %

  * **Precisión:** 88,2 %

  * **Recall:** 63,8 %

  * **AUC:** 0,982

  * **Detalle de casos positivos (47 reales):** 30 detectados, 17 no detectados (escapes) y 4 falsas alarmas.

## 2. Informes de caso para TurisData

### A. Clasificador de reseñas negativas urgentes

* **Objetivo:** Detectar quejas urgentes antes de que afecten a las reservas.

* **Resultados (prueba sobre 500 reseñas):**

  * **Coste sin modelo:** 12.000 €

  * **Coste con modelo:** 4.500 € (**ahorro de 7.500 €**)

  * **Reseñas negativas detectadas:** 82 % (18 % de escapes)

  * **Avisos innecesarios:** 15 %

* **Recomendación:** Desplegar un piloto durante un mes para priorizar alertas en recepción y auditar semanalmente los errores antes de automatizar respuestas.

### B. Asistente web con umbral de parecido

* **Objetivo:** Evaluar la viabilidad de publicar el asistente documental en la web reduciendo respuestas inventadas.

* **Resultados (prueba sobre 18 preguntas, umbral `0.2`):**

  * **Coste sin umbral (contestar siempre):** 450 €

  * **Coste con umbral:** 110 € (**ahorro de 340 €**)

  * **Preguntas bien respondidas:** 77,8 %

  * **Respuestas inventadas:** 2 (frente a 9 si contesta siempre)

  * **Veces que calla:** 2

* **Recomendación:** Publicar con umbral `0.2` y respuesta explícita de «no consta claro», revisando semanalmente las respuestas inventadas debido al tamaño reducido de la prueba.

## 3. Prácticas, juegos y puntuaciones del equipo `5_GREEN`

| Actividad / Juego | Puntuación | Porcentaje | Aprendizajes clave | 
| ----- | ----- | ----- | ----- | 
| **Duelos de modelo** (*Reservas que se cancelan*) | 54 / 54 | **100 %** | Selección con validación, mirada única a prueba, rivales simples exigentes y cálculo real de ahorro. | 
| **Detective de pipelines** (*El buscador que nunca falla*) | 90 / 90 | **100 %** | Detección de fugas de datos (*data leakage*), escalado sobre prueba, métricas engañosas y columnas chivata. | 
| **Primer día de trabajo** (*El hotel rural y las reseñas*) | 119 / 120 | **99 %** | Asignación adecuada de técnicas de IA/ML a 8 problemas de negocio distintos. | 
| **Entrevista de trabajo** | 54 / 54 | **100 %** | Dominio de los conceptos clave en las 18 tarjetas evaluadas. | 
| **Subastas cerradas** (*Asistente con documentos*) | 49 / 50 | **98 %** | Priorización por costes (matriz de confusión y umbrales) y optimización del presupuesto. | 
| **Memorama de modelos** (*Ronda 3*) | 3 / 24 | **13 %** | Actividad pendiente de repetición para consolidar el mapa de modelos y casos de uso en TurisData. | 

## 4. Documentación adicional adjunta

* **Modelo 130 (Agencia Tributaria):** Formulario oficial en blanco correspondiente al pago fraccionado trimestral del IRPF (actividades económicas en estimación directa), sin datos ni importes cumplimentados.