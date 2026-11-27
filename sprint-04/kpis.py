import argparse
import csv
import json
import sys
from datetime import date

COLUMNAS_OBLIGATORIAS = [
    "fecha_llegada",
    "noches",
    "precio_noche",
    "canal",
    "cancelada",
]


def tasa_cancelacion_por_canal(reservas):
    """Devuelve {canal: porcentaje_cancelacion_1_decimal}."""
    totales = {}
    canceladas = {}
    for r in reservas:
        canal = r["canal"]
        totales[canal] = totales.get(canal, 0) + 1
        if r.get("cancelada") == 1:
            canceladas[canal] = canceladas.get(canal, 0) + 1
    resultado = {}
    for canal, total in totales.items():
        pct = (canceladas.get(canal, 0) / total) * 100 if total > 0 else 0.0
        resultado[canal] = round(pct, 1)
    return resultado


def ingreso_medio_por_reserva(reservas):
    """Ingreso medio (noches * precio_noche) de las reservas confirmadas (cancelada == 0)."""
    confirmadas = [r for r in reservas if r.get("cancelada") == 0]
    if not confirmadas:
        return 0.0
    total = sum(r["noches"] * r["precio_noche"] for r in confirmadas)
    return round(total / len(confirmadas), 2)


def ocupacion_proxy(reservas, capacidad_habitaciones=40):
    """Porcentaje de ocupación estimado sobre noches posibles en el rango de fechas."""
    if capacidad_habitaciones <= 0 or not reservas:
        return 0.0
    fechas = [r["fecha_llegada"] for r in reservas if "fecha_llegada" in r]
    if not fechas:
        return 0.0
    dias_totales = (max(fechas) - min(fechas)).days + 1
    if dias_totales <= 0:
        dias_totales = 1
    noches_posibles = capacidad_habitaciones * dias_totales
    noches_ocupadas = sum(r["noches"] for r in reservas if r.get("cancelada") == 0)
    return round((noches_ocupadas / noches_posibles) * 100, 1)


def calcular_kpis(reservas, capacidad_habitaciones=40):
    """Consolida los KPIs principales de TurisData Canarias."""
    return {
        "reservas_analizadas": len(reservas),
        "ocupacion_proxy_pct": ocupacion_proxy(reservas, capacidad_habitaciones),
        "ingreso_medio_por_reserva": ingreso_medio_por_reserva(reservas),
        "tasa_cancelacion_por_canal_pct": tasa_cancelacion_por_canal(reservas),
    }


def _convertir_fila(fila):
    """Convierte una fila del CSV a tipos Python y valida reglas de negocio."""
    try:
        canal = str(fila.get("canal", "")).strip()
        if not canal:
            raise ValueError("El canal no puede estar vacío")
        noches = int(fila["noches"])
        precio_noche = float(fila["precio_noche"])
        cancelada = int(fila["cancelada"])
        fecha_llegada = date.fromisoformat(str(fila["fecha_llegada"]).strip())
    except (ValueError, KeyError, TypeError) as exc:
        raise ValueError(f"Error de formato en los datos: {exc}")

    if noches < 1:
        raise ValueError("noches debe ser >= 1")
    if precio_noche <= 0:
        raise ValueError("precio_noche debe ser > 0")
    if cancelada not in (0, 1):
        raise ValueError("cancelada debe ser 0 o 1")

    return {
        "fecha_llegada": fecha_llegada,
        "noches": noches,
        "precio_noche": precio_noche,
        "canal": canal,
        "cancelada": cancelada,
    }


def leer_reservas(ruta):
    """Lee el CSV y devuelve (reservas_validas, avisos)."""
    reservas = []
    avisos = []
    try:
        archivo = open(ruta, mode="r", encoding="utf-8", newline="")
    except FileNotFoundError:
        raise FileNotFoundError(f"El fichero no existe: {ruta}")

    with archivo:
        lector = csv.DictReader(archivo)
        fieldnames = lector.fieldnames or []
        faltantes = [c for c in COLUMNAS_OBLIGATORIAS if c not in fieldnames]
        if faltantes:
            raise ValueError(f"Faltan columnas obligatorias en el CSV: {faltantes}")

        for num_fila, fila in enumerate(lector, start=2):
            try:
                reservas.append(_convertir_fila(fila))
            except ValueError as err:
                avisos.append(f"Fila {num_fila} descartada: {err}")

    return reservas, avisos


def exportar_json(datos, ruta):
    """Guarda datos en JSON con UTF-8 y sangría de 2 espacios."""
    with open(ruta, mode="w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)


def main(argumentos=None):
    parser = argparse.ArgumentParser(description="KPIs de reservas de TurisData Canarias")
    parser.add_argument("entrada", help="CSV de reservas")
    parser.add_argument("salida", help="JSON de salida")
    parser.add_argument("--capacidad", type=int, default=40, help="Habitaciones disponibles")
    args = parser.parse_args(argumentos)

    try:
        reservas, avisos = leer_reservas(args.entrada)
        kpis = calcular_kpis(reservas, args.capacidad)
        kpis["calidad"] = {
            "filas_validas": len(reservas),
            "filas_descartadas": len(avisos),
            "avisos": avisos[:20],
        }
        exportar_json(kpis, args.salida)
        print(f"OK: Fichero generado correctamente en '{args.salida}'")
        return 0
    except (FileNotFoundError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
