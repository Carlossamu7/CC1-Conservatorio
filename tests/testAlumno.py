"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de tests sobre la clase Alumno
"""

import unittest
import sys
sys.path.append('src')

from Alumno import Alumno, valido_dni, valido_email

class TestAlumno(unittest.TestCase):

    def setUp(self):
        self.alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", ["Lenguaje Musical", "Coro"])

    def test_get_nombre(self):
        self.assertEqual(self.alumno.get_nombre(), "Carlos", "Comprobando get_nombre()")

    def test_get_email(self):
        self.assertEqual(self.alumno.get_email(), "carlossamu7@correo.ugr.es", "Comprobando get_email()")

    def test_get_dni(self):
        self.assertEqual(self.alumno.get_dni(), "75931715K", "Comprobando get_dni()")

    def test_get_lista_asignaturas(self):
        self.assertEqual(self.alumno.get_lista_asignaturas(), ["Lenguaje Musical", "Coro"], "Comprobando get_lista_asignaturas()")

    def test_set_nombre(self):
        self.alumno.set_nombre("Pepe")
        self.assertEqual(self.alumno.get_nombre(), "Pepe", "Comprobando set_nombre()")

    def test_set_email(self):
        self.alumno.set_email("otro_correo@correo.ugr.es")
        self.assertEqual(self.alumno.get_email(), "otro_correo@correo.ugr.es", "Comprobando set_email()")
        with self.assertRaises(ValueError): self.alumno.set_email("@correo.ugr.es")

    def test_to_string(self):
        self.assertEqual(self.alumno.to_string(),
            "--> Carlos (DNI: 75931715K, @: carlossamu7@correo.ugr.es)\n    Asignaturas: Lenguaje Musical, Coro",
            "Comprobando to_string()")

    def test_matricula_asignatura(self):
        # Alumno con asignaturas
        self.alumno.matricula_asignatura("Piano")
        self.assertEqual(self.alumno.get_lista_asignaturas(), ["Lenguaje Musical", "Coro", "Piano"],
                         "Comprobando matricula_asignatura() con alumno que ya tiene asignaturas matriculadas")

        # Alumno sin asignaturas
        alumno2 = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", [])
        alumno2.matricula_asignatura("Coro")
        self.assertEqual(alumno2.get_lista_asignaturas(), ["Coro"], "Comprobando matricula_asignatura() con alumno sin asignaturas")

        # Excepción asignatura ya matriculada
        alumno3 = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical, Coro")
        with self.assertRaises(ValueError): alumno3.matricula_asignatura("Coro")

    def test_desmatricula_asignatura(self):
        self.alumno.desmatricula_asignatura("Coro")
        self.assertEqual(self.alumno.get_lista_asignaturas(), ["Lenguaje Musical"], "Comprobando desmatricula_asignatura()")

        # Excepción asignatura no matriculada
        alumno2 = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", ["Lenguaje Musical"])
        with self.assertRaises(ValueError): alumno2.desmatricula_asignatura("Coro")

    def test_valido_dni(self):
        self.assertTrue(valido_dni("75931715K"), "Comprobando valido_dni() con DNI correcto")
        self.assertFalse(valido_dni("759317156"), "Comprobando valido_dni() con DNI incorrecto sin letra")
        self.assertFalse(valido_dni("75A31715K"), "Comprobando valido_dni() con DNI incorrecto")
        self.assertFalse(valido_dni("232A"), "Comprobando valido_dni() con DNI de longitud incorrecta")
        self.assertFalse(valido_dni("X1234567Z"), "Comprobando valido_dni() con DNI extranjero incorrecto")

    def test_crea_alumno_no_valido(self):
        with self.assertRaises(ValueError): Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715A", "Lenguaje Musical")
        with self.assertRaises(ValueError): Alumno("Carlos", "@correo.ugr.es", "75931715A", "Lenguaje Musical")

    def test_valido_email(self):
        self.assertTrue(valido_email('a@b.com'), "Comprobando valido_email() con email correcto")  # True.
        self.assertTrue(valido_email('abc@def.com'), "Comprobando valido_email() con email correcto")  # True.
        self.assertTrue(valido_email('abc@3def.com'), "Comprobando valido_email() con email correcto")  # True.
        self.assertTrue(valido_email('abc@def.us'), "Comprobando valido_email() con email correcto")  # True.
        self.assertTrue(valido_email('abc@d_-f.us'), "Comprobando valido_email() con email correcto")  # True.

        self.assertFalse(valido_email('@def.com'), "Comprobando valido_email() con email incorrecto")  # False.
        self.assertFalse(valido_email('"abc@def".com'), "Comprobando valido_email() con email incorrecto")  # False.
        self.assertFalse(valido_email('abc+def.com'), "Comprobando valido_email() con email incorrecto")  # False.
        self.assertFalse(valido_email('abc@def.x'), "Comprobando valido_email() con email incorrecto")  # False.
        self.assertFalse(valido_email('abc@def.12'), "Comprobando valido_email() con email incorrecto")  # False.
        self.assertFalse(valido_email('abc@def..com'), "Comprobando valido_email() con email incorrecto")  # False.

    def test_eq(self):
        al = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", ["Lenguaje Musical", "Coro"])
        self.assertTrue(self.alumno.__eq__(al))


if __name__ == '__main__':
    unittest.main()
