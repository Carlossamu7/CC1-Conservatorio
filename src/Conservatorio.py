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

    def getNumeroAlumnos(self):
        return len(self.listaAlum)

    def getListaAsignaturas(self):
        return self.listaAsig

    def getNumeroAsignaturas(self):
        return len(self.listaAsig)

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

    def getAlumno(self, dni):
        for alum in self.listaAlum:
            if(alum.getDni()==dni):
                return alum
        return "No existe ningún alumno con ese DNI."

    def getNombreAlumno(self, dni):
        if(self.existAlumno(dni)):
            return self.getAlumno(dni).getNombre()
        else:
            return "No existe ningún alumno con ese DNI."

    def getEmail(self, dni):
        if(self.existAlumno(dni)):
            return self.getAlumno(dni).getEmail()
        else:
            return "No existe ningún alumno con ese DNI."

    def getAsignaturas(self, dni):
        if(self.existAlumno(dni)):
            return self.getAlumno(dni).getAsignaturas()
        else:
            return "No existe ningún alumno con ese DNI."

    def getAlumnos(self, nombreAlum):
        list = []
        for alum in self.listaAlum:
            if(alum.getNombre()==nombreAlum):
                list.append(alum.getDni())
        return list

    def getHorarioAlumno(self, dni):
        list = []
        if(self.existAlumno(dni)):
            alum = self.getAlumno(dni)
            for asig in alum.listaAsignaturas():
                for asi in self.listaAsig:
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
                for asi in self.listaAsig:
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
        for asig in self.listaAsig:
            if(asig.getAsignatura()==asignatura):
                return True
        return False

    def darAltaAsignatura(self, asignatura, profesor, horario, aula):
        if(self.existAsignatura(asignatura)):
            raise ValueError("Ya existe esta asignatura.")
        else:
            self.listaAsig.append(Asignatura(asignatura, profesor, horario, aula))

    def getAsignatura(self, nombreAsig):
        for asig in self.listaAsig:
            if(asig.getAsignatura()==nombreAsig):
                return asig
        return "No existe la asignatura " + nombreAsig + "."

    def getProfesor(self, nombreAsig):
        if(self.existAsignatura(nombreAsig)):
            return self.getAsignatura(nombreAsig).getProfesor()
        else:
            return "No existe la asignatura " + nombreAsig + "."

    def getHorario(self, nombreAsig):
        if(self.existAsignatura(nombreAsig)):
            return self.getAsignatura(nombreAsig).getHorario()
        else:
            return "No existe la asignatura " + nombreAsig + "."

    def getAula(self, nombreAsig):
        if(self.existAsignatura(nombreAsig)):
            return self.getAsignatura(nombreAsig).getAula()
        else:
            return "No existe la asignatura " + nombreAsig + "."

    def getListaAsignaturasProfesor(self, profesor):
        list = []
        for asig in self.listaAsig:
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
