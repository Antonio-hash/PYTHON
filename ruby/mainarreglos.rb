# Cargar archivo de la clase arreglos
load "Arreglos.rb"

# Creamos un objeto de la clase Arreglos
vec = Arreglo.new()


# Insertar un elemento
vec.insert("first")
vec.insert(12)
vec.insert(false)
vec.insert("C")
vec.insert(12.45)
vec.printAll()

vec.cambiar("peludo", true)
vec.printAll()
