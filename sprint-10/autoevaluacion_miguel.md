# Autoevaluación y coevaluación · «¿Vale la pena la red?»

Equipo 5 Green · Se puntúa con la [rúbrica del reto](https://github.com/cCoolBoox/IFCD107-alumnado/tree/main/sprints/S10), de 1 a 4\.

Fecha : 17-18.11.2026&nbsp;

Scrum master Cristina, Tecnico Francis&nbsp;

&nbsp;

---

## 1\. Autoevaluación

**Nombre:** Miguel

**Repaso rápido** (Sí / No / A medias):

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El cuaderno se ejecuta de arriba abajo, con semillas fijas? | Sí: comprobado tras Reiniciar y ejecutar todo con semillas fijas (42 y 1, 2, 3\) |
| ¿La partición es única y la prueba se usa una sola vez? | Sí: una sola partición (semilla 42\) y la prueba solo se usa en la sección 6 |
| ¿Hay al menos un MLP y un modelo de árboles/boosting comparados con las mismas métricas? | Sí: MLP y boosting, con AUC, AP, F1 y exactitud |
| ¿Hay curvas de aprendizaje y un diagnóstico explícito de sobreajuste? | Sí: sin sobreajuste claro |
| ¿La comparación tiene incertidumbre (varias semillas o bootstrap)? | Sí: 3 semillas (0,748 ± 0,001 en validación) y bootstrap con intervalo \[−0,005, \+0,020\] |
| ¿El informe recomienda algo concreto, con coste y límites? | Sí: mantener el boosting |
| ¿Hay al menos dos riesgos de IA responsable específicos? | Sí: tres, con su medida |

**Puntúate de 1 a 4**:

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 4 | Los cuatro ejercicios pasan, una sola partición, 3 variantes elegidas con validación y modelo guardado y recargado con el mismo resultado | Explorar combinaciones de hiperparámetros de forma más amplia sin tocar prueba |
| Reproducibilidad | 3 | El README explica cómo repetirlo; confirmado tras reiniciar y ejecutar todo en Colab que salen las cifras del informe | Comprobar que otra persona en otro entorno obtiene las mismas cifras |
| Análisis y comunicación al cliente | 3 | Responde a «¿vale la pena?» con media ± desviación, intervalo, coste y límites | Añadir cuándo cambiaría la recomendación con un coste real de *overbooking* |
| IA responsable | 3 | Tres riesgos concretos con medida; además medimos el AUC por país y canal y el efecto del umbral | Analizar por qué el canal directo tiene menor AUC (0,712) frente a empresa (0,775) |

- **Lo que más me costó fue:** interpretar las variantes del MLP con regularización L2 y programar la función de diagnóstico del ejercicio 3\.  
- **Sobre el uso de IA:** he usado IA para generar el cuaderno completo y los borradores del informe; comprobé a mano la generación de `curvas_aprendizaje.png` y las épocas de parada temprana.

---

## 2\. Coevaluación (durante la review)

**Trabajo revisado de (persona o equipo):** Fran (Equipo 5 Green)  **Revisado por (yo):** Miguel

| Entregable (nómbralo) | ¿Está y se entiende? ✔ / ✘ / — | Comentario breve |
| :---- | :---- | :---- |
| Cuaderno y bloques de Bootstrap | ✔ | Código de remuestreo limpio y bien comentado. |
| Informe comparativo (`informe_comparativo.md`) | ✔ | Síntesis excelente de los resultados y de la incertidumbre estadística. |
| Estructura general del repositorio | ✔ | Todos los archivos organizados correctamente en la carpeta del sprint. |

&nbsp;

| Criterio | Puntuación (1–4) | Comentario breve |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Implementación rigurosa del intervalo bootstrap al 95 % sin fugas de datos. |
| Reproducibilidad | 4 | Los scripts corren de forma determinista fijando correctamente las semillas. |
| Análisis y comunicación al cliente | 4 | Excelente comunicación del veredicto estadístico (empate técnico / intervalo que cruza el cero). |
| IA responsable | 3 | Planteamiento claro de los límites de los datos sintéticos. |

- **Lo que está muy bien:** Me ha ayudado mucho la explicación que redactó Fran sobre cómo interpretar el intervalo de confianza de Bootstrap para justificar el empate técnico.  
- **Lo que yo cambiaría, y por qué:** Yo añadiría una representación gráfica del histograma de las diferencias de AUC obtenidas en el bootstrap para visualizar mejor la distribución.