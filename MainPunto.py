"""
Nombre: MainPunto.py
Objetivo: muestra como trabajar con múltiples archivos en python
Autor: sergio antonio ortiz
Fecha:30 de julio de 2020
"""
# Incluir el archivo de la clase Punto

from Punto import Punto

# Creamos objetos dentro del mismo archivo
puntoA = Punto(0,0)
# Invocamos métodos get
print("El valor de la coordenada X es:",puntoA.getX())
print("El valor de la coordenada Y es:",puntoA.getY())
# Invocamos métodos set
puntoA.setX(23)
puntoA.setY(12)
# Imprimimos los valores de los atributos del objeto puntoA
print(puntoA.toString())

# Creamos objetos dentro del mismo archivo
puntoB = Punto(-10,-20)
# Invocamos métodos get
print("El valor de la coordenada X es:",puntoB.getX())
print("El valor de la coordenada Y es:",puntoB.getY())
# Invocamos métodos set
puntoB.setX(10)
puntoB.setY(20)
# Imprimimos los valores de los atributos del objeto puntoA
print(puntoB.toString())