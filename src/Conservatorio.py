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
        self.__dicAlum = {}     # Diccionario
        self.__dicAsig = {}     # Diccionario

    def getNombreConservatorio(self):
        return self.nombreConservatorio

    def getDiccionarioAlumnos(self):
        return self.__dicAlum

    def getNumeroAlumnos(self):
        return len(self.__dicAlum)

    def getDiccionarioAsignaturas(self):
        return self.__dicAsig

    def getNumeroAsignaturas(self):
        return len(self.__dicAsig)

    ###############
    ### Alumnos ###
    ###############

    def existAlumno(self, dni):
        if dni in self.__dicAlum:
            return True
        else:
            return False

    def darAltaAlumno(self, nombre, email, dni, asignaturas):
        if(self.existAlumno(dni)):
            raise ValueError("Ya existe un alumno con este DNI.")
        else:
            # En caso de DNI inválido se levanta una expeción
            alumno = Alumno(nombre, email, dni, asignaturas)
            self.__dicAlum[dni] = alumno

    def getAlumno(self, dni):
        if self.existAlumno(dni):
            return self.__dicAlum[dni]
        else:
            return "No existe ningún alumno con ese DNI."

    def getAlumnos(self, nombreAlum):
        list = []
        for alum in self.__dicAlum:
            if(self.__dicAlum[alum].getNombre()==nombreAlum):
                list.append(self.__dicAlum[alum].getDni())
        return list

    def getHorarioAsignaturaAlumno(self, dni, asignatura):
        if(self.existAlumno(dni)):
            alum = self.__dicAlum[dni]
            if (asignatura in alum.listaAsignaturas()):
                for asi in self.__dicAsig:
                    if(asi==asignatura):
                        return self.__dicAsig[asi].getHorario()
            else:
                return "Este alumno no está matriculado en esa asignatura."

        else:
            return "No existe ningún alumno con ese DNI."

    def getHorarioAlumno(self, dni):
        list = []
        if(self.existAlumno(dni)):
            alum = self.__dicAlum[dni]
            for asig in alum.listaAsignaturas():
                for asi in self.__dicAsig:
                    if(asi==asig):
                        list.append(self.__dicAsig[asi].getHorario())
            return list
        else:
            return "No existe ningún alumno con ese DNI."

    def getAulasAlumno(self, dni):
        list = []
        if(self.existAlumno(dni)):
            alum = self.__dicAlum[dni]
            for asig in alum.listaAsignaturas():
                for asi in self.__dicAsig:
                    if(asi==asig):
                        if(not self.__dicAsig[asi].getAula() in list):
                            list.append(self.__dicAsig[asi].getAula())
            return list
        else:
            return "No existe ningún alumno con ese DNI."

    ###################
    ### Asignaturas ###
    ###################

    def existAsignatura(self, asignatura):
        if asignatura in self.__dicAsig:
            return True
        else:
            return False

    def darAltaAsignatura(self, asignatura, profesor, horario, aula):
        if(self.existAsignatura(asignatura)):
            raise ValueError("Ya existe esta asignatura.")
        else:
            self.__dicAsig[asignatura] = Asignatura(asignatura, profesor, horario, aula)

    def borrarAsignatura(self, asignatura):
        if(self.existAsignatura(asignatura)):
            del self.__dicAsig[asignatura]
        else:
            raise ValueError("Ya existe esta asignatura.")

    def getAsignatura(self, nombreAsig):
        if self.existAsignatura(nombreAsig):
            return self.__dicAsig[nombreAsig]
        else:
            return "No existe la asignatura " + nombreAsig + "."

    def getListaAsignaturasProfesor(self, profesor):
        list = []
        for asig in self.__dicAsig:
            if(self.__dicAsig[asig].getProfesor()==profesor):
                list.append(self.__dicAsig[asig])
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
        for alum in self.__dicAlum:
            str += self.__dicAlum[alum].toString()
            str += "\n"
        str += "\n\n"

        str += "--------------  ASIGNATURAS  --------------\n\n"
        for asig in self.__dicAsig:
            str += self.__dicAsig[asig].toString()
            str += "\n"
        return str
