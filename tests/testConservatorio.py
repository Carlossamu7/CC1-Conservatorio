"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de tests sobre la clase Conservatorio
"""

import unittest
import sys
sys.path.append('src')

from Conservatorio import Conservatorio
from Alumno import Alumno
from Asignatura import Asignatura

class TestConservatorio(unittest.TestCase):

    def test_getConservatorio(self):
        conser = Conservatorio()
        self.assertEqual(conser.getNombreConservatorio(), "MiConservatorio", "Comprobando getConservatorio()")

    def test_getListaAlumnos(self):
        conser = Conservatorio()
        self.assertEqual(conser.getListaAlumnos(), [], "Comprobando getListaAlumnos()")

    def test_getListaAsignaturas(self):
        conser = Conservatorio()
        self.assertEqual(conser.getListaAsignaturas(), [], "Comprobando getListaAsignaturas()")


if __name__ == '__main__':
    unittest.main()
