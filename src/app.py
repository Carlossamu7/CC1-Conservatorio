"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la API
"""

import os
import json
from Conservatorio import Conservatorio
from flask import Flask, jsonify, request

app = Flask(__name__)

# Función que lee conservatorio.json
def lee_json(fichero):
    try: # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
        if os.path.exists('../data/{:s}'.format(fichero)):
            path='../data/' + fichero
        elif os.path.exists('./data/{:s}'.format(fichero)):
            path='./data/' + fichero
        else:
            raise IOError("No se encuentra '{:s}'".format(fichero))

        with open(path) as data_file:
            data = json.load(data_file)

    except IOError as fallo:
        print("Error {:s} leyendo '{:s}'".format(fichero, fallo))

    return data

# Función que crea el Conservatorio a partir del json
def crea_conservatorio(data):
    # Creando el conservatorio
    conser = Conservatorio()

    # Dando de alta a los alumnos existentes
    for i in range(len(data["alumnos"])):
        conser.dar_alta_alumno(data["alumnos"][i]["nombre"],
                               data["alumnos"][i]["email"],
                               data["alumnos"][i]["dni"],
                               [asig for asig in data["alumnos"][i]["lista_asignaturas"]])

    # Dando de alta las asignaturas existentes
    for i in range(len(data["asignaturas"])):
        conser.dar_alta_asignatura(data["asignaturas"][i]["id"],
                                   data["asignaturas"][i]["nombre_asignatura"],
                                   data["asignaturas"][i]["curso"],
                                   data["asignaturas"][i]["concepto"],
                                   data["asignaturas"][i]["profesor"],
                                   data["asignaturas"][i]["horario"],
                                   data["asignaturas"][i]["aula"])

    return conser

# Devuelve el json de las asignaturas
def get_asignaturas_json(dic):
    asigs = []
    for asi in dic:
        asig = {}
        asig["id"] = dic[asi].get_id()
        asig["nombre_asignatura"] = dic[asi].get_nombre_asignatura()
        asig["curso"] = dic[asi].get_curso()
        asig["concepto"] = dic[asi].get_concepto()
        asig["profesor"] = dic[asi].get_profesor()
        asig["horario"] = dic[asi].get_horario()
        asig["aula"] = dic[asi].get_aula()
        asigs.append(asig)
    return asigs

# Devuelve el json de los alumnos
def get_alumnos_json(dic):
    alums = []
    for alu in dic:
        alum = {}
        alum["nombre"] = dic[alu].get_nombre()
        alum["email"] = dic[alu].get_email()
        alum["dni"] = dic[alu].get_dni()
        alum["lista_asignaturas"] = dic[alu].get_lista_asignaturas()
        alums.append(alum)
    return alums

@app.route('/')
def hello_conser():
    return jsonify({'mensaje': "Bienvenido a MiConservatorio!"}), 200

# [HU1] Como administrador quiero dar de alta una asignatura
# [HU17] Como administrador quiero obtener un listado de las asignaturas y su información
@app.route('/asignatura', methods=['GET', 'POST'])
def dar_alta_asignatura():
    """ Espera un json del tipo
    {
        "id": "003",
        "nombre_asignatura": "Armonía",
        "curso": 2,
        "concepto": "Nociones de acordes",
        "profesor": "Valdivia",
        "horario": "V:16-18",
        "aula": "Aula02"
    }
    """
    if(request.method == 'POST'):
        try:
            conser.dar_alta_asignatura(request.json["id"],
                                       request.json["nombre_asignatura"],
                                       request.json["curso"],
                                       request.json["concepto"],
                                       request.json["profesor"],
                                       request.json["horario"],
                                       request.json["aula"])
        except Exception as err:   # Error: ya existe la asignatura.
            return jsonify({"Mensaje": str(err)}), 400

    # Tanto 'POST' como 'GET'
    return jsonify({"Asignaturas": get_asignaturas_json(conser.get_diccionario_asignaturas())}), 200

# [HU2] Como administrador quiero modificar una asignatura
# [HU3] Como administrador quiero borrar una asignatura
@app.route('/asignatura/<id_asignatura>', methods=['GET', 'PUT', 'DELETE'])
def set_delete_asignatura(id_asignatura: str):
    if(request.method == 'PUT'):
        """ Espera un json del tipo
        {
            "id": "002",
            "nombre_asignatura": "Coro",
            "curso": 1,
            "concepto": "Nociones básicas acerca de canto",
            "profesor": "JJ",
            "horario": "M:20-21",
            "aula": "Aula02"
        }
        """
        if(conser.exist_asignatura(request.json["id"])):
            asi = conser.get_asignatura(request.json["id"])
            asi.set_profesor(request.json["profesor"])
            asi.set_horario(request.json["horario"])
            asi.set_aula(request.json["aula"])
        else:
            return jsonify({"Mensaje": str(conser.get_asignatura(request.json["id"]))}), 400
    elif(request.method == 'DELETE'):
        try:
            conser.borrar_asignatura(id_asignatura)
        except Exception as err:   # Error: No existe tal asignatura.
            return jsonify({"Mensaje": str(err)}), 400
    # Tanto 'POST' como 'GET' como 'DELETE'
    return jsonify({"Asignaturas": get_asignaturas_json(conser.get_diccionario_asignaturas())}), 200

# [HU4] Como alumno quiero matricularme de ciertas asignaturas
# [HU6] Como alumno consultar mis asignaturas matriculadas
@app.route('/alumno/<string:id_alumno>/asignatura', methods=['GET', 'POST'])
def get_asignaturas_alumno(id_alumno: str):
    if(conser.exist_alumno(id_alumno)):
        if(request.method == 'POST'):
            """
            {
                "nombre_asignatura" : "Lenguaje Musical"
            }
            """
            try:
                conser.get_alumno(id_alumno).matricula_asignatura(request.json["nombre_asignatura"])
            except Exception as err:   # Error: Asignatura ya matriculada.
                return jsonify({"Mensaje": str(err)}), 400
        return jsonify({"Asignaturas": conser.get_alumno(id_alumno).get_lista_asignaturas()}), 200
    else:
        return jsonify({"Mensaje": "No existe ningún alumno con ese DNI."}), 404

# [HU5] Como alumno quiero desmatricularme de ciertas asignaturas
@app.route('/alumno/<string:id_alumno>/asignatura/<string:nombre_asignatura>', methods=['DELETE'])
def delete_asignatura_alumno(id_alumno: str, nombre_asignatura :str):
    if(conser.exist_alumno(id_alumno)):
        if(request.method == 'DELETE'):
            try:
                conser.get_alumno(id_alumno).desmatricula_asignatura(nombre_asignatura)
            except Exception as err:   # Error: No existe tal asignatura.
                return jsonify({"Mensaje": str(err)}), 400
        return jsonify({"Asignaturas": conser.get_alumno(id_alumno).get_lista_asignaturas()}), 200
    else:
        return jsonify({"Mensaje": "No existe ningún alumno con ese DNI."}), 404

# [HU7] Como alumno quiero modificar la dirección de correo
@app.route('/alumno/<string:id_alumno>', methods=['GET', 'PUT'])
def actualiza_email_alumno(id_alumno: str):
    if(conser.exist_alumno(id_alumno)):
        if(request.method == 'PUT'):
            """
            {
                "email" : "otroemail@gmail.com"
            }
            """
            try:
                conser.get_alumno(id_alumno).set_email(request.json["email"])
            except Exception as err:   # Error: Email no válido.
                return jsonify({"Mensaje": str(err)}), 400
        return jsonify({"Alumno": get_alumnos_json({id_alumno: conser.get_alumno(id_alumno)})}), 200
    else:
        return jsonify({"Mensaje": "No existe ningún alumno con ese DNI."}), 404

# [HU8] Como alumno quiero consultar el horario de una asignatura
@app.route('/alumno/<string:id_alumno>/asignatura/<string:nombre_asignatura>/horario')
def get_horario_asignatura_alumno(id_alumno: str, nombre_asignatura: str):
    content = conser.get_horario_asignatura_alumno(id_alumno, nombre_asignatura)
    if(content=="No existe ningún alumno con ese DNI." or
        content=="Este alumno no está matriculado en esa asignatura."):
        return jsonify({"Mensaje": content}), 404
    else:
        return jsonify({'Horario': content}), 200

# [HU9] Como alumno quiero consultar el aula de una asignatura
@app.route('/alumno/<string:id_alumno>/asignatura/<string:nombre_asignatura>/aula')
def get_aula_asignatura_alumno(id_alumno: str, nombre_asignatura: str):
    content = conser.get_aula_asignatura_alumno(id_alumno, nombre_asignatura)
    if(content=="No existe ningún alumno con ese DNI." or
        content=="Este alumno no está matriculado en esa asignatura."):
        return jsonify({"Mensaje": content}), 404
    else:
        return jsonify({'Aula': content}), 200

# [HU10] Como alumno quiero saber mi horario completo
@app.route('/alumno/<string:id_alumno>/horario')
def get_horario_alumno(id_alumno: str):
    content = conser.get_horario_alumno(id_alumno)
    if(content=="No existe ningún alumno con ese DNI."):
        return jsonify({"Mensaje": content}), 404
    else:
        return jsonify({'Horario completo': content}), 200

# [HU11] Como administrador quiero saber en el número de alumnos y asignaturas del conservatorio
@app.route('/alumno/num')
def get_numero_alumnos():
    return jsonify({'Numero de alumnos': conser.get_numero_alumnos()}), 200

# [HU11] Como administrador quiero saber en el número de alumnos y asignaturas del conservatorio
@app.route('/asignatura/num')
def get_numero_asignaturas():
    return jsonify({'Numero de asignaturas': conser.get_numero_asignaturas()}), 200

# [HU12] Como administrador quiero saber las asignaturas que imparte un profesor
@app.route('/profesor/<string:nombre_profesor>/asignatura')
def get_nombre_asignaturas_profesor(nombre_profesor: str):
    content = conser.get_nombre_asignaturas_profesor(nombre_profesor)
    if(content==[]):
        return jsonify({"Mensaje": "No existe el profesor {}.".format(nombre_profesor)}), 404
    else:
        return jsonify({'Asignaturas': content}), 200

# [HU13] Como administrador quiero saber el horario completo de un profesor
@app.route('/profesor/<string:nombre_profesor>/horario')
def get_horario_profesor(nombre_profesor: str):
    content = conser.get_horario_profesor(nombre_profesor)
    if(content==[]):
        return jsonify({"Mensaje": "No existe el profesor {}.".format(nombre_profesor)}), 404
    else:
        return jsonify({'Horario completo': content}), 200

# [HU14] Como administrador quiero saber las aulas que usa un profesor
@app.route('/profesor/<string:nombre_profesor>/aula')
def get_aulas_profesor(nombre_profesor: str):
    content = conser.get_aulas_profesor(nombre_profesor)
    if(content==[]):
        return jsonify({"Mensaje": "No existe el profesor {} o no imparte asignaturas.".format(nombre_profesor)}), 404
    else:
        return jsonify({'Aulas': content}), 200

# [HU14] Como administrador quiero saber las aulas que usa un alumno
@app.route('/alumno/<string:id_alumno>/aula')
def get_aulas_alumno(id_alumno: str):
    content = conser.get_aulas_alumno(id_alumno)
    if(content==[]):
        return jsonify({"Mensaje": "No existe el alumno {} o no imparte asignaturas.".format(nombre_profesor)}), 404
    else:
        return jsonify({'Aulas': content}), 200

# [HU15] Como administrador quiero dar de alta un alumno
# [HU16] Como administrador quiero obtener un listado de los alumnos y su información
@app.route('/alumno', methods=['GET', 'POST'])
def dar_alta_alumno():
    """ Espera un json del tipo
    {
        "nombre": "Pepe",
        "email": "pepe@gmail.com",
        "dni": "71254236Y",
        "lista_asignaturas" : ["Lenguaje Musical"]
    }
    """
    if(request.method == 'POST'):
        try:
            conser.dar_alta_alumno(request.json["nombre"],
                                   request.json["email"],
                                   request.json["dni"],
                                   request.json["lista_asignaturas"])
        except Exception as err:   # Error: ya existe el alumno.
            return jsonify({"Mensaje": str(err)}), 400

    # Tanto 'POST' como 'GET'
    return jsonify({"Alumnos": get_alumnos_json(conser.get_diccionario_alumnos())}), 200

# Leemos el fichero json
data = lee_json('conservatorio.json')
# Creamos el conservatorio con algunos alumnos y asignaturas
conser = crea_conservatorio(data)

if __name__ == '__main__':
    # Ejecutamos la app
    app.run(debug=True, host="127.0.0.1", port=4000)
