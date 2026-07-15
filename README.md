🛒 FinCommerce – Product Recommendation System

Pipeline End-to-End de Ciencia de Datos para desarrollar un sistema inteligente de recomendación de productos en e-commerce mediante Machine Learning, con despliegue interactivo en Streamlit.

<p align="center">

(INSERTAR BANNER)

</p>
📊 Resumen del proyecto
	
🛒 Dataset	Olist Brazilian E-commerce
👥 Clientes	+99.000
📦 Productos	+32.000
🧾 Pedidos	+100.000
🤖 Modelo ganador	LightGBM
🎯 Evaluación	Precision@K · Recall@K · NDCG
🚀 Deploy	Streamlit
🛠 Tecnologías
<p align="center">

(PEGAR LOS MISMOS BADGES DEL README DE CHURN)

Agregar además:

PostgreSQL
Streamlit
Kaggle
Git
GitHub
</p>
📌 Descripción

Los sistemas de recomendación son uno de los componentes más importantes dentro del comercio electrónico moderno, ya que permiten ofrecer productos personalizados, mejorar la experiencia del usuario e incrementar las ventas.

En este proyecto se desarrolló un pipeline completo de Ciencia de Datos utilizando el dataset público de Olist Brazilian E-Commerce, abordando todas las etapas del proceso analítico: comprensión del negocio, limpieza e integración de datos, análisis exploratorio, ingeniería de variables, entrenamiento de modelos de Machine Learning y desarrollo de una aplicación interactiva para la generación de recomendaciones.

El proyecto fue desarrollado siguiendo la metodología CRISP-DM y mediante un flujo de trabajo colaborativo basado en Scrum, utilizando Git y GitHub para el control de versiones, gestión de ramas y colaboración entre integrantes del equipo.

Más allá del entrenamiento del modelo, el objetivo fue construir una solución reproducible capaz de transformar datos transaccionales en recomendaciones útiles para apoyar la toma de decisiones comerciales.

🎯 Objetivos de negocio
Analizar el comportamiento de compra de los clientes.
Identificar patrones de consumo y preferencias.
Construir un pipeline reproducible de Ciencia de Datos.
Entrenar modelos de Machine Learning para recomendaciones.
Desarrollar una aplicación interactiva para consultar recomendaciones personalizadas.
Traducir resultados analíticos en información útil para el negocio.
📂 Dataset

Fuente

Olist Brazilian E-Commerce Dataset (Kaggle)

El proyecto integra múltiples tablas relacionales que contienen información sobre:

Clientes
Pedidos
Productos
Categorías
Pagos
Vendedores
Reseñas
Geolocalización

Durante el proceso de ETL estas tablas fueron integradas para construir un único dataset orientado al modelado.

🔄 Metodología CRISP-DM

flowchart LR

A[Business Understanding]
-->B[Data Understanding]
-->C[EDA + ETL]
-->D[Feature Engineering]
-->E[Machine Learning]
-->F[Recommendation Engine]
-->G[Streamlit App]
Durante el proceso de ETL estas tablas fueron integradas para construir un único dataset orientado al modelado.

🏗 Arquitectura del proyecto

Olist Dataset
       │
       ▼
Extracción de datos
       │
       ▼
ETL
       │
       ▼
EDA
       │
       ▼
Feature Engineering
       │
       ▼
Machine Learning
       │
       ▼
Sistema de Recomendación
       │
       ▼
Aplicación Streamlit

📁 Estructura del repositorio

fincommerce-recommendation-system/

│

├── notebooks/

│ ├── 01_EDA_ETL.ipynb

│ ├── 02_EDA_Explorativo.ipynb

│ └── 03_Modelado.ipynb

│

├── data/

├── models/

├── app.py

├── requirements.txt

├── README.md

└── .gitignore

📚 Notebooks

| Notebook                     | Descripción                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------- |
| **01_EDA_ETL.ipynb**         | Descarga del dataset, limpieza, integración y transformación de datos.          |
| **02_EDA_Explorativo.ipynb** | Análisis exploratorio, visualizaciones e identificación de insights de negocio. |
| **03_Modelado.ipynb**        | Entrenamiento y evaluación de modelos de Machine Learning para recomendaciones. |


🤖 Modelos implementados

Se evaluaron distintos algoritmos supervisados para estimar la categoría de producto más adecuada para cada cliente.

Modelos implementados:

Random Forest
XGBoost
LightGBM

Durante la etapa de modelado se realizaron tareas de:

Preprocesamiento
Feature Engineering
Label Encoding
Entrenamiento
Validación
Comparación de desempeño

El modelo LightGBM presentó el mejor equilibrio entre precisión y velocidad de inferencia, por lo que fue seleccionado para el sistema de recomendación final.

🎯 Sistema de recomendación

El sistema desarrollado utiliza el modelo entrenado para generar recomendaciones personalizadas considerando el historial de compras de cada cliente.

La lógica de recomendación combina:

Predicción de categorías mediante Machine Learning.
Popularidad de productos.
Historial de compras.
Afinidad del cliente.
Exclusión de productos previamente adquiridos.

Este enfoque permite generar recomendaciones relevantes y adaptadas al comportamiento individual de cada usuario.

📱 Aplicación interactiva (Streamlit)

El proyecto incluye una aplicación desarrollada en Streamlit que permite explorar las recomendaciones generadas por el modelo.

Funcionalidades principales
Buscar clientes existentes.
Generar recomendaciones personalizadas.
Filtrar por categorías.
Excluir productos previamente comprados.
Visualizar historial de compras.
Consultar métricas del modelo.
📈 Visualizaciones
Exploración de datos

(Agregar imagen)

Análisis exploratorio del comportamiento de clientes y distribución de productos.

Categorías más vendidas

(Agregar imagen)

Distribución de categorías con mayor volumen de ventas.

Desempeño del modelo

(Agregar imagen)

Comparación de modelos de Machine Learning evaluados durante el proyecto.

Aplicación Streamlit

(Agregar captura de pantalla)

Interfaz desarrollada para consultar recomendaciones de productos en tiempo real.

💼 Competencias demostradas
Machine Learning End-to-End
Recommendation Systems
ETL
EDA
Feature Engineering
Modelado supervisado
Business Analytics
CRISP-DM
Storytelling con datos
Desarrollo de aplicaciones con Streamlit
Git & GitHub
Trabajo colaborativo bajo Scrum
⭐ Valor agregado
Pipeline completo de Ciencia de Datos desde la comprensión del negocio hasta el despliegue de una aplicación funcional.
Integración de múltiples fuentes de datos para construir un dataset listo para modelado.
Comparación de distintos algoritmos de Machine Learning.
Desarrollo de un sistema de recomendación personalizado con aplicación interactiva.
Implementación siguiendo buenas prácticas de control de versiones mediante Git y GitHub en un entorno colaborativo.
🚀 Próximas mejoras
Implementar Collaborative Filtering.
Incorporar modelos híbridos de recomendación.
Optimizar hiperparámetros mediante GridSearchCV.
Dockerizar la aplicación.
Integrar MLflow para el seguimiento de experimentos.
Automatizar el pipeline mediante GitHub Actions.
👩‍💻 Autora

Vanina Cavallin

Ph.D. in Biological Sciences | Data Scientist | Data Analyst

📧 Email: vaninacavallin@gmail.com

💼 LinkedIn: https://linkedin.com/in/vanina-cavallin
