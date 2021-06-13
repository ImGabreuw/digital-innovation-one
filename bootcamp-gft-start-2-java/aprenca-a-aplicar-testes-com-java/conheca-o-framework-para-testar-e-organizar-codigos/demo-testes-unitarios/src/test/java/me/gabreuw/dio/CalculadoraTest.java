package me.gabreuw.dio;

import org.junit.Assert;
import org.junit.Test;

public class CalculadoraTest {

    @Test
    public void testSomar() {
        var calculadora = new Calculadora();

        int soma = calculadora.somar("1+1+3");

        Assert.assertEquals(5, soma);
    }

}
