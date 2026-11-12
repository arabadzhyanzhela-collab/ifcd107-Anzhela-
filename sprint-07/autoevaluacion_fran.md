# Autoevaluación y coevaluación · Sprint 7 · Fran

**Equipo:** 5 Green · **Persona:** Fran · **Reto:** «Precio y cancelación»

> Se rellena **de forma individual** y con sinceridad. Usa **la misma rúbrica del reto** (`entrega_y_rubrica`): niveles 1 (empezado), 2 (mínimo), 3 (estándar), 4 (extra). Se pone el nivel cuyo texto **se cumple entero**; si se cumple a medias, el de abajo. Sin una frase de **prueba**, el nivel no vale.

## 1 · Qué he hecho yo en este sprint

- Partes del cuaderno / informe / README en las que he trabajado: Entrené los modelos de clasificación para predecir cancelaciones (Regresión Logística y k-NN), calculé las curvas ROC / AP y evalué las matrices de confusión a distintos umbrales.
- Commits que he hecho (mensajes o fechas): "Entrenamiento de modelos de clasificación", "Matriz de confusión y prueba de umbrales".
- Cosas que he aprendido: He aprendido que cambiar el umbral de decisión (de 0,5 a 0,32) nos permite adaptar el modelo a los costes del negocio.
- Algo que me ha costado y cómo lo he resuelto: Me costó entender cómo funciona el equilibrio entre precisión y *recall*. Lo entendí haciendo una tabla comparativa con varios umbrales.

## 2 · Autoevaluación con la rúbrica

| Criterio | Nivel (1–4) | Prueba (una frase concreta) |
|---|---|---|
| Corrección técnica | 4 | Evalué Regresión Logística frente a k-NN usando validación cruzada y métricas de AUC/AP. |
| Reproducibilidad | 4 | Fijé `random_state=42` en la partición estratificada y en los clasificadores. |
| Análisis y comunicación al cliente | 3 | Expliqué qué significan los falsos positivos y falsos negativos sin usar términos matemáticos raros. |
| IA responsable | 3 | Comprobé que el modelo no dependa de variables discriminatorias para predecir la cancelación. |

## 3 · Mi uso de la IA

- Qué le pedí a una IA (si lo hice): Le pedí ayuda para generar el código de la matriz de confusión con un formato fácil de leer.
- Qué comprobé o cambié yo antes de usarlo: Comprobé que los valores de falsos positivos y falsos negativos coincidieran con los datos de *test*.
- ¿Sé explicar cada línea de mi parte si me lo preguntan? Sí / No / En parte: Sí.

## 4 · Coevaluación (dentro de este mismo fichero)

Aportación de cada compañero o compañera al sprint (1 = casi nada · 2 = lo justo · 3 = lo esperado · 4 = más de lo esperado) and una frase con un ejemplo concreto.

| Compañero/a | Aportación (1–4) | Ejemplo concreto |
|---|---|---|
| Cristina | 4 | Investigó las brechas de falsos alarmas según el canal de reserva. |
| Miguel | 4 | Coordinó la entrega y realizó el análisis financiero de costes e hipótesis. |
| Andri | 3 | Garantizó que las variables de entrada no contuvieran datos del futuro. |
| Anzhela | 4 | Modeló la predicción del precio por noche y ajustó la tabla de tarifas. |

## 5 · Mejora para el próximo sprint

Una cosa que haré distinto: Explicaré mis gráficos en el cuaderno antes de pasárselos al equipo para agilizar la redacción del informe.