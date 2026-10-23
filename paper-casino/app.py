from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Paper Casino", page_icon="🎰", layout="wide",
                   initial_sidebar_state="collapsed")

# Hide Streamlit chrome so the casino fills the page
st.markdown("""
<style>
#MainMenu, header, footer {visibility: hidden;}
.block-container {padding: 0.5rem 0.5rem 0 0.5rem; max-width: 100%;}
</style>
""", unsafe_allow_html=True)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=1650, scrolling=True)
