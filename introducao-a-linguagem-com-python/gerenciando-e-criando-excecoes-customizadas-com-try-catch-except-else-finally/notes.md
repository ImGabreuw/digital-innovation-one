# Gerenciando e criando exceções customizadas com try, except, else e finally

### Tratamento de erros

* **Bloco `try-except`**

  * **Sintaxe** 

    ```python
    try:
      # Código
    except <erro>:
      # Tratamento
    ```

  * **Exemplo** 

    ```python
    try:
      divisao = 10 / 0
    except ZeroDivisionError:
        print("Não é possível realizar uma divisão por 0")
    ```

* **Encadeamento de `except`**

  * **Sintaxe**

    ```python
    try:
      # Código
    except <erro 1>:
      # Tratamento para o erro 1
    except <erro 2>:
      # Tratamento para o erro 2
    ```

    ```python
    try:
      # Código
    except <erro 1>:
      # Tratamento para o erro 1
    except:
      # Qualquer tipo de exceção que não seja o "erro 1" cairá nesse "except"
    ```

  * **Exemplo**

    ```python
    lista = [1, 10]
    try:
      divisao = 10 / 1
      numero = lista[3]
    except ZeroDivisionError:
      print("Não é possível realizar uma divisão por 0")
    except IndexError:
      print("Erro ao acessar um índice inválido da lista")
    ```

    ```python
    lista = [1, 10]
    try:
      divisao = 10 / 1
      numero = lista[3]
    except ZeroDivisionError:
      print("Não é possível realizar uma divisão por 0")
    except:
      print("Erro desconhecido")
    ```

* **Atribuir um "apelido" a uma exceção**

  * **Sintaxe**

    ```python
    try:
      # Código
    except <erro 1> as <"apelido">:
      # Tratamento
    ```

  * **Exemplo**

    ```python
    try:
        divisao = 10 / 0
    except BaseException as ex:
        print("Erro: {}".format(ex))

    ```

### `else`

> O código dentro do bloco `else` é executado quando não houver nenhuma exceção

* **Sintaxe**

  ```python
  try:
    # Código
  except:
    # Tratamento
  else:
    # Não houve nenhuma exceção
  ```

* **Exemplo**

  ```python
  try:
      divisao = 10 / 1
  except ZeroDivisionError:
      print("Não é possível realizar uma divisão por 0")
  except ArithmeticError as err:
      print("Erro: {}".format(err))
  else:
      print("Executa quando não ocorre exceção")
  ```

### `finally`

> o código dentro do bloco `finally` sempre é executado, não importa se foi lança uma exceção ou não

* **Sintaxe**

  ```python
  try:
    # Código
  except:
    # Tratamento
  finally:
    # Sempre é executado
  ```

* **Exemplo**

  ```python
  try:
    divisao = 10 / 1
  except ZeroDivisionError:
    print("Não é possível realizar uma divisão por 0")
  except ArithmeticError as err:
    print("Erro desconhecido. Erro: {}".format(err))
  finally:
    print("Sempre executa")
  ```

### Exceção personalizada

* **Sintaxe**

  ```python
    # É obrigatório uma classe que herde de "Exception", mesmo que ela não tenha implementação
    class Error(Exception):
      pass # OU implementação

    class NomeDaExcecaoPersonalidadeError(Error):
      # implementação
  ```

  > o sufixo **Error** é uma convenção para exceções

* **Exemplo**

  ```python
  class Error(Exception):
    pass


  class InputError(Error):

      def __init__(self, mensagem):
          self.mensagem = mensagem
  ```

### Lançar uma exceção

* **Sintaxe**

  ```python
  raise Excecao()
  ```

* **Exemplo**

  ```python
  class Error(Exception):
    pass


  class InputError(Error):

      def __init__(self, mensagem):
          self.mensagem = mensagem
          

  nota = int(input("Entre com uma nota entre 0 e 10: "))

  if nota > 10 or nota < 0:
      raise InputError("Insira uma nota entre 0 e 10")
  ```