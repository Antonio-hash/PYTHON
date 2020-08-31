import java.rmi.AlreadyBoundException;
import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Servidor {

	private static final int PUERTO = 1100; //Si cambias aquí el puerto, recuerda cambiarlo en el cliente

    public static void main(String[] args) throws RemoteException, AlreadyBoundException {
        
        Remote remote = UnicastRemoteObject.exportObject(new Interfaz() {
        	
            @Override
            public int suma(int numero1, int numero2) throws RemoteException {
                return numero1 + numero2;
            };

            @Override
            public int resta(int numero1, int numero2) throws RemoteException {
                return numero1 - numero2;
            };

            @Override
            public int multiplica(int numero1, int numero2) throws RemoteException {
                return numero1 * numero2;
            };

            @Override
            public float calculaArea(int n1) throws RemoteException {
                return (float)(Math.PI * Math.pow(n1, 2));
            };


            @Override
            public float divide(int numero1, int numero2) throws RemoteException {
                return (float)numero1 / (float)numero2;
            };
        }, 0);

        Registry registry = LocateRegistry.createRegistry(PUERTO);
        System.out.println("Servidor escuchando en el puerto " + String.valueOf(PUERTO));
           
        registry.bind("Calculadora", remote); // Registrar calculadora
    }
}