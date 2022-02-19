import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (nome, endereco, telefone, ref, senha, tipo, cpf_cnpj) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Cliente 1', 'rua de teste 1', 'telefone 1', 'cliente', 'admin', 'cliente', 'cpf-de-teste')
            )

cur.execute("INSERT INTO users (nome, endereco, telefone, ref, senha, tipo, cpf_cnpj, descricao) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('Estabelecimento 1', 'rua de teste 2', 'telefone 2', 'estab', 'admin', 'estab', 'cnpj-de-teste', 'Descricao de teste')
            )

connection.commit()
connection.close()