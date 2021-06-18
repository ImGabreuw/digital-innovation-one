# Como criar um grupo e gerenciar os usuários

### Grupos

* Organizar os usuários

* Definir as permissões de acesso a arquivos e diretórios

* **Comandos**

  * Exibir todos os grupos do sistema: `$ cat /etc/group` ou `$ groups`

  * Adicionar um group (**apenas para usuário _root_**): `$ sudo addgroup <nome do grupo>`

  * Remover um grupo (**apenas para usuário _root_**): `$ sudo groupdel <nome do grupo>`

  * Adicionar um usuário a um grupo

    * `$ adduser <usuário> <grupo>` 

    * `$ gpasswd -a <usuário> <grupo>`