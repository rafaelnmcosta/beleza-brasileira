import sqlite3
from cliente import Cliente


# Função que abre a conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Função que recebe um objeto cliente e o adiciona ao banco de dados
def addCliente(novo_cliente):
    conn = get_db_connection()
    conn.execute('INSERT INTO users'
        '(nome, endereco, telefone, ref, senha, tipo, cpf_cnpj, descricao)'
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        (novo_cliente.nome, novo_cliente.endereco, novo_cliente.telefone, novo_cliente.ref, novo_cliente.senha, novo_cliente.tipo, novo_cliente.cpf_cnpj, novo_cliente.descricao)
    )
    conn.commit()
    conn.close()
    return True

# Função que busca uma ref, instancia um objeto cliente com as informações e retorna esse objeto
def getCliente(ref_cliente):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE ref = ?', (ref_cliente))
    conn.close()
    if user is None:
        abort(404)
        return False
    else
        cli = Cliente(user)
        return cli


def deleteCliente(ref_cliente):
    cli_del = getCliente(ref_cliente)
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE ref = ?', (ref,))
    conn.commit()
    conn.close()
    return cli_del

def listClientes():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    clientes = []
    for user in users:
        cli_atual = Cliente(user)
        clientes.append(cli_atual)
    return clientes


def updateCliente():
    


