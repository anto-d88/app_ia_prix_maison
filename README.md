# 🏡 SPIRLIFE AI Studio – Estimation du prix des maisons

### Créé par **Antonio Robles Soler**  
📍 *Tourcoing – Lille – Belgique*

---

## 💡 Description du projet

Cette application web d’intelligence artificielle prédit le **prix estimé d’une maison** selon :
- sa **surface (m²)**  
- son **nombre de pièces**  
- et sa **ville** *(Lille, Roubaix, ou Tourcoing)*  

L’IA utilise un **modèle de régression linéaire** entraîné sur des données locales fictives.  
Elle permet d’illustrer la puissance du *machine learning* appliqué à l’immobilier.

---

## 🚀 Démo en ligne

🔗 [Accéder à l’application sur Streamlit Cloud](https://anto-d88-app-ia-prix-maison.streamlit.app)

*(Si le lien ne fonctionne pas encore, l’application est en cours de déploiement.)*

---

## 🧠 Technologies utilisées

| Outil | Rôle |
|--------|------|
| **Python** | Langage principal |
| **pandas** | Manipulation des données |
| **scikit-learn** | Modèle d’apprentissage automatique |
| **Streamlit** | Interface web interactive |
| **GitHub / Streamlit Cloud** | Hébergement et déploiement |

---

## 🖥️ Fonctionnement

1. L’utilisateur choisit la surface, le nombre de pièces et la ville  
2. L’IA calcule instantanément le prix estimé 💰  
3. Le résultat s’affiche en temps réel dans l’interface web

---

## 📦 Installation locale

```bash
# Cloner le dépôt
git clone https://github.com/anto-d88/app_ia_prix_maison.git
cd app_ia_prix_maison

# Créer un environnement virtuel
python -m venv venv
venv\Scripts\activate  # sous Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app_ia_prix_maison.py
