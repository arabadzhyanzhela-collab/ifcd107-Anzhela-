# Autoevaluación y coevaluación · Sprint 7 · Anzhela

**Equipo:** 5 Green · **Persona:** Anzhela · **Reto:** «Precio y cancelación»

> Se rellena **de forma individual** y con sinceridad. Usa **la misma rúbrica del reto** (`entrega_y_rubrica`): niveles 1 (empezado), 2 (mínimo), 3 (estándar), 4 (extra). Se pone el nivel cuyo texto **se cumple entero**; si se cumple a medias, el de abajo. Sin una frase de **prueba**, el nivel no vale.

## 1 · Qué he hecho yo en este sprint

- Partes del cuaderno / informe / README en las que he trabajado: He programado el modelo de regresión para estimar los precios de las habitaciones, construí las interacciones entre temporada y tipo de habitación y redacté la tabla de tarifas de referencia.
- Commits que he hecho (mensajes o fechas): "Ajuste de regresión lineal para precio", "Tabla de precios por temporada e interacciones".
- Cosas que he aprendido: He aprendido a calcular el MAE y el R² para saber exactamente cuánto se equivoca un modelo en euros reales.
- Algo que me ha costado y cómo lo he resuelto: Me costó interpretar la diferencia entre el MAE y el RMSE cuando había suites con precios muy altos; lo entendí comparando ambos errores lado a lado.

## 2 · Autoevaluación con la rúbrica

| Criterio | Nivel (1–4) | Prueba (una frase concreta) |
|---|---|---|
| Corrección técnica | 4 | El modelo de regresión logra un R² de 0,928 con interacciones y se validó en *train*. |
| Reproducibilidad | 4 | El cuaderno descarga los datos directamente de GitHub y se ejecuta sin fallos de importación. |
| Análisis y comunicación al cliente | 4 | Redacté la tabla final de precios recomendados por tipo de habitación y temporada en euros enteros. |
| IA responsable | 3 | Explicamos con claridad por qué la predicción de precios no debe perjudicar a ciertos canales. |

## 3 · Mi uso de la IA

- Qué le pedí a una IA (si lo hice): Le pedí sugerencias para estructurar el código de las interacciones en Scikit-Learn.
- Qué comprobé o cambié yo antes de usarlo: Verifiqué los coeficientes a mano e hice los cálculos de comprobación con `assert`.
- ¿Sé explicar cada línea de mi parte si me lo preguntan? Sí / No / En parte: Sí.

## 4 · Coevaluación (dentro de este mismo fichero)

Aportación de cada compañero o compañera al sprint (1 = casi nada · 2 = lo justo · 3 = lo esperado · 4 = más de lo esperado) y una frase con un ejemplo concreto.

| Compañero/a | Aportación (1–4) | Ejemplo concreto |
|---|---|---|
| Cristina | 4 | Evaluó el impacto ético de los falsos positivos en clientes reubicados. |
| Miguel | 4 | Lideró la estrategia de negocio y redactó el resumen ejecutivo para el cliente. |
| Fran | 3 | Ejecuto la validación cruzada para comparar la regresión logística con k-NN. |
| Andri | 3 | Filtró y limpió los datos evitando fugas antes de entrenar los modelos. |

## 5 · Mejora para el próximo sprint

Una cosa que haré distinto: Revisaré las métricas de validación cruzada antes de pasar al informe para evitar rehacer tablas.