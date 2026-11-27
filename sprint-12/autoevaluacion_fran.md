# Autoevaluación y coevaluación · Sprint 12 · Fran

- **Equipo:** 5 Green
- **Miembro:** Fran
- **Repositorio:** https://github.com/cCoolBoox/IFCD107-alumnado/tree/main/sprints/S12

## 1. Qué he hecho yo
- Trabajé en los ejercicios de Transformers/atención (`softmax`, atención completa, máscara causal, temperatura y cambio de embedding en `X2`) y LSA.
- Revisé las salidas numéricas y gráficos para asegurar que coincidieran con lo esperado en cada celda.
- Ayudé a comprobar que las métricas y tablas de evaluación estuvieran bien construidas.

## 2. Autoevaluación (rúbrica 1–4)
| Criterio | Nivel (1–4) | Prueba concreta |
|---|---|---|
| Corrección técnica | 4 | Comprobé `softmax` por filas, `atencion`, `atencion_causal`, probabilidades con `T=0.3` y `T=2.5`, y la reducción LSA. |
| Reproducibilidad | 4 | Ejecuté las celdas respetando `SEMILLA = 42` para obtener los mismos resultados en cada prueba. |
| Análisis y comunicación al cliente | 3 | Expliqué qué cambia al subir o bajar la temperatura y por qué una semana con error alto solo indica revisar. |
| IA responsable | 3 | Señalé que un filtro de palabras sospechosas ayuda, pero no sustituye a otras medidas de seguridad. |

## 3. Coevaluación del equipo (1–4)
| Compañero/a | Aportación (1–4) | Ejemplo concreto |
|---|---|---|
| Cristina | 4 | Ayudó a revisar la redacción y los casos de prueba de texto y negaciones. |
| Miguel | 4 | Mantuvo el enfoque del grupo en los objetivos del reto y en la estructura del RAG. |
| Andri | 4 | Colaboró en la comprobación de los ejercicios de entrenamiento, umbral y anomalías. |
| Anzhela | 4 | Ayudó a estructurar la documentación del sprint para subirla a GitHub. |

## 4. Algo que mejoraré en el próximo sprint
- Explicar aún más breve y visualmente qué pasa en cada paso matemático al compartirlo con el grupo.