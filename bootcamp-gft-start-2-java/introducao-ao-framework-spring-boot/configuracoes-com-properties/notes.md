# Configurações com Properties

### Configuração do banco de dados e **Profiles**

* **OBS**: Caso nenhum **Profile** for informado no `application.properties`, o Spring usará o perfil padrão, ou seja, pegará todas as configurações contidas no `application.properties`

### Checklist

- [X] Projeto com [spring.initializr](https://start.spring.io/) e importar na IDE
- [X] Arquivos application.properties para dev e prod
- [X] Classe de configuração de BD e anotar com `@Configuration`
- [X] Mapear propriedades com `@ConfigurationProperties`
- [X] Criar métodos para instanciar `@Bean` de cada env
- [X] Criar classe anotada com `@RestController`
- [X] Injetar propriedade appMessage com `@Value`
- [X] Criar método que retorna mensagem acima
- [X] Executar projeto no browser