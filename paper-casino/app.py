import os
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# Address where Liquid Island is hosted (e.g. your Vercel URL).
# You can also set it as an environment variable or Streamlit secret named ISLAND_URL.
ISLAND_URL = "https://hypeisland.vercel.app"

st.set_page_config(page_title="Paper Casino", page_icon="🎰", layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown("""
<style>
#MainMenu, header, footer {visibility: hidden;}
.block-container {padding: 0.5rem 0.5rem 0 0.5rem; max-width: 100%;}
</style>
""", unsafe_allow_html=True)


def island_url() -> str:
    try:
        if "ISLAND_URL" in st.secrets:
            return str(st.secrets["ISLAND_URL"])
    except Exception:
        pass
    return os.environ.get("ISLAND_URL", ISLAND_URL)


url = island_url()
if "YOUR-LIQUID-ISLAND" in url:
    url = ""  # not configured yet: the Liquid Island tab shows a setup note

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
html = html.replace("__ISLAND_URL__", url)
components.html(html, height=1750, scrolling=True)
