import psycopg2
import os
from dotenv import load_dotenv
import re

# Cargar las variables del .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# EXPLAIN ANALYZE seguido de la consulta SELECT que queremos medir 
QUERY = "EXPLAIN ANALYZE SELECT * FROM products  where box_id = 80"

REPEATS = 10

def measure_query_time():

    #try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cur = conn.cursor()

    print(f" Ejecutando consulta {REPEATS} veces...")

    results = []
    for i in range(REPEATS):
        cur.execute(QUERY)
        rows = cur.fetchall()  
        text = str(rows)

        # utilizando regex extrae el tiempo de ejecucion de la query
        match = re.search(r"Execution Time:\s*([\d.]+)", text)
        if match:
            result = float(match.group(1))
            print(f" Intento {i+1}: {result} milisegundos") 
            results.append(result)
    
    avg_time = sum(results) / len(results)
    print(f"\n Tiempo promedio: {avg_time:.4f} segundos")

    cur.close()
    conn.close()

    # except Exception as e:
    #     print("Error al ejecutar la consulta:", e)

if __name__ == "__main__":
    measure_query_time()
