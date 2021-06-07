# Funções e imutabilidade em Paradigma Funcional

### Conceitos fundamentais da programação funcional

* Composição de funções

  * Criar uma nova função através da composição de outra

  * Exemplo: 

    * Problema: Criar uma função que vai filtrar um Array, filtrando somente os números pares e multiplicando por dois

    * Resolução com Paradigma Funcional

      ```java
      class ComposicaoDeFuncoes {
        public static void main(String[] args) {
          int[] valores = {1, 2, 3, 4};

          Array.stream()
              .filter(numero -> numero % 2 == 0)
              .map(numero -> numero * 2)
              .forEach(System.out::println);
        }
      }
      ```

    * Resolução com Paradigma Imperativo

      ```java
      class ComposicaoDeFuncoes {
        public static void main(String[] args) {
          int[] valores = {1, 2, 3, 4};

          for (int i = 0; i < valores.length; i++) {
            int valor = 0;

            if (valores[i] % 2 == 0) {
              valor = valores[i] * 2;
              System.out.println(valor);
            }
          }
        }
      }
      ```

* Funções puras

  * São funções que retornam o mesmo resultado, independentemente do número de chamadas (**sem tem efeito colateral**)

  * Exemplo

    ```java
    class FuncoesPuras {
      public static void main(String[] args) {
          BiPredicator<Integer, Integer> verificarSeEMaior = (valor1, valor2) -> valor1 > valor2;

          System.out.println(verificarSeEMaior.test(13, 12)); // true
          System.out.println(verificarSeEMaior.test(13, 12)); // true
      }
    }
    ```

* Imutabilidade

  * Valor de uma variável/objeto, uma vez atribuída, seu valor não pode ser modificada

  * Exemplo

    ```java
    class Imutabilidade {
      public static void main(String[] args) {
          int valor = 20;
          UnaryOperator<Integer> retornarDobro = valor -> valor * 2;

          System.out.println(retornarDobro.apply(valor)); // 40
          System.out.println(valor); // 20
      }
    }
    ```