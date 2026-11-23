# Sprint 11 · Autoevaluación y Coevaluación · Andri

- **Equipo:** 5 Green · **Reto:** Visión artificial para el cliente (TurisData Canarias)\[cite: 1\]  
- Fecha : 19-20.11.2026&nbsp;  
- Scrum master Francis, Tecnico Cristina

&nbsp;

## 1\. Autoevaluación (Rúbrica 1–4)

| Criterio | Nivel (1–4) | Prueba / Justificación |
| :---- | :---- | :---- |
| **Corrección técnica** | 3 | Implementé `indices_errores` ordenado por confianza descendente y `cobertura_y_exactitud` manejando el caso sin aceptaciones `(0.0, 0.0)` y pasando todos los `assert`\[cite: 1\]. |
| **Reproducibilidad** | 3 | Comprobé que el umbral (`0.70`) se selecciona exclusivamente sobre `prob_val` y se aplica una sola vez al final sobre `prob_pru` de forma reproducible\[cite: 1\]. |
| **Análisis y comunicación al cliente** | 3 | Analicé las imágenes mal clasificadas con mayor confianza y redacté propuestas concretas de mejora (más muestras, revisión de etiquetas y *data augmentation*)\[cite: 1\]. |
| **IA responsable** | 3 | Diseñé la derivación a revisión humana (`"revisar a mano"`) cuando la confianza es baja y documenté los riesgos de privacidad, sesgo y cambio de dominio\[cite: 1\]. |

## 2\. Qué he hecho y qué he aprendido

- **Qué hice:** Análisis de errores ordenados por confianza (Ejercicio 4), cálculo de cobertura y exactitud según umbral (Ejercicio 5\) y redacción de riesgos y mejoras en la ficha\[cite: 1\].  
- **Qué me costó y cómo lo resolví:** Al principio me costó ordenar los índices de error de mayor a menor confianza sin desalinear los arrays; lo resolví usando `np.argsort(confianzas)[::-1]` sobre el vector de errores\[cite: 1\].  
- **Qué aprendí:** Permitir que un modelo de visión se abstenga cuando duda mejora mucho la fiabilidad de las predicciones automáticas en un entorno real\[cite: 1\].

## 3\. Coevaluación del equipo (1–4)

| Compañero/a | Puntuación (1–4) | Ejemplo concreto |
| :---- | :---- | :---- |
| **Cristina** | 4 | Aseguró que la carga y el conteo de las 5 clases del dataset funcionaran sin fallos\[cite: 1\]. |
| **Miguel** | 4 | Construyó la rama de *transfer learning* \+ *fine-tuning* con claridad y buena estructura\[cite: 1\]. |
| **Fran** | 4 | Calculó de forma rigurosa la precisión y el *recall* por clase y revisó la matriz de confusión\[cite: 1\]. |
| **Anzhela** | 4 | Coordinó la documentación final (`ficha_modelo_vision.md`, `README.md`) y el cierre del sprint\[cite: 1\]. |

&nbsp;