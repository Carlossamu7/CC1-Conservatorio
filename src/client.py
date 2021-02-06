"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación del cliente
"""

import requests
import json
import os
from dotenv import load_dotenv

# Variables de entorno
load_dotenv()
PORT = os.getenv('PORT')
CLIENT_HOST = os.getenv('CLIENT_HOST')

# Variables globales
RUTA = "http://" + CLIENT_HOST + ":" + str(PORT)
PARAM = {'content-type': 'application/json'}

#############################
###         Datos         ###
#############################

asignatura = {
    "id": "003",
    "nombre_asignatura": "Armonía",
    "curso": 2,
    "concepto": "Nociones de acordes",
    "profesor": "Valdivia",
    "horario": "V:16-18",
    "aula": "Aula02"
}

asignatura2 = {
    "id": "002",
    "nombre_asignatura": "Coro",
    "curso": 1,
    "concepto": "Nociones básicas acerca de canto",
    "profesor": "Javi",
    "horario": "V:20-21",
    "aula": "Aula03"
}

alumno = {
    "nombre": "Pepe",
    "email": "pepe@gmail.com",
    "dni": "71254236Y",
    "lista_asignaturas" : ["Lenguaje Musical"]
}

#############################
###       Funciones       ###
#############################

def print_request(response):
    print("Código de estado: {}".format(response.status_code))
    print(response.text)

#############################
###  Historias de usuario ###
#############################

# Ruta inicial de bienvenida
print("Ruta iniciial de bienvenida")
print_request(requests.get(RUTA + "/"))

# [HU1] Como administrador quiero dar de alta una asignatura
print("[HU1] Como administrador quiero dar de alta una asignatura")
print_request(requests.post(RUTA + "/asignaturas", json.dumps(asignatura), headers=PARAM))

# [HU2] Como administrador quiero modificar una asignatura
print("[HU2] Como administrador quiero modificar una asignatura")
print_request(requests.put(RUTA + "/asignaturas/001", json.dumps(asignatura2), headers=PARAM))

# [HU3] Como administrador quiero borrar una asignatura
print("[HU3] Como administrador quiero borrar una asignatura")
print_request(requests.delete(RUTA + "/asignaturas/001"))

# [HU4] Como alumno quiero matricularme de ciertas asignaturas
print("[HU4] Como alumno quiero matricularme de ciertas asignaturas")
print_request(requests.post(RUTA + "/alumnos/74585246H/asignaturas",
              json.dumps({"nombre_asignatura": "Lenguaje Musical"}),
              headers=PARAM))

# [HU5] Como alumno quiero desmatricularme de ciertas asignaturas
print("[HU5] Como alumno quiero desmatricularme de ciertas asignaturas")
print_request(requests.delete(RUTA + "/alumnos/74585246H/asignaturas/Coro"))
