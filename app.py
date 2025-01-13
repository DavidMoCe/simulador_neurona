import streamlit as st
import numpy as np

st.image("neurona.jpg")

st.title("Simulador de neurona")


def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tangente_hiperbolica(x):
    return np.tanh(x)

numero =  st.slider("Elige el número de entradas/pesos que tendrá la neurona", 1, 10, step=1, key="numero")

st.subheader("Pesos")
pesos = []

cols_pesos = st.columns(numero)
for i , col in enumerate(cols_pesos):
    with col:
        st.markdown(f"w<sub>{i}</sub>", unsafe_allow_html=True)
        peso = st.number_input(key=f"w_{i}")
        pesos.append(peso)

st.write(f"w = {pesos}")

st.subheader("Entradas")
entradas = []
cols_entrada = st.columns(numero)
for i , col in enumerate(cols_entrada):
    with col:
        entrada = st.number_input(f"x_{i}", key=f"x_{i}")
        entradas.append(entrada)

st.write(f"x = {entradas}")

col_sesgo, col_func = st.columns(2)
with col_sesgo:
    st.subheader("Sesgo")
    sesgo = st.number_input("Introduce el valor del sesgo", key="sesgo")

with col_func:
    st.subheader("Función de activación")
    funcion_activacion = st.selectbox(
        "Elige la función de activación",
        ["Sigmoide", "ReLU", "Tangente Hiperbólica"]
    )

if st.button("Calcular salida"):
    cuenta = np.dot(pesos, entradas) + sesgo

    if funcion_activacion == "Sigmoide":
        salida = sigmoide(cuenta)
    elif funcion_activacion == "ReLU":
        salida = relu(cuenta)
    elif funcion_activacion == "Tangente Hiperbólica":
        salida = tangente_hiperbolica(cuenta)

    st.subheader("Resultado")
    st.write(f"La salida de la neurona es: {salida}")