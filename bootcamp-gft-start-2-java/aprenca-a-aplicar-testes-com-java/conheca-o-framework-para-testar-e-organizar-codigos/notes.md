# Conheça o framework para testar e organizar códigos

### Objetivos

- [X] Conceitos de JUnit 4

- [X] Asserts

- [X] Rules

- [X] Testando exceções

### Conceitos de JUnit 4

* Framework simple e Open Source

* Testes unitários = testar uma única funcionalidade/método

* Organização do código

  * cada classe Java deve ter uma classe de teste correspondente

  * **Maven** facilita os teste unitários, pois existe um arquitetura que divide o ambiente de teste e de código

* Testar sempre

* **Asserts**

  * Para validação dos teste unitários é utilizado os **Asserts**

  * Verificar se um resultado coincide com o esperado, em um ponto de execução do código

  * Assertions para tipos primitivos, Objetos e Arrays

  * **Import static**

  * Ordem dos parâmetros (valor esperado, depois o valor atual)

* **Rules** 

  * É um componente que intercepta um chamada para um método teste que permite que façamos ao antes ou após o método rodar

  * Todas as classes do JUnit 4 implementam a interface **TestRule**

  * Utilidades

    * Criar arquivos/diretórios que serão deletados após o método ser executado

    * Configurar um recurso externo (**Socket** / conexão com bando de dados)

* Testando exceções

  * Exceções esperadas

    * Exemplo

      ```java
      @Test(expected = IndexOutOfBoundsException.class)
      public void empty() {
          new ArrayList<>().get(0); // Lança: IndexOutOfBoundsException 
      }
      ``` 

  * Exceções esperadas **Rule**

    * Exemplo

      ```java
      @Rule
      public ExpectedException expectedException = ExpectedException.none();

      @Test
      public void shouldTestExceptionMessage() {
        var list = new ArrayList<>();

        expectedException.expect(IndexOutOfBoundsException.class);
        expectedException.expectMessage("index 0 out of bounds for length 0");

        list.get(0);
      }
      ```

  * Try/Catch idiom

    * Exemplo

      ```java
      @Test 
      public void testExceptionMessage() {
          try {
              new ArrayList<>().get(0);
              fail("Esperado que IndexOutOfBoundsException seja lançado");
          } catch (IndexOutOfBoundsException e) {
              assertThat(e.getMessage(), is("Index 0 out of bounds for length 0"));
          }
      }
      ```

* Executar todos os testes do projeto com Maven

  * Maven > nome_do_projeto > Lifecycle > install (build do projeto + testagem do código)