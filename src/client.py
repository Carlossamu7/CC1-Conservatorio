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

# [HU6] Como alumno consultar mis asignaturas matriculadas
print("[HU6] Como alumno consultar mis asignaturas matriculadas")
print_request(requests.get(RUTA + "/alumnos/74585246H/asignaturas"))

# [HU7] Como alumno quiero modificar la dirección de correo
print("[HU7] Como alumno quiero modificar la dirección de correo")
print_request(requests.put(RUTA + "/alumnos/74585246H",
              json.dumps({"email": "otroemail@gmail.com"}),
              headers=PARAM))

# [HU8] Como alumno quiero consultar el horario de una asignatura
print("[HU8] Como alumno quiero consultar el horario de una asignatura")
print_request(requests.get(RUTA + "/alumnos/75931715K/asignaturas/Coro/horario"))

# [HU9] Como alumno quiero consultar el aula de una asignatura
print("[HU9] Como alumno quiero consultar el aula de una asignatura")
print_request(requests.get(RUTA + "/alumnos/75931715K/asignaturas/Coro/aula"))

# [HU10] Como alumno quiero saber mi horario completo
print("[HU10] Como alumno quiero saber mi horario completo")
print_request(requests.get(RUTA + "/alumnos/75931715K/horario"))

# [HU11] Como administrador quiero saber en el número de alumnos y asignaturas del conservatorio
print("[HU11] Como administrador quiero saber en el número de alumnos y asignaturas del conservatorio")
print_request(requests.get(RUTA + "/alumnos/num"))
print_request(requests.get(RUTA + "/asignaturas/num"))

# [HU12] Como administrador quiero saber las asignaturas que imparte un profesor
print("[HU12] Como administrador quiero saber las asignaturas que imparte un profesor")
print_request(requests.get(RUTA + "/profesor/Javi/asignaturas"))

# [HU13] Como administrador quiero saber el horario completo de un profesor
print("[HU13] Como administrador quiero saber el horario completo de un profesor")
print_request(requests.get(RUTA + "/profesor/Javi/horario"))

# [HU14] Como administrador quiero saber las aulas que usa un profesor
print("[HU14] Como administrador quiero saber las aulas que usa un profesor")
print_request(requests.get(RUTA + "/profesor/Javi/aula"))
