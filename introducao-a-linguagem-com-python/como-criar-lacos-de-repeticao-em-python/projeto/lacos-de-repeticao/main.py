# Exemplo 1: (verificar se um número é primo ou não)
# a = int(input("Entre com um número: "))
#
# div = 0
#
# for x in range(1, a + 1):
#     resto = a % x
#
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print("número {} é primo".format(a))
# else:
#     print("número {} não é primo".format(a))

# Exemplo 2: (imprimir todos os números primos de um intervalo)
# intervalo = int(input("Entre com um valor: "))
#
# for num in range(intervalo + 1):
#     div = 0
#
#     for x in range(1, num + 1):
#         resto = num % x
#
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

# Exemplo 3:
# a = 0
# while a < 10:
#     print(a)
#     a += 1

# Exemplo 4:
# nota = int(input("Entre com uma nota: "))
#
# while nota > 10:
#     nota = int(input("Nota inválida. Entre com uma nota entre 0 e 10: "))

a = int(input("Nota do primeiro bimestre: "))
while a > 10:
    a = int(input("Você digitou errado. Primeiro bimestre: "))

b = int(input("Nota do segundo bimestre: "))
while b > 10:
    b = int(input("Você digitou errado. Segundo bimestre: "))

c = int(input("Nota do terceiro bimestre: "))
while c > 10:
    c = int(input("Você digitou errado. Terceiro bimestre: "))

d = int(input("Nota do quarto bimestre: "))
while d > 10:
    d = int(input("Você digitou errado. Quarto bimestre: "))

media = (a + b + c + d) / 4

print("Média: {}".format(media))
