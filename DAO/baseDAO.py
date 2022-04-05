import sqlite3

import sys
sys.path.insert(0, '../')

from Model.cliente import Cliente
from Model.estabelecimento import Estabelecimento

class BaseDAO:

	def __init__(self, param_database):
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

	def list_all_users(self):
		conn = self.get_db_connection()
		users_info = conn.execute('SELECT * FROM users').fetchall()
		conn.close()
		users = []
		for user in users_info:
			user = list(user)
			if user[6] is "cliente":
				user_atual = Cliente(
					user[1],
					user[2],
					user[3],
					user[4],
					user[5],
					user[6],
					user[7]
					)
				users.append(user_atual)
			else:
				user_atual = Estabelecimento(
						user[1],
						user[2],
						user[3],
						user[4],
						user[5],
						user[6],
						user[7],
						user[8]
						)
				users.append(user_atual)

		return users

	def get_user_by_ref(self, ref):
		conn = self.get_db_connection()
		user = conn.execute('SELECT * FROM users WHERE ref = ?', (ref,)).fetchone()
		conn.close()
		if user is None:
			#abort(404)
			return False

		user = list(user)
		if user[6] is "cliente":
			cli = Cliente(
				user[1],
				user[2],
				user[3],
				user[4],
				user[5],
				user[6],
				user[7]
				)
			return cli
		else:
			estab = Estabelecimento(
				user[1],
				user[2],
				user[3],
				user[4],
				user[5],
				user[6],
				user[7],
				user[8]
				)
			return estab

	def delete_user(self, ref):
		user_del = self.get_user_by_ref(ref)
		if user_del:
			conn = self.get_db_connection()
			conn.execute('DELETE FROM users WHERE ref = ?', (ref,))
			conn.commit()
			conn.close()
			return user_del.nome
		else:
			return False