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
