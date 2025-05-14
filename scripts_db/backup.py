import subprocess
import os
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_CONTAINER = os.getenv("DB_CONTAINER")
BACKUP_DIR = os.getenv("BACKUP_DIR", "./backups")

# Generar nombre del archivo
FILENAME = f"{DB_NAME}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.backup"
OUTPUT_PATH = os.path.join(BACKUP_DIR, FILENAME)

def create_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    print("Creando backup desde contenedor Docker...")

    try:
        subprocess.run([
            "docker", "exec", "-e", f"PGPASSWORD={DB_PASSWORD}",
            DB_CONTAINER,
            "pg_dump",
            "-U", DB_USER,
            "-F", "c",
            DB_NAME, 
        ], check=True, stdout=open(OUTPUT_PATH, "wb"))

        print(f"Backup creado exitosamente en: {OUTPUT_PATH}")
    except subprocess.CalledProcessError as e:
        print(" Error al crear el backup:", e)

if __name__ == "__main__":
    create_backup()
