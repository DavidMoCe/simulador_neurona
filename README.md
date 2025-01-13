# Neuron Simulator 🧠

## 🌍 Choose Your Language / Elige tu idioma:
- [English](#english-)
- [Español](#español-)

---

## Project URL 🌐

You can access the project at the following URL:  
[**Neuron Simulator URL**](https://simuladorneurona-david.streamlit.app/)

## English 🇬🇧

This project is a simple simulation of an artificial neuron using Streamlit and NumPy. It allows users to input values for the neuron’s inputs and weights, as well as select an activation function to calculate the neuron's output.

## Requirements ⚙️

- Python 3.x 🐍
- Streamlit 📊
- NumPy 🔢

You can install the necessary dependencies using the following command:

```bash
pip install streamlit numpy
```

## Supported Activation Functions 🔌
The simulator offers three activation functions:
1. **Sigmoid**:
   The sigmoid function is defined as:

    $$ 
   \sigma(x) = \frac{1}{1 + e^{-x}}
   $$
   
   Where \(e\) is Euler's constant, and the function transforms any input value into a value between 0 and 1.
   
2. **ReLU** (Rectified Linear Unit):
   The ReLU function is defined as:

   $$ 
   \text{ReLU}(x) = \max(0, x)
   $$ 
   
   This function returns the value of \(x\) if it is positive, and 0 if it is negative.
   
3. **Hyperbolic Tangent**:
   The hyperbolic tangent function is defined as:

   $$ 
   \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
   $$
   
   This function transforms any input value into a value between -1 and 1.
   
## Instructions 📋
1. **Choose the number of inputs/weights**:
   Use the slider to define how many inputs and weights the neuron will have.
2. **Enter the weights**:
   For each input, enter the corresponding weight value.
3. **Enter the inputs**:
   Provide values for each of the neuron’s inputs.
4. **Enter the bias**:
   Specify the bias value of the neuron.
5. **Select the activation function**:
   Choose from the three available activation functions: Sigmoid, ReLU, or Hyperbolic Tangent.
6. **Calculate the output**:
   Click the "Calculate Output" button to get the result of the neuron with the values you have entered.

## Running the Project 🚀
To run the application, navigate to the project folder and execute the following command:
```bash
streamlit run app.py
```
## License 📜
This project is licensed under the MIT License. See the `LICENSE` file for more details.


---

## Español 🇪🇸

Este proyecto es una simple simulación de una neurona artificial utilizando Streamlit y NumPy. Permite a los usuarios ingresar valores para las entradas y los pesos de una neurona, así como seleccionar una función de activación para calcular la salida de la neurona.

## URL de proyecto 🌐

Puedes acceder al proyecto en la siguiente URL:  
[**Neuron Simulator URL**](https://simuladorneurona-david.streamlit.app/)

## Requisitos ⚙️

- Python 3.x 🐍
- Streamlit 📊
- NumPy 🔢

Puedes instalar las dependencias necesarias usando el siguiente comando:

```bash
pip install streamlit numpy
```

## Funciones de activación soportadas
El simulador ofrece tres funciones de activación:
1. **Sigmoide**:
   La función sigmoide se define como:

    $$ 
   \sigma(x) = \frac{1}{1 + e^{-x}}
   $$
   
   Donde \(e\) es la constante de Euler, y la función transforma cualquier valor de entrada en un valor entre 0 y 1.
   
2. **ReLU** (Rectified Linear Unit):
   La función ReLU se define como:

   $$ 
   \text{ReLU}(x) = \max(0, x)
   $$ 
   
   Esta función devuelve el valor de \(x\) si es positivo, y 0 si es negativo.
   
3. **Tangente Hiperbólica**:
   La función tangente hiperbólica se define como:

   $$ 
   \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
   $$
   
   Esta función transforma cualquier valor de entrada en un valor entre -1 y 1.
   
## Instrucciones 📋
1. **Elige el número de entradas/pesos**:
   Usa el control deslizante para definir cuántas entradas y pesos tendrá la neurona.
2. **Ingresa los pesos**:
   Para cada entrada, ingresa el valor correspondiente del peso.
3. **Ingresa las entradas**:
   Proporciona los valores para cada una de las entradas de la neurona.
4. **Introduce el sesgo**:
   Especifica el valor del sesgo de la neurona.
5. **Selecciona la función de activación**:
   Elige entre las tres funciones de activación disponibles: Sigmoide, ReLU o Tangente Hiperbólica.
6. **Calcula la salida**:
   Haz clic en el botón "Calcular salida" para obtener el resultado de la neurona con los valores que has introducido.

## Ejecución del proyecto 🚀
Para ejecutar la aplicación, navega a la carpeta del proyecto y ejecuta el siguiente comando:
```bash
streamlit run app.py
```
## Licencia 📜
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
