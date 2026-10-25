# Checklist de IA responsable · versión 1

**Se rellena por cada caso de uso** del informe de oportunidades (M8, UD 8.5). Es la **versión 1**: **se reutiliza y se actualiza en el proyecto final** (Sprints 14-16, requisito R6). Guardadla en el repositorio del equipo con un control de versiones (`checklist_etico_v1.md`, luego `v2`…).

**Caso de uso evaluado:** Predicción de cancelaciones de reservas (HMW 1\) · **Equipo:** 5Green · **Fecha:** 23/10/2026 · **Elaborado por:** Miguel y Andrii · **Revisado por (otra persona):** Anzhela

## Cómo se usa

1. Respondéis a cada punto con **Sí / No / No aplica / No lo sé**.  
2. Escribid una **evidencia o una acción** (algo comprobable): "no lo sé" no es una respuesta válida en la versión final: hay que averiguarlo o marcarlo como riesgo abierto.  
3. Al final, asignad un **semáforo**: verde (se puede avanzar), ámbar (con medidas), rojo (no avanzar sin cambios).  
4. Cada "No" o "No lo sé" en puntos marcados con **(★)** se lleva a la tabla de riesgos.

## 0\. Ficha rápida del caso

| Pregunta | Respuesta |
| :---- | :---- |
| ¿Qué problema de negocio resuelve? | Predice la probabilidad de cancelación de reservas y habitaciones vacías a última hora. |
| ¿Quién usa el resultado y quién se ve afectado por él? | Lo usa el equipo comercial y de operaciones de TurisData Canarias; afecta a los huéspedes con reservas (pueden recibir un contacto o una oferta). |
| ¿La IA **decide** o **apoya** a una persona que decide? | **Apoya** a una persona (el equipo comercial decide si aplica una tarifa especial o contacta al cliente). |
| ¿Qué pasa si se equivoca? ¿quién sufre el error y cómo de grave es? | Si predice un falso positivo, se contacta a un cliente que no iba a cancelar (molestia menor). Si es un falso negativo, la habitación queda vacía (pérdida económica moderada). |

## 1\. Propósito y proporcionalidad

| \# | Pregunta | S/N/NA/? | Evidencia o acción |
| :---- | :---- | :---- | :---- |
| 1.1 (★) | ¿El problema es **real y está explicado** con datos o testimonios del cliente? | Sí | Entrevista del 16/10 con el Director General: 2.400 cancelaciones registradas; quiere «reducir las cancelaciones» porque las de última hora pueden dejarlos sin ingresos. |
| 1.2 | ¿Es necesaria la IA o basta con una regla sencilla? | Sí | Una regla simple no contempla las múltiples variables (antelación, canal, importe, estacionalidad); se requiere ML. |
| 1.3 (★) | ¿El beneficio esperado **justifica el riesgo** para las personas? | Sí | El riesgo de privacidad es bajo y el beneficio económico es directo para la sostenibilidad del negocio. |
| 1.4 | ¿Hay una alternativa menos invasiva que consiga casi lo mismo? | No | Las políticas de cancelación rígidas actuales ya se aplican y no resuelven la anticipación de la pérdida. |

## 2\. Datos y privacidad

| \# | Pregunta | S/N/NA/? | Evidencia o acción |
| :---- | :---- | :---- | :---- |
| 2.1 (★) | ¿Sabemos **qué datos** usa, de dónde vienen y con qué **licencia o base legal**? | Sí | Datos históricos internos de reservas propiedad de la empresa (ejecución de contrato). |
| 2.2 (★) | ¿Hay **datos personales**? ¿Se usan solo los necesarios? (minimización) | Sí | Se usan identificadores de cliente y datos de estancia; se deben excluir nombres y datos de contacto directos |
| 2.3 | ¿Hay datos de **menores** o categorías especiales (salud, biometría, creencias)? | No | Ninguno de estos datos forma parte de los registros de reservas hoteleras |
| 2.4 (★) | ¿Se informa a las personas y se respeta la **finalidad** original del dato? | Sí | Según el cliente, «los datos personales no se usarán para otra cosa»; el uso para predecir cancelaciones debe estar cubierto por su política de privacidad (pendiente de confirmar con TurisData). |
| 2.5 | ¿Están **anonimizados o seudonimizados**? ¿Se definió el plazo de conservación? | No lo sé | Falta auditar el estado actual de anonimización en la base de datos operativa y los plazos exactos de retención. *(★ RIESGO)* |
| 2.6 | ¿Se usan servicios de terceros o de IA en la nube? ¿Hay contrato y control de dónde van los datos? | No aplica | El desarrollo se realiza localmente y en entornos de prueba controlados sin volcado a APIs comerciales externas de pago. |
| 2.7 | ¿Puede una persona ejercer sus derechos (acceso, rectificación, supresión, oposición)? | Sí | A través de los canales de atención al cliente y soporte de la empresa estipulados por el marco RGPD |

