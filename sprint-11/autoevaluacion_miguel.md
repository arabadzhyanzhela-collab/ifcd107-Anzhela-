# Sprint 11 · Autoevaluación y Coevaluación · Miguel

- **Equipo:** 5 Green · **Reto:** Visión artificial para el cliente (TurisData Canarias)\[cite: 1\]  
- Fecha : 19-20.11.2026&nbsp;  
- Scrum master Francis, Tecnico Cristina

## 1\. Autoevaluación (Rúbrica 1–4)

| Criterio | Nivel (1–4) | Prueba / Justificación |
| :---- | :---- | :---- |
| **Corrección técnica** | 3 | Programé `modelo_transfer` usando `clone_model` y `set_weights` sin congelar `base_pre`, logré el *fine-tuning* de `bloque3` y comparé su rendimiento frente al modelo desde cero\[cite: 1\]. |
| **Reproducibilidad** | 3 | Ejecuté el cuaderno completo con *Reiniciar y ejecutar todo* y `SEMILLA = 42` verificando que se conservan los pesos congelados y los resultados de validación\[cite: 1\]. |
| **Análisis y comunicación al cliente** | 3 | Expliqué de forma sencilla por qué reutilizar filtros aprendidos (*transfer learning*) rinde mejor que entrenar desde cero cuando hay pocas fotos de alojamientos\[cite: 1\]. |
| **IA responsable** | 3 | Señalé el peligro del sobreajuste y de hacer *fine-tuning* agresivo con pocos datos o etiquetas ruidosas, verificando a mano el código generado con apoyo de IA\[cite: 1\]. |

## 2\. Qué he hecho y qué he aprendido

- **Qué hice:** Implementación del modelo por *transfer learning* \+ *fine-tuning* (Ejercicio 2\) y comparación con el entrenamiento desde cero\[cite: 1\].  
- **Qué me costó y cómo lo resolví:** Al principio me costó distinguir entre congelar la base original y trabajar sobre una copia clonada; lo aclaré revisando `trainable_weights` antes y después de compilar\[cite: 1\].  
- **Qué aprendí:** Descongelar solo el último bloque con una tasa de aprendizaje baja permite adaptar el modelo a las formas del cliente sin destruir lo aprendido\[cite: 1\].

## 3\. Coevaluación del equipo (1–4)

| Compañero/a | Puntuación (1–4) | Ejemplo concreto |
| :---- | :---- | :---- |
| **Cristina** | 4 | Dejó impecable la comprobación por clase del dataset y revisó la coherencia de la entrega\[cite: 1\]. |
| **Fran** | 4 | Sacó adelante las métricas de precisión y *recall* por clase y la lectura de la matriz de confusión\[cite: 1\]. |
| **Andri** | 4 | Analizó muy bien los errores de alta confianza y probó los umbrales de abstención en validación\[cite: 1\]. |
| **Anzhela** | 4 | Redactó la ficha, el `README.md` y el demostrador con todo bien enlazado para el repositorio\[cite: 1\]. |

&nbsp;