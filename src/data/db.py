import json
import mysql.connector

# Leer las credenciales de MySQL desde config.json
with open('config.json') as config_file:
    config = json.load(config_file)

db_config = config['mysql']

def get_db_connection():
    connection = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    return connection
