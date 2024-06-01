from socket import *
import sys

def clientRequest(serverHost, serverPort, fname):

    # Membuat koneksi client
    clientSocket=socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))
    
    #Mengirim request GET HTTP
    request= f"GET {fname} HTTP/1.1\r\nHost: {serverHost}\r\nPort: {serverPort}\r\n\r\n"
    clientSocket.sendall(request.encode())

    #Menerima respons
    response = clientSocket.recv(1024).decode() #Menerima sebesar 1KB buffer
    print(response)

    # Menutup koneksi
    clientSocket.close()

def main():
    # Mengambil argumen server host, server port, dan filename
    serverHost=sys.argv[1]
    serverPort=int(sys.argv[2])
    fname=sys.argv[3]
    clientRequest(serverHost, serverPort, fname)

main()