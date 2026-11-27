import sqlite3
from datetime import date, timedelta
import numpy as np
import pandas as pd

con = sqlite3.connect("turisdata_reto.db")
cur = con.cursor()

cur.executescript("""
DROP TABLE IF EXISTS reservas;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS alojamientos;
DROP TABLE IF EXISTS ocupacion_diaria;

CREATE TABLE alojamientos (
    id_alojamiento INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    isla TEXT NOT NULL,
    categoria TEXT NOT NULL,
    plazas INTEGER NOT NULL
);

CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY,
    pais_origen TEXT NOT NULL,
    cliente_repetidor INTEGER NOT NULL
);

CREATE TABLE reservas (
    id_reserva INTEGER PRIMARY KEY,
    id_alojamiento INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL,
    fecha_reserva TEXT NOT NULL,
    fecha_llegada TEXT NOT NULL,
    noches INTEGER NOT NULL,
    canal TEXT NOT NULL,
    tarifa TEXT NOT NULL,
    deposito TEXT NOT NULL,
    precio_noche REAL NOT NULL,
    cancelada INTEGER NOT NULL,
    FOREIGN KEY (id_alojamiento) REFERENCES alojamientos(id_alojamiento),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE ocupacion_diaria (
    fecha TEXT PRIMARY KEY,
    ocupacion_pct REAL NOT NULL,
    temperatura_c REAL NOT NULL,
    festivo INTEGER NOT NULL,
    precio_medio REAL NOT NULL
);
""")

rng = np.random.default_rng(42)
islas = ["Tenerife", "Gran Canaria", "Lanzarote", "Fuerteventura", "La Palma", "La Gomera"]
categorias = ["hotel", "apartamento", "casa rural", "hotel boutique"]
alojamientos_rows = [
    (i, f"Alojamiento TurisData {i:02d}", islas[(i - 1) % 6], categorias[(i - 1) % 4], int(rng.choice([12, 24, 40, 60, 80])))
    for i in range(1, 21)
]
cur.executemany("INSERT INTO alojamientos VALUES (?, ?, ?, ?, ?)", alojamientos_rows)

paises = ["ES", "GB", "DE", "FR", "IT", "NL"]
clientes_rows = [
    (cid, str(rng.choice(paises, p=[0.35, 0.25, 0.18, 0.10, 0.06, 0.06])), int(rng.choice([0, 1], p=[0.75, 0.25])))
    for cid in range(1, 2501)
]
cur.executemany("INSERT INTO clientes VALUES (?, ?, ?)", clientes_rows)

canales = ["directo", "web_intermediaria", "agencia", "empresa"]
prob_canales = [0.28, 0.38, 0.22, 0.12]
cancel_rate = {"directo": 0.315, "web_intermediaria": 0.539, "agencia": 0.440, "empresa": 0.433}
base_start = date(2023, 1, 1)
reservas_rows = []
for rid in range(1, 6001):
    aloj_id = int(rng.integers(1, 21))
    cli_id = 1234 if rid in (5046, 5760) else (1235 if int(rng.integers(1, 2501)) == 1234 else int(rng.integers(1, 2501)))
    f_llegada = base_start + timedelta(days=int(rng.integers(0, 1095)))
    f_reserva = f_llegada - timedelta(days=int(rng.integers(1, 120)))
    noches = int(rng.choice([2, 3, 4, 5, 6, 7, 10, 14], p=[0.12, 0.18, 0.20, 0.18, 0.12, 0.12, 0.05, 0.03]))
    canal = str(rng.choice(canales, p=prob_canales))
    tarifa = "corporativa" if canal == "empresa" else str(rng.choice(["flexible", "no_reembolsable"], p=[0.65, 0.35]))
    deposito = "con_deposito" if tarifa in ("no_reembolsable", "corporativa") else "sin_deposito"
    precio_noche = round(float(np.clip(rng.normal(105.0, 22.0), 55.0, 220.0)), 2)
    cancelada = int(rng.random() < cancel_rate[canal])
    reservas_rows.append((rid, aloj_id, cli_id, f_reserva.isoformat(), f_llegada.isoformat(), noches, canal, tarifa, deposito, precio_noche, cancelada))

cur.executemany("INSERT INTO reservas VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", reservas_rows)

fechas_1096 = pd.date_range("2023-01-01", periods=1096, freq="D")
ocup_rows = []
for dt in fechas_1096:
    m = dt.month
    base_o = 78.83 if m == 1 else (60.06 if m == 9 else (82.0 if m in (7, 8) else 70.0))
    ocup_val = round(float(np.clip(base_o + rng.normal(0, 4.0), 35.0, 99.0)), 2)
    temp_val = round(float(20.5 + 4.5 * np.sin((m - 3) * np.pi / 6) + rng.normal(0, 1.2)), 1)
    fest = 1 if (dt.weekday() >= 5 or (dt.month == 1 and dt.day == 1) or (dt.month == 12 and dt.day == 25)) else 0
    precio_med = round(float(88.0 + 0.45 * ocup_val + rng.normal(0, 3.0)), 2)
    ocup_rows.append((dt.strftime("%Y-%m-%d"), ocup_val, temp_val, fest, precio_med))

cur.executemany("INSERT INTO ocupacion_diaria VALUES (?, ?, ?, ?, ?)", ocup_rows)
cur.execute("UPDATE ocupacion_diaria SET ocupacion_pct = 78.83 WHERE SUBSTR(fecha, 6, 2) = '01'")
cur.execute("UPDATE ocupacion_diaria SET ocupacion_pct = 60.06 WHERE SUBSTR(fecha, 6, 2) = '09'")
con.commit()
con.close()
print("Base de datos sprint-05/turisdata_reto.db generada con éxito.")
