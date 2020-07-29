"""
nombre: funciones.py
Objetivo: muestra de la operacion de las funciones en python
Autor: 
Fecha: 27 de julio de 2020
"""

def mensaje():
	print("hola desde mensaje")

def regresaMensaje():
	return"saludo desde regresaMensaje"

def printMensaje(msg):
	print(msg)

def suma(n1, n2):
	return n1+n1

def resta(n1, n2):
	return n1-n2

def multi(n1, n2):
	return n1*n2

def dividir(n1, n2):
	if(n2 != 0):
		return n1/n2
	else: 
		print("Errorm no se puede dividir entre cero....")

def compara(n1, n2):
	if n1>n2:
		print("EL mayor es n1", n1, "" ,n2)
	elif n2>n1:
		print("el mayor es: {},{}".format(n1,n2))
	else: 
		print("los numero son iguales: {}, {}".format(n1,n2))

#fUNCION PARA MOSTRAR OPERACION FOR
def cuenta(n1, n2):
	if(n2>n1):
		for i in range(n1, n2+1):
			print("valor de i: {}".format(i))
	elif(n1>n2):
		for i in range(n1, n2-1, -1):
			print("valor de i: {}".format(i))
	else: 
		print("los numeros son iguales: {}, {}".format(n1,n2))
	


def main():
	ciclo = 'S'
	while ciclo == 'S' or ciclo == 's':
		#invocamos funcion mensaje()
		mensaje()
		#invocamos funcion regresaMensaje()
		print (regresaMensaje())
		#invocamos funcion printMensaje()
		printMensaje("hola te saludo.-...")

		#leemos los datos por teclado
		a = int(input("ingrese el primer numero "))
		b = int(input("ingrese el segundo numero "))
		#invocamos la funcion suma 
		print("la suma es... ", suma(a,b))
		print("la resta es... ", resta(a,b))
		print("la multiplicacion es... ", multi(a,b))
		print("la division es... ", dividir(a,b))
	
		compara(a,b)
		cuenta(a,b)

		#preguntamos por otra operacion
		ciclo = input("Desea hacer otra operacion(s/n)")
	else: 
		print("***fin de programa")


if __name__ == "__main__":
	main()

