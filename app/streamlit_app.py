import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="FinCommerce Predictor",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Estilos personalizados ───────────────────────────────────────────────────
st.markdown("""
<style>
    html, body, [class*="css"] {
        font-family: Arial, sans-serif;
    }

    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 0.2rem;
    }

    .sub-title {
        font-size: 1rem;
        color: #6b7280;
        margin-bottom: 2rem;
    }

    .result-box {
        background: linear-gradient(135deg, #0f4c81 0%, #1a7abf 100%);
        color: white;
        border-radius: 16px;
        padding: 1.8rem;
        text-align: center;
        margin-top: 1.5rem;
    }

    .result-label {
        font-size: 0.85rem;
        opacity: 0.8;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }

    .result-categoria {
        font-size: 1.8rem;
        font-weight: 700;
    }

    .section-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a2e;
        border-bottom: 2px solid #0f4c81;
        padding-bottom: 0.4rem;
        margin-bottom: 1rem;
        margin-top: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Traducciones ─────────────────────────────────────────────────────────────
TRADUCCIONES = {
    "hogar_y_decoracion": ("🏠", "Hogar y Decoración"),
    "electronica_y_tecnologia": ("💻", "Electrónica y Tecnología"),
    "moda_y_belleza": ("👗", "Moda y Belleza"),
    "deporte_ocio_y_juguetes": ("⚽", "Deporte, Ocio y Juguetes"),
    "automotriz_y_construccion": ("🔧", "Automotriz y Construcción"),
    "otros_y_servicios": ("📦", "Otros y Servicios"),
}

# ── Carga de artefactos ──────────────────────────────────────────────────────
@st.cache_resource
def cargar_artefactos():
    base = os.path.dirname(os.path.dirname(__file__))

    modelo = joblib.load(
        os.path.join(base, "deployment", "lightgbm_model.pkl")
    )

    encoder = joblib.load(
        os.path.join(base, "deployment", "label_encoder.pkl")
    )

    features = joblib.load(
        os.path.join(base, "deployment", "feature_columns.pkl")
    )

    return modelo, encoder, features

modelo, encoder, features = cargar_artefactos()

# ── Feature engineering ──────────────────────────────────────────────────────
def preparar_features(compras, popularidad, rating, gasto, dias):
    d = {
        "customer_purchase_count": compras,
        "product_popularity": popularidad,
        "product_rating": rating,
        "customer_total_spend": gasto,
        "days_since_last_purchase": dias,
    }

    d["log_customer_total_spend"] = np.log1p(gasto)
    d["log_product_popularity"] = np.log1p(popularidad)
    d["log_purchase_count"] = np.log1p(compras)
    d["log_days_since"] = np.log1p(dias)

    d["spend_per_purchase"] = gasto / (compras + 1)
    d["recency_score"] = 1.0 / (dias + 1)
    d["popularity_x_rating"] = popularidad * rating
    d["spend_x_popularity"] = gasto * popularidad
    d["rating_centered"] = rating - 4.07

    if gasto < 100:
        d["spend_quartile"] = 0
    elif gasto < 500:
        d["spend_quartile"] = 1
    elif gasto < 1500:
        d["spend_quartile"] = 2
    else:
        d["spend_quartile"] = 3

    d["popularity_decile"] = min(int(popularidad / 30), 9)

    df = pd.DataFrame([d])

    return df[features]

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("📊 Modelo")
    st.metric("Accuracy", "70.1%")
    st.metric("F1 Weighted", "70.1%")
    st.metric("F1 Macro", "69.5%")

    st.divider()

    st.write("**Modelo:** LightGBM")
    st.write("**Categorías:** 6")
    st.write("**Features:** 16")
    st.write("**Train:** 92.556 registros")

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="main-title">🛒 FinCommerce Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Predicción de macro-categorías para recomendaciones e-commerce</div>',
    unsafe_allow_html=True
)

# ── Perfiles demo ────────────────────────────────────────────────────────────
st.markdown(
    '<div class="section-header">⚡ Perfiles demo</div>',
    unsafe_allow_html=True
)

if "perfil" not in st.session_state:
    st.session_state.perfil = None

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Cliente frecuente"):
        st.session_state.perfil = (10, 200, 4.5, 800.0, 10)

with col2:
    if st.button("Cliente nuevo"):
        st.session_state.perfil = (1, 30, 3.0, 50.0, 120)

with col3:
    if st.button("Cliente inactivo"):
        st.session_state.perfil = (2, 80, 4.0, 150.0, 200)

with col4:
    if st.button("Cliente premium"):
        st.session_state.perfil = (15, 350, 4.8, 2000.0, 5)

defaults = st.session_state.perfil if st.session_state.perfil else (3, 50, 4.5, 500.0, 15)
compras_def, pop_def, rating_def, gasto_def, dias_def = defaults

# ── Inputs ───────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="section-header">🔢 Datos del cliente</div>',
    unsafe_allow_html=True
)

col_a, col_b = st.columns(2)

with col_a:
    compras = st.number_input("Cantidad de compras", min_value=1, value=int(compras_def))
    popularidad = st.number_input("Popularidad del producto", min_value=1, value=int(pop_def))
    rating = st.number_input("Rating", min_value=1.0, max_value=5.0, value=float(rating_def))

with col_b:
    gasto = st.number_input("Gasto total (R$)", min_value=1.0, value=float(gasto_def))
    dias = st.number_input("Días desde última compra", min_value=0, value=int(dias_def))

# ── Predicción ───────────────────────────────────────────────────────────────
if st.button("🔍 Predecir categoría"):
    input_df = preparar_features(compras, popularidad, rating, gasto, dias)

    pred_num = modelo.predict(input_df)[0]
    pred_label = encoder.inverse_transform([pred_num])[0]
    proba = modelo.predict_proba(input_df)[0]

    emoji, nombre = TRADUCCIONES.get(pred_label, ("📦", pred_label))

    st.markdown(f"""
    <div class="result-box">
        <div class="result-label">Categoría recomendada</div>
        <div class="result-categoria">{emoji} {nombre}</div>
    </div>
    """, unsafe_allow_html=True)

    proba_df = pd.DataFrame({
        "Categoría": [TRADUCCIONES.get(c, ("", c))[1] for c in encoder.classes_],
        "Probabilidad": proba
    }).sort_values("Probabilidad", ascending=False)

    st.markdown(
        '<div class="section-header">📈 Probabilidades por categoría</div>',
        unsafe_allow_html=True
    )

    st.bar_chart(proba_df.set_index("Categoría"))

    confianza = proba.max() * 100

    if confianza >= 60:
        mensaje = "🟢 Alta confianza del modelo."
    elif confianza >= 40:
        mensaje = "🟡 Confianza moderada."
    else:
        mensaje = "🔴 Baja confianza."

    st.info(f"{mensaje} Confianza estimada: {confianza:.1f}%")