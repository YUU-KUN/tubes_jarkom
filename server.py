import socket # Import package socket untuk membuat socket
import urllib.parse # Import package urllib.parse untuk memparsing URL

def tcp_server(): # Definisikan fungsi tcp_server
    host = '192.168.1.24' # Tentukan host
    port = 8080 # Tentukan port

    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Buat objek socket_server sebagai soket TCP
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Setel soket agar dapat menggunakan alamat yang sama lagi

    socket_server.bind((host, port)) # Hubungkan soket dengan host dan port
    socket_server.listen() # Listen / pantau koneksi

    print(f'Web server berjalan di {host}:{port}') # Tampilkan pesan web server berjalan

    while True: # Jalankan server secara terus menerus
        socket_client, client_address = socket_server.accept() # Terima koneksi dari klien, assign ke socket_client dan client_address
        request = socket_client.recv(1024).decode() # Terima permintaan dari klien, decode dari byte ke string & masukkan ke variabel request

        try: # Coba jalankan kode
            request = request.split('\r\n\r\n')[0] # Pisahkan permintaan dari bagian header
            print('Dari Klien:\n') # Tampilkan pesan "Dari Klien:"
            print('Alamat Klien: {}'.format(client_address)) # Tampilkan alamat klien
            print('Host Klien: {}'.format(client_address[0])) # Tampilkan host klien
            print('Port Klien: {}'.format(client_address[1])) # Tampilkan port klien
            print('File yang Diminta: {}'.format(request.split(' ')[1])) # Tampilkan file yang diminta

            response = handle_request(request) # Assign output fungsi handle_request ke variabel response
            print('\n\nRespon:\n{}'.format(response)) # Tampilkan response

            socket_client.sendall(response) # Kirim response ke klien
        except: # Jika terjadi error
            pass # Lewati
        socket_client.close() # Tutup koneksi dengan klien


def handle_request(request): # Definisikan fungsi handle_request untuk mengolah permintaan dari klien
    # print('\nDari Server: \n' + request) # Tampilkan permintaan dari klien
    
    parsed_request = request.split(' ') # Pisahkan permintaan dari klien berdasarkan spasi
    method = parsed_request[0] # Definisikan method sebagai elemen pertama dari permintaan
    url = parsed_request[1] # Definisikan url sebagai elemen kedua dari permintaan

    path = urllib.parse.unquote(urllib.parse.urlparse(url).path) # Definisikan path sebagai path dari url yang sudah di-unquote dan di-parse

    if path == '/': # Jika path adalah '/'
        path = '/index.html' # Set path ke '/index.html'

    try: # Coba jalankan kode
        with open('.' + path, 'rb') as file: # Buka file yang diminta
            if path.endswith('.html'): # Jika path berakhiran '.html'
                response_header = b'Content-Type: text/html\n' # Set response header ke 'Content-Type: text/html'
            elif path.endswith('.css'): # Jika path berakhiran '.css'
                response_header = b'Content-Type: text/css\n' # Set response header ke 'Content-Type: text/css'
            elif path.endswith('.js'): # Jika path berakhiran '.js'
                response_header = b'Content-Type: text/javascript\n' # Set response header ke 'Content-Type: text/javascript'
            elif path.endswith('.jpg'): # Jika path berakhiran '.jpg'
                response_header = b'Content-Type: image/jpeg\n' # Set response header ke 'Content-Type: image/jpeg'
            elif path.endswith('.png'): # Jika path berakhiran '.png'
                response_header = b'Content-Type: image/png\n' # Set response header ke 'Content-Type: image/jpeg'
            elif path.endswith('.pdf'): # Jika path berakhiran '.pdf'
                response_header = b'Content-Type: application/pdf\n' # Set response header ke 'Content-Type: application/pdf'
            else: # Jika tidak ada yang cocok
                response_header = b'Content-Type: *\n' # Set response header ke 'Content-Type: *' untuk menerima semua jenis file
                
            response_body = file.read() # Baca isi file

        response_line = b'HTTP/1.1 200 OK\n' # Definisikan response line sebagai HTTP/1.1 200 OK
        response = response_line + response_header + b'\n' + response_body # Definisikan response sebagai response line + response header + response body
    except FileNotFoundError: # Jika file tidak ditemukan
        response_line = b'HTTP/1.1 404 Not Found\n' # Definisikan response line sebagai HTTP/1.1 404 Not Found
        response_header = b'Content-Type: *\n' # Definisikan response header sebagai 'Content-Type: *' untuk menerima semua jenis file
        response_body = b'<h1>404 Not Found</h1>' # Definisikan response body sebagai '<h1>404 Not Found</h1>'

        response = response_line + response_header + b'\n' + response_body # Definisikan response sebagai response line + response header + response body

    return response # Kembalikan response

tcp_server() # Jalankan fungsi tcp_server
