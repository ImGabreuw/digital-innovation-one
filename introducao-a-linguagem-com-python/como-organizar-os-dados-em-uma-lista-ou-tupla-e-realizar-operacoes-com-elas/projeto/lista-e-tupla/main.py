lista_numero = [1, 3, 5, 7]
lista_animal = ["cachorro", "gato", "elefante"]

# Exemplo 1: (Recuperar um elemento da lista)
# print(lista_animal[1])

# Exemplo 2: (Percorrer uma lista)
# for animal in lista_animal:
#     print(animal)

# Exemplo 3: (Somatório dos números de uma lista)
soma = 0
for numero in lista_numero:
    soma += numero
print(soma)

# OU

print(sum(lista_numero))

# Exemplo 4: (Maior número de uma lista de números)
print(max(lista_numero))

# Exemplo 5: (Menor número de uma lista de números)
print(min(lista_numero))

# Exemplo 6: (Verificar se uma valor está presente em uma lista)
if "gato" in lista_animal:
    print("Existe um gato na lista")
else:
    print("Não existe um gato na lista")

# Exemplo 7: (Multiplicar uma lista)
nova_lista_animal = lista_animal * 3
print(nova_lista_animal)

# Exemplo 8: (Adicionar um elemento na lista)
if "lobo" in lista_animal:
    print("Existe um lobo na lista")
else:
    print("Não existe um lobo na lista")
    lista_animal.append("lobo")
    print(lista_animal)

lista_animal.pop()
print(lista_animal)

# Exemplo 9: (Remover um elemento da lista pelo valor)
lista_animal.remove("cachorro")
print(lista_animal)

# Exemplo 10: (Organizar, em ordem crescente, os elementos da lista)
lista_numero.sort()
lista_animal.sort()

print(lista_numero)
print(lista_animal)

# Exemplo 11: (Organizar, em ordem decrescente, os elementos da lista)
lista_numero.reverse()
lista_animal.reverse()

print(lista_numero)
print(lista_animal)

# Exemplo 12: (Tamanho da lista)
print(len(lista_animal))

# Exemplo 13: (Criar uma tuple)
tupla = (1, 10, 12, 14)
print(tupla)