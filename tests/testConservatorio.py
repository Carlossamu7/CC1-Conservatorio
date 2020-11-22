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

    def test_getDiccionarioAlumnos(self):
        conser = Conservatorio()
        self.assertEqual(conser.getDiccionarioAlumnos(), {}, "Comprobando getDiccionarioAlumnos()")

    def test_getNumeroAlumnos(self):
        conser = Conservatorio()
        conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        conser.darAltaAlumno("Carlos", "otro@correo.ugr.es", "74606489D", "Coro")
        self.assertEqual(conser.getNumeroAlumnos(), 2, "Comprobando getNumeroAlumnos()")

    def test_getDiccionarioAsignaturas(self):
        conser = Conservatorio()
        self.assertEqual(conser.getDiccionarioAsignaturas(), {}, "Comprobando getDiccionarioAsignaturas()")

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
        self.assertEqual(conser.getDiccionarioAlumnos()["75931715K"].toString(), alumno.toString(), "Comprobando darAltaAlumno()")
        with self.assertRaises(ValueError): conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")

    def test_getAlumno(self):
        conser = Conservatorio()
        conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        self.assertEqual(conser.getAlumno("75931715K").toString(), alumno.toString(), "Comprobando getAlumno()")
        self.assertEqual(conser.getAlumno("00000000A"), "No existe ningún alumno con ese DNI.", "Comprobando getAlumno() con alumno no existente")

    def test_getAlumnos(self):
        conser = Conservatorio()
        conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        conser.darAltaAlumno("Carlos", "otro@correo.ugr.es", "74606489D", "Coro")
        self.assertEqual(conser.getAlumnos("Carlos"), ["75931715K", "74606489D"], "Comprobando getAlumnos()")

    def test_getHorarioAsignaturaAlumno(self):
        conser = Conservatorio()
        conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical, Coro")
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        conser.darAltaAsignatura("Coro", "JJ", "M:20-21", "Aula01")
        self.assertEqual(conser.getHorarioAsignaturaAlumno("75931715K", "Lenguaje Musical"), "L:16-17, X:16-17", "Comprobando getHorarioAsignaturaAlumno()")
        self.assertEqual(conser.getHorarioAsignaturaAlumno("75931715K", "Piano"), "Este alumno no está matriculado en esa asignatura.", "Comprobando getHorarioAsignaturaAlumno() con alumno no existente")
        self.assertEqual(conser.getHorarioAsignaturaAlumno("00000000A", "Lenguaje Musical"), "No existe ningún alumno con ese DNI.", "Comprobando getHorarioAsignaturaAlumno() con alumno no existente")

    def test_getHorarioAlumno(self):
        conser = Conservatorio()
        conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical, Coro")
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        conser.darAltaAsignatura("Coro", "JJ", "M:20-21", "Aula01")
        self.assertEqual(conser.getHorarioAlumno("75931715K"), ["L:16-17, X:16-17", "M:20-21"], "Comprobando getHorarioAlumno()")
        self.assertEqual(conser.getHorarioAlumno("00000000A"), "No existe ningún alumno con ese DNI.", "Comprobando getHorarioAlumno() con alumno no existente")

    def test_getAulasAlumno(self):
        conser = Conservatorio()
        conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical, Coro")
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        conser.darAltaAsignatura("Coro", "JJ", "M:20-21", "Aula01")
        self.assertEqual(conser.getAulasAlumno("75931715K"), ["Aula01"], "Comprobando getAulasAlumno()")
        self.assertEqual(conser.getAulasAlumno("00000000A"), "No existe ningún alumno con ese DNI.", "Comprobando getAulasAlumno() con alumno no existente")

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
        self.assertEqual(conser.getDiccionarioAsignaturas()["Lenguaje Musical"].toString(), asig.toString(), "Comprobando darAltaAsignatura()")
        with self.assertRaises(ValueError): conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")

    def test_borrarAsignatura(self):
        conser = Conservatorio()
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        conser.borrarAsignatura("Lenguaje Musical")
        self.assertEqual(conser.getNumeroAsignaturas(), 0, "Comprobando borrarAsignatura()")
        with self.assertRaises(ValueError): conser.borrarAsignatura("Lenguaje Musical")

    def test_getAsignatura(self):
        conser = Conservatorio()
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        asig = Asignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        self.assertEqual(conser.getAsignatura("Lenguaje Musical").toString(), asig.toString(), "Comprobando getAsignatura()")
        self.assertEqual(conser.getAsignatura("Piano"), "No existe la asignatura Piano.", "Comprobando getAsignatura() con asignatura no existente")

    def test_getListaAsignaturasProfesor(self):
        conser = Conservatorio()
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        conser.darAltaAsignatura("Armonía", "JJ", "M:20-21", "Aula01")
        listaAsig = conser.getListaAsignaturasProfesor("JJ")
        listaAsig2 = [Asignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01"), Asignatura("Armonía", "JJ", "M:20-21", "Aula01")]
        for i in range(len(listaAsig)):
            self.assertEqual(listaAsig[i].toString(), listaAsig2[i].toString(), "Comprobando getListaAsignaturasProfesor()")

    def test_getNombreAsignaturasProfesor(self):
        conser = Conservatorio()
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        conser.darAltaAsignatura("Armonía", "JJ", "M:20-21", "Aula01")
        self.assertEqual(conser.getNombreAsignaturasProfesor("JJ"), ["Lenguaje Musical", "Armonía"], "Comprobando getNombreAsignaturasProfesor()")

    def test_getHorarioProfesor(self):
        conser = Conservatorio()
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        conser.darAltaAsignatura("Armonía", "JJ", "M:20-21", "Aula01")
        self.assertEqual(conser.getHorarioProfesor("JJ"), ["L:16-17, X:16-17", "M:20-21"], "Comprobando getHorarioProfesor()")

    def test_getAulasProfesor(self):
        conser = Conservatorio()
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        conser.darAltaAsignatura("Armonía", "JJ", "M:20-21", "Aula01")
        self.assertEqual(conser.getAulasProfesor("JJ"), ["Aula01"], "Comprobando getAulasProfesor()")

    def test_toString(self):
        conser = Conservatorio()
        conser.darAltaAlumno("Carlos", "carlossamu7@correo.ugr.es", "75931715K", "Lenguaje Musical")
        conser.darAltaAlumno("Carlos", "otro@correo.ugr.es", "74606489D", "Coro")
        conser.darAltaAsignatura("Lenguaje Musical", "JJ", "L:16-17, X:16-17", "Aula01")
        conser.darAltaAsignatura("Coro", "JJ", "M:20-21", "Aula01")
        str = "¡Bienvenido a MiConservatorio!\n\n"
        str += "--------------    ALUMNOS    --------------\n\n"
        str += "--> Carlos (DNI: 75931715K, @: carlossamu7@correo.ugr.es)\n"
        str += "    Asignaturas: Lenguaje Musical\n"
        str += "--> Carlos (DNI: 74606489D, @: otro@correo.ugr.es)\n"
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
        self.assertEqual(conser.toString(), str, "Comprobando toString()")


if __name__ == '__main__':
    unittest.main()
