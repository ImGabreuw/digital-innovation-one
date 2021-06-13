package me.gabreuw.dio;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CalculadoraTDDTest {

    @Test
    public void deveSomarDoisValores() {
        var calculadora = new CalculadoraTDD();

        int numero1 = 1;
        int numero2 = 2;

        int soma = calculadora.somar(numero1, numero2);

        assertEquals(3, soma);
    }

}
