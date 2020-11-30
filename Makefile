# Instala las dependencias
install: requirements.txt
	pipenv install --three
	pipenv install -r requirements.txt

# Comprueba sintaxis
sintaxis:
	pipenv run python3.8 src/Alumno.py
	pipenv run python3.8 src/AsignaturaConcepto.py
	pipenv run python3.8 src/Asignatura.py
	pipenv run python3.8 src/Conservatorio.py

# Ejecuta los tests
test:
	# Tests unitarios e informe a través de report -m
	##########################  Test de Alumno  ##########################
	pipenv run coverage run tests/testAlumno.py -v
	pipenv run coverage report -m
	########################  Test de AsignaturaConcepto  ########################
	pipenv run coverage run tests/testAsignaturaConcepto.py -v
	pipenv run coverage report -m
	########################  Test de Asignatura  ########################
	pipenv run coverage run tests/testAsignatura.py -v
	pipenv run coverage report -m
	#######################  Test de Conservatorio  ######################
	pipenv run coverage run tests/testConservatorio.py -v
	pipenv run coverage report -m

# Borra ficheros creados
clean:
	#rm -r ./src/__pycache__
	rm .coverage
	rm Pipfile*
