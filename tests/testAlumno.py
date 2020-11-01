"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de tests sobre la clase Alumno
"""

import unittest
import sys
sys.path.append('src')

from Alumno import Alumno
from Alumno import validoDNI

class ResultTest(unittest.TestCase):

    def test_getNombre(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        self.assertEqual(alumno.getNombre(), "Carlos")

    def test_getEmail(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        self.assertEqual(alumno.getEmail(), "carlossamu7@correo.ugr.es")

    def test_getDni(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        self.assertEqual(alumno.getDni(), "75931715K")

    def test_getAsignaturas(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        self.assertEqual(alumno.getAsignaturas(), "LenguajeMusical")

    def test_setNombre(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        alumno.setNombre("Pepe")
        self.assertEqual(alumno.getNombre(), "Pepe")

    def test_setEmail(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        alumno.setEmail("otro_correo@correo.ugr.es")
        self.assertEqual(alumno.getEmail(), "otro_correo@correo.ugr.es")

    def test_setAsignaturas(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        alumno.setAsignaturas("Coro")
        self.assertEqual(alumno.getAsignaturas(), "Coro")

    # Funciones que testean validoDNI()
    def test_dni(self):
        dni = "75931715K"
        self.assertTrue(validoDNI(dni))

    def test_dni2(self):
        dni2 = "759317156"
        self.assertTrue(not validoDNI(dni2))

    def test_dni3(self):
        dni3 = "75A31715K"
        self.assertTrue(not validoDNI(dni3))

    def test_dni4(self):
        dni4 = "232A"
        self.assertTrue(not validoDNI(dni4))


if __name__ == '__main__':
    unittest.main()
