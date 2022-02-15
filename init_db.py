import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (nome, endereco, telefone) VALUES (?, ?, ?)",
            ('usuario 1', 'rua de teste 1', 'telefone 1')
            )

cur.execute("INSERT INTO users (nome, endereco, telefone) VALUES (?, ?, ?)",
            ('usuario 2', 'rua de teste 2', 'telefone 2')
            )

connection.commit()
connection.close()