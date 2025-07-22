import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
FECHA = datetime.now().strftime("%Y-%m-%d")
BACKUP_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backups_mongo'))
OUTPUT_DIR = os.path.join(BACKUP_FOLDER, FECHA)

os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"Creando backup en {OUTPUT_DIR}...")

result = subprocess.run(
    ["mongodump", f"--uri={MONGO_URI}", f"--out={OUTPUT_DIR}"],
    capture_output=True, text=True
)

if result.returncode == 0:
    print("Backup completado correctamente.")
else:
    print("Error al crear el backup:")
    print(result.stderr)