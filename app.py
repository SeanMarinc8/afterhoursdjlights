import streamlit as st

st.set_page_config(page_title="AFTERHOURS VJ", page_icon="⚡", layout="wide")
st.markdown("""<style>
.stApp{background:#09090c;color:#f5f5f5}
[data-testid="stHeader"]{background:transparent}
h1{letter-spacing:.12em;font-weight:900}
</style>""", unsafe_allow_html=True)
st.title("⚡ AFTERHOURS VJ")
st.caption("WAREHOUSE VISUAL ENGINE  •  BASS-REACTIVE  •  THREE-SCREEN READY")
st.write("Run the live visualizer in a separate browser tab. This dashboard is your setup guide; the visualizer has its own live controls and microphone access.")
st.info("Open **/app/static/visuals.html** on the same Streamlit site. For example: `https://YOUR-APP.streamlit.app/app/static/visuals.html`. If you're running locally, use `http://localhost:8501/app/static/visuals.html`.")
st.link_button(
    "⚡ OPEN VISUAL ENGINE",
    "/static/visuals.html",
    use_container_width=True
)
a,b,c=st.columns(3)
with a:
    st.subheader("01 · AUDIO")
    st.write("Click START AUDIO and grant microphone permission. Point your Mac's mic toward your speakers. For cleaner reaction later, use an audio interface or virtual audio routing.")
with b:
    st.subheader("02 · PERFORMANCE")
    st.write("Keys 1–5 switch scenes. SPACE triggers a flash. D toggles automatic scene changes. F enters fullscreen. Controls also appear on screen.")
with c:
    st.subheader("03 · TVs")
    st.write("Start with HDMI to one TV. A powered 1×4 HDMI splitter duplicates the same fullscreen visuals to three TVs. Different visuals per TV need separate video outputs.")
st.warning("Browser microphone access requires HTTPS (Streamlit Cloud provides this) or localhost. If a hosted browser blocks audio input, run locally. Flashing scenes may be unsuitable for photosensitive viewers; disable strobe or reduce intensity.")
st.caption("Built with Streamlit + HTML Canvas + Web Audio API. No external JavaScript libraries or paid accounts required.")
