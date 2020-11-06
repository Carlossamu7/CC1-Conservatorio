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

class TestAlumno(unittest.TestCase):

    def test_getNombre(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        self.assertEqual(alumno.getNombre(), "Carlos", "Comprobando getNombre()")

    def test_getEmail(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        self.assertEqual(alumno.getEmail(), "carlossamu7@correo.ugr.es", "Comprobando getEmail()")

    def test_getDni(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        self.assertEqual(alumno.getDni(), "75931715K", "Comprobando getDni()")

    def test_getAsignaturas(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        self.assertEqual(alumno.getAsignaturas(), "LenguajeMusical", "Comprobando getAsignaturas()")

    def test_setNombre(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        alumno.setNombre("Pepe")
        self.assertEqual(alumno.getNombre(), "Pepe", "Comprobando setNombre()")

    def test_setAsignaturas(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        alumno.setAsignaturas("Coro")
        self.assertEqual(alumno.getAsignaturas(), "Coro", "Comprobando setAsignaturas()")

    def test_setAsignaturas(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        alumno.setAsignaturas("Coro")
        self.assertEqual(alumno.getAsignaturas(), "Coro", "Comprobando setAsignaturas()")

    def test_toString(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "LenguajeMusical")
        self.assertEqual(alumno.toString(),
            "--> Carlos (DNI: 75931715K, @: carlossamu7@correo.ugr.es)\nAsignaturas: LenguajeMusical",
            "Comprobando toString()")

    def test_validoDni(self):
        self.assertTrue(validoDNI("75931715K"), "Comprobando validoDNI() con DNI correcto")
        self.assertTrue(not validoDNI("759317156"), "Comprobando validoDNI() con DNI incorrecto sin letra")
        self.assertTrue(not validoDNI("75A31715K"), "Comprobando validoDNI() con DNI incorrecto")
        self.assertTrue(not validoDNI("232A"), "Comprobando validoDNI() con DNI de longitud incorrecta")
        self.assertTrue(not validoDNI("X1234567Z"), "Comprobando validoDNI() con DNI extranjero incorrecto")

    def test_creaAlumnoDniNoValido(self):
        with self.assertRaises(ValueError): Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715A", "LenguajeMusical")


if __name__ == '__main__':
    unittest.main()
