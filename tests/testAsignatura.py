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
        self.assertEqual(asig.getAsignatura(), "LenguajeMusical")

    def test_getProfesor(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(asig.getProfesor(), "JJ")

    def test_getHorario(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(asig.getHorario(), "L:16-17, X:16-17")

    def test_getAula(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(asig.getAula(), "Aula01")

    def test_setProfesor(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        asig.setProfesor("Pepe")
        self.assertEqual(asig.getProfesor(), "Pepe")

    def test_setHorario(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        asig.setHorario("V:10-11")
        self.assertEqual(asig.getHorario(), "V:10-11")

    def test_setAula(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        asig.setAula("Aula02")
        self.assertEqual(asig.getAula(), "Aula02")

    def test_toString(self):
        asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(asig.toString(),
            "--> LenguajeMusical\nProfesor: JJ\nHorario: L:16-17, X:16-17\nAula: Aula01")


if __name__ == '__main__':
    unittest.main()
