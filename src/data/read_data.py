import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# Cargar las variables de entorno desde el archivo .env
load_dotenv(find_dotenv())

# Configurar la conexión
connection_string = f"user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} dbname={os.getenv('DB_NAME')}"
connection = psycopg2.connect(connection_string)
print("Connection established")

cursor = connection.cursor()

# Fetch all rows from table
cursor.execute("SELECT * FROM preprocessedDB;")
rows = cursor.fetchall()

# Print all rows

for row in rows:
    print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
    break