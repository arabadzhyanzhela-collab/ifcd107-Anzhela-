# Autoevaluación y coevaluación · Sprint 9 · Cristina

**Equipo:** 5 Green · **Persona:** Cristina · **Reto:** «Conocer al huésped»

## 1 · Qué he hecho yo en este sprint

- **Partes trabajadas:** Estandarización de variables (`StandardScaler`), cálculo de siluetas para elegir $k=4$ y definición de perfiles de segmentos en `reto_S09.ipynb`.  
- **Commits realizados:** `feat(S09): clustering kmeans y perfiles de segmentos`&nbsp;  
- **Qué he aprendido:** A escalar variables antes de medir distancias euclídeas y a traducir centros estandarizados (`perfil_z`) en segmentos útiles para marketing.  
- **Qué me ha costado y cómo lo resolví:** Diferenciar entre `.max()` e `.idxmax()` al identificar automáticamente los grupos de familias y aventureros; lo comprobé verificando las medias por grupo.

## 2 · Autoevaluación con la rúbrica

| Criterio | Nivel (1–4) | Prueba (una frase concreta) |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Matriz escalada `X` (1200×7) verificada con media 0, desviación 1 y óptimo $k=4$ (silueta 0,431). |
| Reproducibilidad | 4 | Cuaderno ejecutado de principio a fin con `SEMILLA = 42` sin errores. |
| Análisis y comunicación al cliente | 4 | Tabla de 4 segmentos redactada con tamaño, rasgos clave y acción comercial concreta. |
| IA responsable | 4 | Revisión de riesgos de discriminación al aplicar descuentos por perfil estadístico. |

## 3 · Mi uso de la IA

- **Qué pedí:** Ayuda para estructurar el bucle de cálculo de siluetas entre $k=2$ y $k=8$.  
- **Qué comprobé:** Ejecuté la celda en Colab y validé todos los `assert` y gráficos de calor.  
- **¿Sé explicar cada línea de mi parte?** Sí.

## 4 · Coevaluación

| Compañero/a | Aportación (1–4) | Ejemplo concreto |
| :---- | :---- | :---- |
| Miguel | 4 | Desarrolló todo el análisis PCA 2D y la interpretación de las cargas de los componentes. |
| Fran | 4 | Implementó el recomendador item-item y la función `recomendar(..., P=P_item)`. |
| Andri | 4 | Redactó el análisis de arranque en frío, sesgo de popularidad y cumplimiento RGPD. |
| Anzhela | 4 | Consolidó `informe_huespedes.md`, verificó la reproducibilidad y organizó el `README.md`. |

## 5 · Mejora para el próximo sprint

Documentar directamente en celdas Markdown del cuaderno las conclusiones de cada gráfico conforme se generan.