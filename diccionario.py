"""
Nombre:diccionario.py
Objetivo: muestra la operación de los diccionarios en python
Autor: sergio antonio ortiz
Fecha: 5 de agosto de 2020
"""

# un diccionario es una estructura de datos que almacena valores heterogeneos
# pero los almacena en un formato de clave:valor. Quiere decir que cada elemento
# en el diccionario se almacena como una lista de pares key:valor.
# Por ejemplo: 'nombre':'sergio antonio ortiz figueroa'
# No son mutables, it does mean no cambian. Una vez que los creamos permanecerán
# con los mismos valores, no podremos introducir mas datos


def main():
    # Creamos un diccionario con distintos key y datos
    dic = {'clave': 20082133, 'nombre':'sergio antonio ortiz figueroa', 'edad':54, 'cursos':['Python', 'Progra Web', 'Inteligencia Artificial'] }
    # Listar items del diccionario
    print("Los items son: ", dic)
    # Imprimir un item de un diccionario proporcionando su key
    print("El valor de la key es: ", dic['nombre'], "\n")
    # Imprimir los valores de todos los keys del diccionario
    for i in dic:
        print(i, ":", dic[i])

    # En el caso de la lista incluidad como un item del diccionario, lo accesamos
    print("\n")
    for i in dic['cursos']:
        print(i)

    

    # Investigar los métodos de los diccionarios y correrlos en el programa
    # get, pop, key, clean, items, update


if __name__=="__main__":
    main()    

