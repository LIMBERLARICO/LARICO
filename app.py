import random

# Base de datos resumida
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

def hacer_pregunta():
    elemento = random.choice(tabla_periodica)
    tipo_pregunta = random.choice(["simbolo", "grupo", "periodo", "tipo"])

    if tipo_pregunta == "simbolo":
        respuesta = input(f"¿Cuál es el símbolo del elemento {elemento['nombre']}? ").strip()
        correcta = elemento['simbolo']

    elif tipo_pregunta == "grupo":
        respuesta = input(f"¿A qué grupo pertenece el elemento {elemento['nombre']}? ").strip()
        correcta = str(elemento['grupo'])

    elif tipo_pregunta == "periodo":
        respuesta = input(f"¿En qué periodo se encuentra el elemento {elemento['nombre']}? ").strip()
        correcta = str(elemento['periodo'])

    elif tipo_pregunta == "tipo":
        respuesta = input(f"¿El elemento {elemento['nombre']} es un metal, no metal, metaloide, etc.? ").strip().lower()
        correcta = elemento['tipo'].lower()

    if respuesta.lower() == correcta.lower():
        print("✅ ¡Correcto!\n")
    else:
        print(f"❌ Incorrecto. La respuesta correcta es: {correcta}\n")

def main():
    print("🧪 Bienvenido al Quiz de la Tabla Periódica 🧪")
    while True:
        hacer_pregunta()
        seguir = input("¿Quieres otra pregunta? (s/n): ").strip().lower()
        if seguir != "s":
            print("¡Gracias por jugar! 👋")
            break

if __name__ == "__main__":
    main()
