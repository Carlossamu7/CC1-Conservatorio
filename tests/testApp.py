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

        # 'GET' no existe
        response = self.app.get('/alumno/745246H/asignatura')
        self.assertEqual(response.status_code, 404)
        # Compruebo que esté Coro que es la asignatura de dicho alumno
        self.assertIn(b'No existe', response.data)

        # 'POST'
        data = json.dumps({"nombre_asignatura": "Lenguaje Musical"})
        response = self.app.post('/alumno/74585246H/asignatura', data = data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Compruebo que el identificador esté en la respuesta
        self.assertIn(b'Lenguaje Musical', response.data)

        # 'POST' segunda vez
        response = self.app.post('/alumno/74585246H/asignatura', data = data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # Compruebo que el identificador esté en la respuesta
        self.assertIn(b'matriculada', response.data)

    # [HU5] Como alumno quiero desmatricularme de ciertas asignaturas
    def test_delete_asignatura_alumno(self):
        # 'DELETE'
        response = self.app.delete('/alumno/74585246H/asignatura/Coro')
        self.assertEqual(response.status_code, 200)
        # Compruebo que ya no está la asignatura con identificador 1.
        self.assertNotIn(b'Coro', response.data)

        # Deshago el efecto de 'DELETE'
        data = json.dumps({"nombre_asignatura": "Coro"})
        response = self.app.post('/alumno/74585246H/asignatura', data = data, content_type='application/json')

        # 'DELETE' de una asignatura que no existe
        response = self.app.delete('/alumno/74585246H/asignatura/Corrrro')
        self.assertEqual(response.status_code, 400)
        # Compruebo que ya no está la asignatura con identificador 1.
        self.assertIn(b'No existe', response.data)

        # 'DELETE' de un alumno que no existe
        response = self.app.delete('/alumno/745246H/asignatura/Coro')
        self.assertEqual(response.status_code, 404)
        # Compruebo que ya no está la asignatura con identificador 1.
        self.assertIn(b'No existe', response.data)

    # [HU7] Como alumno quiero modificar la dirección de correo
    def test_actualiza_email_alumno(self):
        # 'GET'
        response = self.app.get('/alumno/74585246H')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'luis@gmail.com', response.data)

        # 'GET' de un alumno que no existe
        response = self.app.get('/alumno/745246H')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'No existe', response.data)

        # 'PUT'
        data = json.dumps({"email": "otroemail@gmail.com"})
        response = self.app.put('alumno/74585246H', data = data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Compruebo los datos cambiados estén en la respuesta
        self.assertIn(b'otroemail@gmail.com', response.data)
        self.assertNotIn(b'luis@gmail.com', response.data)

        # 'PUT' de un email no válido
        data = json.dumps({"email": "otroemailgmail.com"})
        response = self.app.put('alumno/74585246H', data = data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # Compruebo los datos cambiados estén en la respuesta
        self.assertIn(b'El email no es', response.data)

    # [HU8] Como alumno quiero consultar el horario de una asignatura
    def test_get_horario_asignatura_alumno(self):
        # 'GET'
        response = self.app.get('/alumno/74585246H/asignatura/Coro/horario')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'M:20-21', response.data)

        # 'GET' de asignatura que no existe
        response = self.app.get('/alumno/74585246H/asignatura/Corrro/horario')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Este alumno no', response.data)

        # 'GET' de alumno que no existe
        response = self.app.get('/alumno/745846H/asignatura/Coro/horario')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'No existe', response.data)

if __name__ == '__main__':
    unittest.main()
