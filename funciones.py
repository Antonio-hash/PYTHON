"""
Nombre: funciones.py
Objetivo: muestra la operación de las funciones en python
Autor: sergio antonio ortiz
Fecha: 27 julio de 2020
"""

def mensaje():
	print("hola desde mensaje")


def regresaMensaje():
	return "saludo desde regresaMensaje"


def printMensaje(msg):
	print(msg)


def suma(n1, n2):
	return n1+n2

def resta(n1, n2):
        return n1-n2

def multiplica(n1, n2):
        return n1*n2

def divide(n1, n2):
	if (n2 != 0):
		return n1/n2
	else:
		print("Error no se puede dividir entre cero...")


def compara(n1, n2):
	if n1>n2:
		print("El mayor es n1: ", n1," ", n2)
	elif n2>n1:
		print("El mayor es : {},{}".format(n2,n1))
	else:
		print("Los numeros son iguales: {}, {}".format(n1,n2))


# Función para mostrar operación de for
def cuenta(n1, n2):
	if (n2>n1):
		for i in  range(n1, n2+1):
			print("Valor de i: {}".format(i))
	elif (n1>n2):
		for i in range(n1, n2-1, -1):
			print("Valor de i: {}".format(i))
	else:
		print("Los números son iguales, no puedo contar: {}, {}".format(n1,n2))




# Inicia función principal

def main():

	ciclo ='S'
	while ciclo == 'S'  or  ciclo == 's':

		#invocamos función mensaje
		mensaje()
		#invocamos función regresaMensaje
		print(regresaMensaje())
		#invocamos función printMensaje
		printMensaje("hola te saludo ...")

		#Leemos los dato por teclado
		a = int(input("Ingresa el primer entero: "))
		b = int(input("Ingresa el segundo entero: "))
		#Invocamos la función suma
		print("La suma es: ", suma(a,b))
		print("La resta es: ",resta(a,b))
		print("La multiplicación es: ", multiplica(a,b))
		print("La división es: ", divide(a,b))

		compara(a,b)
		cuenta(a, b)

              	# Preguntamos por otra operación
		ciclo = input("¿Desea otra operación (s/n)?")

	else:
		print("*** Fin de programa")	




if __name__ == "__main__":
	main()
