"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la clase Asignatura
"""

class Asignatura:
    def __init__(self, asignatura, profesor, horario, aula):
        self.__asignatura = asignatura
        self.__profesor = profesor
        self.__horario = horario
        self.__aula = aula

    def getAsignatura(self):
        return self.__asignatura

    def getProfesor(self):
        return self.__profesor

    def getHorario(self):
        return self.__horario

    def getAula(self):
        return self.__aula

    # La asignatura no cambia, no existe setter.

    def setProfesor(self, profesor):
        self.__profesor = profesor

    def setHorario(self, horario):
        self.__horario = horario

    def setAula(self, aula):
        self.__aula = aula

    def toString(self):
        str = "--> " + self.__asignatura + "\n"
        str += "    Profesor: " + self.__profesor + "\n"
        str += "    Horario: " + self.__horario + "\n"
        str += "    Aula: " + self.__aula
        return str
