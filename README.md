# Grupo7

## Integrantes del grupo 
- Julieta Chaki
- María Guadalupe Cuartara 
- María Belén Sarome

## Descripción
Proyecto de software que permite que un usuario identifique cada caja con un código y gestionar información sobre los objetos que se encuentran dentro.

## Tecnologías
Usamos el lenguaje de programación python, sqlalchemy como ORM, la libreria flask.
Como motor de bases de datos usamos postgresql.
Utilizamos contenedores Docker para la base de datos y para implementar el proyecto.

## Como preparar entorno de trabajo

Clonar este repositorio

### Entorno virtual

Crear un entorno virtual de python con el comando (ejecutar en la carpeta raiz del repositorio)

`virtualenv venv`

A continuación activamos el entorno virtual
`venv/Scripts/Activate`

Luego instalar los requerimientos del proyecto dentro del entorno virtual con el comando

`pip install -r requirements.txt`

### Preparacion de la base de datos
Crear una instancia de postgress en un contenedor docker. Es necesario tener instalado docker desktop en la computadora antes. 

Dentro de la carpeta postgresql crear un archivo .env como el siguiente ejemplo y definir las credenciales de postgresql y pgadmin.

```
POSTGRES_PASSWORD = 'usuario'
POSTGRES_DB = 'db_0'
POSTGRES_USER = 'contraseña'

PGADMIN_EMAIL = 'ejemplo@gmail.com'
PGADMIN_PASSWORD = 'contraseña-pgadmin'

```

En una terminal en la carpeta raiz del repositorio ejecutar

`cd postgresql`

`docker compose up -d`

Estos comandos crearan una instancia de postgresql y de pgAdmin. 
Para conectar pgAdmin a postgresql entar en un navegador a `http://localhost:5052/`, iniciar
con las credenciales definidas anteriormente para pgAdmin y registrar un nuevo servidor.
En la parte de connection del servidor, configurar 
- Host name/address:  postgresql
- Port: 5432
- Username  y Password: usar credenciames definidas anteriormente para postgres

Crear una base de datos. 

Es necesario crear un archivo `.env` en la carpeta principal del repositorio y configurar la ruta de acceso a la bases de datos . Definirla como
`DEV_DATABASE_URI` 

### Migraciones

Para crear una nueva migracion ejecutar con el entorno virtual activado el comando:

`flask db migrate -m "nombre-migracion"`


Para aplicar las migraciones existentes a la base de datos ejecutar:

`flask db upgrade`

### Carga de datos de prueba

Para cargar datos a la base de datos ejecutar:

`python seed_data.py`
