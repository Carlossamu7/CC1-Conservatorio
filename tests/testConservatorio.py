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

    def test_getNumeroAlumnos(self):
        conser = Conservatorio()
        conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        conser.darAltaAlumno("Carlos", "otro@correo.ugr.es", "74606489D", "Coro")
        self.assertEqual(conser.getNumeroAlumnos(), 2, "Comprobando getNumeroAlumnos()")

    def test_getListaAsignaturas(self):
        conser = Conservatorio()
        self.assertEqual(conser.getListaAsignaturas(), [], "Comprobando getListaAsignaturas()")

    def test_getNumeroAsignaturas(self):
        conser = Conservatorio()
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        conser.darAltaAsignatura("Armonia", "JJ", "M:20-21", "Aula01")
        self.assertEqual(conser.getNumeroAsignaturas(), 2, "Comprobando getNumeroAsignaturas()")

    ###############
    ### Alumnos ###
    ###############

    def test_existAlumno(self):
        conser = Conservatorio()
        conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        self.assertTrue(conser.existAlumno("75931715K"), "Comprobando existAlumno()")

    def test_darAltaAlumno(self):
        conser = Conservatorio()
        conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        self.assertEqual(conser.getListaAlumnos()[0].toString(), alumno.toString(), "Comprobando darAltaAlumno()")
        with self.assertRaises(ValueError): conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")

    ###################
    ### Asignaturas ###
    ###################

    def test_existAsignatura(self):
        conser = Conservatorio()
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertTrue(conser.existAsignatura("Lenguaje Musical"), "Comprobando existAsignatura()")

    def test_darAltaAsignatura(self):
        conser = Conservatorio()
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        asig = Asignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(conser.getListaAsignaturas()[0].toString(), asig.toString(), "Comprobando darAltaAsignatura()")
        with self.assertRaises(ValueError): conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")


if __name__ == '__main__':
    unittest.main()
