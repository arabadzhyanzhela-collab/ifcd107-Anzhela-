import json
import os
import tempfile
import unittest
from datetime import date

import kpis


class TestKpis(unittest.TestCase):
    def setUp(self):
        self.muestra = [
            {"fecha_llegada": date(2026, 5, 1), "noches": 4, "precio_noche": 85.0, "canal": "web_intermediaria", "cancelada": 1},
            {"fecha_llegada": date(2026, 5, 2), "noches": 7, "precio_noche": 110.0, "canal": "directo", "cancelada": 0},
            {"fecha_llegada": date(2026, 5, 3), "noches": 3, "precio_noche": 95.0, "canal": "agencia", "cancelada": 1},
            {"fecha_llegada": date(2026, 5, 4), "noches": 5, "precio_noche": 120.0, "canal": "directo", "cancelada": 0},
            {"fecha_llegada": date(2026, 5, 5), "noches": 2, "precio_noche": 150.0, "canal": "empresa", "cancelada": 0},
        ]

    def test_tasa_cancelacion_por_canal(self):
        tasas = kpis.tasa_cancelacion_por_canal(self.muestra)
        self.assertEqual(tasas["directo"], 0.0)
        self.assertEqual(tasas["web_intermediaria"], 100.0)

    def test_ingreso_medio_por_reserva(self):
        # Confirmadas: (7*110 + 5*120 + 2*150) / 3 = (770 + 600 + 300) / 3 = 556.67
        self.assertEqual(kpis.ingreso_medio_por_reserva(self.muestra), 556.67)

    def test_ocupacion_proxy(self):
        # 5 días (1 al 5 mayo), 40 hab -> 200 noches posibles; ocupadas = 7+5+2 = 14 -> 7.0%
        self.assertEqual(kpis.ocupacion_proxy(self.muestra, 40), 7.0)

    def test_leer_y_exportar_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = os.path.join(tmp, "reservas.csv")
            json_path = os.path.join(tmp, "salida.json")
            with open(csv_path, "w", encoding="utf-8") as f:
                f.write("fecha_llegada,noches,precio_noche,canal,cancelada\n")
                f.write("2026-05-01,4,100.0,directo,0\n")
                f.write("2026-05-02,-2,100.0,directo,0\n")  # fila defectuosa
            rc = kpis.main([csv_path, json_path, "--capacidad", "40"])
            self.assertEqual(rc, 0)
            with open(json_path, encoding="utf-8") as f:
                data = json.load(f)
            self.assertEqual(data["reservas_analizadas"], 1)
            self.assertEqual(data["calidad"]["filas_descartadas"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
