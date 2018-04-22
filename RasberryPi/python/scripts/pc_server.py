import socket
import sys

#host = 'localhost'
host = '192.168.1.135' #laptop ip
port = 8000
address = (host, port)

while True:
    print "Listening for client . . ."

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(5)

    conn, address = server_socket.accept()
    print "Connected to client at ", address
    #pick a large output buffer size because i dont necessarily know how big the incoming packet is                                                    

    while True:
        output = conn.recv(2048);
        if output.strip() == "disconnect":
            conn.close()
            # sys.exit("Received disconnect message.  Shutting down.")
            conn.send("dack")
            print "disconnect current client!"
            break

        elif output:
            print "Message received from client:"
            
            #ouput received readings here!
            print output 
            conn.send("ack")