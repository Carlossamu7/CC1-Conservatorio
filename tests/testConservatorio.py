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
        self.conser.dar_alta_alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", ["Lenguaje Musical", "Coro"])
        self.conser.dar_alta_asignatura("001", "Lenguaje Musical", 1, "Nociones básicas acerca de leer una partitura, entonar y hacer dictados",
                                        "JJ", "L:16-17, X:16-17", "Aula01")
        self.conser.dar_alta_asignatura("002", "Coro", 1, "Nociones básicas acerca de canto",
                                        "JJ", "M:20-21", "Aula01")

    def test_get_conservatorio(self):
        self.assertEqual(self.conser.get_nombre_conservatorio(), "MiConservatorio", "Comprobando get_nombre_conservatorio()")

    def test_get_numero_alumnos(self):
        self.conser.dar_alta_alumno("Carlos", "otro@correo.ugr.es", "74606489D", ["Coro"])
        self.assertEqual(self.conser.get_numero_alumnos(), 2, "Comprobando get_numero_alumnos()")

    def test_get_numero_asignaturas(self):
        self.assertEqual(self.conser.get_numero_asignaturas(), 2, "Comprobando get_numero_asignaturas()")

    ###############
    ### Alumnos ###
    ###############

    def test_exist_alumno(self):
        self.assertTrue(self.conser.exist_alumno("75931715K"), "Comprobando exist_alumno()")

    def test_dar_alta_alumno(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", ["Lenguaje Musical", "Coro"])
        self.assertTrue (self.conser.get_diccionario_alumnos()["75931715K"].__eq__(alumno), "Comprobando dar_alta_alumno()")
        with self.assertRaises(ValueError): self.conser.dar_alta_alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", ["Lenguaje Musical"])

    def test_get_alumno(self):
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", ["Lenguaje Musical", "Coro"])
        self.assertTrue(self.conser.get_alumno("75931715K").__eq__(alumno), "Comprobando get_alumno()")
        self.assertEqual(self.conser.get_alumno("00000000A"), "No existe ningún alumno con ese DNI.", "Comprobando get_alumno() con alumno no existente")

    def test_get_alumnos_nombre(self):
        self.conser.dar_alta_alumno("Carlos", "otro@correo.ugr.es", "74606489D", ["Coro"])
        self.assertEqual(self.conser.get_alumnos_nombre("Carlos"), ["75931715K", "74606489D"], "Comprobando get_alumnos_nombre()")

    def test_get_horario_asignatura_alumno(self):
        self.assertEqual(self.conser.get_horario_asignatura_alumno("75931715K", "Lenguaje Musical"), "L:16-17, X:16-17", "Comprobando get_horario_asignatura_alumno()")
        self.assertEqual(self.conser.get_horario_asignatura_alumno("75931715K", "Piano"), "Este alumno no está matriculado en esa asignatura.", "Comprobando get_horario_asignatura_alumno() con alumno no existente")
        self.assertEqual(self.conser.get_horario_asignatura_alumno("00000000A", "Lenguaje Musical"), "No existe ningún alumno con ese DNI.", "Comprobando get_horario_asignatura_alumno() con alumno no existente")

    def test_get_aula_asignatura_alumno(self):
        self.assertEqual(self.conser.get_aula_asignatura_alumno("75931715K", "Lenguaje Musical"), "Aula01", "Comprobando get_aula_asignatura_alumno()")
        self.assertEqual(self.conser.get_aula_asignatura_alumno("75931715K", "Piano"), "Este alumno no está matriculado en esa asignatura.", "Comprobando get_horario_asignatura_alumno() con alumno no existente")
        self.assertEqual(self.conser.get_aula_asignatura_alumno("00000000A", "Lenguaje Musical"), "No existe ningún alumno con ese DNI.", "Comprobando get_horario_asignatura_alumno() con alumno no existente")

    def test_get_horario_alumno(self):
        self.assertEqual(self.conser.get_horario_alumno("75931715K"), ["L:16-17, X:16-17", "M:20-21"], "Comprobando get_horario_alumno()")
        self.assertEqual(self.conser.get_horario_alumno("00000000A"), "No existe ningún alumno con ese DNI.", "Comprobando get_horario_alumno() con alumno no existente")

    def test_get_aulas_alumno(self):
        self.assertEqual(self.conser.get_aulas_alumno("75931715K"), ["Aula01"], "Comprobando get_aulas_alumno()")
        self.assertEqual(self.conser.get_aulas_alumno("00000000A"), "No existe ningún alumno con ese DNI.", "Comprobando get_aulas_alumno() con alumno no existente")

    ###################
    ### Asignaturas ###
    ###################

    def test_exist_asignatura(self):
        self.assertTrue(self.conser.exist_asignatura("001"), "Comprobando exist_asignatura()")

    def test_dar_alta_asignatura(self):
        asig = Asignatura("001", "Lenguaje Musical", 1, "Nociones básicas acerca de leer una partitura, entonar y hacer dictados",
                          "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertTrue(self.conser.get_diccionario_asignaturas()["001"].__eq__(asig), "Comprobando dar_alta_asignatura()")
        with self.assertRaises(ValueError): self.conser.dar_alta_asignatura("001", "LenguajeMusical", 1, "Nociones básicas acerca de leer una partitura, entonar y hacer dictados",
                                                                            "JJ", "L:16-17, X:16-17", "Aula01")

    def test_borrar_asignatura(self):
        self.conser.borrar_asignatura("001")
        self.assertEqual(self.conser.get_numero_asignaturas(), 1, "Comprobando borrar_asignatura()")
        with self.assertRaises(ValueError): self.conser.borrar_asignatura("001")

    def test_get_asignatura(self):
        asig = Asignatura("001", "Lenguaje Musical", 1, "Nociones básicas acerca de leer una partitura, entonar y hacer dictados",
                          "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertTrue(self.conser.get_asignatura("001").__eq__(asig), "Comprobando get_asignatura()")
        self.assertEqual(self.conser.get_asignatura("010"), "No existe la asignatura con ID 010.", "Comprobando get_asignatura() con asignatura no existente")

    def test_get_lista_asignaturas_profesor(self):
        listaAsig = self.conser.get_lista_asignaturas_profesor("JJ")
        listaAsig2 = [Asignatura("001", "Lenguaje Musical", 1, "Nociones básicas acerca de leer una partitura, entonar y hacer dictados",
                                 "JJ", "L:16-17, X:16-17", "Aula01"),
                      Asignatura("002", "Coro", 1, "Nociones básicas acerca de canto",
                                 "JJ", "M:20-21", "Aula01")]
        for i in range(len(listaAsig)):
            self.assertTrue(listaAsig[i].__eq__(listaAsig2[i]), "Comprobando get_lista_asignaturas_profesor()")

    def test_get_nombre_asignaturas_profesor(self):
        self.assertEqual(self.conser.get_nombre_asignaturas_profesor("JJ"), ["Lenguaje Musical", "Coro"], "Comprobando get_nombre_asignaturas_profesor()")

    def test_get_horario_profesor(self):
        self.assertEqual(self.conser.get_horario_profesor("JJ"), ["L:16-17, X:16-17", "M:20-21"], "Comprobando get_horario_profesor()")

    def test_get_aulas_profesor(self):
        self.assertEqual(self.conser.get_aulas_profesor("JJ"), ["Aula01"], "Comprobando get_aulas_profesor()")

    def test_to_string(self):
        self.conser.dar_alta_alumno("Luis", "otro@correo.ugr.es", "74606489D", ["Coro"])
        str = "¡Bienvenido a MiConservatorio!\n\n"
        str += "--------------    ALUMNOS    --------------\n\n"
        str += "--> Carlos (DNI: 75931715K, @: carlossamu7@correo.ugr.es)\n"
        str += "    Asignaturas: Lenguaje Musical, Coro\n"
        str += "--> Luis (DNI: 74606489D, @: otro@correo.ugr.es)\n"
        str += "    Asignaturas: Coro\n\n\n"
        str += "--------------  ASIGNATURAS  --------------\n\n"
        str += "--> Lenguaje Musical (001)\n"
        str += "    Curso: 1\n"
        str += "    Concepto: Nociones básicas acerca de leer una partitura, entonar y hacer dictados\n"
        str += "    Profesor: JJ\n"
        str += "    Horario: L:16-17, X:16-17\n"
        str += "    Aula: Aula01\n"
        str += "--> Coro (002)\n"
        str += "    Curso: 1\n"
        str += "    Concepto: Nociones básicas acerca de canto\n"
        str += "    Profesor: JJ\n"
        str += "    Horario: M:20-21\n"
        str += "    Aula: Aula01\n"
        self.assertEqual(self.conser.to_string(), str, "Comprobando to_string()")

if __name__ == '__main__':
    unittest.main()
