import streamlit as st
import random

st.set_page_config(page_title="Quiz de la Tabla Periódica", layout="centered")

st.title("🧪 Quiz de la Tabla Periódica")

# Datos simples, puedes extenderlos o cargarlos de un JSON externo
tabla_periodica = [
    {"nombre": "Hidrógeno", "simbolo": "H", "numero_atomico": 1, "grupo": 1, "periodo": 1, "tipo": "No metal"},
    {"nombre": "Helio", "simbolo": "He", "numero_atomico": 2, "grupo": 18, "periodo": 1, "tipo": "Gas noble"},
    {"nombre": "Litio", "simbolo": "Li", "numero_atomico": 3, "grupo": 1, "periodo": 2, "tipo": "Metal alcalino"},
    {"nombre": "Berilio", "simbolo": "Be", "numero_atomico": 4, "grupo": 2, "periodo": 2, "tipo": "Metal alcalinotérreo"},
    {"nombre": "Boro", "simbolo": "B", "numero_atomico": 5, "grupo": 13, "periodo": 2, "tipo": "Metaloide"},
    {"nombre": "Carbono", "simbolo": "C", "numero_atomico": 6, "grupo": 14, "periodo": 2, "tipo": "No metal"},
    {"nombre": "Nitrógeno", "simbolo": "N", "numero_atomico": 7, "grupo": 15, "periodo": 2, "tipo": "No metal"},
    {"nombre": "Oxígeno", "simbolo": "O", "numero_atomico": 8, "grupo": 16, "periodo": 2, "tipo": "No metal"},
    {"nombre": "Flúor", "simbolo": "F", "numero_atomico": 9, "grupo": 17, "periodo": 2, "tipo": "Halógeno"},
    {"nombre": "Neón", "simbolo": "Ne", "numero_atomico": 10, "grupo": 18, "periodo": 2, "tipo": "Gas noble"}
]

# Preguntas posibles
preguntas = {
    "simbolo": "¿Cuál es el símbolo del elemento {nombre}?",
    "grupo": "¿A qué grupo pertenece el elemento {nombre}?",
    "periodo": "¿En qué período está el elemento {nombre}?",
    "tipo": "¿Qué tipo de elemento es {nombre}?"
}

if "elemento" not in st.session_state:
    st.session_state.elemento = random.choice(tabla_periodica)
    st.session_state.tipo_pregunta = random.choice(list(preguntas.keys()))
    st.session_state.mostrar_resultado = False

elemento = st.session_state.elemento
tipo_pregunta = st.session_state.tipo_pregunta
pregunta_texto = preguntas[tipo_pregunta].format(nombre=elemento["nombre"])

st.subheader(pregunta_texto)

respuesta_usuario = st.text_input("Tu respuesta:")

if st.button("Responder"):
    correcta = str(elemento[tipo_pregunta]).lower()
    if respuesta_usuario.strip().lower() == correcta:
        st.success("✅ ¡Correcto!")
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta es: **{correcta}**")
    st.session_state.mostrar_resultado = True

if st.session_state.mostrar_resultado:
    if st.button("Siguiente pregunta"):
        st.session_state.elemento = random.choice(tabla_periodica)
        st.session_state.tipo_pregunta = random.choice(list(preguntas.keys()))
        st.session_state.mostrar_resultado = False

