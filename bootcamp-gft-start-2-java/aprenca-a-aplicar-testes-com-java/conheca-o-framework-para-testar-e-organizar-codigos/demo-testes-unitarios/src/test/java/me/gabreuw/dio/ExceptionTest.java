package me.gabreuw.dio;

import org.junit.Assert;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

import java.util.ArrayList;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.fail;

public class ExceptionTest {

    @Test(expected = IndexOutOfBoundsException.class)
    public void empty() {
//        Falha no teste unitário: Não ocorreu a exceção experada
//        var names = new ArrayList<String>(){{
//            add("Rodrigo");
//        }};
//
//        names.get(0);

//      Sucesso no teste unitário: a exceção experada foi lançada
        new ArrayList<>().get(0);
    }

    @Rule
    public ExpectedException expectedException = ExpectedException.none();

    @Test
    public void shouldTestExceptionMessage() {
        var list = new ArrayList<>();

        expectedException.expect(IndexOutOfBoundsException.class);
        expectedException.expectMessage("Index 0 out of bounds for length 0");

        list.get(0);
    }

    @Test
    public void testExceptionMessage() {
        try {
            new ArrayList<>().get(0);
            fail("Esperado que IndexOutOfBoundsException seja lançado");
        } catch (IndexOutOfBoundsException e) {
            assertThat(e.getMessage(), is("Index 0 out of bounds for length 0"));
        }
    }
}
