class Alumno:
    def __init__(self, nombre, email, dni, asignaturas):
        self.nombre = nombre
        self.email = email
        self.dni = dni
        self.asignaturas = asignaturas

    def getNombre(self):
        return self.nombre

    def getEmail(self):
        return self.email

    def getDni(self):
        return self.dni

    def getAsignaturas(self):
        return self.asignaturas

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEmail(self, email):
        self.email = email

    # El DNI no cambia, no existe setter.

    def setAsignaturas(self, asignaturas):
        self.asignaturas = asignaturas

    # Añadir métodos para matricular y desmatricular asignaturas.

    def printAlumno(self):
        print("--> " + self.nombre + " (DNI: " + self.dni + ", @: " + self.email + ")")
        print("Asignaturas: " + self.asignaturas)

if __name__ == "__main__":
    alumno = Alumno("Carlos", "carlossamu7@correo.ugr.es", "00000000A", "LenguajeMusical")
    alumno.printAlumno()
