"""
Nombre: servidorUDP.py
Objetivo: implementa un servidor con sockets UDP
Autor: tomado de https://pythontic.com/modules/socket/udp-client-server-example
04/08/2020
Modificado por : jesus verduzco el 04/08/2020

Fecha: 04/08/220  
"""




import socket


localIP     = "127.0.0.1"
localPort   = 10000
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening at the port 1000 ...")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)