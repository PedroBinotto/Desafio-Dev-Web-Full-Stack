# Desafio Dev Web Full Stack @ Laboratório Bridge
### CTC | UFSC

### Introdução/Apresentação

**Seja bem vindo!**

Este repositório é a minha solução para o Desafio Dev Full Stack do processo seletivo dos laboratórios Bridge. Trata-se de um *WebApp* que calcula todos os números primos dentro dos limites informados pelo usuário através de um formulário.
O aplicativo também mantém um histórico dos valores informados em uma base de dados no servidor, registrando os dados informados e a Data/Hora em que foi feito.

Demonstração em servidor [Heroku](https://des-fullstack.herokuapp.com/)

### Especificações

O Backend do aplicativo é escrito em Python3 utilizando a framework web [Flask](https://flask.palletsprojects.com/en/1.1.x/) para construção de rotas e *templating* das páginas, e as extenções [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) e [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) para integração de bancos de dados e modelagem de formulários, respectivamente.
As bases de dados do aplicativo são gerenciadas pelo banco MariaDB/MySQL (ambos são compatíveis) e conectadas ao aplicativo utilizando as bibliotecas PyMySQL e SQLAlchemy.

No Frontend, foi utilizada a framework [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) para os temas pré definidos (HTML+CSS) e a funcionalidade de layout adaptável (*responsive design*) para displays de tamanhos variáveis.
 
### Instalação/Execução Local
> OBS.: Detalhes da instalação previstos para um ambiente **Linux**, como foi utilizado no desenvolvimento do projeto.

Antes de qualquer outra coisa, fazer o download/clonar repositório para sua máquina e extrair os arquivos.

##### Configurando um Ambiente Virtual

Quando trabalhando com aplicações em Python, é uma prática comum a utilização de Ambientes Virtuais (Virtual Environments) para que se possa fazer a correta configuração do intérprete Python e o gerenciamento de pacotes (bibliotecas).

Para a configuração do ambiente virtual:
* Certifique-se de que possui o **pip** instalado em seu sistema executando `pip -h` em seu terminal.
  * Se o terminal exibir o texto de ajuda do pip, então você já possui a ferramenta instalada.
  * Caso contrário, [instale o pip em seu sistema](https://pip.pypa.io/en/latest/installing/).
* Instale a ferramenta de ambientes com o comando `pip install virtualenv`
* Em seguida, crie um ambiente Python3 para a execução do aplicativo com `virtualenv -p python3 nomeDoSeuAmbiente`
* Para ativar o ambiente, execute o comando `source nomeDoSeuAmbiente/bin/activate`
* Quando desejar desativa-lo, simplesemente execute `deactivate`

##### Instalação das Dependências

Após a configuração de seu ambiente virtual, será necessário instalar os pacotes utilizados pelo aplicativo em sua máquina. Para isso, foi criado o arquivo 'requirements.txt' na raíz do repositório.

Para a instalação dos pacotes:
* Certifique-se de estar dentro do seu ambiente virtual; caso não esteja, execute `source nomeDoSeuAmbiente/bin/activate`
* Navegue até a localização de 'requirements.txt', no diretório onde tiver extraído os arquivos do repositório.
* Execute `pip install -r requirements.txt` e aguarde a instalação dos pacotes.

##### Instalação do Gerenciador de Bancos de Dados

O aplicativo conta com a função de registro dos dados informados, e para isso utiliza uma base de dados locais. Para isso, é necessário que haja um gerenciador de bancos de dados instalado no sistema. No desenvolvimento do projeto, foi utilizado o banco [**MariaDB**](https://mariadb.org/), mas também pode ser executado com **MySQL**. 

Para a instalação do gerenciador MariaDB:
* Atualize seu índice de pacotes (`sudo apt update`)
* Após atualizar a lista de pacotes, instale o gerenciador com o comando `sudo apt install mariadb-server`
* Aguarde o tempo de instalação e verifique com `sudo systemctl status mariadb` ou cheque a versão com `mysql -V`

##### Configurações do Banco de Dados

Para que o aplicativo possa comunicar-se corretamente com o Banco de Dados, é necessario configurar este antes de executar o código.

Para a configuração do MariaDB:
* Certifique-se de que o gerenciador está instalado corretamente com `mysql -V`
* Execute o comando `sudo mysql_secure_installation`
* Defina a senha de administrador do Banco quando receber o prompt no terminal.

Após definir os dados de administrador do banco, conecte-se através do terminal para configurar a base de dados que será utilizada pelo aplicativo.
* Execute `mysql -u root -p` e informe sua senha quando for requisitado.
* No desenvolvimento do aplicativo, foi utilizada uma base de dados declarada 'app', mas pode ser utilizado o nome que for desejado.
* Para criar a base de dados, execute `CREATE DATABASE nomeDeSuaBaseDeDados`
* Digite `exit` para sair do gerenciador.

##### Exportando Variáveis de Ambiente/ Configuração do Aplicativo

Para garantir maior segurança do aplicativo, é uma boa prática manter dados específicos de configuração armazenadas como variáveis de ambiente, e não escritas diretamente no código-fonte. No respositório, aplicativo está configurado para importar estas configurações. Caso hajam complicações para configurar variáveis de sistema, pode ser rapidamente reconfigurado para operar com as informações escritas diretamente no arquivo **flaskapp/config.py**.

Para configurar as variáveis de sistema:
* Em seu diretório *home* (/home/nomeDeUsuaio/) abra um terminal.
* Execute o comando `ls -al`, para listar todos os arquivos no diretório.
* Você deverá encontrar o arquivo **.bash_profile** em meio a essa lista.
* Abra o arquivo com um editor de texto de sua escolha.
* Para adicionar a variável de configuração:
  * Adicione ao final do arquivo o código `export DATABASE_URL="mysql+pymysql://root:senhaDoBancoDeDados@localhost/nomeDaBaseDeDados"`
  * Salve as modificações e saia do editor.

**Alternativamente**;

Para executar o aplicativo **SEM variáveis de ambiente** (menos seguro):
* Navegue até o diretório onde extraiu os arquivos do aplicativo.
* Acesse o diretório '**flaskapp**'
* Localize o arquivo de configuração '**config.py**' e abra em um editor de texto de sua escolha.

Você deverá encontrar o seguinte código:

```python

import os
import pymysql

class Config:
	# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:senha@localhost/app'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

```

Para reconfigurar o aplicativo, basta remover a linha de código **06** e "*descomentar*" a linha **05**, substituindo sua senha e nome da base de dados.

##### Importando os Modelos de BD

Para configurar as tabelas do seu banco de dados, será necessário importar os modelos do aplicativo. Para fazer isso, navegue até o diretório raíz do aplicativo e, dentro do ambiente virtual do projeto, execute a seguinte sequência de comandos:

```
$ python
$ from flaskapp import create_app, db
$ app = create_app()
$ from flaskapp.models import *
$ with app.app_context():
$     db.create_all()
$ exit()
```

**Finalmente**,

##### Executando o Aplicativo

Após realizar toda a configuração, para executar o aplicativo deve-se ativar o Ambiente Virtual e, no diretório raíz do aplicativo, executar o comando `python run.py`

