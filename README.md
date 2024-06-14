# **Detección de Fraudes en Transacciones Bancarias**

### *CABRI, Ramiro | PELARTES, Sidney | VERA, Fidel*

![Transacciones Bancarias](/reports/figures/vitaly-gariev-1JnN9QhmTGU-unsplash.jpg)

## **Introducción**
Este repositorio contiene el código y la documentación para un proyecto de detección de fraude en cuentas bancarias para el cumplimiento del proyecto de simulación en No Country.
Se empleó como fuente de datos, un dataset sintetico, extraido de Kaggle: 
![Bank Account Fraud Dataset Suite (NeurIPS 2022)](https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022)
Se utilizan tres modelos de machine learning para identificar transacciones fraudulentas en un conjunto de datos desbalanceado. Los modelos incluyen Regresión Logística, Bosque Aleatorio y Gradient Boosting. Además, se aplica SMOTE (Synthetic Minority Over-sampling Technique) para balancear las clases en el conjunto de datos de entrenamiento.

## **Descripción del Dataset**
Para más información sobre el dataset ingresar a este link:
![Bank Account Fraud Dataset Suite (NeurIPS 2022)](https://github.com/feedzai/bank-account-fraud/blob/main/documents/datasheet.pdf)

## Requisitos
- Python 3.11 o superior
- Librerías necesarias están listadas en `environment.yml`

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/fevc08/c18-61-m-data-bi.git
    cd c18-61-m-data-bi.git
    ```

2. Crea un entorno de Conda e instala las dependencias:
    ```bash
    conda env create -f environment.yml
    conda activate fintech-env
    ```

## Conexión a la Base de Datos
Se realizó la conexión mediante la creación de un servidor de Postgres en Azure de la siguiente forma:
![Base de Datos](/reports/figures/Slide3.PNG)

## Tecnologías Empleadas
![Tecnologías](/reports/figures/Slide4.PNG)

## Resultados

Model: LogisticRegression
Accuracy: 0.70
Confusion Matrix:
 [[208770  87921]
 [  1208   2101]]
Classification Report:
               precision    recall  f1-score   support

           0       0.99      0.70      0.82    296691
           1       0.02      0.63      0.05      3309

    accuracy                           0.70    300000
   macro avg       0.51      0.67      0.43    300000
weighted avg       0.98      0.70      0.82    300000

============================================================
Model: RandomForestClassifier
Accuracy: 0.99
Confusion Matrix:
 [[295617   1074]
 [  3189    120]]
Classification Report:
               precision    recall  f1-score   support

           0       0.99      1.00      0.99    296691
           1       0.10      0.04      0.05      3309

    accuracy                           0.99    300000
   macro avg       0.54      0.52      0.52    300000
weighted avg       0.98      0.99      0.98    300000

============================================================
Model: GradientBoostingClassifier
Accuracy: 0.98
Confusion Matrix:
 [[293324   3367]
 [  2978    331]]
Classification Report:
               precision    recall  f1-score   support

           0       0.99      0.99      0.99    296691
           1       0.09      0.10      0.09      3309

    accuracy                           0.98    300000
   macro avg       0.54      0.54      0.54    300000
weighted avg       0.98      0.98      0.98    300000

============================================================


