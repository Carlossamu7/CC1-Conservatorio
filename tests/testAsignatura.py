"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de tests sobre la clase Asignatura
"""

import unittest
import sys
sys.path.append('src')

from Asignatura import Asignatura

class ResultTest(unittest.TestCase):

    def test_getAsignatura(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(asig.getAsignatura(), "LenguajeMusical", "Comprobando getAsignatura()")

    def test_getProfesor(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(asig.getProfesor(), "JJ", "Comprobando getProfesor()")

    def test_getHorario(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(asig.getHorario(), "L:16-17, X:16-17", "Comprobando getHorario()")

    def test_getAula(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(asig.getAula(), "Aula01", "Comprobando getAula()")

    def test_toString(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(asig.toString(),
            "--> LenguajeMusical\nProfesor: JJ\nHorario: L:16-17, X:16-17\nAula: Aula01",
            "Comprobando toString()")


if __name__ == '__main__':
    unittest.main()
