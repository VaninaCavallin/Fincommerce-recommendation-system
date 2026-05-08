import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# =========================
# CARGA DE ARTEFACTOS
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEPLOYMENT_DIR = os.path.join(BASE_DIR, "deployment")

modelo = joblib.load(os.path.join(DEPLOYMENT_DIR, "lightgbm_model.pkl"))
encoder = joblib.load(os.path.join(DEPLOYMENT_DIR, "label_encoder.pkl"))
features = joblib.load(os.path.join(DEPLOYMENT_DIR, "feature_columns.pkl"))

# =========================
# CONFIG APP
# =========================
st.set_page_config(
    page_title="FinCommerce Predictor",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 FinCommerce - Predictor de Categoría")
st.markdown("Predicción de macro-categoría basada en comportamiento del cliente.")

# =========================
# INPUTS
# =========================
customer_purchase_count = st.number_input(
    "Cantidad de compras del cliente",
    min_value=1,
    value=1
)

product_popularity = st.number_input(
    "Popularidad del producto",
    min_value=1,
    value=20
)

product_rating = st.number_input(
    "Rating del producto",
    min_value=0.0,
    max_value=5.0,
    value=4.0
)

customer_total_spend = st.number_input(
    "Gasto total del cliente",
    min_value=0.0,
    value=250.0
)

days_since_last_purchase = st.number_input(
    "Días desde última compra",
    min_value=0,
    value=30
)

# =========================
# FEATURE ENGINEERING
# =========================
input_data = pd.DataFrame([{
    "customer_purchase_count": customer_purchase_count,
    "product_popularity": product_popularity,
    "product_rating": product_rating,
    "customer_total_spend": customer_total_spend,
    "days_since_last_purchase": days_since_last_purchase,
}])

input_data["log_customer_total_spend"] = input_data["customer_total_spend"].apply(np.log1p)
input_data["log_product_popularity"] = input_data["product_popularity"].apply(np.log1p)
input_data["log_purchase_count"] = input_data["customer_purchase_count"].apply(np.log1p)
input_data["log_days_since"] = input_data["days_since_last_purchase"].apply(np.log1p)

input_data["spend_per_purchase"] = (
    input_data["customer_total_spend"] /
    input_data["customer_purchase_count"].replace(0, 1)
)

input_data["recency_score"] = 1 / (1 + input_data["days_since_last_purchase"])

for col in features:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[features]

# =========================
# PREDICCIÓN
# =========================
if st.button("Predecir categoría"):
    pred_num = modelo.predict(input_data)[0]
    pred_label = encoder.inverse_transform([pred_num])[0]

    st.success(f"Categoría predicha: {pred_label}")