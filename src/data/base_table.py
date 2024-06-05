import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar la conexión
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
print("Connection established")

# Leer el CSV con pandas
bank_account_fraud_df = pd.read_csv("./data/raw/Base.csv")

# Crear la tabla base
create_table_query = '''
CREATE TABLE IF NOT EXISTS base (
    id SERIAL PRIMARY KEY,
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

with engine.connect() as connection:
    connection.execute(text(create_table_query))

# Insertar los datos en la tabla
bank_account_fraud_df.to_sql('base', con=engine, if_exists='append', index=False)

# Crear la session de la Bases de Datos 
with Session(engine) as session:
    # Commit cambios
    session.commit()

# Cerrar session
session.close()