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

# Leer el CSV con pandas
bank_account_fraud_df = pd.read_csv("./data/Preprocessed/preprocessed_data.csv")

# Crear la tabla base
create_table_query = '''
CREATE TABLE IF NOT EXISTS preprocessedDB (
    id SERIAL PRIMARY KEY,
    income FLOAT,
    name_email_similarity FLOAT,
    current_address_months_count FLOAT,
    customer_age FLOAT,
    days_since_request FLOAT,
    payment_type FLOAT,
    zip_count_4w FLOAT,
    velocity_6h FLOAT,
    velocity_24h FLOAT,
    velocity_4w FLOAT,
    bank_branch_count_8w FLOAT,
    date_of_birth_distinct_emails_4w FLOAT,
    employment_status FLOAT,
    credit_risk_score FLOAT,
    email_is_free FLOAT,
    housing_status FLOAT,
    phone_home_valid FLOAT,
    phone_mobile_valid FLOAT,
    bank_months_count FLOAT,
    has_other_cards FLOAT,
    proposed_credit_limit FLOAT,
    foreign_request FLOAT,
    source FLOAT,
    session_length_in_minutes FLOAT,
    device_os FLOAT,
    keep_alive_session FLOAT,
    device_distinct_emails_8w FLOAT,
    device_fraud_count FLOAT,
    month FLOAT,
    fraud_class INTEGER
);
'''

with engine.connect() as connection:
    connection.execute(text(create_table_query))
    

# Insertar los datos en la tabla
bank_account_fraud_df.to_sql('preprocessedDB', con=engine, if_exists='append', index=False)
print('Datos creados')

# Crear la session de la Bases de Datos 
with Session(engine) as session:
    # Commit cambios
    session.commit()

# Cerrar session
session.close()