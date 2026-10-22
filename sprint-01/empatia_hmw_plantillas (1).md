# Mapa de empatía y "How might we" · TurisData Canarias (Sprint 0)

## 1. Mapa de empatía

**Persona / usuario:** Directora de Operaciones de TurisData · **Situación:** Gestión diaria de reservas, sobrecarga de atención al cliente y pérdidas de ingresos por cancelaciones de última hora. [cite: 8, 9]

```
                    ┌───────────────────────────────────────┐
                    │ 1. ¿QUÉ PIENSA Y SIENTE?              │
                    │ - Impotencia por habitaciones vacías  │
                    │   a última hora sin poder venderlas.  │
                    │ - Temor a que la IA dé respuestas     │
                    │   frías o erróneas a clientes VIP.   │
                    │ - Ilusión por digitalizar el negocio. │
 ┌──────────────────┼───────────────────────────────────────┼──────────────────┐
 │ 2. ¿QUÉ VE?      │             USUARIO                   │ 3. ¿QUÉ OYE?     │
 │ - Tableros con   │      Directora de Operaciones         │ - Huéspedes      │
 │   un 21,25 % de  │             TurisData                 │   quejándose por │
 │   cancelaciones. │                                       │   retrasos fuera │
 │ - Datos en CSV,  │                                       │   de horario.    │
 │   SQLite y Excel │                                       │ - Socios pidiendo│
 │   desorganizados.│                                       │   mayor margen.  │
 └──────────────────┼───────────────────────────────────────┼──────────────────┘
                    │ 4. ¿QUÉ DICE Y HACE?                  │
                    │ - "Perdemos dinero cada fin de semana"│
                    │ - Trabaja horas extra respondiendo    │
                    │   correos y mensajes repetitivos.     │
                    │ - Revisa manualmente la ocupación.    │
                    ├───────────────────┬───────────────────┤
                    │ 5. DOLORES        │ 6. GANANCIAS      │
                    │ - Cancelaciones   │ - Predecir la     │
                    │   imprevistas.    │   ocupación real. │
                    │ - Trabajo manual  │ - Reducir la carga│
                    │   e ineficiente.  │   operativa 24/7. │
                    └───────────────────┴───────────────────┘
```

### Versión tabla (para pegar en el tablero o el `.md` del equipo)

| Cuadrante | Anotaciones (hechos y frases textuales) |
|---|---|
| **Piensa y siente** | Preocupada por los márgenes de beneficio. Siente frustración al no poder reaccionar a tiempo ante cancelaciones. Miedo a perder la cercanía y reputación de la empresa. [cite: 8, 9] |
| **Ve** | Una tasa de cancelación global del 21,25 % (30 % en tarifas flexibles). Archivos con miles de registros sin limpiar (`reservas_turisdata.csv`, `turisdata.db`). [cite: 4, 6, 8, 9] |
| **Oye** | Quejas de huéspedes cuando no reciben respuesta rápida fuera de horario comercial. Recomendaciones de la industria sobre automatización responsable. [cite: 8, 9] |
| **Dice y hace** | *"Tenemos miles de datos guardados, pero nadie ha tenido tiempo de analizarlos"*. Intenta gestionar incidencias operativas y la comercialización al mismo tiempo. [cite: 8, 9] |
| **Dolores** | **Dolor 1:** Cancelaciones imprevistas que dejan plazas vacías y reducen la rentabilidad.<br>**Dolor 2:** Saturación del personal al responder dudas repetitivas fuera de horario. [cite: 8, 9] |
| **Ganancias** | **Ganancia 1:** Anticipar la ocupación real para optimizar la política de precios y sobreventa.<br>**Ganancia 2:** Automatizar respuestas frecuentes con precisión manteniendo la satisfacción. [cite: 8, 9] |

---

## 2. Del mapa al punto de vista (POV)

> **La Directora de Operaciones de TurisData** necesita **predecir las cancelaciones con antelación y optimizar la atención inicial al cliente** porque **las cancelaciones imprevistas destruyen la rentabilidad del negocio y la atención manual fuera de horario genera cuellos de botella e ineficiencias.** [cite: 8, 9]

---

## 3. How might we (¿Cómo podríamos…?)

### Tabla de HMW

| Nº | Dolor o ganancia de origen | ¿Cómo podríamos…? |
|---|---|---|
| 1 | Dolor 1 (Cancelaciones) | ¿Cómo podríamos anticipar qué reservas tienen un alto riesgo de cancelación para tomar medidas preventivas? [cite: 2, 9] |
| 2 | Dolor 2 (Sobrecarga de consultas) | ¿Cómo podríamos resolver las dudas frecuentes de los huéspedes fuera de horario sin perder la calidez humana? [cite: 2, 9] |
| 3 | Ganancia 1 (Aumentar ocupación) | ¿Cómo podríamos optimizar la reasignación de habitaciones canceladas para maximizar la ocupación de fin de semana? [cite: 2, 9] |
| 4 | Ganancia 2 (Eficiencia operativa) | ¿Cómo podríamos automatizar la limpieza y clasificación de los datos del PMS para tomar decisiones comerciales más rápidas? [cite: 2, 9] |

### Matriz de priorización

| HMW | Impacto para el usuario (1-5) | Viabilidad con datos e IA (1-5) | Aprendizaje (1-5) | Total |
|---|---|---|---|---|
| **HMW 1 (Predicción de cancelaciones)** | 5 | 4 | 5 | **14** |
| HMW 2 (Atención de dudas 24/7) | 4 | 4 | 4 | 12 |
| HMW 3 (Optimización de ocupación) | 4 | 3 | 4 | 11 |
| HMW 4 (Calidad de datos) | 3 | 5 | 3 | 11 |

**Elección final para el reto:** **HMW 1 (Predicción de cancelaciones)**. [cite: 9]  
*Motivo:* Ataca directamente el dolor financiero más crítico del cliente (21,25 % de cancelaciones), cuenta con una base de datos histórica adecuada para modelos supervisados (`reservas_turisdata.csv`, `turisdata.db`) y ofrece un aprendizaje metodológico de alto impacto para el equipo. [cite: 4, 6, 9]

---

## 4. Ficha del usuario ficticio de la práctica 2 (Ejemplo resuelto)

**Persona C · Ainhoa, 41 años, gestora de un pequeño apartamento vacacional en La Palma.** [cite: 2, 9]

- **Situación:** Trabaja sola gestionando la propiedad en paralelo a su empleo habitual. Recibe reservas por Airbnb, Booking y su web. [cite: 2, 9]
- **Dolores:** Cancelaciones de última hora sin indemnización suficiente, solapamiento de calendarios (overbooking) y falta de tiempo para atender mensajes a tiempo. [cite: 2, 9]
- **Necesidad:** Una herramienta sencilla de alertas predictivas e integración de calendarios que no le exija conocimientos técnicos avanzados. [cite: 2, 9]
