import streamlit as st
import pandas as pd
import numpy as np

# Título y texto principal
st.title("Hola Grupo Samsung Innovation Campus")
st.write("Estamos aprendiendo a usar Streamlit.")

# Widget interactivo: Deslizador
valor_slider = st.slider("Selecciona un número", 0, 100, 50)
st.write(f"El número seleccionado es: {valor_slider}")

# Creación de datos aleatorios y gráfico
st.subheader("Gráfico de datos aleatorios")
datos = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Columna A', 'Columna B', 'Columna C']
)

st.line_chart(datos)

# Widget de entrada de texto
nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.success(f"¡Mucho gusto, {nombre}!")


##Solo probando cambios en la rama
