# Trabalhando com o GitHub

### Outros comandos Git

* Listagem das configurações do Git na maquina local: `$ git config --list`

* Alteração no email configurado no Git: 
  * `$ git config --global --unset user.email`
  * `$ git config --global user.email "seuemail@gmail.com"`

* Alteração no nome configurado no Git: 
  * `$ git config --global --unset user.name`
  * `$ git config --global user.email SeuNome`

### Salvando repositório no GitHub

* Configuração do repositório remoto: `$ git remote add origin <link do repositório remoto>`

* Listagem dos repositórios remotos: `$ git remote -v`

* "Empurra" os **commits** para o repositório remoto: `$ git push -u origin master`
  > **master** = _branch_ padrão do GitHub