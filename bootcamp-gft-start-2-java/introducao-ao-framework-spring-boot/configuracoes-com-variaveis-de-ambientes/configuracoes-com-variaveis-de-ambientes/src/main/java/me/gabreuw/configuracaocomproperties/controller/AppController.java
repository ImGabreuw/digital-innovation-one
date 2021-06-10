package me.gabreuw.configuracaocomproperties.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AppController {

    @Value("${app.message}")
    private String appMessage;

    @Value("${ENV_DB_URL:NENHUMA}")
    private String dbEnvironmentVariable;

    @GetMapping(path = "/")
    public String getAppMessage() {
        return appMessage;
    }

    @GetMapping(path = "/env-variable")
    public String getEnvironmentVariable() {
        return "A seguinte variável de ambiente foi passada: " + dbEnvironmentVariable;
    }

}
