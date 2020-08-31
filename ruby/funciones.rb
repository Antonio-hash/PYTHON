# Programa de funciones en ruby

include Math


def mensaje()
    return "hola"
end

def suma(n1, n2)
    return n1+n2
end

def resta(n1, n2)
    return n1-n2
end

def multiplica(n1, n2)
    return n1*n2
end

def divide(n1, n2)
    return Float(n1)/Float(n2)
end

def compara(n1, n2)
    if n1 > n2
        puts "#{n1} es mayor que #{n2}"
    elsif n2>n1
        puts "#{n2} es mayor que #{n1}"
    else
        puts "Los números son iguales: #{n1} , #{n2}"
    end
end

def cuenta(n1, n2)
    if n1<n2
        (n1..n2).each do |i|
            puts "#{i}"
        end
    elsif (n1>n2)
        while n1>=n2
            puts "#{n1}"
            n1 = n1-1
        end  
    else
        puts "Los números son iguales : #{n1}, #{n2}"    
    end
end  


# Función para calcular are
def getArea(radio)
    return Math::PI * (radio**2)
end