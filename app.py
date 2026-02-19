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

    /* Caption plus foncée */
    .stMarkdown div p, .stCaption {{
        color: #333333 !important;  /* gris foncé */
        font-weight: 500;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- FIN DU CONTENU ---
st.markdown("---")
st.caption("⚡ Logiciels GIS favoris : QGIS, GRASS, SNAP | Dakar · Disponible")
