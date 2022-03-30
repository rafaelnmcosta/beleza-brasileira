import sqlite3
from Model.estabelecimento import Estabelecimento

class estabelecimentoDAO:

    def __init__(self, param_database):
        self.__database = param_database

    @property
    def database(self):
        return self.__database


    @database.setter
    def ref(self, new_database):
        raise ValueError("Nao e permitido alterar o banco de dados")


    def get_db_connection(self):
        conn = sqlite3.connect(self.__database)
        if conn:
            conn.row_factory = sqlite3.Row
            return conn
        else:
            return False

    # Função que recebe um estabelecimento e o adiciona ao banco de dados
    def addEstabelecimento(self, novo_estabelecimento):
        conn = self.get_db_connection()
        conn.execute('INSERT INTO users'
            '(nome, endereco, telefone, ref, senha, tipo, cpf_cnpj, descricao)'
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (novo_estabelecimento.nome, novo_estabelecimento.endereco, novo_estabelecimento.telefone, novo_estabelecimento.ref, novo_estabelecimento.senha, novo_estabelecimento.tipo, novo_estabelecimento.cnpj, novo_estabelecimento.descricao)
        )
        conn.commit()
        conn.close()
        return True

    # Função que busca uma ref, instancia um objeto estabelecimento e retorna esse objeto
    def getEstabelecimento(self, ref_estabelecimento):
        conn = self.get_db_connection()
        estabelecimento = list(conn.execute('SELECT * FROM users WHERE ref = ?', (ref_estabelecimento,)).fetchone())
        conn.close()
        if estabelecimento is None:
            #abort(404)
            return False
        else:
            estab = Estabelecimento(
                estabelecimento[1],
                estabelecimento[2],
                estabelecimento[3],
                estabelecimento[4],
                estabelecimento[5],
                estabelecimento[6],
                estabelecimento[7],
                estabelecimento[8]
            )
            return estab

    #Função que deleta um registro do banco de dados de acordo com a referencia que será informada
    def deleteEstabelecimento(self, ref_estabelecimento):
        estab_del = self.getEstabelecimento(ref_estabelecimento)
        if estab_del:
            conn = self.get_db_connection()
            conn.execute('DELETE FROM users WHERE ref = ?', (ref_estabelecimento,))
            conn.commit()
            conn.close()
            return estab_del.nome
        else:
            return False

    #Função que instancia um objeto para cada estabelecimento no banco de dados e os coloca em uma lista, depois retorna essa lista
    def listEstabelecimentos(self):
        conn = self.get_db_connection()
        estabelecimentos_info = conn.execute('SELECT * FROM users WHERE tipo = "estabelecimento"').fetchall()
        conn.close()
        estabelecimentos = []
        for estab in estabelecimentos_info:
            estab = list(estab)
            estab_atual = Estabelecimento(
                estab[1],
                estab[2],
                estab[3],
                estab[4],
                estab[5],
                estab[6],
                estab[7],
                estab[8]
            )
            estabelecimentos.append(estab_atual)
        return estabelecimentos

    ''' Função que recebe um objeto estabelecimento e uma string ref, e altera no BD, na linha da ref,
    os dados de acordo com as informações do objeto passado como parâmetro '''
    def updateEstabelecimento(self, ref_original, estab_alterado):
        conn = self.get_db_connection()
        conn.execute('UPDATE users SET nome = ?, endereco = ?, telefone = ?, ref = ?, senha = ?, cpf_cnpj = ?'
            ' WHERE ref = ?',
            (estab_alterado.nome,
            estab_alterado.endereco,
            estab_alterado.telefone,
            estab_alterado.ref,
            estab_alterado.senha,
            estab_alterado.cnpj,
            estab_alterado.descricao,
            ref_original
            )
        )
        conn.commit()
        conn.close()
        return True