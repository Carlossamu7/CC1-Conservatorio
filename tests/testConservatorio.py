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

    def setUp(self):
        self.conser = Conservatorio()
        self.conser.dar_alta_alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical, Coro")
        self.conser.dar_alta_asignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")

    def test_get_conservatorio(self):
        self.assertEqual(self.conser.get_nombre_conservatorio(), "MiConservatorio", "Comprobando get_nombre_conservatorio()")

    def test_get_diccionario_alumnos(self):
        conser2 = Conservatorio()
        self.assertEqual(conser2.get_diccionario_alumnos(), {}, "Comprobando get_diccionario_alumnos()")

    def test_get_numero_alumnos(self):

        self.conser.dar_alta_alumno("Carlos", "otro@correo.ugr.es", "74606489D", "Coro")
        self.assertEqual(self.conser.get_numero_alumnos(), 2, "Comprobando get_numero_alumnos()")

    def test_get_diccionario_asignaturas(self):
        conser2 = Conservatorio()
        self.assertEqual(conser2.get_diccionario_asignaturas(), {}, "Comprobando get_diccionario_asignaturas()")

    def test_get_numero_asignaturas(self):

        self.conser.dar_alta_asignatura("Armonia", "JJ", "M:20-21", "Aula01")
        self.assertEqual(self.conser.get_numero_asignaturas(), 2, "Comprobando get_numero_asignaturas()")

    ###############
    ### Alumnos ###
    ###############

    def test_exist_alumno(self):
        self.assertTrue(self.conser.exist_alumno("75931715K"), "Comprobando exist_alumno()")

    def test_dar_alta_alumno(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical, Coro")
        self.assertEqual(self.conser.get_diccionario_alumnos()["75931715K"].to_string(), alumno.to_string(), "Comprobando dar_alta_alumno()")
        with self.assertRaises(ValueError): self.conser.dar_alta_alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")

    def test_get_alumno(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical, Coro")
        self.assertEqual(self.conser.get_alumno("75931715K").to_string(), alumno.to_string(), "Comprobando get_alumno()")
        self.assertEqual(self.conser.get_alumno("00000000A"), "No existe ningún alumno con ese DNI.", "Comprobando get_alumno() con alumno no existente")

    def test_get_alumnos_nombre(self):
        self.conser.dar_alta_alumno("Carlos", "otro@correo.ugr.es", "74606489D", "Coro")
        self.assertEqual(self.conser.get_alumnos_nombre("Carlos"), ["75931715K", "74606489D"], "Comprobando get_alumnos_nombre()")

    def test_get_horario_asignatura_alumno(self):
        self.conser.dar_alta_asignatura("Coro", "JJ", "M:20-21", "Aula01")
        self.assertEqual(self.conser.get_horario_asignatura_alumno("75931715K", "Lenguaje Musical"), "L:16-17, X:16-17", "Comprobando get_horario_asignatura_alumno()")
        self.assertEqual(self.conser.get_horario_asignatura_alumno("75931715K", "Piano"), "Este alumno no está matriculado en esa asignatura.", "Comprobando get_horario_asignatura_alumno() con alumno no existente")
        self.assertEqual(self.conser.get_horario_asignatura_alumno("00000000A", "Lenguaje Musical"), "No existe ningún alumno con ese DNI.", "Comprobando get_horario_asignatura_alumno() con alumno no existente")

    def test_get_horario_alumno(self):
        self.conser.dar_alta_asignatura("Coro", "JJ", "M:20-21", "Aula01")
        self.assertEqual(self.conser.get_horario_alumno("75931715K"), ["L:16-17, X:16-17", "M:20-21"], "Comprobando get_horario_alumno()")
        self.assertEqual(self.conser.get_horario_alumno("00000000A"), "No existe ningún alumno con ese DNI.", "Comprobando get_horario_alumno() con alumno no existente")

    def test_get_aulas_alumno(self):
        self.conser.dar_alta_asignatura("Coro", "JJ", "M:20-21", "Aula01")
        self.assertEqual(self.conser.get_aulas_alumno("75931715K"), ["Aula01"], "Comprobando get_aulas_alumno()")
        self.assertEqual(self.conser.get_aulas_alumno("00000000A"), "No existe ningún alumno con ese DNI.", "Comprobando get_aulas_alumno() con alumno no existente")

    ###################
    ### Asignaturas ###
    ###################

    def test_exist_asignatura(self):
        self.assertTrue(self.conser.exist_asignatura("Lenguaje Musical"), "Comprobando exist_asignatura()")

    def test_dar_alta_asignatura(self):
        asig = Asignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(self.conser.get_diccionario_asignaturas()["Lenguaje Musical"].to_string(), asig.to_string(), "Comprobando dar_alta_asignatura()")
        with self.assertRaises(ValueError): self.conser.dar_alta_asignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")

    def test_borrar_asignatura(self):
        self.conser.borrar_asignatura("Lenguaje Musical")
        self.assertEqual(self.conser.get_numero_asignaturas(), 0, "Comprobando borrar_asignatura()")
        with self.assertRaises(ValueError): self.conser.borrar_asignatura("Lenguaje Musical")

    def test_get_asignatura(self):
        asig = Asignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(self.conser.get_asignatura("Lenguaje Musical").to_string(), asig.to_string(), "Comprobando get_asignatura()")
        self.assertEqual(self.conser.get_asignatura("Piano"), "No existe la asignatura Piano.", "Comprobando get_asignatura() con asignatura no existente")

    def test_get_lista_asignaturas_profesor(self):
        self.conser.dar_alta_asignatura("Armonía", "JJ", "M:20-21", "Aula01")
        listaAsig = self.conser.get_lista_asignaturas_profesor("JJ")
        listaAsig2 = [Asignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01"), Asignatura("Armonía", "JJ", "M:20-21", "Aula01")]
        for i in range(len(listaAsig)):
            self.assertEqual(listaAsig[i].to_string(), listaAsig2[i].to_string(), "Comprobando get_lista_asignaturas_profesor()")

    def test_get_nombre_asignaturas_profesor(self):
        self.conser.dar_alta_asignatura("Armonía", "JJ", "M:20-21", "Aula01")
        self.assertEqual(self.conser.get_nombre_asignaturas_profesor("JJ"), ["Lenguaje Musical", "Armonía"], "Comprobando get_nombre_asignaturas_profesor()")

    def test_get_horario_profesor(self):
        self.conser.dar_alta_asignatura("Armonía", "JJ", "M:20-21", "Aula01")
        self.assertEqual(self.conser.get_horario_profesor("JJ"), ["L:16-17, X:16-17", "M:20-21"], "Comprobando get_horario_profesor()")

    def test_get_aulas_profesor(self):
        self.conser.dar_alta_asignatura("Armonía", "JJ", "M:20-21", "Aula01")
        self.assertEqual(self.conser.get_aulas_profesor("JJ"), ["Aula01"], "Comprobando get_aulas_profesor()")

    def test_to_string(self):
        self.conser.dar_alta_alumno("Luis", "otro@correo.ugr.es", "74606489D", "Coro")
        self.conser.dar_alta_asignatura("Coro", "JJ", "M:20-21", "Aula01")
        str = "¡Bienvenido a MiConservatorio!\n\n"
        str += "--------------    ALUMNOS    --------------\n\n"
        str += "--> Carlos (DNI: 75931715K, @: carlossamu7@correo.ugr.es)\n"
        str += "    Asignaturas: Lenguaje Musical, Coro\n"
        str += "--> Luis (DNI: 74606489D, @: otro@correo.ugr.es)\n"
        str += "    Asignaturas: Coro\n\n\n"
        str += "--------------  ASIGNATURAS  --------------\n\n"
        str += "--> Lenguaje Musical\n"
        str += "    Profesor: JJ\n"
        str += "    Horario: L:16-17, X:16-17\n"
        str += "    Aula: Aula01\n"
        str += "--> Coro\n"
        str += "    Profesor: JJ\n"
        str += "    Horario: M:20-21\n"
        str += "    Aula: Aula01\n"
        self.assertEqual(self.conser.to_string(), str, "Comprobando to_string()")


if __name__ == '__main__':
    unittest.main()
