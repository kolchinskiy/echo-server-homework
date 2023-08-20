import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    while True:
        request = input("Введите HTTP-запрос (или 'exit' для выхода): ")
        # example: GET / HTTP/1.1\r\nHost: 127.0.0.1:8080\r\n\r\n
        if request.lower() == 'exit':
            break

        client_socket.sendall(request.encode())

        response = client_socket.recv(4096)
        print(response.decode())
