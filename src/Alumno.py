"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la clase Alumno
"""

import re

# Función sacada de https://perezmartin.es/codigo-python-para-comprobar-si-un-dni-nif-o-nie-es-valido/
# Eso comprueba que:
# - Tenga una longitud de 9 dígitos, todos numéricos menos el primero (extranjeros) y
#   el último (control) que pueden estar entre unas letras concretas.
# - Si es extranjero se sustituye la primera letra por su número correspondiente.
# - Se comprueba el dígito de control (última cifra).
def valido_dni(dni):
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

# Comprobación de email válido
# Función sacada de https://micro.recursospython.com/recursos/como-validar-una-direccion-de-correo-electronico.html
body_regex = re.compile('''
    ^(?!\.)                            # name may not begin with a dot
    (
      [-a-z0-9!\#$%&'*+/=?^_`{|}~]     # all legal characters except dot
      |
      (?<!\.)\.                        # single dots only
    )+
    (?<!\.)$                            # name may not end with a dot
''', re.VERBOSE | re.IGNORECASE)
domain_regex = re.compile('''
    (
      localhost
      |
      (
        [a-z0-9]
            # [sub]domain begins with alphanumeric
        (
          [-\w]*                         # alphanumeric, underscore, dot, hyphen
          [a-z0-9]                       # ending alphanumeric
        )?
      \.                               # ending dot
      )+
      [a-z]{2,}                        # TLD alpha-only
   )$
''', re.VERBOSE | re.IGNORECASE)

def valido_email(email):
    if not isinstance(email, str) or not email or '@' not in email:
        return False

    body, domain = email.rsplit('@', 1)

    match_body = body_regex.match(body)
    match_domain = domain_regex.match(domain)

    if not match_domain:
        # check for Internationalized Domain Names
        # see https://docs.python.org/2/library/codecs.html#module-encodings.idna
        try:
            domain_encoded = domain.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        match_domain = domain_regex.match(domain_encoded)

    return (match_body is not None) and (match_domain is not None)

class Alumno:
    def __init__(self, nombre, email, dni, asignaturas):
        self.__nombre = nombre
        self.__email = email
        if(valido_dni(dni)):
            self.__dni = dni
        else: # Lanza excepción
            raise ValueError("El DNI no es válido.")
        self.__asignaturas = asignaturas

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_dni(self):
        return self.__dni

    def get_asignaturas(self):
        return self.__asignaturas

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_email(self, email):
        self.__email = email

    # El DNI no cambia, no existe setter.

    def lista_asignaturas(self):
        return self.__asignaturas.split(", ")

    def matricula_asignatura(self, asig):
        if asig in self.lista_asignaturas():	# Lanza excepción
            raise ValueError("Asignatura ya matriculada.")
        else:
            if self.__asignaturas == "":
                self.__asignaturas = asig
            else:
                self.__asignaturas += ", " + asig

    def desmatricula_asignatura(self, asig):
        list = self.lista_asignaturas()
        if(asig in list):
            list.remove(asig)
            self.__asignaturas = ", ".join(list)
        else:	# Lanza excepción
            raise ValueError("No existe tal asignatura.")

    def to_string(self):
        str = "--> " + self.__nombre + " (DNI: " + self.__dni + ", @: " + self.__email + ")" + "\n"
        str += "    Asignaturas: " + self.__asignaturas
        return str
