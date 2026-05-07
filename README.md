# FinCommerce Recommendation System

Proyecto de Machine Learning enfocado en el análisis del dataset brasileño de E-commerce de Olist y en la construcción de modelos de recomendación y clasificación basados en comportamiento de clientes, popularidad de productos y patrones transaccionales.

## Descripción General

Este proyecto explora datos reales de e-commerce para:

* Realizar limpieza y transformación de datos
* Construir variables y features para modelado
* Analizar comportamiento de clientes y productos
* Entrenar modelos de Machine Learning
* Generar recomendaciones y predicciones de categorías de productos
* Evaluar el desempeño de distintos modelos de clasificación

El proyecto fue desarrollado utilizando Python, Pandas, Scikit-learn, XGBoost y LightGBM.

---

## Dataset

Fuente: Olist Brazilian E-Commerce Dataset

El dataset se descarga automáticamente utilizando `kagglehub`.

---

## Estructura del Proyecto

```text
fincommerce-recommendation-system/
│
├── notebooks/
│   ├── 01_EDA_ETL.ipynb
│   ├── 02_EDA_Explorativo.ipynb
│   └── 03_Modelado.ipynb
│
├── data/
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Notebooks

#### `01_EDA_ETL.ipynb`

* Descarga el dataset desde Kaggle
* Limpia y transforma los datos
* Construye variables derivadas y features
* Genera el dataset final para modelado

Output generado:

```text
data/dataset_modelo.csv
```

---

#### `02_EDA_Explorativo.ipynb`

* Análisis Exploratorio de Datos (EDA)
* Análisis de comportamiento de clientes
* Análisis de categorías y productos
* Visualizaciones e insights de negocio

---

#### `03_Modelado.ipynb`

* Preprocesamiento de datos
* Selección de variables
* Label Encoding
* Entrenamiento de modelos
* Evaluación de:

  * Random Forest
  * XGBoost
  * LightGBM

---

## Tecnologías Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* LightGBM
* Jupyter Notebook

---

## Cómo Reproducir el Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Nataliafdiaz/fincommerce-recommendation-system.git
cd fincommerce-recommendation-system
```

---

### 2. Crear un entorno virtual

Mac/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Ejecutar los notebooks en orden

```text
1. notebooks/01_EDA_ETL.ipynb
2. notebooks/02_EDA_Explorativo.ipynb
3. notebooks/03_Modelado.ipynb
```

El primer notebook descarga automáticamente el dataset y genera el archivo procesado utilizado en los notebooks posteriores.

---

## Modelos de Machine Learning

El proyecto compara múltiples modelos supervisados:

* Random Forest Classifier
* XGBoost Classifier
* LightGBM Classifier

Métricas evaluadas:

* Accuracy
* Precision
* Recall
* F1-Score

---

## Próximas Mejoras

* Desplegar una API de recomendaciones
* Implementar modelos de collaborative filtering
* Optimización de hiperparámetros
* Dockerización del proyecto
* Tracking de experimentos con MLflow
* Pipeline CI/CD con GitHub Actions

---


