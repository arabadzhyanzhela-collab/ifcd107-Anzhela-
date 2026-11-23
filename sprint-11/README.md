# Sprint 11 · Reto «Visión artificial para el cliente (TurisData Canarias)»

- **Equipo:** 5 Green (Cristina, Miguel, Fran, Andri y Anzhela)  
- Fecha : 19-20.11.2026&nbsp;  
- Scrum master Francis, Tecnico Cristina  
- **Curso:** [IFCD107 · Especialista en Inteligencia Artificial](https://github.com/cCoolBoox/IFCD107-alumnado/tree/main/sprints/S11)  
- **Problema:** Clasificación automática de fotos de alojamientos y zonas comunes (`hotel`, `apartamentos`, `casa_rural`, `camping`, `piscina`) con derivación a revisión humana cuando la red duda.

## Qué se entrega en `sprint-11/`

| Fichero | Contenido |
| :---- | :---- |
| `reto_S11_vision_cliente.ipynb` | Cuaderno principal ejecutado de arriba abajo con los 5 ejercicios resueltos, entrenamiento por *transfer learning* \+ *fine-tuning*, análisis de errores, umbral de abstención y demostrador `clasificar_foto()` |
| `ficha_modelo_vision.md` | Informe técnico y de negocio para el cliente: métricas en prueba, análisis de errores, umbral de abstención, nota de IA responsable y revisión con la rúbrica |
| `README.md` | Este archivo con guía de reproducción y reparto del equipo |
| `autoevaluacion_<nombre>.md` | Hojas individuales de autoevaluación y coevaluación de Cristina, Miguel, Fran, Andri y Anzhela |

*(Nota: Los datos sintéticos se generan automáticamente al ejecutar el cuaderno y se borran al final; no se suben al repositorio).*

## Quién hizo qué

| Parte | Responsable | Revisión |
| :---- | :---- | :---- |
| Dataset, comprobación de clases (Ej. 1\) y carga | Cristina | Miguel |
| Modelo *transfer learning* \+ *fine-tuning* (Ej. 2\) y comparación desde cero | Miguel | Fran |
| Evaluación en prueba, matriz de confusión y métricas por clase (Ej. 3\) | Fran | Andri |
| Análisis de errores (Ej. 4\) y umbral de abstención (Ej. 5\) | Andri | Anzhela |
| Demostrador, `ficha_modelo_vision.md`, `README.md` y subida a GitHub | Anzhela | Cristina |

## Cómo reproducirlo

1. Abrir `reto_S11_vision_cliente.ipynb` en **Google Colab**.  
2. Pulsar **Entorno de ejecución → Reiniciar y ejecutar todo**.  
3. **Semilla fija:** `SEMILLA = 42` en todas las particiones y entrenamientos.  
4. **Tiempo de ejecución:** Menos de 1 minuto en CPU (no requiere descarga externa ni GPU para la rama offline).

## Resultado en una línea

El modelo con *transfer learning* \+ *fine-tuning* supera claramente al entrenamiento desde cero y clasifica automáticamente alrededor del **80 % de las fotos con un umbral de confianza de 0,70**, enviando el resto a revisión humana para evitar errores graves frente al cliente.