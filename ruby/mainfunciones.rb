# Módulo principal de funciones

load "funciones.rb"

ciclo = "S"
while (ciclo =="S" or ciclo == "s")

print "--- Operaciones Básicas con Ruy ---","\n"
print "Introduce el primer número: "
n1 = Integer(gets.chomp)
print "Introduce el segundo número: "
n2 = Integer(gets.chomp)


print "La suma es :", suma(n1, n2), "\n"
print "La resta es :", resta(n1, n2), "\n"
print "La multiplicación es :", multiplica(n1, n2), "\n"
print "La división es :", divide(n1, n2), "\n"

compara(n1, n2)
cuenta(n1, n2)

puts "el area de la circunferencia es: #{getArea(n1)}"

puts "¿Desea otra operación (S/N)?"
ciclo = gets.chomp

end

puts "*** Fin de programa"