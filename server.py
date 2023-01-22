import socket

if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 1234
    
#If tcp is asked then SOCK_STREAM IS USED
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#If tcp is asked then SOCK_DGRAM IS USED
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((ip, port))

server.listen(5)


while True:
    client, address = server.accept()
    print(f"Connection Established - {address[0]}:{address[1]}")

    string = client.recv(1024)
    string = string.decode('utf-8')
    string = string.upper()

    print(string)

    client.close()