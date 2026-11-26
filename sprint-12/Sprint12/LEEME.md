# Sprint 12 ·&nbsp;

- **Equipo:** 5 Green  
- **Integrantes:** Cristina, Miguel, Fran, Andri, Anzhela  
- **Contexto:** TurisData Canarias  
- **Fecha:** 24-25.11.2026  
- **scrum master** Miguel, técnico Anzela&nbsp;

## Cómo ejecutar todo (5 líneas)

1. Los datos van a `data/` (`resenas.csv`, `ocupacion_diaria.csv`, `politica_alojamiento.md`, `preguntas_referencia.csv`). Si faltan, la primera celda de cada cuaderno los descarga.  
2. Ejecutar en orden: `resenas.ipynb` → `ocupacion.ipynb` → `asistente_rag.ipynb`. Cada uno con *Reiniciar y ejecutar todo*.  
3. `resenas.ipynb` genera `grafico_resenas.png`. `asistente_rag.ipynb` genera `evaluacion_asistente.csv`.  
4. Resultados esperados: exactitud de sentimiento ≈0.99; MAE del baseline ≈4.4; asistente con 24/25 aciertos y 0 alucinaciones; 3 ataques bloqueados por el filtro.  
5. Semilla `SEMILLA = 42`. Versiones: Python 3.13, numpy 2.5.3, pandas 2.3.3, scikit-learn 1.9.1, statsmodels 0.15.0.

## Revisión con la rúbrica

Revisado por: Anzhela (no escribió el informe). Fecha: 23/11/2026.

| Criterio | Nivel (1-4) | Prueba |
| :---- | :---- | :---- |
| Corrección técnica | 3 | El baseline tiene MAE; el asistente cita y dice "No consta"; 25 preguntas evaluadas; 3 ataques probados. |
| Reproducibilidad | 3 | Reiniciar y ejecutar todo da los mismos números. |
| Análisis y comunicación | 3 | Informe con 3 recomendaciones ejecutables y límites explicados. |
| IA responsable | 3 | Cada riesgo tiene su medida; el filtro bloqueó 3 de 3 ataques. |

**Lo primero que mejoraríamos:** probar el asistente con un LLM real y medir el filtro con más ataques.