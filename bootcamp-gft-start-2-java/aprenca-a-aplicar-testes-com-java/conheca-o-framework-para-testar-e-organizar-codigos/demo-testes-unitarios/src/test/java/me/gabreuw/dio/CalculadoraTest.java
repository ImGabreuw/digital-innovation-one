package me.gabreuw.dio;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class CalculadoraTest {

    @Test
    public void testSomar() {
        var calculadora = new Calculadora();

        int soma = calculadora.somar("1+1+3");

        assertEquals(5, soma);
    }

    @Test
    public void testeSomarComMock() {
        // Mockit
        Calculadora calculadora = mock(Calculadora.class);

        when(calculadora.somar("1+2")).thenReturn(10);

        // JUnit 4
        int resultado = calculadora.somar("1+2");

        assertEquals(10, resultado);
    }

}
