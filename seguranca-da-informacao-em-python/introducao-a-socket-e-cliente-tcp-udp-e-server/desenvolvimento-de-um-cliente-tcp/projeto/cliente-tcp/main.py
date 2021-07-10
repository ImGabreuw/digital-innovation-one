import socket
import sys


def main():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("A conexão falhou!")
        print("Erro: {}".format(error))
        sys.exit()

    print("Socket criado com sucesso!")

    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectado: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no host {}:{}".format(HostAlvo, PortaAlvo))
        s.shutdown(2)
    except socket.error as error:
        print("A conexão falhou!")
        print("Erro: {}".format(error))
        sys.exit()


if __name__ == '__main__':
    main()