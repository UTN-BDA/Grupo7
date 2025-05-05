# Grupo7

## Integrantes del grupo 
- Julieta Chaki
- María Guadalupe Cuartara 
- María Belén Sarome

## Descripción
Proyecto de software para una empresa de mudanzas que permita identificar cada caja con un código y gestionar información sobre los clientes y objetos transportados

## Tecnologías
Usamos el lenguaje de programación python, sqlalchemy como ORM, la libreria flask.
Como motor de bases de datos usamos postgresql.
Utilizamos contenedores Docker para la base de datos y para implementar el proyecto.

## Como preparar entorno de trabajo

### Entorno virtual

Lo primero es crear un entorno virtual de python con el comando

`virtualenv venv`

A continuación activamos el entorno virtual
`venv/Scripts/Activate`

Luego instalar los requerimientos del proyecto dentro del entorno virtual con el comando

`pip install -r requirements.txt`

### Preparacion de la base de datos
Crear bases de datos.

Es necesario crear un archivo `.env` en la carpeta principal del repositorio, donde se encuentra el archivo app.py y configurar las rutas de acceso a las bases de datos . Definirlas como `TEST_DATABASE_URI` , `DEV_DATABASE_URI`  y `PROD_DATABASE_URI`
