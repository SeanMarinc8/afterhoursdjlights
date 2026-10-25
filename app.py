import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="AFTERHOURS VJ",
    page_icon="🎧",
    layout="wide"
)

st.title("⚡ AFTERHOURS VJ")
st.caption("LIVE WAREHOUSE VISUAL ENGINE • BASS REACTIVE • DJ MODE")

visuals_file = Path(__file__).parent / "static" / "visuals.html"

if visuals_file.exists():
    html_code = visuals_file.read_text(encoding="utf-8")
    components.html(
        html_code,
        height=750,
        scrolling=False
    )
else:
    st.error("Visual engine not found. Check static/visuals.html in GitHub.")
