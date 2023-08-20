import socket
from http.client import responses

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер слушает на {HOST}:{PORT}")

    while True:
        client_connection, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")

        with client_connection:
            request_data = client_connection.recv(1024).decode()

            request_method = request_data.split()[0]
            status_full = request_data.split()[1]
            status = status_full[status_full.find("=") + 1:]
            try:
                phrase = responses[int(status)]
            except ValueError:
                pass

            response = (
                f"HTTP/1.1 200 OK\r\n"
                f"Content-Type: text/plain\r\n"
                f"\r\n"
                f"Request Method: {request_method}\r\n"
                f"Request Source: {client_address}\r\n"
                f"Response Status: {status} {phrase}\r\n"
            )
            client_connection.sendall(response.encode())
