# Preparación del ambiente de trabajo

La puesta en el ambiente de trabajo de la asignatura está explicada brevemente en este documento como parte del hito 0.

### Creación de par clave pública/privada SSH

En mi caso ya disponía de dicho par. La guía de este proceso se encuentra [aquí](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh).
![](./images/sem_01/ssh_key.png)

### Creación de repositorios para la asignatura: ejercicios de autoevaluación, proyecto y fork de la asignatura.

A continuación se muestran los tres repositorios con todos los documentos que debe de haber presentes como la licencia, el `README` y el `.gitignore` .

- `fork` de la asignatura.
![](./images/sem_01/repo_CC-20-21.png)

- Repositorio para los ejercicios de autoevaluación del temario.
![](./images/sem_01/repo_EjercicioAutoevaluacion.png)

- Repositorio para el proyecto.
![](./images/sem_01/repo_Proyecto.png)

### Configuración de los remotes correcto para repositorio CC-20-21.

Definimos el  repositorio `upstream` con la orden:

`git remote add upstream https://github.com/JJ/CC-20-21.git `

y acualizaremos con

`git pull upstream master --rebase`.

Comprobamos:

![](./images/sem_01/remotos.png)

### Configuración de git local correcta: nombre, dirección de correo electrónico, configuración de rebase.

Toda la información está debidamente actualizada.

![](./images/sem_01/info_personal.png)

Configuración de `pull --rebase` por defecto:

![](./images/sem_01/config_git.png)
