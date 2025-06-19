import os
import subprocess

from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_CONTAINER = os.getenv("DB_CONTAINER")
TEST_DB = os.getenv("TEST_DB")
BACKUP_FILE = os.getenv("TEST_BACKUP_FILE")  # Ruta relativa al .backup
LOCAL_PATH = os.path.join(os.getenv("BACKUP_DIR", "./backups"), BACKUP_FILE)

def restore_backup():
    if not os.path.exists(LOCAL_PATH):
        print(f" El archivo {LOCAL_PATH} no existe.")
        return

    print(" Copiando backup al contenedor...")
    subprocess.run(["docker", "cp", LOCAL_PATH, f"{DB_CONTAINER}:/tmp/backup.backup"], check=True)

    print(f" Creando base de datos '{TEST_DB}'...")
    subprocess.run([
        "docker", "exec", "-u", "postgres", DB_CONTAINER,
        "psql", "-U", DB_USER,"-d", "postgres", "-c",f"CREATE DATABASE {TEST_DB};"
    ], check=True)

    print(" Restaurando backup...")
    subprocess.run([
        "docker", "exec", "-u", "postgres", DB_CONTAINER,
        "pg_restore", "-U", DB_USER, "-d", TEST_DB, "--clean",            # limpia los objetos antes de restaurar
    "--if-exists", "/tmp/backup.backup"
    ], check=True)

    print(" Restauración completa.")

if __name__ == "__main__":
    restore_backup()
