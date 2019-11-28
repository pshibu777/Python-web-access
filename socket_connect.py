import socket
#socket connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
#comment to send requset to server
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

#recieve and decode
while True:
    # we are going to recieve 512 characters
    data=mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()
