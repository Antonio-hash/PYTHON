"""
Nombre: Punto.py
Objetivo: muestra como trabajar en objetos con python
Autor: sergio antonio ortiz
Fecha:30 de julio de 2020
"""
class Punto():

    # Definir una especie de constructor
    def __init__(self, valorX, valorY):
        # definimos el nombre de los atributos del objeto o variables
        self.x = valorX 
        self.y = valorY

    # Lista de métodos get
    def getX(self):
        return  self.x

    def getY(self):
        return self.y

    # Lista de métodos set
    def setX(self, valorX):
        #asignar el argumento al atributo del objeto
        self.x = valorX

    def setY(self, valorY):
        self.y = valorY

    # Método toString: regresa los valores de los atributos x,y
    def toString(self):
        return "Las coordenadas X,Y del punto son:["+ str(self.getX())+","+str(self.getY())+"]"

# Fin de clase












