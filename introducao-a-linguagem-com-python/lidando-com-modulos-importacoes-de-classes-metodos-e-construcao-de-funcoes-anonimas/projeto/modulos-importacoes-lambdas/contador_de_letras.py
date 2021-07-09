def contador_de_letras(lista_de_palavras):
    contador = []

    for palavra in lista_de_palavras:
        quantidade = len(palavra)
        contador.append(quantidade)

    return contador


if __name__ == '__main__':
    lista = ["cachorro", "gato"]
    print(contador_de_letras(lista))
