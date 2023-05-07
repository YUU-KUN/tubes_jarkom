import socket  # import library socket


def tcp_server():  # definisikan fungsi tcp_server
    host = '127.0.0.1'  # inisialisasi host
    port = 8080  # inisialisasi port

    # inisialisasi objek socket
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # set socket option

    socket_server.bind((host, port))  # bind socket ke host dan port
    socket_server.listen()  # listen socket

    print(f'Web server running on {host}:{port}')  # print host dan port

    while True:  # loop selama true
        socket_client, client_address = socket_server.accept()  # terima koneksi dari client

        request = socket_client.recv(1024).decode()  # terima data dari client
        print('dari client: ', request)  # print data dari client

        response = handle_request(request)  # handle request dari client
        print('\nresponse: ', response)  # print response

        socket_client.sendall(response.encode())  # kirim response ke client

        socket_client.close()  # tutup koneksi agar tidak memakan resource


def handle_request(request):  # definisikan fungsi handle_request
    print('ini dari server: ' + request)  # print request dari client
    response_line = 'HTTP/1.1 200 OK\n'  # inisialisasi response line
    response_header = 'Content-Type: text/html\n'  # inisialisasi response header

    try:  # try catch untuk membaca file agar tidak error
        # cari & buka file index.html pada root folder
        file = open('index.html', 'r')
        response_body = file.read()  # baca isi file dan simpan ke response body
        file.close()  # tutup file agar tidak memakan resource
    except FileNotFoundError:  # jika file tidak ditemukan
        # isi response body dengan 404 Not Found
        response_body = '<h1>404 Not Found</h1>'

    response = response_line + response_header + '\n' + \
        response_body  # gabungkan response line, header, dan body
    return response  # return response sebagai hasil dari fungsi handle_request


tcp_server()  # jalankan fungsi tcp_server
