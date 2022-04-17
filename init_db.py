import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


cur.execute("INSERT INTO users (nome, endereco, telefone, ref, senha, tipo, cpf_cnpj) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Cliente 1', 'rua de teste 1', 'telefone 1', 'cliente', 'admin', 'cliente', 'cpf-de-teste')
            )

cur.execute("INSERT INTO users (nome, endereco, telefone, ref, senha, tipo, cpf_cnpj, descricao) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('Estabelecimento 1', 'rua de teste 2', 'telefone 2', 'estab1', 'admin', 'estabelecimento', 'cnpj-de-teste', 'Descricao de teste')
            )


cur.execute("INSERT INTO services (data, horario, descricao, ref_cliente, ref_estab) VALUES (?, ?, ?, ?, ?)",
            ('2022-01-01', '15:30', 'A descrição do agendamento 1', 'cliente', 'estab1')
            )

connection.commit()
connection.close()