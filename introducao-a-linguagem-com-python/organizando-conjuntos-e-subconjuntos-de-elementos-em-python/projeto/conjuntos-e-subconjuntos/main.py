conjunto = {1, 2, 3, 4, 4, 3}
print(conjunto)

# Exemplo 1:
conjunto.add(7)
print(conjunto)

# Exemplo 2:
conjunto.discard(2)
print(conjunto)

# Exemplo 3:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto1.union(conjunto2)
print(conjunto_uniao)

# Exemplo 4:
conjunto_interseccao = conjunto1.intersection(conjunto2)
print(conjunto_interseccao)

# Exemplo 5:
conjunto_diferenca1 = conjunto1.difference(conjunto2)
print(conjunto_diferenca1)

conjunto_diferenca2 = conjunto2.difference(conjunto1)
print(conjunto_diferenca2)

# Exemplo 6:
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print(conjunto_diff_simetrica)

# Exemplo 7:
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

# Exemplo 8:
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

# Exemplo 9:
lista_animais = ["cachorro", "cachorro", "gato", "gato", "elefante"]
conjunto_animais = set(lista_animais)
print(conjunto_animais)
