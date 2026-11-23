# Sprint 11 · Autoevaluación y Coevaluación · Fran

- **Equipo:** 5 Green · **Reto:** Visión artificial para el cliente (TurisData Canarias)\[cite: 1\]  
- Fecha : 19-20.11.2026&nbsp;  
- Scrum master Francis, Tecnico Cristina

## 1\. Autoevaluación (Rúbrica 1–4)

| Criterio | Nivel (1–4) | Prueba / Justificación |
| :---- | :---- | :---- |
| **Corrección técnica** | 3 | Calculé `recall_clase` (dividiendo por la suma de filas), `precision_clase` (dividiendo por la suma de columnas) e identifiqué `clase_mas_dificil` sobre el conjunto de prueba\[cite: 1\]. |
| **Reproducibilidad** | 3 | Verifiqué que al ejecutar todo el cuaderno en orden se obtiene la misma matriz de confusión y las mismas métricas por clase sin tocar `X_pru` durante el ajuste\[cite: 1\]. |
| **Análisis y comunicación al cliente** | 3 | Traduje la matriz de confusión a un lenguaje claro para TurisData, destacando qué categorías se confunden más y cuál exige más atención\[cite: 1\]. |
| **IA responsable** | 3 | Mostré que fijarse solo en la exactitud global oculta clases con menor *recall*, y comprobé los cálculos matriciales frente a `classification_report`\[cite: 1\]. |

## 2\. Qué he hecho y qué he aprendido

- **Qué hice:** Evaluación en el conjunto de prueba, cálculo de precisión y *recall* por clase a partir de la matriz de confusión (Ejercicio 3\) y revisión del cuaderno\[cite: 1\].  
- **Qué me costó y cómo lo resolví:** Me costó asegurarme del eje (`axis=1` vs `axis=0`) al calcular precisión y *recall* desde `cm`; lo comprobé contrastándolo con el `classification_report`\[cite: 1\].  
- **Qué aprendí:** La matriz de confusión es fundamental para ver qué clases se pisan entre sí (como alojamientos con estructura parecida) más allá de una única nota media\[cite: 1\].

## 3\. Coevaluación del equipo (1–4)

| Compañero/a | Puntuación (1–4) | Ejemplo concreto |
| :---- | :---- | :---- |
| **Cristina** | 4 | Resolvió con mucha limpieza la revisión de carpetas y el conteo de imágenes por clase\[cite: 1\]. |
| **Miguel** | 4 | Implementó el *transfer learning* y el *fine-tuning* dejando el modelo listo para evaluar en prueba\[cite: 1\]. |
| **Andri** | 4 | Hizo un gran trabajo ordenando los errores más graves y midiendo cobertura y exactitud al abstenerse\[cite: 1\]. |
| **Anzhela** | 4 | Unió los resultados técnicos y éticos en la ficha del modelo y preparó la subida final a GitHub\[cite: 1\]. |

&nbsp;