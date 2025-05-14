import subprocess
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME_RESTORE")
DB_CONTAINER = os.getenv("DB_CONTAINER")
BACKUP_FILE = os.getenv("BACKUP_FILE", "backup.backup")

def restore_backup():
    if not os.path.exists(BACKUP_FILE):
        print(f"Archivo de backup no encontrado: {BACKUP_FILE}")
        return

    print(f"Restaurando backup en la base '{DB_NAME}' dentro del contenedor '{DB_CONTAINER}'...")

    try:
        with open(BACKUP_FILE, "rb") as f:
            subprocess.run([
                "docker", "exec", "-i",
                DB_CONTAINER,
                "pg_restore",
                #"--no-privileges", # puede evitar errores al restaurar
                "--no-owner", # evita errores el restaurar datos de otro usuario
                "-U", DB_USER,
                "-d", DB_NAME,
                "-c"  # Drop/recreate objects
            ], stdin=f, check=True)

        print("Restauración completada con éxito.")
    except subprocess.CalledProcessError as e:
        print("Error durante la restauración:", e)

if __name__ == "__main__":
    restore_backup()
