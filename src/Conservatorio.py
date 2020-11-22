"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la clase Conservatorio
"""

import sys
sys.path.append('src')

from Alumno import Alumno
from Asignatura import Asignatura

class Conservatorio:
    def __init__(self):
        self.nombreConservatorio = "MiConservatorio"
        self.__listaAlum = []
        self.__listaAsig = []

    def getNombreConservatorio(self):
        return self.nombreConservatorio

    def getListaAlumnos(self):
        return self.__listaAlum

    def getNumeroAlumnos(self):
        return len(self.__listaAlum)

    def getListaAsignaturas(self):
        return self.__listaAsig

    def getNumeroAsignaturas(self):
        return len(self.__listaAsig)

    ###############
    ### Alumnos ###
    ###############

    def existAlumno(self, dni):
        for alum in self.__listaAlum:
            if(alum.getDni()==dni):
                return True
        return False

    def darAltaAlumno(self, nombre, email, dni, asignaturas):
        if(self.existAlumno(dni)):
            raise ValueError("Ya existe un alumno con este DNI.")
        else:
            # En caso de DNI inválido se levanta una expeción
            alumno = Alumno(nombre, email, dni, asignaturas)
            self.__listaAlum.append(alumno)

    def getAlumno(self, dni):
        for alum in self.__listaAlum:
            if(alum.getDni()==dni):
                return alum
        return "No existe ningún alumno con ese DNI."

    def getAlumnos(self, nombreAlum):
        list = []
        for alum in self.__listaAlum:
            if(alum.getNombre()==nombreAlum):
                list.append(alum.getDni())
        return list

    def getHorarioAsignaturaAlumno(self, dni, asignatura):
        if(self.existAlumno(dni)):
            alum = self.getAlumno(dni)
            if (asignatura in alum.listaAsignaturas()):
                for asi in self.__listaAsig:
                    if(asi.getAsignatura()==asignatura):
                        return asi.getHorario()
            else:
                return "Este alumno no está matriculado en esa asignatura."

        else:
            return "No existe ningún alumno con ese DNI."

    def getHorarioAlumno(self, dni):
        list = []
        if(self.existAlumno(dni)):
            alum = self.getAlumno(dni)
            for asig in alum.listaAsignaturas():
                for asi in self.__listaAsig:
                    if(asi.getAsignatura()==asig):
                        list.append(asi.getHorario())
            return ", ".join(list)
        else:
            return "No existe ningún alumno con ese DNI."

    def getAulasAlumno(self, dni):
        list = []
        if(self.existAlumno(dni)):
            alum = self.getAlumno(dni)
            for asig in alum.listaAsignaturas():
                for asi in self.__listaAsig:
                    if(asi.getAsignatura()==asig):
                        if(not asi.getAula() in list):
                            list.append(asi.getAula())
            return ", ".join(list)
        else:
            return "No existe ningún alumno con ese DNI."

    ###################
    ### Asignaturas ###
    ###################

    def existAsignatura(self, asignatura):
        for asig in self.__listaAsig:
            if(asig.getAsignatura()==asignatura):
                return True
        return False

    def darAltaAsignatura(self, asignatura, profesor, horario, aula):
        if(self.existAsignatura(asignatura)):
            raise ValueError("Ya existe esta asignatura.")
        else:
            self.__listaAsig.append(Asignatura(asignatura, profesor, horario, aula))

    def getAsignatura(self, nombreAsig):
        for asig in self.__listaAsig:
            if(asig.getAsignatura()==nombreAsig):
                return asig
        return "No existe la asignatura " + nombreAsig + "."

    def getListaAsignaturasProfesor(self, profesor):
        list = []
        for asig in self.__listaAsig:
            if(asig.getProfesor()==profesor):
                list.append(asig)
        return list

    def getNombreAsignaturasProfesor(self, profesor):
        list = []
        asigProf = self.getListaAsignaturasProfesor(profesor)
        for asig in asigProf:
            list.append(asig.getAsignatura())
        return list

    def getHorarioProfesor(self, profesor):
        list = []
        asigProf = self.getListaAsignaturasProfesor(profesor)
        for asig in asigProf:
            list.append(asig.getHorario())
        return list

    def getAulasProfesor(self, profesor):
        list = []
        asigProf = self.getListaAsignaturasProfesor(profesor)
        for asig in asigProf:
            if(not asig.getAula() in list):
                list.append(asig.getAula())
        return list

    def toString(self):
        str = "¡Bienvenido a " + self.getNombreConservatorio() + "!\n\n"
        str += "--------------    ALUMNOS    --------------\n\n"
        for alum in self.__listaAlum:
            str += alum.toString()
            str += "\n"
        str += "\n\n"
        str += "--------------  ASIGNATURAS  --------------\n\n"
        for asig in self.__listaAsig:
            str += asig.toString()
            str += "\n"
        return str
