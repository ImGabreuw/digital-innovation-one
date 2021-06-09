package me.gabreuw.configuracaocomproperties.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AppController {

    @Value("${app.message}")
    private String appMessage;

    @GetMapping(path = "/")
    public String getAppMessage() {
        return appMessage;
    }

}
