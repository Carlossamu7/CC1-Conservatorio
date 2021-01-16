import os
import json
from Conservatorio import Conservatorio
from flask import Flask, jsonify, request

app = Flask(__name__)

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

# Función para tener algunas instancias en el coleccionable
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

# [HU8] Como alumno quiero consultar el horario de una asignatura
@app.route('/alumno/<string:id_alumno>/asignatura/<string:nombre_asignatura>/horario')
def get_horario_asignatura_alumno(id_alumno: str, nombre_asignatura: str):
    return jsonify({'Horario': conser.get_horario_asignatura_alumno(id_alumno, nombre_asignatura)})

#[HU9] Como alumno quiero consultar el aula de una asignatura
@app.route('/alumno/<string:id_alumno>/asignatura/<string:nombre_asignatura>/aula')
def get_aulas_alumno(id_alumno: str, nombre_asignatura: str):
    return jsonify({'Aula': conser.get_aula_asignatura_alumno(id_alumno, nombre_asignatura)})

# [HU11] Como administrador quiero saber en el número de alumnos y asignaturas del conservatorio
@app.route('/alumno/num')
def get_numero_alumnos():
    return jsonify({'Numero de alumnos': conser.get_numero_alumnos()}), 200

# [HU11] Como administrador quiero saber en el número de alumnos y asignaturas del conservatorio
@app.route('/asignatura/num')
def get_numero_asignaturas():
    return jsonify({'Numero de asignaturas': conser.get_numero_asignaturas()}), 200

# [HU15] Como alumno consultar mis asignaturas matriculadas
@app.route('/alumno/<string:id_alumno>/asignatura')
def get_asignaturas_alumno(id_alumno: str):
    if(conser.exist_alumno(id_alumno)):
        status = 200
        content = {"Asignaturas": conser.get_alumno(id_alumno).get_lista_asignaturas()}
    else:
        status = 204
        content = {"mensaje": "No existe ningún alumno con ese DNI."}
    return jsonify(content), status

if __name__ == '__main__':
    # Leemos el fichero json
    data = lee_json()
    # Creamos el conservatorio con algunos alumnos y asignaturas
    conser = crea_conservatorio(data)
    print(conser.to_string())
    app.run(debug=True, port=4000)
