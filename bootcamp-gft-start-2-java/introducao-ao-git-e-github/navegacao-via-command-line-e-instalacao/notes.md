# Comandos básicos para um bom desempenho no terminal

### GUI VS CLI

* GUI = (G)raphical (U)ser (I)nterface
* CLI = (C)ommand (L)ine (I)nterface

### Comandos básicos

* Windows

  * Mudar de diretório: `> cd`
    * Mudar para o diretório **HOME**: `> cd /`
    * Voltar um diretório: `> cd ..` 

  * Listar as pastas: `> dir`

  * Criar diretórios / arquivos:
    * Criar diretório: `> mkdir Projects`
    * Criar arquivo: `> echo hello > hello.txt`
      > `>` = redirecionador de fluxo
      
  * Deletar diretórios / arquivos:
    * Deletar diretório: `> rmdir Projects`
      > **rmdir** = (R)e(m)ove (DIR)etory
    * Deletar arquivo(s): `> del Projects`
      * Deletar todos os arquivos presente no diretório `Projects`
      > `> del` só funciona para arquivos

  * Limpar tela do terminal: `> cls`
    > **cls** = (C)(l)ear (S)creen

  * Autocomplete
    > **Atalho**: TAB

  * Visualizar o histórico de comandos utilizados
    > **Atalho**: SETA PARA CIMA / SETA PARA BAIXO

* Unix (MacOS / Linux)

  * Mudar de diretório: `$ cd`
    * Mudar para o diretório **HOME**: `$ cd /`
    * Voltar um diretório: `$ cd ..`  

  * Listar as pastas: `$ ls`

  * Criar pastas / arquivos:
    * Criar pasta: `$ mkdir Projects`
    * Criar arquivo: `$ echo hello > hello.txt`
      > `>` = redirecionador de fluxo

  * Deletar diretórios / arquivos:
    * Deletar diretório: `$ rm -rf Projects`
      * `-rf` = forçar a deleção de todos os subdiretórios do diretório `Projects`
      > **rm -rf** = (R)e(m)ove (R)ecursive (F)orce
    * Deletar arquivo(s): `> del Projects`
      * Esse comando deletará todos os arquivos presente no diretório `Projects`
      > `> del` só funciona para arquivos

  * Limpar tela do terminal: `$ clear`
    > **Atalho**: CONTROL + L

  * Autocomplete
    > **Atalho**: TAB

  * Visualizar o histórico de comandos utilizados
    > **Atalho**: SETA PARA CIMA / SETA PARA BAIXO
