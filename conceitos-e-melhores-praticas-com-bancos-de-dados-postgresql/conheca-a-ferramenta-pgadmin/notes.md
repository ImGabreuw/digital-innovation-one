# Conheça a ferramenta PGAdmin

## Objetivos

- [X] Visão geral do PGAdmin4
- [X] Configurar acesso ao servidor PostgreSQL
- [X] Visão geral do cluster e novo primeiro comando

### Configurações para o PGAdmin

* Importante para conexão

  * Liberar acesso ao cluster em `postgresql.conf`

    * Trocar `localhost` por `*` no parâmetro `listen_addresses`
    * Salvar e sair: `$ :wq!`

  * Liberar acesso ao cluster para o usuário do banco de dados em `pg_hba.conf`

  * Criar/editar usuários

* Conectar ao servidor

  * `$ psql -h <host> -p <porta> -U <usuário> <banco de dados>`

  > Os valores padrão para o esses parâmetro são os seguintes: `$ psql -h 127.0.0.1 -p 5432 -U postgres`. O PostgreSQL pegará o banco de dados conectado ao usuário

* Edição do do arquivo `pg_hba.conf`

  * Definir uma senha: `$ ALTER USER postgre PASSWORD '123';`

  * Sair do PostreSQL: `$ \q` 

  * Abrir o arquivo `pg_hba.conf`: `$ vi /etc/postgresql/11/aula/pg_hba.conf`

  * Alterar método de senha

    * Caso não for um servidor de desenvolvimento

      * Alterar o parâmetro `METHOD` do `TYPE` da conexão **host** para `md5`

    * Caso for um servidor de desenvolvimento

      * Alterar o parâmetro `METHOD` do `TYPE` da conexão **local** para `md5`

### PGAdmin

* Criar um _Server Group_ (Grupo de servidores):

  * `Server > botão esquerdo > Server Group`

  * Informar o **name** desse grupo de servidores. Exemplo: `aula`

* Criar um _Server_ (Servidor)

  * `Server > botão esquerdo > Server`

  * Informar o **name**, **server group**, **comments**

    > A adição do comentário é um boa prática. Nela é importante colocar informações (propósito/funções) sobre o banco de dados.