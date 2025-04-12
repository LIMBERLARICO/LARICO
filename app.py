import streamlit as st

st.title("🔬 Calculadora de Química Básica")

opcion = st.selectbox("¿Qué operación deseas hacer?", [
    "Cálculo de masa molar",
    "Ley de los gases ideales",
    "Estequiometría básica"
])

if opcion == "Cálculo de masa molar":
    st.header("🧪 Cálculo de masa molar")
    elemento = st.text_input("Introduce el símbolo del elemento (ej. H, O, Na, Cl):")
    
    masas_molares = {
        'H': 1.008,
        'O': 15.999,
        'Na': 22.990,
        'Cl': 35.45,
        'C': 12.011,
        'N': 14.007,
        'S': 32.06,
        'Mg': 24.305
    }
    
    if elemento in masas_molares:
        st.success(f"La masa molar de {elemento} es {masas_molares[elemento]} g/mol.")
    elif elemento:
        st.error("Elemento no reconocido. Intenta con H, O, Na, etc.")

elif opcion == "Ley de los gases ideales":
    st.header("💨 Ley de los gases ideales: PV = nRT")
    
    P = st.number_input("Presión (atm)", min_value=0.0)
    V = st.number_input("Volumen (L)", min_value=0.0)
    T = st.number_input("Temperatura (K)", min_value=0.0)
    R = 0.0821  # Constante de los gases ideales (L·atm/mol·K)

    if st.button("Calcular moles (n)"):
        if T > 0:
            n = (P * V) / (R * T)
            st.success(f"Cantidad de sustancia: {n:.4f} moles")
        else:
            st.error("La temperatura debe ser mayor que 0 K")

elif opcion == "Estequiometría básica":
    st.header("⚖️ Cálculo estequiométrico")
    
    masa_dada = st.number_input("Masa del reactivo (g)", min_value=0.0)
    masa_molar = st.number_input("Masa molar del reactivo (g/mol)", min_value=0.0)
    relacion = st.number_input("Relación molar producto/reactivo", value=1.0)

    if st.button("Calcular moles del producto"):
        if masa_molar > 0:
            moles_reactivo = masa_dada / masa_molar
            moles_producto = moles_reactivo * relacion
            st.success(f"Se producen {moles_producto:.2f} moles del producto.")
        else:
            st.error("La masa molar debe ser mayor que 0")
