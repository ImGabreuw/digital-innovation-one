# Entenda o que é Paradigma Funcional

### Paradigma Funcional no Java

* Processo de construir software através de composição de funções puras 

* Principais características

  * Evita compartilhamento de estados

  * Dados imutáveis

  * Sem efeitos colaterais

  * Paradigma Declarativa, ou seja, respeita ordens (Definição de Eric Elliott) 

    * Paradigma Imperativo (padrão do Java)

      * Expressa o código através de comandos ao computador, nele é possível ter controle de estado dos objetos

      * Exemplo

        ```java
        class Imperativo {
          public static void main(String[] args) {
            int valor = 10;
            int resultado = valor * 3;

            System.out.println("O resultado é :: " + resultado);
          }
        }
        ```
* Damos um regra/declaração de como queremos que o programa se comporte

* Exemplo

  ```java
  class Funcional {
    public static void main(String[] args) {
      UnaryOperator<Integer> calcularValorVezes3 = valor -> valor * 3;
      int valor = 10;

      System.out.println("O resultado é :: " + calcularValorVezes3.apply(10));
    }
  }
  ```