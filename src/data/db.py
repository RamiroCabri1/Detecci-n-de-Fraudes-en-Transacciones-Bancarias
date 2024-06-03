import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

# Configurar la conexión
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Leer el CSV con pandas
bank_account_fraud_df = pd.read_csv(".\Base.csv")

# Crear un cursor
cur = conn.cursor()

# Crear la tabla base
cur.execute(
    '''CREATE TABLE IF NOT EXISTS base (
    applications_id INT PRIMARY KEY,
    fraud_bool INTEGER,
    income FLOAT,
    name_email_similarity FLOAT,
    prev_address_months_count INTEGER,
    current_address_months_count INTEGER,
    customer_age INTEGER,
    days_since_request FLOAT,
    intended_balcon_amount FLOAT,
    payment_type VARCHAR(255),
    zip_count_4w INTEGER,
    velocity_6h FLOAT,
    velocity_24h FLOAT,
    velocity_4w FLOAT,
    bank_branch_count_8w INTEGER,
    date_of_birth_distinct_emails_4w INTEGER,
    employment_status VARCHAR(255),
    credit_risk_score INTEGER,
    email_is_free INTEGER,
    housing_status VARCHAR(255),
    phone_home_valid INTEGER,
    phone_mobile_valid INTEGER,
    bank_months_count INTEGER,
    has_other_cards INTEGER,
    proposed_credit_limit FLOAT,
    foreign_request INTEGER,
    source VARCHAR(255),
    session_length_in_minutes FLOAT,
    device_os VARCHAR(255),
    keep_alive_session INTEGER,
    device_distinct_emails_8w INTEGER,
    device_fraud_count INTEGER,
    month INTEGER
);
'''
)

# Insertar los datos en la tabla
bank_account_fraud_df.to_sql('base', con = conn, if_exists = 'append')

# Cerrar la conexión
conn.commit()
cur.close()
conn.close()