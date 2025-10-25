import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# --- ESTILO MODERNO CON FONDO DE COLOR ---
st.markdown("""
    <style>
        /* Fondo con gradiente de color */
        body {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            font-family: 'Poppins', sans-serif;
        }

        .main {
            background: rgba(255, 255, 255, 0.85);
            border-radius: 25px;
            padding: 2rem;
            box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
            margin-top: 30px;
        }

        h1 {
            color: #222;
            text-align: center;
            font-size: 2.6em !important;
            margin-bottom: 0.6em;
            background: linear-gradient(90deg, #0072ff, #b457ff);
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
            box-shadow: inset 3px 3px 8px rgba(0,0,0,0.05),
                        inset -3px -3px 8px rgba(255,255,255,0.8);
        }

        .stButton button {
            background: linear-gradient(90deg, #8e2de2, #4a00e0);
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
            box-shadow: 0 4px 10px rgba(142, 45, 226, 0.4);
        }

        [data-testid="stSidebar"] {
            background: rgba(255,255,255,0.6);
            border-right: 1px solid rgba(255,255,255,0.3);
            padding: 1.5rem 1rem;
        }

        .stExpander {
            background-color: rgba(255,255,255,0.85) !important;
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
