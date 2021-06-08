# Lambda no Java

### Lambda

* Obedecem o conceito do paradigma funcional

* Facilitam a leitura do código

* Com a nova API Funcional do Java, houve um grande aumento na produtividade para lidar com objetos 

* Interfaces funcionais

  * São interfaces que possuem apenas um método

  * São anotadas, em nível de classe, com a anotação `@FuncionalInterface`

    * Essa anotação serve para validar se a interface, com `@FuncionalInterface` atende as regras de uma interface funcional.

    > O uso da `@FuncionalInterface` é optional, uma vez que o compilador pode inferir isso

  * Antes do Java 8, a implementação de um comportamento específico era feito a partir de uma **classe anônima** (código poluído)

  * Estrutura de uma lambda

    ```java
    InterfaceFuncional variável = parâmetro -> lógica;
    ```

    * Lambdas com apenas uma instrução, o uso de chaves é opcional
        
      * Exemplo:

        ```java
        InterfaceFuncional saudacao = nome -> "Olá " + nome;
        ```

    * Lambdas com mais de 1 instrução, o uso de chaves e `return` é obrigatório

      * Exemplo:

        ```java
        InterfaceFuncional saudacao = nome -> {
          String concatenacaoComNome = "Olá " + nome;
          String concatenacaoComPontoFinal = concatenacaoComNome + ".";

          return concatenacaoComNome;
        }
        ```