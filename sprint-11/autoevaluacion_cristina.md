# Sprint 11 · Autoevaluación y Coevaluación · Cristina

- **Equipo:** 5 Green · **Reto:** Visión artificial para el cliente (TurisData Canarias)\[cite: 1\]  
- Fecha : 19-20.11.2026&nbsp;  
- Scrum master Francis, Tecnico Cristina

## 1\. Autoevaluación (Rúbrica 1–4)

| Criterio | Nivel (1–4) | Prueba / Justificación |
| :---- | :---- | :---- |
| **Corrección técnica** | 3 | Implementé `contar_por_clase(ruta)` filtrando extensiones de imagen (`.png`, `.jpg`, `.jpeg`) e ignorando `_ambiguas.csv`, superando todos los `assert` de comprobación del dataset\[cite: 1\]. |
| **Reproducibilidad** | 3 | Comprobé que el dataset sintético se genera con `semilla=7` y el particionado con `SEMILLA = 42` de forma idéntica al reiniciar el entorno en Colab\[cite: 1\]. |
| **Análisis y comunicación al cliente** | 3 | Revisé la distribución de clases (60 imágenes por categoría) y ayudé a explicar al cliente por qué el equilibrio y la limpieza de carpetas son el primer paso antes de entrenar\[cite: 1\]. |
| **IA responsable** | 3 | Documenté el riesgo de que imágenes mal etiquetadas o carpetas desiguales contaminen el entrenamiento, y revisé que el uso de IA se declarara claramente\[cite: 1\]. |

## 2\. Qué he hecho y qué he aprendido

- **Qué hice:** Verificación del dataset por carpeta (Ejercicio 1), carga con `image_dataset_from_directory` y revisión cruzada de la entrega final\[cite: 1\].  
- **Qué me costó y cómo lo resolví:** Al principio dudé sobre cómo excluir archivos auxiliares como `_ambiguas.csv`; lo resolví comprobando con `os.path.isdir` y filtrando por extensión en minúsculas\[cite: 1\].  
- **Qué aprendí:** Antes de tocar cualquier red neuronal, revisar que cada clase tenga muestras suficientes y limpias evita perder horas entrenando sobre datos rotos\[cite: 1\].

## 3\. Coevaluación del equipo (1–4)

| Compañero/a | Puntuación (1–4) | Ejemplo concreto |
| :---- | :---- | :---- |
| **Miguel** | 4 | Montó muy bien `modelo_transfer` congelando la copia de la base y ajustando el último bloque con *fine-tuning*\[cite: 1\]. |
| **Fran** | 4 | Calculó con mucha precisión el *recall* y la precisión por clase desde la matriz de confusión\[cite: 1\]. |
| **Andri** | 4 | Ordenó los errores por confianza y ajustó el umbral de abstención mirando solo la validación\[cite: 1\]. |
| **Anzhela** | 4 | Dejó listos el demostrador, la ficha del modelo, el `README.md` y la subida ordenada a GitHub\[cite: 1\]. |

&nbsp;