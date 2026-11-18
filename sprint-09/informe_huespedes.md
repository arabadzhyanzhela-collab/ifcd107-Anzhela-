# Informe Ejecutivo: Conocer al Huésped y Personalizar Experiencias

Fecha : 16 \- 17.11.2026&nbsp;

Scrum master Cristina, Tecnico Francis&nbsp;

**Cliente:** TurisData Canarias · **Consultora:** Equipo 5 Green · **Sprint:** 09

---

## 1\. Resumen Ejecutivo

Hasta ahora, TurisData Canarias enviaba la misma comunicación comercial a sus 1.200 huéspedes. Mediante técnicas de aprendizaje no supervisado (**k-means** y **PCA**) hemos identificado **4 segmentos de clientes claramente diferenciados** y hemos desarrollado un **motor de recomendación personalizado (item-item)** para las 25 experiencias turísticas del catálogo. Esta estrategia permite sustituir las campañas genéricas por ofertas relevantes para cada perfil y mejorar la conversión sin saturar al cliente.

&nbsp;

## 2\. Segmentación de Huéspedes (4 Perfiles)

Tras estandarizar las 7 variables de comportamiento y evaluar valores de $k$ entre 2 y 8, el óptimo estadístico y de negocio se sitúa en **$k=4$ grupos** (coeficiente de silueta \= **0,431**), validado visualmente mediante proyección PCA 2D (68,7 % de varianza explicada).

| Grupo | Nombre del Segmento | Tamaño | Rasgos distintivos (medias) | Acción comercial recomendada | Experiencia estrella&nbsp; |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **0** | **Escapadas cortas** | 194 (16,2 %) | 2,6 noches, baja antelación, 4,0 reservas/año | Alertas de última hora (*flash deals*) para fines de semana y escapadas exprés. | *Dato no especificado en el informe* (ofertas exprés de fin de semana)&nbsp; |
| **1** | **Familias** | 402 (33,5 %) | 91 % viaja con niños, 110 días de antelación | Paquetes familiares con reserva anticipada y entradas combinadas a parques temáticos. | **Parques temáticos** (entradas combinadas)&nbsp; |
| **2** | **Descanso premium** | 317 (26,4 %) | 57 años de media, gasto alto (211,4 €/día) | Experiencias gastronómicas, bienestar/spa y excursiones privadas de baja exigencia física. | Gastronomía, bienestar/spa y excursiones privadas&nbsp; |
| **3** | **Aventureros** | 287 (23,9 %) | 29 años de media, 74,6 % de gasto en actividades | Packs multiaventura (Teide, parapente, deportes acuáticos) con descuentos por volumen. | **Teide, parapente y deportes acuáticos**&nbsp; |

&nbsp;

## 3\. Sistema de Recomendación de Experiencias

Comparamos el modelo base de **Popularidad** (recomendar a todos lo más valorado) frente al **Filtrado Colaborativo Item-Item** (basado en similitud coseno sobre residuos de valoración):

| Método | Error de predicción (RMSE) | Acierto en Top-3 (`precision@3`) | Capacidad de personalización |
| :---- | :---- | :---- | :---- |
| **Popularidad (Baseline)** | 1,029 estrellas | 0,125 | Nula (misma lista para todos) |
| **Colaborativo Item-Item** | **0,895 estrellas** | **0,171** | **Alta** (adaptada al historial previo) |

- **Conclusión técnica:** El modelo **item-item** reduce el error medio en 0,134 estrellas y aumenta un **36,8 %** la tasa de acierto en las 3 primeras recomendaciones (`precision@3`), evitando además volver a sugerir actividades que el huésped ya ha valorado.

&nbsp;

## 4\. IA Responsable, Sesgos y Cumplimiento RGPD

1. **Arranque en frío (*Cold Start*):** Para huéspedes nuevos sin valoraciones previas, el sistema aplica automáticamente el recomendador por **popularidad** (o filtrado por categoría declarada en el *check-in*). Para experiencias nuevas sin valoraciones, se emplea similitud por **contenido** (categoría e isla).  
2. **Mitigación del sesgo de popularidad:** Para evitar que los proveedores locales pequeños queden invisibles frente a actividades estrella como el Parque Timanfaya, se reserva 1 de los 3 huecos de recomendación (*slot* de exploración) a experiencias bien valoradas de baja exposición.  
3. **Privacidad y RGPD:** Los perfiles de segmentación y recomendación utilizan exclusivamente identificadores seudonimizados (`id_huesped`, `id_usuario`) e historial interno de reservas/valoraciones (principio de minimización). Se informa al cliente en la política de privacidad sobre el perfilado comercial con opción clara de exclusión (*opt-out*).