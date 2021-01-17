"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de tests sobre la API
"""

import unittest
import json
import sys
sys.path.append('src')

from app import app, lee_json

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello_conser(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenido a MiConservatorio!', response.data)

    # [HU1] Como administrador quiero dar de alta una asignatura
    # [HU16] Como administrador quiero obtener un listado de las asignaturas y su información
    def test_dar_alta_asignatura(self):
        # 'GET'
        response = self.app.get('/asignatura')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Asignaturas', response.data)

        # 'POST'
        # La información que se envía se lee de conservatorio_test.json
        data = json.dumps(lee_json('conservatorio_test.json')["asignaturas"][0])
        response = self.app.post('/asignatura', data = data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Compruebo que el identificador esté en la respuesta
        self.assertIn(b'003', response.data)

        # 'POST' segunda vez
        response = self.app.post('/asignatura', data = data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Ya existe esta asignatura.', response.data)

    # [HU2] Como administrador quiero modificar una asignatura
    # [HU3] Como administrador quiero borrar una asignatura
    def test_set_delete_asignatura(self):
        # 'GET'
        response = self.app.get('/asignatura/001')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Lenguaje Musical', response.data)

        # 'PUT'
        # La información que se envía se lee de conservatorio_test.json
        data = json.dumps(lee_json('conservatorio_test.json')["asignaturas"][1])
        response = self.app.put('/asignatura/001', data = data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Compruebo los datos cambiados estén en la respuesta
        self.assertIn(b'Javi', response.data)
        self.assertIn(b'V:20-21', response.data)
        self.assertIn(b'Aula03', response.data)

        # 'DELETE'
        response = self.app.delete('/asignatura/001')
        self.assertEqual(response.status_code, 200)
        # Compruebo que ya no está la asignatura con identificador 1.
        self.assertNotIn(b'001', response.data)

    # [HU4] Como alumno quiero matricularme de ciertas asignaturas
    # [HU6] Como alumno consultar mis asignaturas matriculadas
    def test_get_asignaturas_alumno(self):
        # 'GET'
        response = self.app.get('/alumno/74585246H/asignatura')
        self.assertEqual(response.status_code, 200)
        # Compruebo que esté Coro que es la asignatura de dicho alumno
        self.assertIn(b'Coro', response.data)

        # 'POST'
        data = json.dumps({"nombre_asignatura": "Lenguaje Musical"})
        response = self.app.post('/alumno/74585246H/asignatura', data = data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Compruebo que el identificador esté en la respuesta
        self.assertIn(b'Lenguaje Musical', response.data)

if __name__ == '__main__':
    unittest.main()
