"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()
"""
#more good way of doing http request is below:
import socket

HOST = 'data.pr4e.org'
PORT = 80
#RESOURCE = '/romeo.txt'
RESOURCE = '/intro-short.txt'

#by using with keyword no need to explicitly close the socket.
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
        mysock.connect((HOST, PORT))
        cmd = f'GET {RESOURCE} HTTP/1.1\r\nHost: {HOST}\r\n\r\n'.encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode())

except socket.gaierror:
    print("Error: Unable to resolve host.")
except socket.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
