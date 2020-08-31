require 'socket'                 # Get sockets from stdlib

server = TCPServer.open(2000)    # socket escuchando en el puerto 2000
puts "Servidor escuchando el puerto 2000..."
loop {                           # servidor corriendo
   client = server.accept        # el cliente espera para conectarse
   client.puts(Time.now.ctime)   # envia hacia el cliente
   client.puts("nos vemos")
   client.puts "Cerrando conexion. Bye!"
   client.close                  # desconexion del cliente
}