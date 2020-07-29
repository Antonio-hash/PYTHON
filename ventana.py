"""
Nombre: ventana.py
Objetivo: muestra como trabajar con ventanas gui en python y tkinter
Autor: MSI
fecha: 29 de julio de 2020
"""


#importar las librerias de tkinter

from tkinter import*
from tkinter import ttk

#funcion para eviar informacion al servidor 
def send():
	print("Se ha enviado")


#funcion main
def main():
	#creamos la ventana contenedora
	win = Tk()
	#modificamos parametro de la ventana win
	win.geometry("400x400")
	win.title("mi primer ventana en python tkinter")

	#creamos la etiqueta
	label = ttk.Label(win, text="Texto a enviar al servidor").pack(side=TOP)
	txtCampo = ttk.Entry(win).pack(side=TOP)


	#creamos un boton en la ventana
	ttk.Button(win, text="salir", command=quit).pack(side=BOTTOM)

	#boton para enviar la informacion del label entry al servdior
	ttk.Button(win, text="Enviar", command=send).pack(side=BOTTOM)

	#hacemos un ciclo para dibujar y esperar eventos
	win.mainloop()




#para funcion main
if __name__ == "__main__":
	main()
