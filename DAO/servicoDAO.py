import sqlite3

import sys
sys.path.insert(0, '../')

from Model.servico import Servico

class ServicoDAO:

    def _init_(self, param_database):
        self.__database = param_database #String que contém o nome do banco de dados que será acessado

    @property
    def database(self):
        return self.__database


    @database.setter
    def ref(self, new_database):
        raise ValueError("Nao e permitido alterar o banco de dados")

    # Função que abre a conexão com o banco de dados
    def get_db_connection(self):
        conn = sqlite3.connect(self.__database)
        if conn:
            conn.row_factory = sqlite3.Row
            return conn
        else:
            return False

    def list_services_for_user(self, ref):
        conn = self.get_db_connection()
        services_info = conn.execute('SELECT * FROM services WHERE ref_cliente = ?', (ref,)).fetchall()
        conn.close()
        services = []
        for service in services_info:
            service = list(service)
            service_atual = Servico(
                service[1],
                service[2],
                service[3],
                service[4],
                service[5]
                )
            services.append(service_atual)

        return services

    def new_service(self, new_service):
        conn = self.get_db_connection()
        conn.execute('INSERT INTO services '
            '(data, horario, descricao, ref_cliente, ref_estab)'
            'VALUES (?, ?, ?, ?, ?)',
            (new_service.data, new_service.horario, new_service.descricao, new_service.cliente, new_service.estabelecimento)
        )
        conn.commit()
        conn.close()
        return True