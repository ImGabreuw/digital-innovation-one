# Spring Boot

### O que é?

* Criado pela Spring Source em 2012.
* Necessidade de uma ferramenta de que facilitaria todo o setup e configuração de projetos Spring.
* Principal objetivo: facilitar setup de projetos Spring
* Sem necessidade de criar arquivos de configuração
* Foco em produtividade.
* Maior tempo de desenvolvimento de valor

### Quais os problemas do Spring?

* Configurações de beans em arquivos `.xml`.
* Dispatcher Servlet e view resolver em web.xml.
* Setup manual de bancos de dados.
* Muito tempo gasto em configurações.
* Perda de foco em valor (entrega de projetos)

### Quais problemas o Spring Boot Resolve?

* Produtividade: setup simplificado de projeto (Spring Initializr)
* Starters: dependências auto configuráveis pelo Spring Boot. Exemplo: spring-boot-starter-web
* Execução simplificada: sem deploy em servidor externo
* Configuração: arquivo externo para configuração, como por exemplo o arquivo `application.yml` ou `application.properties` onde é feito a configuração de banco de dados, segurança, log, etc
* Valor: maior tempo em desenvolvimento

### Checklist

- [ x ] Criação de um projeto no site https://start.spring.io/
- [ x ] Importar o projeto no Intellij IDEA
- [ x ] Adicionar spring-boot-starter-mvc no pom.xml
- [ x ] Adicionar classe HelloController e o método `hello()`
- [ x ] Executar o projeto através do terminal 

### Como executar um projeto Spring a partir do terminal

* No diretório do projeto execute o seguinte comando:

  ```cmd
  > mvn spring-boot:run
  ```