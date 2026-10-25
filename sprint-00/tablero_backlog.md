# 5Green · Tablero de Trello y backlog del curso

**Enlace al tablero:** [pegar aquí el enlace de Trello] · **Responsable de mantenerlo al día:** el Scrum Master de cada sprint (S0: Anzhela).

## 1. Cómo montar el tablero (10 minutos)

1. En Trello: **Crear tablero** → nombre `5Green · TurisData Canarias`. Lo más rápido es **copiar el tablero plantilla del curso** si el docente lo ha compartido.
2. Crear estas **7 columnas**, en este orden:

| # | Columna | Qué va ahí |
|---|---|---|
| 1 | **Información** | Tarjetas fijas: acuerdo, DoD, enlace a GitHub, roles, calendario |
| 2 | **Backlog del curso** | Una tarjeta por reto (épica) de los sprints 1–17, ordenadas por prioridad |
| 3 | **Por hacer (sprint actual)** | Historias del sprint en curso, ya repartidas |
| 4 | **En curso** | Lo que se está haciendo ahora (máx. 2 tarjetas por persona) |
| 5 | **En revisión** | Esperando la revisión cruzada de otra persona |
| 6 | **Hecho** | Cumple las 8 casillas de la DoD |
| 7 | **Bloqueos** | Algo impide avanzar: se avisa en la daily |

3. Crear las **etiquetas**:

| Color | Etiqueta |
|---|---|
| 🟢 Verde | Sprint 0 |
| 🔵 Azul | Sprint 1 |
| 🟠 Naranja | Sprint 2 |
| 🟣 Morado | Sprint 3 |
| 🔴 Rojo | IA responsable / riesgo |
| 🟡 Amarillo | Ceremonia (planning, review, retro) |
| ⚫ Negro | Bloqueado |

4. Añadir a cada tarjeta: **miembro responsable**, **fecha**, etiqueta y, al terminar, el **enlace al archivo en GitHub**.

## 2. Tarjetas de la columna «Información»

| Tarjeta | Contenido |
|---|---|
| 📜 Acuerdo de trabajo | Enlace a `sprint-00/acuerdo_trabajo.md` |
| ✅ Definition of Done | Las 8 casillas (enlace a `sprint-00/definition_of_done.md`) |
| 👥 Equipo y roles | S0: SM Anzhela · Téc. Fran. S1: SM Miguel · Téc. Andrii. S2: SM Cristina · Téc. Anzhela. S3: SM Andrii · Téc. Miguel |
| 🔗 Repositorio GitHub | Enlace al repositorio privado `ifcd107-equipo-5green` |
| 📅 Calendario | S0 16–19/10 · S1 20–21/10 · S2 22–23/10 · S3 26–27/10 · Brief 26/11 · Memoria 10/12 · Defensa 14/12 |
| 🧭 Cliente | TurisData Canarias. HMW priorizada: anticipar las cancelaciones |

## 3. Backlog del curso (priorizado y estimado)

Estimación en **puntos de historia** (escala Fibonacci 1, 2, 3, 5, 8, 13): mide el esfuerzo relativo, no las horas.

| Prio | Sprint | Reto (épica) | Entregable | Estado | Puntos |
|---|---|---|---|---|---|
| 1 | 0 | Constituir la consultora | Tablero + acuerdo + DoD + mapa de empatía y 3 HMW | Hecho | 8 |
| 2 | 1 | Auditoría de oportunidades de IA | Informe (2–3 pág., 7 apartados) + checklist ético v1 + piloto ≤ 15.000 € | Hecho | 13 |
| 3 | 2 | ¿Nos fiamos de este informe? | Dictamen de auditoría + hojas de ejercicios (mín. 8/12 y 10/14) | En curso | 13 |
| 4 | 3 | Primer modelo en producción | Informe del mejor modelo + evidencia de llamada a la API + informe de costes y cierre | Por hacer | 13 |
| 5 | 4 | Herramientas internas | Repositorio con README y pruebas | Pendiente | 8 |
| 6 | 5 | ¿La ocupación depende de esto? | Notebook con gradiente + análisis estadístico + BD poblada | Pendiente | 13 |
| 7 | 6 | Datos sucios, cliente impaciente | Notebook de EDA + pipeline + informe de defectos | Pendiente | 13 |
| 8 | 7 | Precio y cancelación | Informe de modelado con recomendación | Pendiente | 13 |
| 9 | 8 | Duelo de modelos | Leaderboard + ficha del modelo | Pendiente | 8 |
| 10 | 9 | Conocer al huésped | Segmentos interpretados + prototipo de recomendador | Pendiente | 8 |
| 11 | 10 | ¿Vale la pena la red? | Notebook + informe comparativo | Pendiente | 8 |
| 12 | 11 | Visión artificial para el cliente | Modelo + demostrador + análisis de errores | Pendiente | 13 |
| 13 | 12 | Escuchar al cliente | Informe de reseñas + serie temporal + demo del asistente | Pendiente | 13 |
| 14 | 13 | Informe visual para dirección | Informe de una página | Pendiente | 5 |
| 15 | 14–17 | Proyecto de cierre (brief a elegir) | Ficha, EDA, modelos, demostrador, memoria, defensa | Pendiente | 21 |

