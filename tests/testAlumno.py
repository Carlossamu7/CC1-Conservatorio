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
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        self.assertEqual(alumno.getNombre(), "Carlos", "Comprobando getNombre()")

    def test_getEmail(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        self.assertEqual(alumno.getEmail(), "carlossamu7@correo.ugr.es", "Comprobando getEmail()")

    def test_getDni(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        self.assertEqual(alumno.getDni(), "75931715K", "Comprobando getDni()")

    def test_getAsignaturas(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        self.assertEqual(alumno.getAsignaturas(), "Lenguaje Musical", "Comprobando getAsignaturas()")

    def test_setNombre(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        alumno.setNombre("Pepe")
        self.assertEqual(alumno.getNombre(), "Pepe", "Comprobando setNombre()")

    def test_setEmail(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        alumno.setEmail("otro_correo@correo.ugr.es")
        self.assertEqual(alumno.getEmail(), "otro_correo@correo.ugr.es", "Comprobando setEmail()")

    def test_setAsignaturas(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        alumno.setAsignaturas("Coro")
        self.assertEqual(alumno.getAsignaturas(), "Coro", "Comprobando setAsignaturas()")

    def test_toString(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        self.assertEqual(alumno.toString(),
            "--> Carlos (DNI: 75931715K, @: carlossamu7@correo.ugr.es)\n    Asignaturas: Lenguaje Musical",
            "Comprobando toString()")

    def test_listaAsignaturas(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical, Coro")
        self.assertEqual(alumno.listaAsignaturas(), ["Lenguaje Musical", "Coro"],
                         "Comprobando listaAsignaturas()")

    def test_matriculaAsignatura(self):
        # Alumno con asignaturas
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        alumno.matriculaAsignatura("Coro")
        self.assertEqual(alumno.getAsignaturas(), "Lenguaje Musical, Coro",
                         "Comprobando matriculaAsignatura() con alumno que ya tiene asignaturas matriculadas")

        # Alumno sin asignaturas
        alumno2 = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "")
        alumno2.matriculaAsignatura("Coro")
        self.assertEqual(alumno2.getAsignaturas(), "Coro", "Comprobando matriculaAsignatura() con alumno sin asignaturas")

        # Excepción asignatura ya matriculada
        alumno3 = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical, Coro")
        with self.assertRaises(ValueError): alumno3.matriculaAsignatura("Coro")

    def test_desmatriculaAsignatura(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical, Coro")
        alumno.desmatriculaAsignatura("Coro")
        self.assertEqual(alumno.getAsignaturas(), "Lenguaje Musical", "Comproband desmatriculaAsignatura()")

        # Excepción asignatura no matriculada
        alumno2 = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        with self.assertRaises(ValueError): alumno2.desmatriculaAsignatura("Coro")

    def test_validoDni(self):
        self.assertTrue(validoDNI("75931715K"), "Comprobando validoDNI() con DNI correcto")
        self.assertFalse(validoDNI("759317156"), "Comprobando validoDNI() con DNI incorrecto sin letra")
        self.assertFalse(validoDNI("75A31715K"), "Comprobando validoDNI() con DNI incorrecto")
        self.assertFalse(validoDNI("232A"), "Comprobando validoDNI() con DNI de longitud incorrecta")
        self.assertFalse(validoDNI("X1234567Z"), "Comprobando validoDNI() con DNI extranjero incorrecto")

    def test_creaAlumnoDniNoValido(self):
        with self.assertRaises(ValueError): Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715A", "Lenguaje Musical")


if __name__ == '__main__':
    unittest.main()
