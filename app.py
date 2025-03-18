import streamlit as st

# Lista de elementos químicos y sus abreviaturas
elementos = {
    "Hidrógeno": "H",
    "Helio": "He",
    "Litio": "Li",
    "Berilio": "Be",
    "Boro": "B",
    "Carbono": "C",
    "Nitrógeno": "N",
    "Oxígeno": "O",
    "Flúor": "F",
    "Neón": "Ne",
    # Agrega más elementos según sea necesario
}

# Función para verificar si la respuesta es correcta
def verificar_respuesta(elemento, respuesta):
    if elementos[elemento] == respuesta:
        return True
    return False

# Título de la página
st.title("Prueba de Abreviaturas de Elementos Químicos")

# Descripción
st.write(
    "En esta página podrás poner a prueba tus conocimientos sobre los elementos químicos y sus abreviaturas."
)

# Pregunta aleatoria
import random

elemento_random = random.choice(list(elementos.keys()))

# Mostrar el nombre del elemento y pedir la abreviatura
respuesta_usuario = st.text_input(f"¿Cuál es la abreviatura de {elemento_random}?")

# Función para manejar los botones
if respuesta_usuario:
    if verificar_respuesta(elemento_random, respuesta_usuario.upper()):
        if st.button("¡Correcto! 🎉"):
            st.success("¡Respuesta correcta!")
    else:
        if st.button("¡Incorrecto! 😞"):
            st.error(f"Respuesta incorrecta. La respuesta correcta es {elementos[elemento_random]}")
else:
    st.warning("Por favor, ingresa una respuesta para verificar.")

