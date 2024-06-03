import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Identificación en Kaggle
api = KaggleApi()
api.authenticate()

# Definir el dataset y la ubicación
dataset = 'sgpjesus/bank-account-fraud-dataset-neurips-2022'
file_name = 'Base.csv'
zip_file = 'bank-account-fraud-dataset-neurips-2022.zip'

# Descargar la dataset
api.dataset_download_files(dataset, path='.', unzip=False)

# Extraer el csv específico
with zipfile.ZipFile(zip_file, 'r') as z:
    z.extract(file_name, "../data/raw")

# Borrar archivo .zip
os.remove(zip_file)