## 3\. Sesgo y equidad

| \# | Pregunta | S/N/NA/? | Evidencia o acción |
| :---- | :---- | :---- | :---- |
| 3.1 (★) | ¿Los datos de entrenamiento **representan** a las personas a las que se aplicará? ¿quién falta? | Sí | Representan el histórico de las islas (Tenerife, Gran Canaria, La Palma); falta evaluar si faltan perfiles de temporada baja extrema. |
| 3.2 (★) | ¿Hay variables sensibles o **proxies** (código postal, país, apellido, edad, sexo)? | No lo sé | Es necesario revisar las bases de datos |
| 3.3 | ¿Se evaluará el rendimiento **por grupos** (no solo la media)? ¿con qué métrica? | No | Se planteó métrica global |
| 3.4 | ¿Las etiquetas reflejan una **realidad** o decisiones humanas anteriores potencialmente sesgadas? | Sí | Reflejan el estado final real de la reserva extraído directamente del sistema de gestión (PMS). |
| 3.5 | ¿Hay un plan si aparece un sesgo (corregir, limitar el uso, retirar)? | No | No se ha redactado un protocolo formal de actuación ante sesgos algorítmicos en las predicciones. *(★ RIESGO)* |

4\. Transparencia y explicabilidad

| \# | Pregunta | S/N/NA/? | Evidencia o acción |
| :---- | :---- | :---- | :---- |
| 4.1 (★) | ¿Las personas saben que **interactúan con IA** o que una IA interviene en una decisión? | No aplica | el cliente final no recibe resoluciones automáticas directas. |
| 4.2 | ¿Se puede **explicar** el resultado en lenguaje sencillo (qué factores pesan)? | Sí | se pueden extraer los factores de peso principales (antelación, tipo de tarifa). |
| 4.3 | ¿Se documenta **qué hace el sistema y qué no** (límites, casos donde falla)? | Sí | Se incluirá en una memoria técnica |
| 4.4 | ¿Los contenidos generados por IA están **etiquetados**? | No aplica | No se generan contenidos automáticos de texto o creatividades dirigidos al usuario final. |

## 5\. Supervisión humana y decisiones automatizadas

| \# | Pregunta | S/N/NA/? | Evidencia o acción |
| :---- | :---- | :---- | :---- |
| 5.1 (★) | ¿Hay una **persona con capacidad real** de revisar y cambiar el resultado? | Sí | El gestor comercial decide manualmente si contacta al huésped o aplica una contraoferta basada en la alerta del sistema. |
| 5.2 (★) | ¿La decisión tiene efectos **significativos** (dinero, acceso, empleo)? Si es así, ¿existe vía de reclamación? | Sí | Implica ofertas comerciales y condiciones de estancia; los canales habituales de atención al cliente cubren cualquier aclaración. |
| 5.3 | ¿Se puede **desactivar** el sistema con rapidez si algo va mal? | Sí | Al ser una herramienta interna y local, el script se puede detener de forma inmediata si surge cualquier problema. |
| 5.4 | ¿Se forma al personal para que **no confíe ciegamente** en el sistema? | No (previsto) | Está previsto hacer una sesión de formación interna para explicar los límites del modelo al personal antes de ponerlo en marcha. |

## 6\. Robustez, seguridad y calidad

| \# | Pregunta | S/N/NA/? | Evidencia o acción |
| :---- | :---- | :---- | :---- |
| 6.1 | ¿Se ha **medido** el error con datos que el modelo no ha visto? | Sí | Se comprobará usando datos independientes que el modelo no ha visto antes (con técnicas de validación cruzada y un conjunto de prueba) . |
| 6.2 | ¿Se sabe qué pasa con datos raros, incompletos o de otro año? | No lo sé | Falta comprobar cómo reacciona el sistema ante datos extraños, incompletos o de otros años  *(★ RIESGO)* |
| 6.3 | ¿Hay medidas ante **ataques o abusos** (inyección de instrucciones, fuga de datos)? | Sí | Control estricto de accesos al repositorio Github e impedimento de subida de claves o datos sin filtrar a la nube pública. |
| 6.4 | Está previsto **monitorizar** el sistema tras ponerlo en marcha (deriva de datos, errores)? | No | Al tratarse de un prototipo o proyecto piloto, vigilar el sistema a largo plazo no está incluido en esta primera fase. |

## 7\. Impacto social y ambiental

| \# | Pregunta | S/N/NA/? | Evidencia o acción |
| :---- | :---- | :---- | :---- |
| 7.1 | ¿Cómo afecta a las **personas empleadas** (tareas, formación, puestos)? | Sí | Reduce las tareas manuales de revisar agendas, ahorrando tiempo al equipo comercial para que se enfoque en tareas más importantes |
| 7.2 | ¿Puede tener un efecto negativo en el **territorio o la comunidad** (precios de vivienda, presión turística)? | No | El sistema optimiza la ocupación de alojamientos ya existentes sin incrementar la presión turística ni la planta alojativa. |
| 7.3 | ¿Es proporcionado el **coste de computación** y energía? | Sí | Los modelos clásicos de Machine Learning seleccionados consumen recursos mínimos de computación. |

