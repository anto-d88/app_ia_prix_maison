import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ---------------------
# 🧠 Données de base
# ---------------------
data = {
    "surface_m2": [35, 45, 60, 70, 80, 90, 100, 120, 150, 180, 200],
    "nb_pieces":  [1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7],
    "ville": ["Tourcoing","Lille","Roubaix","Lille","Tourcoing","Roubaix",
              "Lille","Tourcoing","Roubaix","Lille","Tourcoing"],
    "prix_k€": [80, 110, 145, 170, 200, 230, 260, 300, 340, 390, 430]
}
df = pd.DataFrame(data)

# ---------------------
# ⚙️ Préparation du modèle
# ---------------------
df_ml = pd.get_dummies(df, columns=["ville"], drop_first=True)
X = df_ml.drop("prix_k€", axis=1)
y = df_ml["prix_k€"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# ---------------------
# 🎨 Interface Streamlit
# ---------------------
st.set_page_config(page_title="SPIRLIFE AI Estimation", page_icon="🏠", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stSlider > div > div > div > div {
        background: #f54242;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#111;'>🏡 <b>Estimation du prix des maisons</b></h1>", unsafe_allow_html=True)
st.write("Entrez les caractéristiques de la maison pour estimer son prix avec **SPIRLIFE AI Studio** 🧠")

# ---------------------
# 🧩 Entrée utilisateur
# ---------------------
col1, col2 = st.columns(2)
with col1:
    surface = st.slider("Surface (m²)", 30, 250, 100)
with col2:
    pieces = st.slider("Nombre de pièces", 1, 10, 4)

ville = st.selectbox("Ville", ["Lille", "Roubaix", "Tourcoing"])

# ---------------------
# 🔮 Prédiction
# ---------------------
if ville == "Lille":
    data_input = pd.DataFrame([[surface, pieces, 0, 0]], columns=X.columns)
elif ville == "Roubaix":
    data_input = pd.DataFrame([[surface, pieces, 1, 0]], columns=X.columns)
else:
    data_input = pd.DataFrame([[surface, pieces, 0, 1]], columns=X.columns)

prix = model.predict(data_input)[0]

# ---------------------
# 💰 Affichage du résultat
# ---------------------
st.success(f"💰 **Prix estimé : {prix:.1f} k€**")

# ---------------------
# 🖋️ Footer
# ---------------------
st.markdown("""
---
👨‍💻 Créé par **Antonio Robles Soler** – *SPIRLIFE AI Studio*  
💡 Propulsé par *Python, scikit-learn & Streamlit*  
""")
