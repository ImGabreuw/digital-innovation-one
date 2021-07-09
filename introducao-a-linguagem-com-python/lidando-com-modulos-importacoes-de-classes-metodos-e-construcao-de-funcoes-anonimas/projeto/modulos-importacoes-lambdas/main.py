from contador_de_letras import contador_de_letras

if __name__ == '__main__':
    lista = ["cachorro", "gato", "elefante"]

    letras_por_palavra = contador_de_letras(lista)

    print("Total de letras por palavra: {}".format(letras_por_palavra))
