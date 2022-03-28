import sqlite3
from Model.cliente import Cliente

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def getCliente(ref_cliente):
    conn = get_db_connection()
    cliente = list(conn.execute('SELECT * FROM users WHERE ref = ?', (ref_cliente,)).fetchone())
    conn.close()
    if cliente is None:
        #abort(404)
        print('cliente nao existe')
        return False
    else:
        cli = Cliente(
                cliente[1],
                cliente[2],
                cliente[3],
                cliente[4],
                cliente[5],
                cliente[6],
                cliente[7]
                )
        return cli


def listClientes():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users WHERE tipo = "cliente"').fetchall()
    conn.close()
    clientes = []
    for user in users:
        user = list(user)
        cli_atual = Cliente(
                user[1],
                user[2],
                user[3],
                user[4],
                user[5],
                user[6],
                user[7]
                )
        clientes.append(cli_atual)
    return clientes


def deleteCliente(ref_cliente):
        cli_del = getCliente(ref_cliente)
        if(cli_del):
                conn = get_db_connection()
                conn.execute('DELETE FROM users WHERE ref = ?', (ref_cliente,))
                conn.commit()
                conn.close()
                return cli_del.nome
        else: return False


def addCliente(novo_cliente):
    conn = get_db_connection()
    conn.execute('INSERT INTO users'
        '(nome, endereco, telefone, ref, senha, tipo, cpf_cnpj, descricao)'
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        (novo_cliente.nome, novo_cliente.endereco, novo_cliente.telefone, novo_cliente.ref, novo_cliente.senha, novo_cliente.tipo, novo_cliente.cpf, None)
    )
    conn.commit()
    conn.close()
    return True


def updateCliente(ref_original, cli_alterado):
        conn = get_db_connection()
        conn.execute('UPDATE users SET nome = ?, endereco = ?, telefone = ?, ref = ?, senha = ?, cpf_cnpj = ?'
                        ' WHERE ref = ?',
                        (cli_alterado.nome,
                        cli_alterado.endereco,
                        cli_alterado.telefone,
                        cli_alterado.ref,
                        cli_alterado.senha,
                        cli_alterado.cpf,
                        ref_original
                        )
                )
        conn.commit()
        conn.close()
        return True


#---------------------------------------------------------------------------------------------------#
print("\nLista de cliente no inicio:")
listaCli = listClientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)


novoCli2 = Cliente("Cliente 2", "endereco 2", "telefone 2", "cliente2", "12345", "cliente", "cpf-novo-2")
novoCli3 = Cliente("Cliente 3", "endereco 3", "telefone 3", "cliente3", "12345", "cliente", "cpf-novo-3")

addCliente(novoCli2)
addCliente(novoCli3)

print("\nlista com clientes adicionados")
listaCli = listClientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)

cli_editado = Cliente("Cliente 3 v2", "endereco 3 v2", "telefone 3 v2", novoCli3.ref, "12345", "cliente", "cpf-novo-3 v2")
updateCliente(novoCli3.ref, cli_editado)

print("\nlista com o cliente alterado:")
listaCli = listClientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)

print("\n")
print("O ", deleteCliente(novoCli2.ref), " foi deletado")
print("O ", deleteCliente(novoCli3.ref), " foi deletado")

print("\nLista no fim do programa")
listaCli = listClientes()
for cli in listaCli:
        print(cli.nome)
        print(cli.cpf)
