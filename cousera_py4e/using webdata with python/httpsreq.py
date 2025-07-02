import socket
import ssl


"""
HOST = 'data.pr4e.org'
PORT = 443
RESOURCE = '/romeo.txt'
"""

HOST = 'wttr.in'
PORT = 443
RESOURCE = '/Bangalore?format=3'

try:
    # Create a plain socket
    with socket.create_connection((HOST, PORT)) as plain_sock:
        # Wrap the socket with SSL for HTTPS
        with ssl.create_default_context().wrap_socket(plain_sock, server_hostname=HOST) as mysock:
            # Prepare and send the HTTP request
            cmd = f'GET {RESOURCE} HTTP/1.1\r\nHost: {HOST}\r\n\r\n'.encode()
            mysock.send(cmd)

            # Receive and print the response
            while True:
                data = mysock.recv(1024)
                if len(data) < 1:
                    break
                print(data.decode().rstrip())

except socket.gaierror:
    print("Error: Unable to resolve host.")
except ssl.SSLError as e:
    print(f"SSL error: {e}")
except socket.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
