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
        (novo_cliente.nome, novo_cliente.endereco, novo_cliente.telefone, novo_cliente.ref, novo_cliente.senha, novo_cliente.tipo, novo_cliente.cpf, None)
    )
    conn.commit()
    conn.close()
    return True

# Função que busca uma ref, instancia um objeto cliente com as informações e retorna esse objeto
def getCliente(ref_cliente):
    conn = get_db_connection()
    cliente = list(conn.execute('SELECT * FROM users WHERE ref = ?', (ref_cliente,)).fetchone())
    conn.close()
    if cliente is None:
        #abort(404)
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

#Função que deleta um registro do banco de dados de acordo com a referencia informada
def deleteCliente(ref_cliente):
        cli_del = getCliente(ref_cliente)
        if(cli_del):
            conn = get_db_connection()
            conn.execute('DELETE FROM users WHERE ref = ?', (ref_cliente,))
            conn.commit()
            conn.close()
            return cli_del.nome
        else:
            return False

#Função que instancia um objeto para cada cliente no banco de dados e os coloca em uma lista, depois retorna essa lista
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

#Função que recebe um objeto cliente e uma string ref, e altera no BD, na linha da ref,
# os dados de acordo com as informações do objeto passado como parâmetro 
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