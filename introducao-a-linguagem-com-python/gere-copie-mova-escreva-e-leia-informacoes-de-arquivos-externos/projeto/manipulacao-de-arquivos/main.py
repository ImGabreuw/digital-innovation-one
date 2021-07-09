import shutil


def escrever_arquivo(texto):
    arquivo = open("teste.txt", "w")
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, "a")
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    texto = arquivo.read()
    print(texto)


def media_alunos(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    notas_aluno = arquivo.read().split("\n")

    for elemento in notas_aluno:
        info_aluno = elemento.split(",")

        aluno = info_aluno[0]
        info_aluno.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4

        print("Média do aluno {} é {}".format(aluno, media(info_aluno)))


def copiar_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, ".")


def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, ".")


if __name__ == '__main__':
    # Exemplo 1:
    # escrever_arquivo("primeira linha.\n")
    # atualizar_arquivo("segunda linha.\n")
    # ler_arquivo("teste.txt")

    # Exemplo 2:
    # aluno = "\nCesar,7,9,3,8"
    # atualizar_arquivo("notas.txt", aluno)

    # Exemplo 3:
    # media_alunos("notas.txt")

    # Exemplo 4:
    copiar_arquivo("notas.txt")
