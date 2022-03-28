import sqlite3
from Model.cliente import Cliente
from DAO.clienteDAO import ClienteDAO


#---------------------------------------------------------------------------------------------------#
novoDAO = ClienteDAO('database.db')

print("\nLista de cliente no inicio:")
listaCli = novoDAO.listClientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)


novoCli2 = Cliente("Cliente 2", "endereco 2", "telefone 2", "cliente2", "12345", "cliente", "cpf-novo-2")
novoCli3 = Cliente("Cliente 3", "endereco 3", "telefone 3", "cliente3", "12345", "cliente", "cpf-novo-3")

novoDAO.addCliente(novoCli2)
novoDAO.addCliente(novoCli3)

print("\nlista com clientes adicionados")
listaCli = novoDAO.listClientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)

cli_editado = Cliente("Cliente 3 v2", "endereco 3 v2", "telefone 3 v2", novoCli3.ref, "12345", "cliente", "cpf-novo-3 v2")
novoDAO.updateCliente(novoCli3.ref, cli_editado)

print("\nlista com o cliente alterado:")
listaCli = novoDAO.listClientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)

print("\n")
print("O ", novoDAO.deleteCliente(novoCli2.ref), " foi deletado")
print("O ", novoDAO.deleteCliente(novoCli3.ref), " foi deletado")

print("\nLista no fim do programa")
listaCli = novoDAO.listClientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)
