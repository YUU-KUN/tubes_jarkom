import socket

import os

def tcp_server():
    host = '127.0.0.1'
    port = 8080

    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    socket_server.bind((host, port))
    socket_server.listen()

    print(f'Web server running on {host}:{port}')

    while True:
        socket_client, client_address = socket_server.accept()

        request = socket_client.recv(1024).decode()
        print('dari client: ', request)

        response = handle_request(request)
        socket_client.sendall(response.encode())

        socket_client.close()

def handle_request(request):
    print('ini dari server: ' + request)
    response_line = 'HTTP/1.1 200 OK\n'
    response_header = 'Content-Type: text/html\n'

    try:
        # file = open(request.split()[1], 'r')
        # response_body = file.read()
        # file.close()
        file = open('index.html', 'r')
        response_body = file.read()
        file.close()
    except FileNotFoundError:
        response_body = '<h1>404 Not Found</h1>'


    response = response_line + response_header + '\n' + response_body

    print('\nresponse: ', response)
    return response
    

tcp_server()