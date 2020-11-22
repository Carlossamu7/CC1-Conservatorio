"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la clase Alumno
"""

# Función sacada de https://perezmartin.es/codigo-python-para-comprobar-si-un-dni-nif-o-nie-es-valido/
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
        self.__nombre = nombre
        self.__email = email
        if(validoDNI(dni)):
            self.__dni = dni
        else: # Lanza excepción
            raise ValueError("El DNI no es válido.")
        self.__asignaturas = asignaturas

    def getNombre(self):
        return self.__nombre

    def getEmail(self):
        return self.__email

    def getDni(self):
        return self.__dni

    def getAsignaturas(self):
        return self.__asignaturas

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEmail(self, email):
        self.__email = email

    # El DNI no cambia, no existe setter.

    def setAsignaturas(self, asignaturas):
        self.__asignaturas = asignaturas

    def listaAsignaturas(self):
        return self.__asignaturas.split(", ")

    def matriculaAsignatura(self, asig):
        if asig in self.listaAsignaturas():	# Lanza excepción
            raise ValueError("Asignatura ya matriculada.")
        else:
            if self.__asignaturas == "":
                self.__asignaturas = asig
            else:
                self.__asignaturas += ", " + asig

    def desmatriculaAsignatura(self, asig):
        list = self.listaAsignaturas()
        if(asig in list):
            list.remove(asig)
            self.__asignaturas = ", ".join(list)
        else:	# Lanza excepción
            raise ValueError("No existe tal asignatura.")

    def toString(self):
        str = "--> " + self.__nombre + " (DNI: " + self.__dni + ", @: " + self.__email + ")" + "\n"
        str += "    Asignaturas: " + self.__asignaturas
        return str
