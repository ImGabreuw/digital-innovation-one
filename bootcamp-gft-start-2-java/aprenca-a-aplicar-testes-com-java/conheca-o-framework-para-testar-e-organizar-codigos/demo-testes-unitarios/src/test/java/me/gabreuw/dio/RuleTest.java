package me.gabreuw.dio;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;

import java.io.IOException;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class RuleTest {

    @Rule // Criação do diretório antes da execução do teste
    public TemporaryFolder temporaryFolder = new TemporaryFolder();

    @Test
    public void shouldCreateNewFileInTemporaryFolder() throws IOException {
        var createdFile = temporaryFolder.newFile("file.txt");

        assertTrue(createdFile.isFile());
        assertEquals(temporaryFolder.getRoot(), createdFile.getParentFile());
    }


}
