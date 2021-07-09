# Refatorando o contador de letras
contador_de_letras = lambda lista: [len(x) for x in lista]
lista_animais = ["cachorro", "gato", "elefante"]
print(contador_de_letras(lista_animais))

# Exemplo 2:
soma = lambda a, b: a + b
print(soma(5, 10))

# Exemplo 3:
subtracao = lambda a, b: a - b
print(subtracao(10, 2))

# Exemplo 4:
calculadora = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b,
    "divisao": lambda a, b: a / b,
}

print(type(calculadora))

soma = calculadora["soma"]
subtracao = calculadora["subtracao"]
multiplicacao = calculadora["multiplicacao"]
divisao = calculadora["divisao"]

print(soma(10, 5))
print(multiplicacao(2, 5))
