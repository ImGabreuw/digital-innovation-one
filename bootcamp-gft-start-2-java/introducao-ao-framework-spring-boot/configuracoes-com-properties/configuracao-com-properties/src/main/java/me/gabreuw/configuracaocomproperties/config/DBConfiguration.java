package me.gabreuw.configuracaocomproperties.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

@Data
@Configuration // indicar como arquivo de configuração
@ConfigurationProperties("spring.datasource") // mapear todos as configurações com o caminho passado como argumento
public class DBConfiguration {

    private String driverClassName;
    private String url;
    private String username;
    private String password;

    @Profile("dev") // mapeamento das configurações do arquivo application-dev.properties
    @Bean // intanciar o método como um bean (instanciação será feita logo na subida da aplicação)
    public String testDatabaseConnection() {
        System.out.println("DB connection for DEV - H2");
        System.out.println(driverClassName);
        System.out.println(url);

        return "DB Connection to H2_TEST - Test instance";
    }

    @Profile("prod") // mapeamento das configurações do arquivo application-prod.properties
    @Bean
    public String productionDatabaseConnection() {
        System.out.println("DB Connection for Production - MySQL");
        System.out.println(driverClassName);
        System.out.println(url);

        return "DB Connection to MYSQL_PROD - Production instance";
    }
}
