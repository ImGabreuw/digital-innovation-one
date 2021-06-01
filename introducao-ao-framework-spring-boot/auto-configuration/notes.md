# Auto Configuration

### Configuração manual

* Mútiplos arquivos XML
* Configuração manual do Spring MVC: Dispatcher Sevlet, web.xml, spring-mvc.xml
* Configuração manual dos beans Spring
* Aplicado também ao Spring Data, SPring Security, etc

### Auto configuration

* Staters: dependências simplificadas e auto configuráveis

  ```xml
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-test</artifactId>
      <scope>test</scope>
    </dependency>
  </dependencies>
  ```

* Identificação e configuração automática da dependência

* Spring Boot detecta as dependências e configura para nós

* Projeto simplicado e pronto para desenvolvimento

### Checklist

- [ ] Adicionar propriedade`debug=true` no `application.properties`
- [ ] Executar projeto no terminal e analisar o log
- [ ] Identificar e visualizar o auto configuration do Spring MVC
- [ ] Visualizar a dependências do auto configuration do projeto

