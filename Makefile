# Instala las dependencias
install: requirements.txt
	pip3 install -r requirements.txt

# Comprueba sintaxis
sintaxis:
	python3.8 src/Alumno.py
	python3.8 src/AsignaturaConcepto.py
	python3.8 src/Asignatura.py
	python3.8 src/Conservatorio.py

# Ejecuta los tests
test:
	# Tests unitarios e informe a través de report -m
	##########################  Test de Alumno  ##########################
	python3.8 tests/testAlumno.py
	########################  Test de AsignaturaConcepto  ########################
	python3.8 tests/testAsignaturaConcepto.py
	########################  Test de Asignatura  ########################
	python3.8 tests/testAsignatura.py
	#######################  Test de Conservatorio  ######################
	python3.8 tests/testConservatorio.py

# Borra ficheros creados
clean:
	#rm -r ./src/__pycache__
	rm .coverage
	rm Pipfile*
