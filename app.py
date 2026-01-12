import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="🏆 F1 2025 Tracker", layout="wide", initial_sidebar_state="expanded")

st.sidebar.title("🏁 F1 2025 Tracker")
page = st.sidebar.selectbox("Navigation", ["🏠 Accueil", "🏆 Pilotes", "🏆 Équipes", "🏎️ Courses", "📈 Évolution"])

if page == "🏠 Accueil":
    st.title("🏆 F1 2025 Season Tracker - Saison Complete")
    st.markdown("**Lando Norris Champion du Monde • McLaren Double Champion**")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Courses", "24/24", "100%")
    with col2: st.metric("Champion Pilotes", "Lando Norris", "🇬🇧 McLaren")
    with col3: st.metric("Champion Constructeurs", "McLaren", "623 pts")
    with col4: st.metric("Victoires McLaren", "12", "50%")

elif page == "🏆 Pilotes":
    exec(open('pages/01_pilotes.py').read())
    
elif page == "🏆 Équipes":
    exec(open('pages/02_equipes.py').read())
    
elif page == "🏎️ Courses":
    exec(open('pages/03_circuits.py').read())
    
elif page == "📈 Évolution":
    exec(open('pages/04_evolution.py').read())
