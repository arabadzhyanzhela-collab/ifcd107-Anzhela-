# Sprint 9 · Reto «Conocer al huésped» · Equipo 5 Green

Fecha : 16 \- 17.11.2026&nbsp;

Scrum master Cristina, Tecnico Francis&nbsp;

**Equipo:** Cristina, Miguel, Fran, Andri y Anzhela&nbsp;

**Curso:** Especialista en Inteligencia Artificial (IFCD107)  
**Repositorio del Sprint:** Carpeta `sprint-09/` del repositorio privado del equipo.

## Qué se entrega

| Fichero | Contenido |
| :---- | :---- |
| `reto_S09.ipynb` | Cuaderno principal del reto: segmentación de huéspedes (k-means, PCA), sistema de recomendación de experiencias (popularidad vs. item-item) y prototipo Q-learning |
| `informe_huespedes.md` | Informe ejecutivo para TurisData con los 4 perfiles de clientes, acciones comerciales, comparativa del recomendador y análisis de IA responsable |
| `README.md` | Este fichero con instrucciones de reproducción y reparto del equipo |
| `autoevaluacion_<nombre>.md` | Hojas individuales de autoevaluación y coevaluación de los 5 integrantes |

Los datos **no se suben** al repositorio: el cuaderno descarga automáticamente `huespedes.csv`, `experiencias.csv` y `valoraciones_experiencias.csv` desde el repositorio oficial del curso.

## Resultados principales

- **Segmentación (`k = 4`, silueta \= `0,431`):**  
  1. **Escapadas cortas (194 huéspedes):** Estancias breves (2,6 noches), poca antelación y alta frecuencia anual (4,0 reservas/año).  
  2. **Familias (402 huéspedes):** El 91 % viaja con niños, planifican con gran antelación (110 días).  
  3. **Descanso premium (317 huéspedes):** Mayor edad media (57 años) y gasto diario elevado (211,4 €/día).  
  4. **Aventureros (287 huéspedes):** Perfil joven (29 años) que destina el 74,6 % de su gasto extra a actividades.  
- **Reducción dimensional (PCA):** Con 2 componentes se conserva el `68,7 %` de la varianza para visualización 2D; con 5 componentes se alcanza el `93,8 %` (superando el umbral del 90 % y manteniendo `ARI = 1,00`).  
- **Recomendador de experiencias:** El filtrado colaborativo **item-item** reduce el RMSE de `1,029` (popularidad) a `0,895` y mejora `precision@3` de `0,125` a `0,171`.

## Cómo reproducirlo

1. Abrir `reto_S09.ipynb` en [Google Colab](https://colab.research.google.com).  
2. Ejecutar *Entorno de ejecución → Reiniciar y ejecutar todo* (no requiere instalaciones adicionales).  
3. **Semilla fija:** `SEMILLA = 42`.  
4. **Versiones de entorno:** Python 3.12 · scikit-learn 1.6+ · pandas 2.2+ · numpy 2.0+ · matplotlib / seaborn.

## Quién hizo qué

| Parte | Responsable | Revisión |
| :---- | :---- | :---- |
| Segmentación (k-means, silueta y perfiles) | Cristina | Miguel |
| Proyección PCA 2D e interpretación de cargas | Miguel | Fran |
| Recomendador (popularidad vs. item-item y `recomendar`) | Fran | Andri |
| IA responsable (arranque en frío, sesgo y RGPD) | Andri | Anzhela |
| Consolidación de `informe_huespedes.md` y `README.md` | Anzhela | Cristina |

## Uso de IA

- **Qué se pidió:** Apoyo en la redacción ejecutiva del informe para TurisData y estructuración de plantillas Markdown.  
- **Qué se comprobó y cambió:** Todas las métricas (`silueta = 0,431`, `RMSE = 0,895`, `precision@3 = 0,171`, `ARI = 1,00`) y listas de recomendación (`P=P_item`) fueron ejecutadas y verificadas directamente en Google Colab.