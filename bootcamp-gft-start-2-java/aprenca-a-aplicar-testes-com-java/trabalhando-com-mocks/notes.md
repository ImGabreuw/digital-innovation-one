# Trabalhando com Mocks

### Objetivos

- [X] O que são Mocks

- [X] Frameworks

    * Mockito
    * EasyMock
    * PowerMockito

- [X] Exemplo com Mockito

### Mocks

* Objeto Mock, Objeto simulado ou Mock = são objetos que simulam comportamentos de objetos reais

### Frameworks

* Mockito = mais utilizado para fazer testes unitários

* PowerMockito = é uma extensão da API do Mockito


### Exemplo (Mockito / JUnit 4)

```java
@Test
public void testeSomarComMock() {
    // Mockit
    Calculadora calculadora = mock(Calculadora.class);

    when(calculadora.somar("1+2")).thenReturn(10);

    // JUnit 4
    int resultado = calculadora.somar("1+2");

    assertEquals(10, resultado);
}
```