## 8\. Normativa (orientación; no sustituye el asesoramiento legal)

| \# | Pregunta | S/N/NA/? | Evidencia o acción |
| :---- | :---- | :---- | :---- |
| 8.1 (★) | ¿Aplica el **RGPD/LOPDGDD**? ¿Hace falta una evaluación de impacto? | Sí | Aplica RGPD por tratamiento de datos de reservas de clientes; se comprobará la necesidad formal de EIPD |
| 8.2 (★) | Nivel de riesgo aproximado según el **AI Act**: inaceptable / alto / transparencia (limitado) / mínimo | Sí | **Riesgo Mínimo**: Sistema de soporte a la decisión interna sin afectar derechos fundamentales |
| 8.3 | ¿Qué obligaciones de esa clase se aplican y **desde cuándo**? **\[verificar calendario vigente antes de impartir\]** | Sí | Se comprobarán las normas que se aplican en España y sus fechas clave durante la primera parte del proyecto |
| 8.4 | ¿Hay otras normas (consumo, propiedad intelectual, sectoriales)? | No | No se identifican normativas específicas más allá de las habituales de alojamientos turísticos. |

## 9\. Gobernanza y responsabilidad

| \# | Pregunta | S/N/NA/? | Evidencia o acción |
| :---- | :---- | :---- | :---- |
| 9.1 (★) | ¿Hay una **persona responsable** del sistema y de sus efectos? | Sí | Responsable de IA responsable del equipo: Anzhela; por parte del cliente, el Director General (a confirmar). |
| 9.2 | ¿Se registra quién decidió qué y cuándo (trazabilidad, versiones del modelo y de los datos)? | Sí | Mediante el control de versiones en GitHub y la documentación de métricas correspondientes. |
| 9.3 | ¿Hay un canal para **quejas y errores**? | Sí | Canal interno del equipo y reporte de incidencias mediante los issues de GitHub |
| 9.4 | ¿Se ha pedido opinión a las **personas afectadas**? | Sí | Se han tomado como base los dolores expresados directamente por el Director General en la entrevista del 16/10. |

## 10\. Resultado

**Tabla de riesgos** (una fila por cada ★ con "No" o "No lo sé", más los que detectéis):

| Riesgo | Probabilidad (B/M/A) | Impacto (B/M/A) | Medida propuesta | Responsable | Semáforo de riesgos |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1\. Desconocimiento del estado de anonimización y plazos de conservación de los datos (2.5) | M | M | Revisar los datos del archivo, proteger la información personal y borrar lo que no sirva antes de entrenar el sistema. | Fran | \[X\] Ámbar (avanzar con medidas) |
| 2\. Posible presencia de variables sensibles o proxies (código postal/país) en los datos (3.2) | M | A | Revisar bien el listado de datos y quitar cualquier variable que pueda causar discriminación antes de crear el modelo | Miguel | \[X\] Ámbar (avanzar con medidas) |
| 3\. Ausencia de un protocolo formal ante sesgos en las predicciones (3.5) | B | M | Escribir una norma sencilla para que una persona revise manualmente cuando el sistema falle. | Anzhela | \[X\] Ámbar (avanzar con medidas) |
| 4\. Comportamiento del modelo ante datos incompletos o atípicos (6.2) | M | M | Preparar el programa para que sepa rellenar o manejar esos huecos vacíos sin romperse | Andrii | \[X\] Ámbar (avanzar con medidas) |



**Semáforo:** \[ \] Verde (avanzar) · \[X\] Ámbar (avanzar con medidas) · \[ \] Rojo (no avanzar sin cambios)



**Justificación en 3 líneas:** El caso es viable y cuenta con un beneficio de negocio claro, pero presenta riesgos moderados en la privacidad de los datos y en el control de posibles variables proxy que debemos disminuir antes de entrenar los modelos supervisados.

**Qué actualizaremos en el proyecto final:** En la versión 2 para el proyecto final, validaremos la efectividad real del modelo con datos actualizados de TurisData y documentaremos la ausencia definitiva de sesgos discriminatorios por origen o nacionalidad.

## Consejos

- Un **checklist no es un trámite**: si todo es "Sí" sin evidencia, no se ha hecho.  
- Rellenad el checklist **con otra persona** que no haya diseñado el caso.  
- Priorizad las preguntas (★): con poco tiempo, empezad por ellas.  
- Guardad esta versión: en el proyecto final se pide **actualizarla** y demostrar qué medidas se aplicaron y cómo se evaluaron.  
- 