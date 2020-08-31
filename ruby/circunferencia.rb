# clase que muestra la herencia en ruby

load "punto.rb"
include Math


class Circunferencia <  Punto

    def initialize(vRadio)
        @radio = vRadio
    end

    def getRadio()
        return @radio
    end
    
    def setRadio(vRadio)
        @radio = vRadio
    end

    # Escribir un método que calcule el área de la circunferencia
    def getArea()
        return Math::PI * getRadio()**2
    end    
    
end 

