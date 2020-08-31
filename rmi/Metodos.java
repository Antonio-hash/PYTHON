public class Metodos {

// Constructor    
public Metodos(){

}

private static void mensaje(){
    System.out.println("Hola soy un método estático");
}

private int suma(int n1, int n2){
    return n1+n2;
}
private int resta(int n1, int n2){
    return n1-n2;
}
private int multiplica(int n1, int n2){
    return n1*n2;
}
private float divide(int n1, int n2){
     float res;
     res = (float)n1/(float)n2;

    return res;
}

// Método main
public static void main(String [] args){
    Metodos op = new Metodos();
    System.out.println("La suma es: "+ op.suma(4,5));
    System.out.println("La resta es: "+ op.resta(4,5));
    System.out.println("La multiplicación es: "+ op.multiplica(4,5));
    System.out.println("La división es: "+ op.divide(4,5));
    mensaje();
}



}