import sqlite3

import sys
sys.path.insert(0, '../')

from Model.cliente import Cliente
from .baseDAO import BaseDAO

class ClienteDAO(BaseDAO):

    def __init__(self, param_database):
        super().__init__(param_database) #String que contém o nome do banco de dados que será acessado

    # Função que recebe um objeto cliente e o adiciona ao banco de dados
    def add_cliente(self, novo_cliente):
        conn = self.get_db_connection()
        conn.execute('INSERT INTO users'
            '(nome, endereco, telefone, ref, senha, tipo, cpf_cnpj, descricao)'
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (novo_cliente.nome, novo_cliente.endereco, novo_cliente.telefone, novo_cliente.ref, novo_cliente.senha, novo_cliente.tipo, novo_cliente.cpf, None)
        )
        conn.commit()
        conn.close()
        return True

    # Função que busca uma ref, instancia um objeto cliente com as informações e retorna esse objeto
    def get_cliente(self, ref_cliente):
        conn = self.get_db_connection()
        cliente = conn.execute('SELECT * FROM users WHERE ref = ?', (ref_cliente,)).fetchone()
        conn.close()
        if cliente is None:
            #abort(404)
            return False
        else:
            cliente = list(cliente)
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
    def delete_cliente(self, ref_cliente):
        cli_del = self.get_cliente(ref_cliente)
        if cli_del:
            conn = self.get_db_connection()
            conn.execute('DELETE FROM users WHERE ref = ?', (ref_cliente,))
            conn.commit()
            conn.close()
            return cli_del
        else:
            return False

    #Função que instancia um objeto para cada cliente no banco de dados e os coloca em uma lista, depois retorna essa lista
    def list_clientes(self):
        conn = self.get_db_connection()
        clientes_info = conn.execute('SELECT * FROM users WHERE tipo = "cliente"').fetchall()
        conn.close()
        clientes = []
        for cli in clientes_info:
            cli = list(cli)
            cli_atual = Cliente(
                cli[1],
                cli[2],
                cli[3],
                cli[4],
                cli[5],
                cli[6],
                cli[7]
            )
            clientes.append(cli_atual)
        return clientes

    #Função que recebe um objeto cliente e uma string ref, e altera no BD, na linha da ref,
    # os dados de acordo com as informações do objeto passado como parâmetro 
    def update_cliente(self, ref_original, cli_alterado):
        conn = self.get_db_connection()
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