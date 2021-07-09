class Error(Exception):
    pass


class InputError(Error):

    def __init__(self, mensagem):
        self.mensagem = mensagem


if __name__ == '__main__':

    while True:
        try:
            nota = int(input("Entre com uma nota entre 0 e 10: "))

            if nota > 10 or nota < 0:
                raise InputError("Insira uma nota entre 0 e 10")

            break
        except ValueError:
            print("Nota inválida. Deve-se digitar apenas número.")
        except InputError as ex:
            print(ex)
