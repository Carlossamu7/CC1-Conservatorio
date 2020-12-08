"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de tests sobre la clase AsignaturaConcepto
"""

import unittest
import sys
sys.path.append('src')

from AsignaturaConcepto import AsignaturaConcepto

class TestAsignaturaConcepto(unittest.TestCase):

    def setUp(self):
        self.asig = AsignaturaConcepto("001", "Lenguaje Musical", 1, "Nociones básicas acerca de leer una partitura, entonar y hacer dictados")

    def test_get_id(self):
        self.assertEqual(self.asig.get_id(), "001", "Comprobando get_id()")

    def test_get_nombre_asignatura(self):
        self.assertEqual(self.asig.get_nombre_asignatura(), "Lenguaje Musical", "Comprobando get_nombre_asignatura()")

    def test_get_curso(self):
        self.assertEqual(self.asig.get_curso(), 1, "Comprobando get_curso()")

    def test_get_concepto(self):
        self.assertEqual(self.asig.get_concepto(), "Nociones básicas acerca de leer una partitura, entonar y hacer dictados", "Comprobando get_concepto()")

    def test_to_string(self):
        self.assertEqual(self.asig.to_string(),
            "--> Lenguaje Musical (001)\n    Curso: 1\n    Concepto: Nociones básicas acerca de leer una partitura, entonar y hacer dictados",
            "Comprobando to_string()")

    def test_eq(self):
        asi = AsignaturaConcepto("001", "Lenguaje Musical", 1, "Nociones básicas acerca de leer una partitura, entonar y hacer dictados")
        self.assertTrue(self.asig.__eq__(asi))

if __name__ == '__main__':
    unittest.main()
