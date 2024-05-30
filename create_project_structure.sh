#!/bin/bash

# Crear directorios principales
mkdir -p data/{raw,processed,external}
mkdir -p notebooks
mkdir -p src/{data,features,models,visualization,webapp}
mkdir -p tests
mkdir -p reports/figures

# Crear archivos iniciales
touch requirements.txt
touch .gitignore

# Mensaje de finalización
echo "Estructura del proyecto creada con éxito."

# Opcional: Inicializar un repositorio Git
git add .
git commit -m "Repositorio estructurado"
echo "Repositorio Git actualizado."
cd 'C:/Users/fevc_/c18-61-m-data-bi'

