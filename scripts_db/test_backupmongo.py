import os
import subprocess
from dotenv import load_dotenv
from pymongo import MongoClient

# 1️⃣ Cargar entorno
load_dotenv()
BACKUP_DATE = os.getenv("MONGO_BACKUP_DATE")
BACKUP_BASE_DIR = os.getenv("MONGO_BACKUP_DIR")
DB_NAME_MONGO = os.getenv("DB_NAME_MONGO")
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKUP_PATH = os.path.join(BASE_DIR, BACKUP_BASE_DIR, BACKUP_DATE, DB_NAME_MONGO)


TEST_DB = os.getenv("TEST_DB_NAME")
READ_USER = os.getenv("TEST_READ_USER")
READ_PASSWORD = os.getenv("TEST_READ_PASSWORD")
MONGO_URI = os.getenv("MONGO_URI")

def restore_to_test_db():
    print(f"📂 Restaurando backup de {BACKUP_DATE} en base '{TEST_DB}'...")
    if not os.path.exists(BACKUP_PATH):
        print(f"La carpeta de backup '{BACKUP_PATH}' no existe.")
        return
    try:
        subprocess.run([
            "mongorestore",
            "--uri", MONGO_URI,
            "--nsFrom", "prueba_proyectomudanza.*",
            "--nsTo", f"{TEST_DB}.*",
            "--drop",
            BACKUP_PATH
        ], check=True)
        print("Restauración exitosa.")
    except subprocess.CalledProcessError as e:
        print("Error al restaurar:", e)

def create_readonly_user():
    print(f"Verificando si el usuario '{READ_USER}' ya existe...")
    client = MongoClient(MONGO_URI)
    admin_db = client["admin"]
    try:
        existing_user = admin_db.command("usersInfo", READ_USER)["users"]
        if existing_user:
            print(f"El usuario '{READ_USER}' ya existe. No se requiere creación.")
        else:
            admin_db.command("createUser", READ_USER, pwd=READ_PASSWORD,
                roles=[{"role": "read", "db": TEST_DB}])
            print("Usuario creado con permisos de lectura.")
    except Exception as e:
        print("Error al consultar o crear el usuario:", e)

if __name__ == "__main__":
    restore_to_test_db()
    create_readonly_user()