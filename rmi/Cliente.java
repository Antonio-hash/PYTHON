import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class Cliente {
	private static final String IP = "127.0.0.1"; // Puedes cambiar a localhost
	private static final int PUERTO = 1100; //Si cambias aquí el puerto, recuerda cambiarlo en el servidor
	
    public static void main(String[] args) throws RemoteException, NotBoundException {
        Registry registry = LocateRegistry.getRegistry(IP, PUERTO);
        Interfaz interfaz = (Interfaz) registry.lookup("Calculadora"); //Buscar en el registro...
       
        Scanner sc = new Scanner(System.in);
        int eleccion;
        int  numero1 = 0, numero2 = 0;
        
        float resultadod = 0.0f;
        int resultado = 0;
        boolean divide = false;
        

        String menu = "\n\n------------------\n\n[-1] => Salir\n[0] => Sumar\n[1] => Restar\n[2] => Multiplicar\n[3] => Dividir\n[4] => Area Circunferencia\n Elige: ";
        do {
            System.out.println(menu);

            try {
                eleccion = Integer.parseInt(sc.nextLine());
            } catch (NumberFormatException e) {
                eleccion = -1;
            }

            if(eleccion != -1){

            	System.out.println("Ingresa el número 1: ");
            	try{
                	numero1 = Integer.parseInt(sc.nextLine());
            	}catch(NumberFormatException e){
            		numero1 = 0;
            	}
               
                if (eleccion != 4) {

            	System.out.println("Ingresa el número 2: ");
            	try{
                	numero2 = Integer.parseInt(sc.nextLine());
            	}catch(NumberFormatException e){
            		numero2 = 0;
                }
                
            }
                switch (eleccion) {
	                case 0:
                        resultado = interfaz.suma(numero1, numero2);
                        
	                    break;
	                case 1:
	                    resultado = interfaz.resta(numero1, numero2);
	                    break;
	                case 2:
	                    resultado = interfaz.multiplica(numero1, numero2);
	                    break;
                    case 3:
                        divide = true;
                        resultadod = interfaz.divide(numero1, numero2);
                        break;

                    case 4:
                        divide = true;
                        resultadod = interfaz.calculaArea(numero1);
                        break;   


	            }

                if (divide == true) {
                      System.out.println("Resultado => " + String.valueOf(resultadod));
                } 
                else{
                    System.out.println("Resultado => " + String.valueOf(resultado));
                }    

                divide = false; 
                System.out.println("Presiona ENTER para continuar");
                sc.nextLine();
            }
        } while (eleccion != -1);
     System.out.print("*** Fin de programa"+"\n");

    }
}