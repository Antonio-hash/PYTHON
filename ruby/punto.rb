class Punto
    
    # constructor con argumentos
    def initialize(valorX, valorY)
        # creamos atributos de la clase
        @x = valorX
        @y = valorY
    end 

    # Métodos get para regresar los valores de los atributos del objeto
    def getX()
        return @x 
    end

    def getY()
        return @y 
    end
    
    # Métodos set para modificar el valor de los atributos del objeto
    def setX(valorX)
        @x = valorX
    end
    
    def setY(valorY)
        @y = valorY
    end
    
end 





