# Autoevaluación y coevaluación · Sprint 9 · Miguel

**Equipo:** 5 Green · **Persona:** Miguel · **Reto:** «Conocer al huésped»

## 1 · Qué he hecho yo en este sprint

- **Partes trabajadas:** Reducción dimensional con PCA (varianza acumulada, proyección 2D coloreada por segmento, cargas y verificación ARI con 5 componentes).  
- **Commits realizados:** `feat(S09): analisis PCA 2D y cargas de componentes`&nbsp;  
- **Qué he aprendido:** A interpretar el porcentaje de varianza explicada y cómo leer las cargas opuestas en el primer componente principal.  
- **Qué me ha costado y cómo lo resolví:** Entender por qué con 4 componentes no se llega al 90 % (89,8 %) y se necesitan 5 (93,8 %); lo comprobé con `np.cumsum`.

## 2 · Autoevaluación con la rúbrica

| Criterio | Nivel (1–4) | Prueba (una frase concreta) |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Proyección 2D (68,7 % varianza) y clustering con 5 componentes (`ARI = 1,00`) validados sin errores. |
| Reproducibilidad | 4 | Todas las figuras incluyen etiquetas con el porcentaje de varianza y usan `SEMILLA = 42`. |
| Análisis y comunicación al cliente | 4 | Explicación clara de por qué 2 componentes sirven para visualizar pero no para modelos predictivos. |
| IA responsable | 4 | Advertencia sobre la pérdida de interpretabilidad directa al transformar variables originales en componentes. |

## 3 · Mi uso de la IA

- **Qué pedí:** Sintaxis para añadir leyendas automáticas de segmentos en el gráfico `scatter` de Matplotlib.  
- **Qué comprobé:** Verifiqué que los 4 grupos aparecieran bien diferenciados en el mapa 2D.  
- **¿Sé explicar cada línea de mi parte?** Sí.

## 4 · Coevaluación

| Compañero/a | Aportación (1–4) | Ejemplo concreto |
| :---- | :---- | :---- |
| Cristina | 4 | Construyó la matriz escalada y obtuvo los 4 perfiles de clientes con k-means. |
| Fran | 4 | Evaluó RMSE y `precision@3` comparando popularidad frente a item-item. |
| Andri | 4 | Aportó soluciones claras al problema de arranque en frío y sesgo de proveedores. |
| Anzhela | 4 | Revisó todas las cifras del informe ejecutivo y estructuró la entrega en GitHub. |

## 5 · Mejora para el próximo sprint

Preparar desde el primer día la estructura conjunta del cuaderno del reto para evitar conflictos al fusionar cambios.