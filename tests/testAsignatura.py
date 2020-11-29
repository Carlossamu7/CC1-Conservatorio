"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de tests sobre la clase self.asignatura
"""

import unittest
import sys
sys.path.append('src')

from Asignatura import Asignatura

class TestAsignatura(unittest.TestCase):
    
    def setUp(self):
        self.asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")

    def test_get_asignatura(self):
        self.assertEqual(self.asig.get_asignatura(), "LenguajeMusical", "Comprobando get_self.asignatura()")

    def test_get_profesor(self):
        self.assertEqual(self.asig.get_profesor(), "JJ", "Comprobando get_profesor()")

    def test_get_horario(self):
        self.assertEqual(self.asig.get_horario(), "L:16-17, X:16-17", "Comprobando get_horario()")

    def test_get_aula(self):
        self.assertEqual(self.asig.get_aula(), "Aula01", "Comprobando get_aula()")

    def test_set_profesor(self):
        self.asig.set_profesor("Pepe")
        self.assertEqual(self.asig.get_profesor(), "Pepe", "Comprobando set_profesor()")

    def test_set_horario(self):
        self.asig.set_horario("V:10-11")
        self.assertEqual(self.asig.get_horario(), "V:10-11", "Comprobando set_horario()")

    def test_set_aula(self):
        self.asig.set_aula("Aula02")
        self.assertEqual(self.asig.get_aula(), "Aula02", "Comprobando set_aula()")

    def test_to_string(self):
        self.assertEqual(self.asig.to_string(),
            "--> LenguajeMusical\n    Profesor: JJ\n    Horario: L:16-17, X:16-17\n    Aula: Aula01",
            "Comprobando to_string()")


if __name__ == '__main__':
    unittest.main()
