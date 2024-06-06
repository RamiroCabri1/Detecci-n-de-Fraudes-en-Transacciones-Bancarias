import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# Cargar las variables de entorno desde el archivo .env
load_dotenv(find_dotenv())

# Configurar la conexión
connection_string = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
print("Connection established")

try:
   with engine.connect() as connection:
    
        # Ejecutar la consulta para obtener todas las filas de la tabla
        result = connection.execute(text("SELECT * FROM predata;"))
        rows = result.fetchall()
    
        # Imprimir todas las filas
        for row in rows:
            print("Data row =(%s, %s, %s)" % (str(row[0]), str(row[1]), str(row[2])))
            break
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Cerrar cursor y conexión
    print("Connection closed")