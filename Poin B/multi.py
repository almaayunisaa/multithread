from socket import * 
import sys
import threading
serverSocket = socket(AF_INET, SOCK_STREAM) 

def _thread(connectionSocket, fname):
    while True:
        try:
            f = open(fname, 'r')
            message_body = f.read()
            f.close()

            request = connectionSocket.recv(1024).decode()
            response_line="HTTP/1.1 200 OK\r\n"
            content_type = "Content_Type : text/html\r\n\r\n"
            response = response_line+content_type+message_body
        except FileNotFoundError:
            response_line="HTTP/1.1 404 Not Found\r\n"
            content_type = "Content_Type : text/html\r\n\r\n"
            message_body ="<html><body><h1>HTTP 404 NOT FOUND<h1><body><html>"
            response = response_line+content_type
        connectionSocket.send(response.encode())
    connectionSocket.close()
        

def multi(serverHost, serverPort, fname):
    serverSocket.bind(serverHost, serverPort)
    serverSocket.listen(1)
    print("Server is listening...")
    while True:
        connectionSocket, addr = serverSocket.accept()
        thread=threading.Thread(target=_thread, args=(connectionSocket, fname))
        thread.start()
         
serverHost=sys.argv[1]
serverPort=sys.argv[2]
fname=sys.argv[3]
    
multi(serverHost, serverPort, fname)
    