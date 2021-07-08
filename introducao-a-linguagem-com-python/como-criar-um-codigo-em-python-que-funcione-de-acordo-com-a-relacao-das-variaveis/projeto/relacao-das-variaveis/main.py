# Forma 1:
# a = int(input("Nota do primeiro bimestre: "))
# b = int(input("Nota do segundo bimestre: "))
# c = int(input("Nota do terceiro bimestre: "))
# d = int(input("Nota do quarto bimestre: "))
#
# media = (a + b + c + d) / 4
#
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print("Média: {}".format(media))
# else:
#     print("Foi informado alguma nota errada")

# Forma 2:
a = int(input("Nota do primeiro bimestre: "))
if a > 10:
    a = int(input("Você digitou errado. Primeiro bimestre: "))

b = int(input("Nota do segundo bimestre: "))
if b > 10:
    b = int(input("Você digitou errado. Segundo bimestre: "))

c = int(input("Nota do terceiro bimestre: "))
if c > 10:
    c = int(input("Você digitou errado. Terceiro bimestre: "))

d = int(input("Nota do quarto bimestre: "))
if d > 10:
    d = int(input("Você digitou errado. Quarto bimestre: "))

media = (a + b + c + d) / 4

print("Média: {}".format(media))
