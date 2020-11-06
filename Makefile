# Instala las dependencias
install: requirements.txt
	pipenv install --three
	pipenv run pip3 install -r requirements.txt

# Ejecuta los tests
test:
	# Tests unitarios e informe a través de report -m
	pipenv run coverage run tests/testAlumno.py
	pipenv run coverage report -m
	pipenv run coverage run tests/testAsignatura.py
	pipenv run coverage report -m

# Borra ficheros creados
clean:
	#rm -r ./src/__pycache__
	rm .coverage
	rm Pipfile*
