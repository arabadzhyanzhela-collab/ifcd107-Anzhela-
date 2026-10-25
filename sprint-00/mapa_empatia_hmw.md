# 5Green · Entrevista, mapa de empatía y preguntas «¿Cómo podríamos…?»

**Cliente:** TurisData Canarias (lo interpreta el docente como Director General) · **Fecha de la entrevista:** 16/10/2026
**Anotan:** todo el equipo · **Convención:** «entre comillas» = frase literal del cliente · (?) = suposición nuestra que hay que confirmar.

## 1. Notas de la entrevista

| Bloque | Lo que dijo el cliente (hechos, cifras, frases) | Suposiciones (?) que confirmar |
|---|---|---|
| Negocio y personas | Agencia de viajes TurisData: gestiona alojamientos y vende experiencias turísticas. Habla el Director General. | ¿Qué servicio genera más trabajo y más ingresos? (?) |
| Dolores y objetivos | Hay un documento con muchas cancelaciones: **2.400 en total**. Quiere **reducir las cancelaciones, agilizar los trabajos y ofrecer mejor atención al cliente**. | ¿Las 2.400 son cancelaciones o reservas totales del periodo? ¿Cuántas son de última hora? (?) |
| IA y expectativas | Quiere **un chat de voz que agilice y automatice las reservas**. | ¿Un chat de voz reduce las cancelaciones o resuelve otro problema? (?) |
| Datos y recursos | Tiene **datos incompletos y no revisados**. Quiere **una base de datos controlada**. | ¿En qué sistema están (PMS, Excel)? ¿Quién los mantiene? (?) |
| Restricciones | «Los datos personales no se usarán para otra cosa» · «Presupuesto de 15.000 euros» · «Lo ideal, que esté listo antes de la próxima temporada y que no sea eterno» | ¿Cuándo empieza exactamente la próxima temporada? (?) |

## 2. Mapa de empatía

| Cuadrante | Anotaciones |
|---|---|
| **Piensa y siente** | Tiene muchas cancelaciones y miedo a seguir perdiendo dinero. Cree que el chat de voz lo va a solucionar todo (?). |
| **Ve** | Que la competencia ya usa IA. |
| **Oye** | Que la IA (un chat de voz) le solucionará sus problemas. |
| **Dice y hace** | Delega en sus asesores y en nosotros como consultora. Dice: «Lo ideal, que esté listo antes de la próxima temporada y que no sea eterno». |
| **Dolores** | 1. Las cancelaciones de última hora pueden dejarlos sin ingresos (2.400 cancelaciones). 2. Los datos están incompletos y sin revisar, así que no puede tomar decisiones fiables. |
| **Ganancias** | 1. Menos cancelaciones y más ingresos. 2. Gestionar los alojamientos con menos esfuerzo, sin perder calidad en la atención. |

## 3. Punto de vista (POV)

> El Director General de TurisData necesita **anticiparse a las cancelaciones y trabajar con datos fiables** porque tiene **2.400 cancelaciones** que le hacen perder ingresos, sus **datos están incompletos** y dispone de **15.000 €** y poco tiempo (antes de la próxima temporada).

## 4. Tres preguntas «¿Cómo podríamos…?» (HMW)

| Nº | Dolor o ganancia de origen | ¿Cómo podríamos…? |
|---|---|---|
| HMW 1 | Cancelaciones de última hora | ¿Cómo podríamos ayudar al cliente a **anticiparse a las cancelaciones** y reducir su impacto económico? |
| HMW 2 | Pérdida de ingresos por apartamentos libres | ¿Cómo podríamos ayudarle a **aprovechar mejor los periodos en que el alojamiento queda libre**? |
| HMW 3 | Datos incompletos y sin revisar | ¿Cómo podríamos conseguir una **base de datos de reservas fiable** sobre la que tomar decisiones? |

Otra HMW que salió en el equipo y queda en reserva: ¿cómo podríamos agilizar la atención al cliente sin perder calidad?

## 5. Priorización (1 = bajo, 5 = alto)

| HMW | Impacto para el cliente | Viabilidad con datos e IA | Aprendizaje para el equipo | Total |
|---|---|---|---|---|
| **HMW 1 · Anticipar cancelaciones** | 5 | 4 | 5 | **14** |
| HMW 3 · Base de datos fiable | 4 | 4 | 3 | 11 |
| HMW 2 · Aprovechar periodos libres | 4 | 3 | 4 | 11 |

**Priorizada: HMW 1.** Ataca el dolor más caro (las cancelaciones), hay histórico de reservas para trabajar y encaja en el presupuesto y en el plazo. La HMW 3 es un **requisito previo**: sin datos revisados no se puede entrenar ningún modelo fiable, así que la incluimos como primer paso del piloto.

**Sobre el chat de voz:** el cliente lo propone como solución, pero todavía no sabemos si reduce las cancelaciones. No lo descartamos. Lo evaluaremos en el Sprint 1 como caso de uso separado, sin dar por hecho que la IA es la respuesta.

## 6. Riesgos de IA responsable detectados

| Riesgo | Por qué | Medida preventiva |
|---|---|---|
| Privacidad de los datos personales (RGPD) | Las reservas contienen nombres, correos y teléfonos de huéspedes | Minimizar los datos, seudonimizar los identificadores, limitar los accesos y usar los datos solo para la finalidad acordada («Los datos personales no se usarán para otra cosa») |
| Sesgo / discriminación | Variables como país de origen o código postal pueden penalizar a ciertos grupos | Revisar las variables antes de entrenar y que una persona valide toda acción sobre el cliente |
| Datos incompletos | El cliente reconoce que no están revisados | Auditar la calidad de los datos antes de entrenar ningún modelo |

## 7. Dudas abiertas para el Sprint 1

1. ¿Las 2.400 son cancelaciones o reservas totales, y de qué periodo?
2. ¿Qué datos se registran por reserva (antelación, canal, tarifa, país) y en qué sistema?
3. ¿Qué haría el equipo con una alerta de «riesgo de cancelación»: llamar, pedir depósito, ofrecer otra fecha?
4. ¿El chat de voz es una prioridad del cliente o una idea que ha oído?
5. ¿Cuándo empieza la próxima temporada?
