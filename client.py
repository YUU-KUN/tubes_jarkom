import socket

def tcp_client():
    host = '192.168.1.24'  # Tentukan host yang dituju
    port = 8080  # Tentukan port yang dituju

    file_path = '/' + input('Masukkan file yang ingin diminta: ') # Tentukan file yang ingin diminta berdasarkan input dari user

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Buat objek socket sebagai soket TCP

    socket_client.connect((host, port)) # Hubungkan socket ke host dan port yang dituju

    request = "GET {} HTTP/1.1\r\nHost: {}\r\n\r\n".format(file_path, host) # Siapkan permintaan HTTP GET

    socket_client.sendall(request.encode()) # Kirim permintaan ke server

    print("Host Klien: {}, Port: {}".format(socket_client.getsockname()[0], socket_client.getsockname()[1])) # Cetak host dan port klien
    print("File yang Diminta: {}".format(file_path)) # Cetak file yang diminta

    response = socket_client.recv(1024) # Terima dan cetak respon dari server
    print('\n\nRespon:\n{}'.format(response)) # Tampilkan response

    socket_client.close() # Tutup koneksi

tcp_client() # Panggil fungsi tcp_client