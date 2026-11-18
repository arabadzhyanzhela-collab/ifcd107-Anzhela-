# Autoevaluación y coevaluación · Sprint 9 · Andri

**Equipo:** 5 Green · **Persona:** Andri · **Reto:** «Conocer al huésped»

## 1 · Qué he hecho yo en este sprint

- **Partes trabajadas:** Apartado de IA responsable (soluciones al arranque en frío para usuarios y experiencias nuevas, mitigación del sesgo de popularidad y cumplimiento RGPD) y validación del cuaderno de Q-learning.  
- **Commits realizados:** `docs(S09): seccion ia responsable y rgpd en informe`&nbsp;  
- **Qué he aprendido:** Cómo un sistema de recomendación puede invisibilizar a proveedores pequeños si no se introduce exploración, y cómo resolver el *cold start*.  
- **Qué me ha costado y cómo lo resolví:** Distinguir qué técnica usar cuando el nuevo es el usuario (popularidad) frente a cuando es nueva la experiencia (contenido); lo aclaré comparando matrices.

## 2 · Autoevaluación con la rúbrica

| Criterio | Nivel (1–4) | Prueba (una frase concreta) |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Verificación de funcionamiento de Q-learning y recomendaciones sin ítems repetidos. |
| Reproducibilidad | 4 | Comprobación de descarga automática de CSVs desde GitHub en entorno limpio de Colab. |
| Análisis y comunicación al cliente | 4 | Propuesta práctica de *slot* de exploración para equilibrar conversión y diversidad local. |
| IA responsable | 4 | Análisis completo de *cold start*, sesgo de popularidad y derechos de acceso/oposición RGPD. |

## 3 · Mi uso de la IA

- **Qué pedí:** Ejemplos de medidas prácticas para mitigar el sesgo de popularidad en turismo.  
- **Qué comprobé:** Adapté las medidas al catálogo real de 25 experiencias de TurisData Canarias.  
- **¿Sé explicar cada línea de mi parte?** Sí.

## 4 · Coevaluación

| Compañero/a | Aportación (1–4) | Ejemplo concreto |
| :---- | :---- | :---- |
| Cristina | 4 | Realizó el clustering completo y caracterizó los 4 perfiles de huéspedes. |
| Miguel | 4 | Desarrolló la reducción dimensional PCA y explicó la interpretación de cargas. |
| Fran | 4 | Programó la evaluación de RMSE y `precision@3` para el recomendador item-item. |
| Anzhela | 4 | Coordinó la entrega en GitHub, el `README.md` y la revisión final del informe. |

## 5 · Mejora para el próximo sprint

Compartir antes el borrador de riesgos éticos para integrarlo en las decisiones de diseño del modelo desde el inicio.