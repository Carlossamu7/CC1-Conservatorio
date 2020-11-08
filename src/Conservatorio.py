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
        self.listaAlum = []
        self.listaAsig = []

    def getNombreConservatorio(self):
        return self.nombreConservatorio

    def getListaAlumnos(self):
        return self.listaAlum

    def getListaAsignaturas(self):
        return self.listaAsig

    ###############
    ### Alumnos ###
    ###############

    def existAlumno(self, dni):
        for alum in self.listaAlum:
            if(alum.getDni()==dni):
                return True
        return False

    def darAltaAlumno(self, nombre, email, dni, asignaturas):
        if(self.existAlumno(dni)):
            raise ValueError("Ya existe un alumno con este DNI.")
        else:
            # En caso de DNI inválido se levanta una expeción
            alumno = Alumno(nombre, email, dni, asignaturas)
            self.listaAlum.append(alumno)

    ###################
    ### Asignaturas ###
    ###################

    def existAsignatura(self, asignatura):
        for asig in self.listaAsig:
            if(asig.getAsignatura()==asignatura):
                return True
        return False

    def darAltaAsignatura(self, asignatura, profesor, horario, aula):
        if(self.existAsignatura(asignatura)):
            raise ValueError("Ya existe esta asignatura.")
        else:
            self.listaAsig.append(Asignatura(asignatura, profesor, horario, aula))
