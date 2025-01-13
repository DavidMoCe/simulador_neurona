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

st.header("Elige el número de entradas/pesos que tendrá la neurona")

numero =  st.slider("Elige el número de entradas/pesos", 1, 10, step=1, key="numero")

st.subheader("Pesos")
pesos = []

cols_pesos = st.columns(numero)
for i , col in enumerate(cols_pesos):
    with col:
        peso = st.number_input(f"w_{i}", key=f"w_{i}")
        pesos.append(peso)

st.subheader("Entradas")
entradas = []
cols_entrada = st.columns(numero)
for i , col in enumerate(cols_entrada):
    with col:
        entrada = st.number_input(f"x_{i}", key=f"x_{i}")
        entradas.append(entrada)



col_func, col_sesgo = st.columns(2)
with col_sesgo:
    st.subheader("Sesgo")
    sesgo = st.number_input("sesgo", key="sesgo")

with col_func:
    funcion_activacion = st.selectbox(
        "Función de activación",
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