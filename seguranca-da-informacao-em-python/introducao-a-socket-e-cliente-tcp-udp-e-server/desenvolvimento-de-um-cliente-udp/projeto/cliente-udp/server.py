import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as error:
    print("Não foi possível criar o socket.")
else:
    print("Socket criado com sucesso.")

    host = "localhost"
    port = 5432

    s.bind((host, port))
    mensagem = "\nServidor: Olá cliente!"

    while 1:
        dados, end = s.recvfrom(4096)

        if dados:
            print("Servidor enviando mensagem")
            s.sendto(dados + (mensagem.encode()), end)

