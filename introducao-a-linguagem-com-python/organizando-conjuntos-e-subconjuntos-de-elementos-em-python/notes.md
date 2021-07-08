# Organizando conjuntos e subconjuntos de elementos em Python

### Set (Conjunto)

* **Criar um set**

  * **Sintaxe**

    ```python
    {<elemento 1>, <elemento 2>, ...}
    ```

  * **Exemplo**

    ```python
    conjunto = {1, 2, 3, 4}
    print(conjunto) # {1, 2, 3, 4}
    ```

    ```python
    conjunto = {1, 2, 3, 4, 4, 3}
    print(conjunto) # {1, 2, 3, 4}
    ```

    > No _set_, não há duplicidade de elementos

* **Adicionar um elemento**

  * **Sintaxe**

    ```python
    <nome do conjunto>.add(<elemento>)
    ```

  * **Exemplo**

    ```python
    conjunto = {1, 2, 3, 4}
    conjunto.add(7)
    print(conjunto) # {1, 2, 3, 4, 7}
    ```

* **Remover um elemento**

  * **Sintaxe**

    ```python
    <nome do conjunto>.discard(<elemento>)
    ```

  * **Exemplo**

    ```python
    conjunto = {1, 2, 3, 4}
    conjunto.add(2)
    print(conjunto) # {1, 3, 4, 7}
    ```

* **União de conjuntos**

  > Juntar os elemento do conjuntos e eliminar os repetidos

  * **Sintaxe**

    ```python
    <conjunto 1>.union(<conjunto 2>)
    ```

  * **Exemplo**

    ```python
    conjunto1 = {1, 2, 3, 4, 5}
    conjunto2 = {5, 6, 7, 8}

    conjunto_uniao = conjunto1.union(conjunto2)
    print(conjunto_uniao) # {1, 2, 3, 4, 5, 6, 7, 8}
    ```

* **Intersecção de conjuntos**

  > Pegar apenas os elementos que estão nos 2 conjuntos

  * **Sintaxe**

    ```python
    <conjunto 1>.intersection(<conjunto 2>)
    ```

  * **Exemplo**

    ```python
    conjunto1 = {1, 2, 3, 4, 5}
    conjunto2 = {5, 6, 7, 8}

    conjunto_interseccao = conjunto1.intersection(conjunto2)
    print(conjunto_interseccao) # {5}
    ```

* **Diferença de conjuntos**

  > Pegar os elementos que estão presentes apenas em um dos conjuntos

  * **Sintaxe**

    ```python
    <conjunto 1>.difference(<conjunto 2>)
    ```

  * **Exemplo**

    ```python
    conjunto1 = {1, 2, 3, 4, 5}
    conjunto2 = {5, 6, 7, 8}

    conjunto_diferenca = conjunto1.difference(conjunto2)
    print(conjunto_diferenca) # {1, 2, 3, 4} (elementos presentes apenas no conjunto 1)
    ```

    ```python
    conjunto1 = {1, 2, 3, 4, 5}
    conjunto2 = {5, 6, 7, 8}

    conjunto_diferenca = conjunto2.difference(conjunto1)
    print(conjunto_diferenca) # {8, 6, 7} (elementos presentes apenas no conjunto 2)
    ```

* **Diferença simétrica de conjuntos**

  > Pegar os elementos que não se repetem nos 2 conjuntos

  * **Sintaxe**

    ```python
    <conjunto 1>.symmetric_difference(<conjunto 2>)
    ```

  * **Exemplo**

    ```python
    conjunto1 = {1, 2, 3, 4, 5}
    conjunto2 = {5, 6, 7, 8}

    conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
    print(conjunto_diff_simetrica) # {1, 2, 3, 4, 6, 7, 8}
    ```

    ```python
    conjunto1 = {1, 2, 3}
    conjunto2 = {1, 2, 3}

    conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
    print(conjunto_diff_simetrica) # set()
    ```

### Pertinências

> Pertinências = métodos subset, superset, join

* **Conjunto subset**

  > Verificar se um conjunto está contido em outro

  * **Sintaxe**

    ```python
    <conjunto 1>.issubset(<conjunto 2>)
    ```
  
  * **Exemplo**

    ```python
    conjunto_a = {1, 2, 3}
    conjunto_b = {1, 2, 3, 4, 5}

    conjunto_subset = conjunto_a.issubset(conjunto_b)
    print(conjunto_subset) # True
    ```

    ```python
    conjunto_a = {1, 2, 3}
    conjunto_b = {1, 2, 3, 4, 5}

    conjunto_subset = conjunto_b.issubset(conjunto_a)
    print(conjunto_subset) # True
    ```

* **Conjunto superset**

  > Inverso do `issubset()`

  * **Sintaxe**

    ```python
    <conjunto 1>.issubset(<conjunto 2>)
    ```

  * **Exemplo**

    ```python
    conjunto_a = {1, 2, 3}
    conjunto_b = {1, 2, 3, 4, 5}

    conjunto_superset = conjunto_b.issuperset(conjunto_a)
    print(conjunto_superset) # True
    ```

    ```python
    conjunto_a = {1, 2, 3}
    conjunto_b = {1, 2, 3, 4, 5}

    conjunto_superset = conjunto_a.issuperset(conjunto_b)
    print(conjunto_superset) # False
    ```

* **Converter uma lista para conjunto**

  * **Sintaxe**

    ```python
    set(<lista>)
    ```

  * **Exemplo**

    ```python
    lista_animais = ["cachorro", "cachorro", "gato", "gato", "elefante"]
    conjunto_animais = set(lista_animais)
    print(conjunto_animais) # {'gato', 'cachorro', 'elefante'}
    ```

* **Converter um conjunto para lista**

  * **Sintaxe**

    ```python
    list(<conjunto>)
    ```

  * **Exemplo**

    ```python
    conjunto_animais = {"gato", "cachorro", "elefante"}
    lista_animais = list(conjunto_animais)
    print(lista_animais) # ['gato', 'cachorro', 'elefante']
    ```