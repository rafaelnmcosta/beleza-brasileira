# Projeto POO

## Informações
Este projeto está sendo desenvolvido pelos alunos: Rafael(CC), Isadora(IA), Alerhandra(IA) e Evellyn(IA) com o objetivo de  estudar técnicas de programação orientada a objetos em Python.

## Estrutura de classes do programa
Classe: Usuário

- Nome
- Endereço
- Telefone
- ID (uma string ou um número único pra identificar igual @ de rede social)
- Senha
- Tipo (Cliente ou Loja)

+ addNome()
+ addEndereco()
+ addTelefone()
+ addID()
+ addSenha()
_______
Classe: Cliente
Herda Usuário

- CPF
- Lista de serviços

+ addCPF
+ solicitaServico() -cria uma solicitação de um serviço em determinado horário pra um estabelecimento
+ cancelaSolicitacao() -cancela a solicitação feita
_______
Classe: Estabelecimento
Herda Usuário

- CNPJ
- Tipo de estabelecimento
- Calendário de serviços (uma lista com serviços marcados e respectivos horários)
- Lista de solicitações (Lista com as solicitações de serviços feitas por clientes)

+ addCNPJ()
+ addTipo()
+ addCalendario()
+ addSolicitacoes()
+ aceitaServico() -adiciona um serviço na lista do estabelecimento e do cliente, torna o horário ocupado
+ cancelaServico() -remove o serviço da lista do estabelecimento e do cliente, torna o horário livre
+ mostraHorariosLivres() -dá uma lista dos horários livres dentro do dia informado