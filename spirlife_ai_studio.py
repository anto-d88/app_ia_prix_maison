import streamlit as st

# --- Configuration de la page ---
st.set_page_config(page_title="SPIRLIFE AI Studio", page_icon="🧠", layout="wide")

# --- En-tête / Branding ---
st.markdown("""
<h1 style='text-align:center; color:#0e1117;'>🧠 <b>SPIRLIFE AI Studio</b></h1>
<h3 style='text-align:center; color:gray;'>Créé par <b>Antonio Robles Soler</b> | Lille – Belgique</h3>
<p style='text-align:center; color:#ff4b4b;'>L'intelligence artificielle au service de la créativité et de l'humain.</p>
""", unsafe_allow_html=True)

st.write("---")

# --- Présentation ---
st.markdown("""
### 🌍 Bienvenue !
**SPIRLIFE AI Studio** est un espace de création dédié à l’**intelligence artificielle accessible et positive**.

Antonio développe ici des applications IA à but éducatif, créatif et utile :
- 🧱 **IA de prédiction immobilière**
- 💬 **Chatbots intelligents**
- 🧠 **Reconnaissance d’images et analyse visuelle**
- ⚡ **Automatisation & créativité assistée**
- 🎨 **IA artistique et 3D interactive**

""")

st.write("---")

# --- Projets ---
st.header("🚀 Projets IA disponibles")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏡 Estimation du prix des maisons")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/House_icon.svg/800px-House_icon.svg.png", width=200)
    st.write("""
    Une IA de prédiction du prix des maisons selon la surface, le nombre de pièces et la ville.
    """)
    st.markdown("[🔗 Voir le projet](https://appiaprixmaison-p9u3kvtztlqw6ko77db3jx.streamlit.app/)")

with col2:
    st.subheader("💬 Chatbot IA (à venir)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Robot_icon.svg/640px-Robot_icon.svg.png", width=200)
    st.write("""
    Un assistant conversationnel intelligent développé avec Python et OpenAI API.
    """)

st.write("---")

# --- Section Contact ---
st.header("📬 Contact & Réseaux")
st.write("""
👨‍💻 **Antonio Robles Soler**  
📧 antonioroblessoler@gmail.com  
🌍 Basé entre **Tourcoing**, **Lille** et **Belgique**  
💡 *Fondateur de SPIRLIFE AI Studio*
""")

st.write("---")

# --- Citation ---
st.markdown("""
> 🧠 *« L’intelligence artificielle doit servir l’humanité, pas la remplacer. »*  
> — Antonio Robles Soler
""")
