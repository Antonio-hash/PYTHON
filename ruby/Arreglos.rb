# clase para el manejo de arreglos en ruby

class Arreglo 

    # Método constructo
    def initialize()
        # crear un arreglo vacio
        @vector = []
    end

    # insertar elemento en el arreglo
    def insert(elem)
        @vector.push(elem)
 
    end


    # buscar un elemento dentro del arreglo
    def buscar(elem)
        @vector.each_with_index do |elemento, index|
            if elemento == elem
                puts "El elemento buscado es:[#{index}]=#{elemento}"
                return index
            # verificamos que estamos al final del arreglo y no encontramos el elemento    
            elsif (elemento != elem) && (index+1 == @vector.length)
                puts "El elemento que buscas no existe:#{elem}"
                return -1
            end    
        end   
     
    end
    

    # cambiar elemento
    def cambiar(elem, elem_new)
        #Buscamos elemento y obtenemos su posición en el arreglo
        puntero = buscar(elem)
        if ( puntero >= 0)
            # elemento existe y lo modificamos
            @vector[puntero]=elem_new
            puts "Elemento modificado.."
        else
            puts "Nada se cambió..."   
        end
    end        



    # Borra elemento
    def borrar(elem)
        #Buscamos elemento y obtenemos su posición en el arreglo
        puntero = buscar(elem)
        if ( puntero >= 0)
            @vector.delete_at(puntero)
            puts "Elemento borrado #{elem}..."
        else
            puts "Nada se borró..."   
        end
    end        


    # Imprime todos los elementos del arreglo
    def printAll()
        if @vector.length > 0
            @vector.each_with_index do |elemento, index|
                puts "Elemento[#{index}]=#{elemento}"
            end    
        else
            puts "El arreglo está vacio"
        end
    end        
    
end


