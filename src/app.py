import os
import json
from Conservatorio import Conservatorio
from flask import Flask, jsonify, request

app = Flask(__name__)

# Función que lee conservatorio.json
def lee_json():
    try: # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
        if os.path.exists('../data/conservatorio.json'):
            path='../data/conservatorio.json'
        elif os.path.exists('./data/conservatorio.json'):
            path='./data/conservatorio.json'
        else:
            raise IOError("No se encuentra 'conservatorio.json'")

        with open(path) as data_file:
            data = json.load(data_file)

    except IOError as fallo:
        print("Error {:s} leyendo conservatorio.json".format( fallo ) )

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

@app.route('/')
def hello_conser():
    return jsonify({'mensaje': "Bienvenido a MiConservatorio!"})

# [HU1] Como administrador quiero dar de alta una asignatura
# [HU16] Como administrador quiero obtener un listado de las asignaturas y su información
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
            return str(err), 400

    # Tanto 'POST' como 'GET'
    asigs = []
    for asi in conser.get_diccionario_asignaturas():
        asig = {}
        asig["id"] = conser.get_diccionario_asignaturas()[asi].get_id()
        asig["nombre_asignatura"] = conser.get_diccionario_asignaturas()[asi].get_nombre_asignatura()
        asig["curso"] = conser.get_diccionario_asignaturas()[asi].get_curso()
        asig["concepto"] = conser.get_diccionario_asignaturas()[asi].get_concepto()
        asig["profesor"] = conser.get_diccionario_asignaturas()[asi].get_profesor()
        asig["horario"] = conser.get_diccionario_asignaturas()[asi].get_horario()
        asig["aula"] = conser.get_diccionario_asignaturas()[asi].get_aula()
        asigs.append(asig)
    return jsonify({"Asignaturas": asigs}), 200

# [HU6] Como alumno consultar mis asignaturas matriculadas
@app.route('/alumno/<string:id_alumno>/asignatura')
def get_asignaturas_alumno(id_alumno: str):
    if(conser.exist_alumno(id_alumno)):
        return jsonify({"Asignaturas": conser.get_alumno(id_alumno).get_lista_asignaturas()}), 200
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
            return str(err), 400

    # Tanto 'POST' como 'GET'
    alums = []
    for alu in conser.get_diccionario_alumnos():
        alum = {}
        alum["nombre"] = conser.get_diccionario_alumnos()[alu].get_nombre()
        alum["email"] = conser.get_diccionario_alumnos()[alu].get_email()
        alum["dni"] = conser.get_diccionario_alumnos()[alu].get_dni()
        alum["lista_asignaturas"] = conser.get_diccionario_alumnos()[alu].get_lista_asignaturas()
        alums.append(alum)
    return jsonify({"Alumnos": alums}), 200

if __name__ == '__main__':
    # Leemos el fichero json
    data = lee_json()
    # Creamos el conservatorio con algunos alumnos y asignaturas
    conser = crea_conservatorio(data)
    # Ejecutamos la app
    app.run(debug=True, host="127.0.0.1", port=4000)
