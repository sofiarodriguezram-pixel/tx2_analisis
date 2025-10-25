import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# --- CONFIGURACIÓN DE ESTILO MODERNO ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #f9fafb 0%, #eef2f3 100%);
            font-family: 'Poppins', sans-serif;
        }
        .main {
            background: #ffffff;
            border-radius: 25px;
            padding: 2rem;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        h1 {
            color: #222;
            text-align: center;
            font-size: 2.5em !important;
            margin-bottom: 0.5em;
            background: linear-gradient(90deg, #0061ff, #60efff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        h2, h3 {
            color: #333;
            font-style: italic;
        }
        textarea, .stTextArea textarea {
            background: #f5f7fa;
            border-radius: 12px;
            border: none;
            padding: 1rem;
            font-size: 1.1em;
            color: #333;
            box-shadow: inset 3px 3px 8px rgba(0,0,0,0.05), inset -3px -3px 8px rgba(255,255,255,0.8);
        }
        .stButton button {
            background: linear-gradient(90deg, #0078ff, #00e5ff);
            color: white;
            border: none;
            padding: 0.7rem 1.5rem;
            border-radius: 10px;
            font-size: 1em;
            transition: 0.3s ease;
            font-weight: 600;
        }
        .stButton button:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 10px rgba(0, 136, 255, 0.3);
        }
        [data-testid="stSidebar"] {
            background: #f0f2f5;
            border-right: 1px solid #e0e0e0;
            padding: 1.5rem 1rem;
        }
        .stExpander {
            background-color: #ffffff !important;
            border-radius: 15px !important;
            border: 1px solid #ddd !important;
            box-shadow: 0 3px 10px rgba(0,0,0,0.05) !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIONALIDAD ORIGINAL ---
translator = Translator()
st.title('Uso de TextBlob')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
    **Polaridad:** Indica si el sentimiento expresado en el texto es positivo, negativo o neutral.  
    Su valor oscila entre **-1 (muy negativo)** y **1 (muy positivo)**, con **0** representando un sentimiento neutral.
    
    **Subjetividad:** Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo (hechos).  
    Va de **0 (objetivo)** a **1 (subjetivo)**.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        
        st.write('**Polarity:** ', round(blob.sentiment.polarity, 2))
        st.write('**Subjectivity:** ', round(blob.sentiment.subjectivity, 2))
        x = round(blob.sentiment.polarity, 2)
        if x >= 0.5:
            st.success('💚 Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.error('💔 Es un sentimiento Negativo 😔')
        else:
            st.warning('😐 Es un sentimiento Neutral')

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.info(f"Texto corregido: **{blob2.correct()}**")
