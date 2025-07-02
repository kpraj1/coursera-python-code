import socket

HOST = 'data.pr4e.org'
PORT = 80
RESOURCE = '/romeo.txt'

try:
    with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
        mysock.connect((HOST,PORT))
        cmd = f'GET {RESOURCE} HTTP/1.1\r\nHost:{HOST}\r\n\r\n'.encode()

        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data)<1:
                break
            print(data.decode())
except socket.gaierror:
    print("Error: unable to resolve host")
except socket.error as e:
    print(f"socket error:{e}")
except Exception as e:
    print(f"an unexpected error occurred:{e}")