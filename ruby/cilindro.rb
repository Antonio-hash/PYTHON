# clase que muestra la herencia en ruby

load "circunferencia.rb"


class Cilindro <  Circunferencia 

    def initialize(vAltura)
        @altura = vAltura
    end

    def getAltura()
        return @altura
    end
    
    def setAltura(vAltura)
        @altura = vAltura
    end

    # Escribir un método que calcule el área de la circunferencia
    def getVolumen()
        return getArea()*getAltura()
    end    
    
end 

cil = Cilindro.new(3)
cil.setX(2)
cil.setY(3)
cil.setRadio(4)


puts "Los datos del cilindro son: #{cil.getX()},#{cil.getY()}, 
con radio igual a: #{cil.getRadio()}, y altura igual a:#{cil.getAltura()},  el volumen es : #{cil.getVolumen()}"
