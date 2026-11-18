# Autoevaluación y coevaluación · Sprint 9 · Fran

**Equipo:** 5 Green · **Persona:** Fran · **Reto:** «Conocer al huésped»

## 1 · Qué he hecho yo en este sprint

- **Partes trabajadas:** Sistema de recomendación de experiencias (popularidad, `precision@3`, similitud coseno `item-item` y función `recomendar(..., P=P_item)`).  
- **Commits realizados:** `feat(S09): recomendador item-item y funcion recomendar`&nbsp;  
- **Qué he aprendido:** La diferencia entre medir error de nota (RMSE) y calidad del ranking (`precision@k`), y la importancia de ocultar ítems ya valorados con `-np.inf`.  
- **Qué me ha costado y cómo lo resolví:** Evitar que `recomendar(0)` devolviera el último usuario por indexación negativa en Python; añadí una validación con `ValueError`.

## 2 · Autoevaluación con la rúbrica

| Criterio | Nivel (1–4) | Prueba (una frase concreta) |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Item-item mejora a popularidad en RMSE (0,895 vs 1,029) y `precision@3` (0,171 vs 0,125). |
| Reproducibilidad | 4 | División train/test (80/20) con `SEMILLA = 42` evitando fuga de datos en el cálculo de medias. |
| Análisis y comunicación al cliente | 4 | Comparativa clara en tabla y demostración de recomendaciones personalizadas distintas para usuarios 1 y 2\. |
| IA responsable | 4 | Exclusión de ítems ya consumidos y control de validación de entradas en `recomendar`. |

## 3 · Mi uso de la IA

- **Qué pedí:** Revisión de la indexación 1-based de `id_usuario` frente a los índices 0-based de NumPy.  
- **Qué comprobé:** Ejecuté todos los tests con `assert` y comprobé que `recomendar(0)` lanza `ValueError`.  
- **¿Sé explicar cada línea de mi parte?** Sí.

## 4 · Coevaluación

| Compañero/a | Aportación (1–4) | Ejemplo concreto |
| :---- | :---- | :---- |
| Cristina | 4 | Lideró la segmentación de clientes y la definición de acciones comerciales por grupo. |
| Miguel | 4 | Elaboró el mapa PCA 2D y el análisis de varianza acumulada. |
| Andri | 4 | Desarrolló el apartado ético sobre RGPD y sesgo de popularidad. |
| Anzhela | 4 | Integró todos los resultados en `informe_huespedes.md` y validó el `README.md`. |

## 5 · Mejora para el próximo sprint

Añadir pruebas unitarias adicionales para casos límite (usuarios sin historial) antes de cerrar el código.