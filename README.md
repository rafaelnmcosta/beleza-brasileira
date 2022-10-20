# Beleza Brasileira

## Informações
É um projeto com o objetivo de criar um sistema que conecte clientes e estabelecimentos de beleza/estética, facilitando
o processo de agendamento e realização de serviços.<br>
É escrito em python com foco para a Programação Orientada a Objetos, utilizando flask, banco de dados SQLite e Bootstrap, utilizando o padrão de projeto de software MVC.<br>
Este projeto está sendo desenvolvido pelos alunos: Rafael(CC), Isadora(IA), Alerhandra(IA) e Evellyn(IA).<br>
O projeto é apenas básico para trabalhar 

## Estrutura do projeto
** Raíz do projeto
Possui todas as pastas do projeto, um arquivo gitignore e um README.<br>
O arquivo teste.py não possui uso direto e é apenas vestígio dos testes do programa.
**O arquivo init.db cria o banco de dados, que será chamado por padrão "database.db"**
O arquivo schema.sql define os parâmetros das tabelas do banco de dados
	++ *A pasta ".idea" foi criada automáticamente pela IDE utilizada por alguns colaboradores, não apresentando efeitos no projeto total.*

	++ Pasta View
Guarda os arquivos html da interface do programa.

	++ Pasta Model
Guarda os arquivos de modelos de classes, que definem os objetos instanciados na execução do programa.
O arquivo utils.py foi apenas usado durante testes para facilitar o acompanhamento do desenvolvimento do programa, e não tem efeito na versão publicada.

	++ Pasta DAO
Guarda os arquivos de classes que geram objetos capazes de controlar o banco de dados.

	++ Pasta Beleza-brasileira
Foi criada automaticamente pelo pip e foi commitada por erro, é relativa ao VirtualEnv e não apresenta problemas quando um novo ambiente virtual é criado

	++ Pasta Controller
Guarda o arquivo principal do programa, que possui as funções do flask e todas as regras de negócio a serem utilizadas ao longo da execução.

## Instalação e execução
*Por ser apenas um projeto com foco em praticar técnicas de programação orientada a objetos, o programa só foi preparado para rodar em servidor local com banco de dados simples, sem segurança efetiva.*
### Versões utilizadas no teste mais recente do programa:
	
	++ Python versão 3.10 - Linguagem e interpretador do projeto
	++ Pip versão 22.2.2 - Gerenciador de pacotes
	++ Flask versão 2.2.2 - Framework web
	++ Werkzeug versão 2.2.2 - Lib usada para uso de mensagens de aviso no aplicativo

### Configuração do ambiente
	++ Primeiramente deve-se criar um novo ambiente virtual através do comando `python3 -m venv venv`, que criará uma pasta chamada "venv" na raíz do projeto, onde o pip armazenará as ferramentas instaladas. <br>
	++ Em seguida se ativa o ambiente virtual com o comando `source venv/bin/activate`
	++ Realiza a instalação do flask através do comando `pip install flask`
	++ Na raíz do projeto, inicia-se o banco de dados com o comando `python3 init_db.py` - *(Obs: caso esse comando seja executado novamente, todo registro no banco dados será APAGADO e ele será reiniciado aos registros básicos definidos no arquivo "init_db.py")*

### Execução
	Com o ambiente configurado, basta acessar a pasta Controller e executar o comando `python3 app.py`

