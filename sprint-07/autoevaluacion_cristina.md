# Autoevaluación y coevaluación · Sprint 7 · Cristina

**Equipo:** 5 Green · **Persona:** Cristina · **Reto:** «Precio y cancelación»

> Se rellena **de forma individual** y con sinceridad. Usa **la misma rúbrica del reto** (`entrega_y_rubrica`): niveles 1 (empezado), 2 (mínimo), 3 (estándar), 4 (extra). Se pone el nivel cuyo texto **se cumple entero**; si se cumple a medias, el de abajo. Sin una frase de **prueba**, el nivel no vale.

## 1 · Qué he hecho yo en este sprint

- Partes del cuaderno / informe / README en las que he trabajado: Me centré en la sección de IA responsable, analizando los sesgos del modelo según el país de origen y el canal de reserva, y redacté las medidas para evitar discriminación.
- Commits que he hecho (mensajes o fechas): "Análisis de sesgos categóricos", "Redacción de apartado de IA Responsable y recomendaciones".
- Cosas que he aprendido: He aprendido a medir cómo una diferencia en la tasa de falsos positivos afecta de forma desigual a distintos tipos de clientes.
- Algo que me ha costado y cómo lo he resuelto: Me costó entender por qué las reservas por web intermediaria tenían más falsas alarmas que las directas. Lo resolví calculando las tasas base por grupo en el conjunto de datos.

## 2 · Autoevaluación con la rúbrica

| Criterio | Nivel (1–4) | Prueba (una frase concreta) |
|---|---|---|
| Corrección técnica | 3 | Comprobé que no se utilizaran variables prohibidas o posteriores al momento de la reserva. |
| Reproducibilidad | 4 | Todas las pruebas y tablas de sesgo son totalmente reproducibles con la semilla 42. |
| Análisis y comunicación al cliente | 4 | Redacté recomendaciones claras para no penalizar individualmente a los clientes según su país. |
| IA responsable | 4 | Medí numéricamente la brecha de falsos positivos (41,4 puntos) entre canales y propuse medidas. |

## 3 · Mi uso de la IA

- Qué le pedí a una IA (si lo hice): Pedí ejemplos sobre cómo redactar advertencias éticas de forma constructiva para un cliente hotelero.
- Qué comprobé o cambié yo antes de usarlo: Adapté todo el texto al contexto real de TurisData y verifiqué las cifras con el cuaderno.
- ¿Sé explicar cada línea de mi parte si me lo preguntan? Sí / No / En parte: Sí.

## 4 · Coevaluación (dentro de este mismo fichero)

Aportación de cada compañero o compañera al sprint (1 = casi nada · 2 = lo justo · 3 = lo esperado · 4 = más de lo esperado) y una frase con un ejemplo concreto.

| Compañero/a | Aportación (1–4) | Ejemplo concreto |
|---|---|---|
| Miguel | 4 | Organizó el reparto de tareas y calculó el umbral financiero óptimo. |
| Fran | 3 | Creó las visualizaciones y las matrices de confusión a distintos umbrales. |
| Andri | 3 | Preparó la carga de datos sin datos trampa y verificó la ausencia de nulos. |
| Anzhela | 4 | Construyó el modelo de regresión para estimar precios por habitación. |

## 5 · Mejora para el próximo sprint

Una cosa que haré distinto: Participaré más activamente en las primeras pruebas de código para entender la estructura desde el principio.