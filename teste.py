from Model.cliente import Cliente
from DAO.clienteDAO import ClienteDAO
from DAO.baseDAO import BaseDAO

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

#---------------------------------------------------------------------------------------------------#

novoDAO = ClienteDAO('database.db')

print("\nLista de cliente no inicio:")
listaCli = novoDAO.list_clientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)


novoCli2 = Cliente("Cliente 2", "endereco 2", "telefone 2", "cliente2", "12345", "cliente", "cpf-novo-2")
novoCli3 = Cliente("Cliente 3", "endereco 3", "telefone 3", "cliente3", "12345", "cliente", "cpf-novo-3")

novoDAO.add_cliente(novoCli2)
novoDAO.add_cliente(novoCli3)

print("\nlista com clientes adicionados")
listaCli = novoDAO.list_clientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)

cli_editado = Cliente("Cliente 3 v2", "endereco 3 v2", "telefone 3 v2", novoCli3.ref, "12345", "cliente", "cpf-novo-3 v2")
novoDAO.update_cliente(novoCli3.ref, cli_editado)

print("\nlista com o cliente alterado:")
listaCli = novoDAO.list_clientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)

print("\n")
print("O ", novoDAO.delete_cliente(novoCli2.ref), " foi deletado")
print("O ", novoDAO.delete_cliente(novoCli3.ref), " foi deletado")

print("\nLista no fim do programa")
listaCli = novoDAO.list_clientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)

print("\nLista de todos os usuarios:")
lista_users = novoDAO.list_all_users()
for user in lista_users:
        print(user.nome)
        print(user.tipo)