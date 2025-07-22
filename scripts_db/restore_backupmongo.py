import os
import sys
import subprocess
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if len(sys.argv) != 2:
    print("Debes indicar la fecha del backup a restaurar.")
    print("Ejemplo: python restore_mongo.py 2025-07-22")
    sys.exit(1)

FECHA = sys.argv[1]
BACKUP_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backups_mongo'))
BACKUP_DIR = os.path.join(BACKUP_FOLDER, FECHA)


if not os.path.isdir(BACKUP_DIR):
    print(f" No se encontró el directorio de backup: {BACKUP_DIR}")
    sys.exit(1)

print(f"Restaurando backup desde {BACKUP_DIR}...")

result = subprocess.run(
    ["mongorestore", f"--uri={MONGO_URI}", BACKUP_DIR],
    capture_output=True, text=True
)

if result.returncode == 0:
    print("Restauración completada correctamente.")
else:
    print("Error al restaurar el backup:")
    print(result.stderr)
