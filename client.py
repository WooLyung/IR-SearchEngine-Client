import socket
import sys

query = ' '.join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 3997))

sock.send(query.encode())
data_size = 5120
data = sock.recv(data_size)
result = data.decode()

print("query : " + query)
print(result)
sock.close()