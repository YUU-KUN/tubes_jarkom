import socket

def tcp_client():
    host = '192.168.1.24'
    port = 8080
    file_path = '/index.html'  # Specify the file path you want to request

    # Create a socket object
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    socket_client.connect((host, port))

    # Prepare the HTTP GET request
    request = "GET {} HTTP/1.1\r\nHost: {}\r\n\r\n".format(file_path, host)

    # Send the request to the server
    socket_client.sendall(request.encode())

    # Print client host and port, and the requested file
    print("Client Host: {}, Port: {}".format(socket_client.getsockname()[0], socket_client.getsockname()[1]))
    print("Requested File: {}".format(file_path))

    # Receive and print the response from the server
    response = socket_client.recv(1024).decode()
    print(response)

    # Close the connection
    socket_client.close()

tcp_client()