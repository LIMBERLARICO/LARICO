import streamlit as st
import random

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
    return elementos[elemento] == respuesta.upper()

# Título de la página
st.title("Prueba de Abreviaturas de Elementos Químicos")

# Descripción
st.write("En esta página podrás poner a prueba tus conocimientos sobre los elementos químicos y sus abreviaturas.")

# Escoger un elemento aleatorio de la lista
elemento_random = random.choice(list(elementos.keys()))

# Mostrar el nombre completo del elemento y pedir la abreviatura
respuesta_usuario = st.text_input(f"¿Cuál es la abreviatura de {elemento_random}?")

# Verificar respuesta y mostrar mensaje según sea correcto o incorrecto
if respuesta_usuario:
    if verificar_respuesta(elemento_random, respuesta_usuario):
        if st.button("¡Correcto! 🎉"):
            st.success("¡Respuesta correcta!")
    else:
        if st.button("¡Incorrecto! 😞"):
            st.error(f"Respuesta incorrecta. La respuesta correcta es {elementos[elemento_random]}")
else:
    st.warning("Por favor, ingresa una respuesta para verificar.")
