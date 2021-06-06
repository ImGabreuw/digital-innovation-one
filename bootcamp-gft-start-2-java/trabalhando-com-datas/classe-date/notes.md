# Classe Date

### Date (`java.util.Date`)

* A implementação do `java.util.Date` está na JDK desde a versão 1.0

* Algumas funcionalidades, atualmente, se tornaram obsoletas

* Construtores da **Classe Date**

  ![](./assets/construtores-classe-date.png)

  * Alguns desses construtores estão descontinuados (anotado com `@Deprecated`)

    ![](./assets/construtores-deprecated-classe-date.png)

  * Construtores mais utilizados

    ![](./assets/construtores-mais-utilizados-classe-date.png)

    * `Date()`

      * Este construtor vai alocar um objeto da classe Date

      * A inicialização dessa classe será o **milissegundo mais próximo** do período de sua execução

      * Exemplo

        ![](./assets/exemplo-construtor-sem-argumentos-classe-date.png)

    * `Date(long date)`

      * Este construtor espera como argumento o tempo no padrão epoch, em milissegundos

        > **epoch** = milissegundos deste `1 de janeiro de 1970 00:00:00` (data início do **Unix Epoch**)

      * `System.currentTimeMillis()` = método estático que retorna o milissegundos mais próximo de sua execução, com base no Sistema Operacional

      * Exemplo

        ![](./assets/exemplo-construtor-com-argumento-classe-date.png)

* Métodos da **Classe Date**

  * Métodos úteis

      ![](./assets/metodos-uteis-da-classe-date.png)

      * Exemplo `after(Date)` e `before(Date)`

        ![](./assets/metodo-after-before-classe-date.png)

      * Exemplo `compareTo(Date)` e `equals(Date)`

        ![](./assets/metodo-equals-compareto-classe-date.png)

      * Exemplo `from(Instant)` e `toInstant()`

        ![](./assets/metodo-toinstant-classe-date.png)

        * **Classe Instant**

          * Surgiu no JDK 1.8
          * Imutável e thread-safe
          * Modela um ponto instantâneo de uma linha do tempo
          * Indicado para gravar marcações temporais em eventos da sua aplicação

        