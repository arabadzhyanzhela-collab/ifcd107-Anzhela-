# Autoevaluación y coevaluación · Sprint 7 · Andri

**Equipo:** 5 Green · **Persona:** Andri · **Reto:** «Precio y cancelación»

> Se rellena **de forma individual** y con sinceridad. Usa **la misma rúbrica del reto** (`entrega_y_rubrica`): niveles 1 (empezado), 2 (mínimo), 3 (estándar), 4 (extra). Se pone el nivel cuyo texto **se cumple entero**; si se cumple a medias, el de abajo. Sin una frase de **prueba**, el nivel no vale.

## 1 · Qué he hecho yo en este sprint

- Partes del cuaderno / informe / README en las que he trabajado: Me he encargado de preparar la base de datos de reservas, hacer el análisis de correlaciones y ayudar a limpiar las columnas que no se podían usar para evitar la fuga de datos (*data leakage*).
- Commits que he hecho (mensajes o fechas): "Carga de reservas y comprobación de nulos", "Eliminación de columnas trampa y prueba de correlación".
- Cosas que he aprendido: He aprendido a identificar cuándo una variable es "trampa" (ocurre después de la reserva) y a interpretar el AUC-ROC de forma sencilla.
- Algo que me ha costado y cómo lo he resuelto: Me costó entender por qué no se puede usar la variable `cancelada` para predecir el precio. Lo resolví comentándolo en grupo y repasando el orden temporal de los datos.

## 2 · Autoevaluación con la rúbrica

| Criterio | Nivel (1–4) | Prueba (una frase concreta) |
|---|---|---|
| Corrección técnica | 3 | He comprobado que el pipeline ajusta los transformadores solo con el conjunto de *train* sin usar datos de *test*. |
| Reproducibilidad | 4 | Al reiniciar la sesión de Colab y ejecutar todo de arriba a abajo, salen exactamente las mismas cifras. |
| Análisis y comunicación al cliente | 3 | He ayudado a traducir el error del modelo a euros entendibles para el cliente. |
| IA responsable | 3 | Hemos analizado cómo afecta el sesgo de canal de reserva a las falsas alarmas. |

## 3 · Mi uso de la IA

- Qué le pedí a una IA (si lo hice): Le pedí ayuda para redactar la explicación del gráfico de correlaciones en palabras sencillas.
- Qué comprobé o cambié yo antes de usarlo: Revisé que los nombres de las variables y los porcentajes coincidieran exactamente con los del cuaderno.
- ¿Sé explicar cada línea de mi parte si me lo preguntan? Sí / No / En parte: Sí.

## 4 · Coevaluación (dentro de este mismo fichero)

Aportación de cada compañero o compañera al sprint (1 = casi nada · 2 = lo justo · 3 = lo esperado · 4 = más de lo esperado) y una frase con un ejemplo concreto.

| Compañero/a | Aportación (1–4) | Ejemplo concreto |
|---|---|---|
| Cristina | 4 | Redactó la sección de IA responsable con el análisis de sesgo por canal de venta. |
| Miguel | 4 | Coordinó las reuniones y calculó el umbral de coste en euros para el negocio. |
| Fran | 3 | Entrenó los modelos de clasificación y preparó las matrices de confusión. |
| Anzhela | 4 | Comprobó todas las aserciones del cuaderno y ajustó el modelo de regresión. |

## 5 · Mejora para el próximo sprint

Una cosa que haré distinto: Empezaré a documentar el código desde el primer día para no acumular explicaciones al final.