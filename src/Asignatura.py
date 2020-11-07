"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la clase Asignatura
"""

class Asignatura:
    def __init__(self, asignatura, profesor, horario, aula):
        self.asignatura = asignatura
        self.profesor = profesor
        self.horario = horario
        self.aula = aula

    def getAsignatura(self):
        return self.asignatura

    def getProfesor(self):
        return self.profesor

    def getHorario(self):
        return self.horario

    def getAula(self):
        return self.aula

    # La asignatura no cambia, no existe setter.

    def setProfesor(self, profesor):
        self.profesor = profesor

    def setHorario(self, horario):
        self.horario = horario

    def setAula(self, aula):
        self.aula = aula

    def toString(self):
        str = "--> " + self.asignatura + "\n"
        str += "    Profesor: " + self.profesor + "\n"
        str += "    Horario: " + self.horario + "\n"
        str += "    Aula: " + self.aula
        return str
