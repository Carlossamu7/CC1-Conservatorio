import os
import json
from Conservatorio import Conservatorio

# Función para tener algunas instancias en el coleccionable
def crea_conservatorio(data):
    # Creando el conservatorio
    conser = Conservatorio()

    # Dando de alta a los alumnos existentes
    for i in range(len(data["alumnos"])):
        conser.dar_alta_alumno(data["alumnos"][i]["nombre"],
                               data["alumnos"][i]["email"],
                               data["alumnos"][i]["dni"],
                               [asig["nombre_asignatura"] for asig in data["alumnos"][0]["lista_asignaturas"]])

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

if __name__ == '__main__':
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

    # Creamos el conservatorio con algunos alumnos y asignatura
    conser = crea_conservatorio(data)
    print(conser.to_string())
