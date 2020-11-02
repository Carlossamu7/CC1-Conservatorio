"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la clase Alumno
"""

# Eso comprueba que:
# - Tenga una longitud de 9 dígitos, todos numéricos menos el primero (extranjeros) y
# el último (control) que pueden estar entre unas letras concretas.
# - Si es extranjero se sustituye la primera letra por su número correspondiente.
# - Se comprueba el dígito de control (última cifra).
def validoDNI(dni):
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    dig_ext = "XYZ"
    reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
    numeros = "1234567890"
    dni = dni.upper()
    if len(dni) == 9:
        dig_control = dni[8]
        dni = dni[:8]
        if dni[0] in dig_ext:
            dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) \
            and tabla[int(dni)%23] == dig_control
    return False

class Alumno:
    def __init__(self, nombre, email, dni, asignaturas):
        self.nombre = nombre
        self.email = email
        if(validoDNI(dni)):
            self.dni = dni
        else: # Lanza excepción
            raise ValueError("El DNI no es válido.")
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

    def listaAsignaturas(self):
        return self.asignaturas.split(",")

    def matriculaAsignatura(self, asig):
        if asig in self.listaAsignaturas():	# Lanza excepción
            raise ValueError("Asignatura ya matriculada.")
        else:
            if self.asignaturas == "":
                self.asignaturas = asig
            else:
                self.asignaturas += "," + asig

    def desmatriculaAsignatura(self, asig):
        list = self.listaAsignaturas()
        if(asig in list):
            list.remove(asig)
            self.asignaturas = ",".join(list)
        else:	# Lanza excepción
            raise ValueError("No existe tal asignatura.")

    def toString(self):
        str = "--> " + self.nombre + " (DNI: " + self.dni + ", @: " + self.email + ")" + "\n"
        str += "Asignaturas: " + self.asignaturas
        return str
