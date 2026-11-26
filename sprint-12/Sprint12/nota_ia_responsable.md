# Nota de IA responsable

- **Equipo:** 5 Green  
- **Integrantes:** Cristina, Miguel, Fran, Andri, Anzhela  
- **Contexto:** TurisData Canarias  
- **Fecha:** 24-25.11.2026  
- **scrum master** Miguel, técnico Anzela&nbsp;

## Riesgos y medidas

| Riesgo | Medida que aplicamos |
| :---- | :---- |
| El asistente inventa una respuesta (alucinación) | Umbral de puntuación: si el fragmento recuperado no es suficientemente parecido, responde "No consta en la política". Además, citamos siempre la fuente \[1\]. |
| El asistente obedece órdenes escondidas en un texto (prompt injection) | Filtro `es_seguro()` que bloquea frases como "ignora las instrucciones". Probamos 3 ataques y el filtro bloqueó los 3\. |
| Se filtran datos personales de huéspedes | No subimos reseñas con nombres ni emails a ningún servicio externo. Todo se ejecuta en local. |
| Sesgos en el análisis de sentimiento | Revisamos a mano una muestra de 20 reseñas para comprobar que el modelo no clasifica mal por el tono. |

## Qué NO cubre esta nota

- El generador de respuestas es un **simulador** (no un LLM real). En producción habría que repetir las pruebas con el modelo real.  
- El filtro de seguridad es básico; un atacante con frases distintas podría colarse.

## Datos

Todos los datos usados son sintéticos y del curso. No hay claves en el código ni en el repositorio.