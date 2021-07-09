# Exemplo 1:
# lista = [1, 10]
# try:
#     divisao = 10 / 1
#     numero = lista[1]
# except ZeroDivisionError:
#     print("Não é possível realizar uma divisão por 0")
# except IndexError:
#     print("Erro ao acessar um índice inválido da lista")
# except BaseException as ex:
#     print("Erro desconhecido. Erro: {}".format(ex))
# else:
#     print("Executa quando não ocorre exceção")

# Exemplo 2:
try:
    divisao = 10 / 1
except ZeroDivisionError:
    print("Não é possível realizar uma divisão por 0")
except ArithmeticError as err:
    print("Erro desconhecido. Erro: {}".format(err))
else:
    print("Executa quando não ocorre exceção")
finally:
    print("Sempre executa")
