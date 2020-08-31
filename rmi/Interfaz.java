import java.rmi.Remote;
import java.rmi.RemoteException;


public interface Interfaz extends Remote {

int suma(int n1, int n2) throws RemoteException;
int resta(int n1, int n2) throws RemoteException;
int multiplica(int n1, int n2) throws RemoteException;
float divide(int n1, int n2) throws RemoteException;

// Agregamos un nueva funcion
float calculaArea(int n1) throws RemoteException;


}
