# Lidando com módulos, importação de classes, métodos e construção de funções anônimas (lambda)

### Módulo

* É cada arquivo `.py`

* Para testar um módulo, é necessário fazer o seguinte:

  ```python
  # Como um método "main" no Java
  if __name__ == '__main__':
    # Código
  ```

  > O código dentro do `__main__` não será executado caso outro arquivo o importe

### Imports

* **Importar um módulo**

  * **Sintaxe**

    ```python
    import nome_do_modulo
    ```

  * **Exemplo**

    ```python
    import aula7_televisao
    ```

* **Importar uma classe**

  * **Sintaxe**

    ```python
    from nome_do_modulo import NomeDaClasse
    ```

  * **Exemplo**

    ```python
    from aula7_televisao import Televisao
    ```

* **Importar uma função/método**

  * **Sintaxe**

    ```python
    from nome_do_modulo import nome_da_funcao
    from nome_do_modulo import nome_do_metodo
    ```

    ```python
    from nome_do_modulo import nome_da_funcao, nome_do_metodo, ...
    ```

  * **Exemplo**

    ```python
    from contador_de_letras import contador_de_letras
    ```

### Lambdas

* **Sintaxe**

  ```python
  lambda parametros, ...: # implementação da função
  ```

* **Exemplo**

  ```python
  lambda lista: [len(x) for x in lista]
  ```

### Dictionary (dicionário)

* **Sintaxe**

  ```python
  {
    "nome do 1º item do dicionário": # implementação da função,
    "nome do 2º item do dicionário": # implementação da função,
    "nome do 3º item do dicionário": # implementação da função,
    ...
  }
  ```

* **Exemplo**

  ```python
  calculadora = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b,
    "divisao": lambda a, b: a / b,
  }

  print(type(calculadora)) # <class 'dict'>

  soma = calculadora["soma"] # <=> soma = lambda a, b: a + b

  print(soma(10, 5)) # 15
  ```