# Instala las dependencias
install: requirements.txt
	pipenv install --three
	pipenv run pip3 install -r requirements.txt

# Ejecuta los tests
test:
	python3 tests/testAlumno.py
	python3 tests/testAsignatura.py

clean:
	rm -r ./src/__pycache__
