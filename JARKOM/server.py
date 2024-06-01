from socket import * 
import threading
import os

def _thread(connectionSocket, addr):
    # Menerima request client
    request=connectionSocket.recv(1024).decode()

    # Menyimpan metode dan nama file  
    metode = request.split()[0]   
    file = (request.split()[1]).lstrip('/')

    # Mengecek apakah terdapat filenya
    if os.path.exists(file):
    # Kalau terdapat filenya
        with open(file, 'r') as f:
            message_body = f.read()
            response_line="HTTP/1.1 200 OK\r\n"
            content_type = "Content_Type : text/html\r\n\r\n"
            response = response_line+content_type+ message_body
    else:
    # Kalau tidak ada filenya
        with open("notFound.html", 'r') as f:
            message_body = f.read()
            response_line="HTTP/1.1 404 Not Found\r\n"
            response = response_line+ message_body
    
    # Mengirim response
    connectionSocket.sendall(response.encode())
    connectionSocket.close()
        
# Membuat server
def main(serverHost, serverPort):
    serverSocket = socket(AF_INET, SOCK_STREAM) 
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen(3) # Antrean klien ada 3
    print("Server is listening...")
    while True:
        # Menerima koneksi dari client
        connectionSocket, addr = serverSocket.accept()
        print(f"Connected Client {addr[1]}")
        # Membuat thread terpisah
        thread=threading.Thread(target=_thread, args=(connectionSocket, addr))
        thread.start()

main('127.0.0.1', 8000)
    