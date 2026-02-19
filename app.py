import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Falo Mbow", page_icon="📍", layout="wide")

# Injection de CSS pour les couleurs spécifiques
st.markdown(f"""
    <style>
    /* Fond de la page principale */
    .stApp {{
        background-color: #f7eeed;
    }}
    
    /* Couleur de la barre latérale (Sidebar) */
    [data-testid="stSidebar"] {{
        background-color: #f7d1d8;
        padding: 20px;
    }}

    /* Style des titres de section */
    .section-title {{
        color: #0b4f60;
        border-bottom: 2px solid #bdd9e6;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 10px;
    }}

    .badge {{
        background-color: #165f70;
        color: white;
        padding: 2px 10px;
        border-radius: 10px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 2px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- BARRE LATÉRALE (30% environ) ---
with st.sidebar:
    st.markdown('<p class="section-title">🎓 Formation</p>', unsafe_allow_html=True)
    st.write("**Licence en Géomatique**")

    st.markdown('<p class="section-title">🛠 Compétences</p>', unsafe_allow_html=True)
    st.markdown("""
        <span class="badge">SIG</span> QGIS, ArcGIS<br>
        <span class="badge">MNT</span> Modélisation terrain<br>
        <span class="badge">Télédétection</span> Landsat, Sentinel<br>
        <span class="badge">Topo</span> GNSS/GPS, levés<br>
        <span class="badge">Dessin</span> AutoCAD, Illustrator
    """, unsafe_allow_html=True)

    st.markdown('<p class="section-title">🌐 Langues</p>', unsafe_allow_html=True)
    st.markdown("- **Français**: Courant\n- **Wolof**: Maternel\n- **Anglais**: Technique")

    st.markdown('<p class="section-title">🧭 Intérêts</p>', unsafe_allow_html=True)
    st.write("🌍 Cartographie Open-source")
    st.write("🥾 Randonnée topo")

# --- CONTENU PRINCIPAL ---
# Header
st.markdown("""
    <div style="background-color: #124c5e; color: white; padding: 25px; border-radius: 15px; margin-bottom: 20px;">
        <h1 style='margin:0;'>FALO MBOW</h1>
        <div style='border-left: 4px solid #ffb347; padding-left: 15px; margin: 10px 0;'>
            Étudiante en Géomatique
        </div>
        <p style='font-size: 0.9rem; opacity: 0.9;'>
            📍 Pikine, Dakar | 📧 falombow1@gmail.com
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<p class="section-title">💼 Expérience Professionnelle</p>', unsafe_allow_html=True)
st.markdown("""
    <div style='margin-bottom: 20px; background: white; padding: 15px; border-radius: 10px;'>
        <span style="background: #daeef7; padding: 2px 10px; border-radius: 10px; float: right;">Août–Sept</span>
        <strong>Stage Géomatique · Mairie Guinaw-Rail</strong><br>
        <i style='color: #666;'>“Réalisation de cartes SIG pour un projet urbain à Pikine”</i>
    </div>
""", unsafe_allow_html=True)

st.markdown('<p class="section-title">📂 Projets Réalisés</p>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)

with col_a:
    with st.expander("🔹 MNT zone côtière (Dakar)", expanded=True):
        st.write("Modélisation numérique de terrain et analyse de pentes pour la gestion du littoral.")

with col_b:
    with st.expander("🔹 Télédétection – Déforestation", expanded=True):
        st.write("Analyse d'images Landsat/Sentinel et calcul d'indices de végétation (NDVI).")

st.info("🗺️ **OpenStreetMap / Pikine** — Contribution participative active à la cartographie locale.")

st.markdown("---")
st.caption("⚡ Logiciels GIS favoris : QGIS, GRASS, SNAP | Dakar · Disponible")
