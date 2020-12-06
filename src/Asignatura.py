"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la clase Asignatura
"""

import sys
sys.path.append('src')

from AsignaturaConcepto import AsignaturaConcepto

class Asignatura(AsignaturaConcepto):
    def __init__(self, id: str, nombre_asignatura: str, curso: int, concepto: str, profesor: str, horario: str, aula: str):
        AsignaturaConcepto.__init__(self, id, nombre_asignatura, curso, concepto)
        self.__profesor = profesor
        self.__horario = horario
        self.__aula = aula

    def get_profesor(self):
        return self.__profesor

    def get_horario(self):
        return self.__horario

    def get_aula(self):
        return self.__aula

    # La asignatura no cambia, no existe setter.

    def set_profesor(self, profesor: str):
        self.__profesor = profesor

    def set_horario(self, horario: str):
        self.__horario = horario

    def set_aula(self, aula: str):
        self.__aula = aula

    def to_string(self):
        str = "--> " + self.get_nombre_asignatura() + " (" + self.get_id() + ")\n"
        str += "    Curso: {}".format(self.get_curso()) + "\n"
        str += "    Concepto: " + self.get_concepto() + "\n"
        str += "    Profesor: " + self.__profesor + "\n"
        str += "    Horario: " + self.__horario + "\n"
        str += "    Aula: " + self.__aula
        return str
