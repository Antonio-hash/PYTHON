"""
Nombre: circunferencia
objetivo: permita calcular el area de una circunferencia
autor: tu mero papi
fecha: 28 de julio de 2020
"""

#IMPORTAMOS LIBRERIA MATH

import math

#funcion para calcular area
def area(valorRadio):
	return math.pi*math.pow(valorRadio, 2)



#modulo principal
def main():
	ciclo = 'S'
	while (ciclo == 'S' or ciclo == 's'):
		print("Programa para calcular el area de una circunferencia")
		vradio = int(input("introduce valor del radio" ))
		print("\n")
		print("el area de la circunferencia con radio igual a: {}, es: {}".format(vradio, area(vradio)))
		ciclo = input("desea ingresar otro valor (s/n)")
	else:
		print("fin de programa")

if __name__ == "__main__":
	main()
