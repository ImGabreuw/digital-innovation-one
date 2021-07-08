# Como organizar os dados em uma lista ou tupla e realizar operações com elas

### Lista

* **Criar uma lista**

  * **Sintaxe**

    ```python
    [<elemento 1>, <elemento 2>, ...]
    ```

  * **Exemplo**

    ```python
    lista_numero = [1, 3, 5, 7]
    lista_animal = ["cachorro", "gato", "elefante"]
    print(type(lista_numero)) # <class 'list'>
    print(type(lista_animal)) # <class 'list'>
    ```

    ```python
    lista = [1, 2, 3, "gato"]
    ```

    > É possível criar uma lista com valores de **tipos diferentes**, porém **não é recomendado**
  
* **Recuperar um elemento da lista**

  * **Sintaxe**

    ```python
    <nome da lista>[<índice>]
    ```

    > **OBS**: índice começa em 0

  * **Exemplo**

    ```python
    lista_animal = ["cachorro", "gato", "elefante"]

    print(lista_animal[1]) # gato
    ```

* **Percorrer uma lista**

  * **Sintaxe**

    ```python
    for <nome da variável> in <nome da lista>:
      # Código
    ```

  * **Exemplo**

    ```python
    lista_animal = ["cachorro", "gato", "elefante"]
    for animal in lista_animal:
      print(animal)

    # Saída:
    # cachorro
    # gato
    # elefante
    ```

* **Funções para listas**

  * **Somatória dos números**

    * **Sintaxe**

      ```python
      sum(<nome da lista>)
      ```

    * **Exemplo**

      ```python
      lista_numero = [1, 3, 5, 7]
      print(sum(lista_numero)) # 16
      ```

  * **Obter o maior valor**

    * **Sintaxe**

      ```python
      max(<nome da lista>)
      ```

    * **Exemplo**

      ```python
      lista_numero = [1, 3, 5, 7]
      print(max(lista_numero)) # 7
      ```

      ```python
      lista_animal = ["cachorro", "gato", "elefante"]
      print(min(lista_animal)) # gato
      ```

      > OBS: para uma lista de Strings, a comparação é feita pela ordem alfabética

  * **Obter o menor valor**

    * **Sintaxe**

      ```python
      max(<nome da lista>)
      ```

      > OBS: para uma lista de Strings, a comparação é feita pela ordem alfabética

    * **Exemplo**

      ```python
      lista_numero = [1, 3, 5, 7]
      print(min(lista_numero)) # 1
      ```

      ```python
      lista_animal = ["cachorro", "gato", "elefante"]
      print(min(lista_animal)) # cachorro
      ```

  * **Verificar se um elemento existe na lista**

    * **Sintaxe**

      ```python
      <valor> in <lista>
      ```

    * **Exemplo**

      ```python
      lista_animal = ["cachorro", "gato", "elefante"]

      if "gato" in lista_animal:
          print("Existe um gato na lista")
      else:
          print("Não existe um gato na lista")
      ```

* **Multiplicar uma lista**

  * **Sintaxe**

    ```python
    <lista> * <número>
    ```

  * **Exemplo**

    ```python
    nova_lista_animal = lista_animal * 3
    print(nova_lista_animal) # ['cachorro', 'gato', 'elefante', 'cachorro', 'gato', 'elefante', 'cachorro', 'gato', 'elefante']
    ``` 

* **Adicionar um elemento na lista**

  * **Sintaxe**

    ```python
    <nome da lista>.append(<elemento>)
    ```

  * **Exemplo**

    ```python
    lista_animal = ["cachorro", "gato", "elefante"]

    if "lobo" in lista_animal:
        print("Existe um lobo na lista")
    else:
        print("Não existe um lobo na lista")
        lista_animal.append("lobo")
        print(lista_animal) # ['cachorro', 'gato', 'elefante', 'lobo']
    ```

* **Remover o último elemento da lista**

  * **Sintaxe**

    ```python
    <nome da lista>.pop()
    ```

  * **Exemplo**

    ```python
    lista_animal = ["cachorro", "gato", "elefante"]
    lista_animal.pop()
    print(lista_animal) # ['cachorro', 'gato']
    ```

* **Remover um elemento da lista**

  * **Sintaxe**

    ```python
    <nome da lista>.pop(<índice>)
    ```

  * **Exemplo**

    ```python
    lista_animal = ["cachorro", "gato", "elefante"]
    lista_animal.pop(1)
    print(lista_animal) # ['cachorro', 'elefante']
    ```

  * **Remover um elemento da lista pelo valor**

    * **Sintaxe**

      ```python
      <nome da lista>.remove(<valor>)
      ```

    * **Exemplo**

      ```python
      lista_animal = ["cachorro", "gato", "elefante"]
      lista_animal.remove("cachorro")
      print(lista_animal) # ['gato', 'elefante']
      ```

  * **Ordenar uma lista em ordem crescente**

    * **Sintaxe**

      ```python
      <nome da lista>.sort()
      ```
    
    * **Exemplo**

      ```python
      lista_numero = [1, 3, 5, 7]
      lista_animal = ["cachorro", "gato", "elefante"]

      lista_numero.sort()
      lista_animal.sort()

      print(lista_numero) # [1, 3, 5, 7]
      print(lista_animal) # ['cachorro', 'elefante', 'gato']
      ```

  * **Ordenar uma lista em ordem decrescente**

    * **Sintaxe**

      ```python
      <nome da lista>.reverse()
      ```
    
    * **Exemplo**

      ```python
      lista_numero = [1, 3, 5, 7]
      lista_animal = ["cachorro", "gato", "elefante"]

      lista_numero.reverse()
      lista_animal.reverse()

      print(lista_numero) # [7, 5, 3, 1]
      print(lista_animal) # ['gato', 'elefante', 'cachorro']
      ```

  * **Obter o tamanho da lista (quantidade de elementos)**

    * **Sintaxe**

      ```python
      len(<nome da lista>)
      ```

    * **Exemplo**

      ```python
      lista_animal = ["cachorro", "gato", "elefante"]
      print(len(lista_animal)) # 3
      ```

### Tuple

* É uma **lista imutável**

* **OBS**: todos as funções da lista são válidas para a _tuple_

* **Criar uma _tuple_**

  * **Sintaxe**

    ```python
    (<elemento 1>, <elemento 2>, ...)
    ```

  * **Exemplo**

    ```python
    tupla = (1, 10, 12, 14)
    print(tupla) # (1, 10, 12, 14)
    ```
