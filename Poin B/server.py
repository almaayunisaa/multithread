from socket import * 
import sys 
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket 
serverPort = 7000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end 
while True: 
#Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    try:
        f = open("html/index.html", 'r')
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
serverSocket.close() 
sys.exit()
