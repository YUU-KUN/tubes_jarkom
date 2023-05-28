import socket
import urllib.parse

def tcp_server():
    host = '192.168.1.24'
    port = 8080

    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    socket_server.bind((host, port))
    socket_server.listen()

    print(f'Web server running on {host}:{port}')

    while True:
        socket_client, client_address = socket_server.accept()
        request = socket_client.recv(1024).decode()
        try:
            request = request.split('\r\n\r\n')[0]
            print('From Client:\n')
            print('Client Address: {}'.format(client_address))
            print('Client Host: {}'.format(client_address[0]))
            print('Client Port: {}'.format(client_address[1]))
            print('File Requested: {}'.format(request.split(' ')[1]))

            response = handle_request(request)
            print('\n\nResponse:\n{}'.format(response))

            socket_client.sendall(response)
        except:
            pass
        socket_client.close()


def handle_request(request):
    print('\nFrom Server: \n' + request)
    response_line = b'HTTP/1.1 200 OK\n'
    response_header = b'Content-Type: *\n'

    parsed_request = request.split(' ')
    method = parsed_request[0]
    url = parsed_request[1]

    path = urllib.parse.unquote(urllib.parse.urlparse(url).path)

    if path == '/':
        path = '/index.html'

    try:
        with open('.' + path, 'rb') as file:
            if path.endswith('.html'):
                response_header = b'Content-Type: text/html\n'
            elif path.endswith('.css'):
                response_header = b'Content-Type: text/css\n'
            elif path.endswith('.js'):
                response_header = b'Content-Type: text/javascript\n'
            elif path.endswith('.jpg'):
                response_header = b'Content-Type: image/jpeg\n'
            elif path.endswith('.pdf'):
                response_header = b'Content-Type: application/pdf\n'
            else:
                response_header = b'Content-Type: *\n'
                
            response_body = file.read()

        response = response_line + response_header + b'\n' + response_body
    except FileNotFoundError:
        response_line = b'HTTP/1.1 404 Not Found\n'
        response_header = b'Content-Type: *\n'
        response_body = b'<h1>404 Not Found</h1>'

        response = response_line + response_header + b'\n' + response_body

    return response

tcp_server()
