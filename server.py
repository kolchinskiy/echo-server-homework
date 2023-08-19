import socket

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
            headers = request_data.split('\r\n')[1:-2]

            status = 200
            for header in headers:
                if "GET" in header:
                    parts = header.split('?')
                    if len(parts) > 1:
                        params = parts[1].split()
                        for param in params:
                            key, value = param.split('=')
                            if key == "status":
                                try:
                                    status = int(value)
                                except ValueError:
                                    pass

            response = (
                f"HTTP/1.1 {status} OK\r\n"
                f"Content-Type: text/plain\r\n"
                f"\r\n"
                f"Request Method: {request_method}\r\n"
                f"Request Source: {client_address}\r\n"
                f"Response Status: {status} {'OK' if status == 200 else ''}\r\n"
            )
            client_connection.sendall(response.encode())
