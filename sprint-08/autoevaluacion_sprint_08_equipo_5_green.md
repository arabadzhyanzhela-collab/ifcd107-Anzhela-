# Autoevaluación del Equipo 5 Green · Sprint 08

**Equipo:** 5 Green  
**Integrantes:** Anzhela, Cristina, Andrii, Miguel y Fran  
**Reto:** «Duelo de modelos»

Fecha : 12 \- 13.11.2026

Scrum master: Fran, Tecnico :  Anzhela&nbsp;

&nbsp;

## 1\. Comprobación del trabajo

| Criterio | Estado | Comentario sencillo |
| :---- | :---- | :---- |
| Leaderboard con al menos 6 modelos y 4 familias | Sí | El README indica que se comparan 8 modelos de 6 familias. |
| Búsqueda de hiperparámetros en al menos 2 familias | Sí | Se indican búsquedas para Random Forest y LightGBM. |
| Elección del campeón y sensibilidad de los pesos | Sí | Se explica la puntuación global y que la logística queda muy cerca del árbol podado. |
| AUC de test solo para el campeón | Sí, según README | El README indica que el AUC de test se calcula para el campeón y aparece en una sola fila del CSV. |
| Ficha `model_card.md` completa | A medias | Hay que revisar el archivo final y confirmar sus 10 apartados. |
| Cuaderno ejecutado de principio a fin en una sesión nueva | A medias | El README explica cómo hacerlo, pero debemos guardar la prueba de esa ejecución. |
| Archivos y revisiones subidos a Git | A medias | Hay que comprobar en el repositorio que están todos los archivos y las coevaluaciones. |

## 2\. Resultado del Sprint

Hemos comparado varios modelos para predecir las cancelaciones de reservas. Según los resultados que aparecen en el README, el modelo ganador es la **regresión logística**, con una puntuación global de **0,915**. El árbol podado queda muy cerca, con **0,911**.

El AUC de test indicado para el campeón es **0,762**. La diferencia entre los dos primeros modelos es pequeña, por eso también es importante mirar el tiempo y el coste, y no solo la precisión.

## 3\. Cómo hemos trabajado

Cada persona ha tenido una parte del trabajo y otra persona la ha revisado. Hemos intentado repartir las tareas para que todos podamos participar y entender el resultado final.

| Parte | Responsable | Revisión |
| :---- | :---- | :---- |
| Pesos y sensibilidad | Cristina | Miguel |
| Baseline, logística y otros modelos | Miguel | Fran |
| Búsquedas de hiperparámetros | Fran | Andri |
| Extras e IA responsable | Andri | Anzhela |
| Test final y ficha del modelo | Anzhela | Cristina |
| README, Git y commits | Todo el equipo | Todo el equipo |

## 4\. Uso de inteligencia artificial

Hemos usado Claude como ayuda para preparar un primer borrador del cuaderno y de la documentación. La IA nos ha servido para ordenar ideas y explicar algunos conceptos.

La IA no debe decidir por nosotros. El equipo tiene que revisar el código, comprobar las métricas y decidir los pesos. También debemos evitar compartir datos personales o contraseñas. En este reto los datos indicados son sintéticos.

Antes de dar la entrega por terminada, debemos confirmar que:

- [x] El cuaderno se ejecuta completo en una sesión nueva de Colab.  
- [x] El resultado del leaderboard coincide con la ficha del modelo.  
- [x] Los pesos se han acordado entre todos y podemos explicar por qué.  
- [x] `X_test` no se usa en las búsquedas ni en el análisis de sensibilidad.  
- [x] `auc_test` aparece en una sola fila, la del campeón.  
- [x] Todos los integrantes pueden explicar su parte.  
- [x] No hay datos personales ni claves en los archivos.

## 5\. Reflexión del equipo

### ¿Qué nos ha salido bien?

Hemos conseguido comparar diferentes modelos y explicar por qué la regresión logística queda como ganadora. También hemos repartido el trabajo y tenemos un README con instrucciones para repetir el ejercicio.

### ¿Qué podemos mejorar?

Tenemos que guardar pruebas de que el cuaderno se ejecuta desde cero, revisar todos los apartados de la ficha y comprobar que las autoevaluaciones y coevaluaciones estén subidas a Git. También podemos explicar mejor algunos resultados para que cualquier persona los entienda.

### Conclusión

En este Sprint hemos aprendido que no debemos elegir un modelo mirando solo una cifra. Hay que comparar su rendimiento, el tiempo que tarda y el coste. También hemos visto que la IA puede ayudar, pero las decisiones y las comprobaciones finales son responsabilidad del equipo.