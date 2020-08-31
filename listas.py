"""
Nombre: listas.py
Objetivo: muestra la función de las listas en python
Autor: sergio antonio ortiz
Fecha: 4 de agosto de 2020
"""



def main():
    # una lista es una estructura de datos en python
    # la ventaja aceptan datos de tipos distintos
    #Creamos una lista
    lista = [1, 23.01, False, "hola lista", 'A', 'A', [-1,-5, "hola", 0.0], -12, 'A']
    #Lista vacia
    listaVacia = []
    # Accesando elementos de la lista
    # imprimimos los elementos de lista 
    for elemento in lista:
        print("El elemento de la lista es: ", elemento)
    for i in listaVacia:
        print("El elemento de la lista es: ", i)

    #imprimir un elemento de la lista
    print("Elemento en la posición 3:", lista[3])  
    print("Elemento en la posición -5:", lista[-5]) 
    print(lista[-2])
    print(lista[5])
    # leer el elemento que está en la posición 2 de la lista interna
    print(lista[5][-1])

    # Métodos de las listas

    # Append agrega un elemento al final de la lista
    lista.append("El maestro no sabe...")
    for elemento in lista:
        print("El elemento de la lista es: ", elemento)


    # count regresa el número de veces que se repite un elemento en la lista
    print("Elemento se repite :", lista.count("pelochas"))

    # index() imprime el indice de un elemento en la lista
    print("La posición de False es: ", lista.index(False))
    # eliminar elementos de la lista : remove()
    lista.remove('A')
    for x in lista:
        print("El elemento de la lista es: ", x)





if __name__=="__main__":
    main()   