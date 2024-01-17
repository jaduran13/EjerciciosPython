# -*- coding: utf-8 -*-
"""Mi Primera red neuronal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1liGhJfhQNuQoKjB2tWD8Djx4mDW0vJuf
"""

import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype = float)

capa = tf.keras.layers.Dense(units = 1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=500, verbose=False)
print("Modelo entrenado!")

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])
plt.show()

print("Hagamos una predicción!!!")
resultado = modelo.predict([50.0])
print(f"El resultado es {resultado[0]} fahreneit!")

print("Variables internas del modelo")
print(capa.get_weights())