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

    def printAsignatura(self):
        print("--> " + self.asignatura)
        print("Profesor: " + self.profesor)
        print("Horario: " + self.horario)
        print("Aula: " + self.aula)

if __name__ == "__main__":
    asig = Asignatura("LenguajeMusical", "JJ", "L:16-17, X:16-17", "Aula01")
    asig.printAsignatura()
