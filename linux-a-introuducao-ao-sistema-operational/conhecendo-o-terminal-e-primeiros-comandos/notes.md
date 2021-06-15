# Conhecendo o terminal e primeiros comandos

### Terminal

> Terminal = Shell = Console

* Execução de programas específicos do Linux através da linha de comando

* A maioria dos comandos são iguais em diversas distribuições

* Uso para automação de processos através dos comandos

* Formas para acessar o terminal

  * **Atalho** = `CTRL + ALT + T`

  * Atividades > Digite: `Terminal` > botão direito no ícone do terminal 

  * Na doca > botão direito em `Mostrar aplicativos` > Digite: `Terminal` > botão direito no ícone do terminal 

  * `/` ou `~` = diretório raíz do sistema operacional

### Comandos do terminal

* `$ pwd` = caminho atual

* `$ ls` = listar diretórios e arquivos do diretório atual

* `$ ls <nome do diretório>`

  * listar diretórios e arquivos do diretório passado como argumento

  * Exemplo: `$ ls ~/Documentos`

* `$ ls -l`

  * listar, com detalhes, diretórios e arquivos do diretório atual

  * **Detalhes de diretório/arquivo** 

    * horário/dia/mês/ano de criação

    * Tamanho

    * Privilégios (Restrições)

    * 

  * Exemplo: `$ ls -l`

* `$ cd <nome do diretório>`

  > **cd** = (C)hange (D)irectory 

  * mudar de diretório

  * Exemplo: `$ cd ~/Documentos`

* `$ cd ..`

  * mudar para o diretório anterior

  * Exemplo: `$ cd ..`

* `$ mkdir <nome do diretório>`

  > **mkdir** = (M)a(K)e (DIR)ectory

  * Criar um diretório

  * Exemplo: `$ mkdir ~/Teste`

* `$ man <comando>`

  * Visualizar o manual de um comando, em inglês

  * Exemplo: `$ man ls`

* `$ <comando> --help`

  * Visualizar o manual de um comando, em português

* `$ history`

  * Visualizar o histórico de todos os programas e comandos utilizados no terminal

  > `$ !!` = executa o último comando do histórico do terminal