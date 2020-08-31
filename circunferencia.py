"""
Nombre: Circunferencia.py
Objetivo: permite calcular el área de una circunferencia
Autor: sergio antonio ortiz
Fecha: 28 de julio de 2020
"""
# importamos libreria math
import math as m


#--------------------------------------
# Función para calcular área
#--------------------------------------
def calcularArea(valorRadio):
	return m.pi*m.pow(valorRadio,2)



# Módulo principal
def main():
	ciclo = 'S'
	while (ciclo == 'S' or ciclo == 's'):
		print("--- Programa para Calcular Área de Circunferencia ---")
		vradio = int(input("Introduce valor del radio:"))
		print("El área de la circunferencia con radio igual a:{},es:{}".format(vradio, calcularArea(vradio)))
		ciclo = input("¿Otro cálculo (s/n)?")
	else:
		print("*** Fin del programa")


if __name__ == "__main__":
	main()


