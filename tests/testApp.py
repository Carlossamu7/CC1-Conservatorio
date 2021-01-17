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
    @app.route('/asignatura', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    unittest.main()