**Hitos fijos:** elección de brief 26/11 · ficha aprobada 27/11 · congelación del repositorio y memoria 10/12, 14:30 · ensayo 11/12 · defensa 14/12 (a confirmar por el docente).

## 4. Historias de usuario detalladas

### Sprint 0 · Constituir la consultora (16–19/10)

| Id | Historia | Criterio de aceptación | Responsable | Puntos |
|---|---|---|---|---|
| S0-1 | Como equipo queremos un tablero con el backlog para ver qué hay que hacer | 7 columnas, etiquetas y backlog priorizado | Cristina | 2 |
| S0-2 | Como equipo queremos un acuerdo de trabajo para evitar conflictos | 10 reglas comprobables, firmado por las 5 personas | Miguel | 1 |
| S0-3 | Como equipo queremos una DoD para saber cuándo algo está terminado | 8 criterios de sí/no | Fran | 1 |
| S0-4 | Como consultora queremos entrevistar al cliente para entender su problema | Notas con frases literales y (?) en las suposiciones | Anzhela | 2 |
| S0-5 | Como consultora queremos un mapa de empatía y 3 HMW para enfocar el problema | 2 dolores, 2 ganancias, POV, 3 HMW y priorización | Andrii | 2 |

### Sprint 1 · Auditoría de oportunidades de IA (20–21/10)

| Id | Historia | Criterio de aceptación | Responsable | Puntos |
|---|---|---|---|---|
| S1-1 | Como consultora quiero listar unas 8 ideas de IA para TurisData y quedarme con 5 (2 inventadas por nosotros) | Lista con dolor, dato necesario y dueño | Todo el equipo | 3 |
| S1-2 | Como consultora quiero una ficha por caso con problema, tipo de dato, tipo de aprendizaje y algoritmo | Tabla con ≥ 3 modalidades de dato y 1 caso sin IA, revisada por otra persona | Miguel · Andrii | 3 |
| S1-3 | Como responsable de IA responsable quiero pasar el checklist ético a cada caso | Checklist v1 con ≥ 1 riesgo específico por caso y semáforo | Anzhela | 3 |
| S1-4 | Como Product Owner quiero un informe de 2–3 páginas con 7 apartados para decidir por dónde empezar | Matriz impacto × facilidad y recomendación clara | Cristina | 3 |
| S1-5 | Como cliente quiero una propuesta de piloto de hasta 15.000 € | Piloto con duración, coste y datos necesarios | Fran | 1 |

### Sprint 2 · ¿Nos fiamos de este informe? (22–23/10)

| Id | Historia | Criterio de aceptación | Responsable | Puntos |
|---|---|---|---|---|
| S2-1 | Como consultora quiero leer el borrador del cliente y detectar el error de cada una de las 6 afirmaciones | Cada afirmación con su error nombrado | Andrii · Miguel | 3 |
| S2-2 | Como responsable técnica quiero rehacer los cálculos con las 2.400 reservas | Cálculos reproducibles (calculadora u hoja de cálculo) | Cristina | 5 |
| S2-3 | Como Product Owner quiero un dictamen de 2–3 páginas con veredicto por afirmación (fiable · parcialmente · no fiable · no se puede saber) y una recomendación sobre el canal | Dictamen revisado por otra persona | Anzhela | 3 |
| S2-4 | Como equipo queremos completar las hojas de ejercicios | Mínimo 8/12 y 10/14 aciertos | Todo el equipo | 2 |

### Sprint 3 · Primer modelo en producción (26–27/10)

| Id | Historia | Criterio de aceptación | Responsable | Puntos |
|---|---|---|---|---|
| S3-1 | Como consultora quiero explorar los datos con SQL y decidir qué predecir | Consulta documentada y variable objetivo definida | Miguel | 2 |
| S3-2 | Como responsable técnico quiero quitar las columnas «trampa» (fuga de datos) | Lista de columnas eliminadas y por qué | Andrii | 2 |
| S3-3 | Como consultora quiero lanzar un experimento de AutoML y comparar modelos | Tabla comparativa con métrica y criterio de elección | Fran | 3 |
| S3-4 | Como Product Owner quiero un umbral de alerta pensado en dinero | Umbral justificado con el coste de FP y FN | Cristina | 2 |
| S3-5 | Como cliente quiero consultar el modelo desde otra aplicación | Evidencia de una llamada real a la API | Fran · Andrii | 2 |
| S3-6 | Como Product Owner quiero un informe de recursos y costes, con prueba del cierre | Informe con costes y captura de los recursos borrados | Anzhela | 2 |

## 5. Ritmo de cada sprint

Planning → Trabajo en equipo (con daily) → Revisión cruzada + DoD → Review (5 min por equipo) → Retro
