import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


# Função que abre a conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Função que encontra um usuário de acordo com sua id no banco de dados
def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user


# Inicia a variavel app que conterá o site
app = Flask(__name__)
app.config['SECRET_KEY'] = 'UmaStringMuitoGrande'


# Render da tela inicial do programa, carrega todos os usuários do banco de dados
@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)


# Retorna a página pessoal de cada usuário, endereçada com sua respectiva id
@app.route('/<int:user_id>')
def user(user_id):
    user = get_user(user_id)
    return render_template('user.html', user=user)


# Função pra exibir nossas carinhas ou qualquer coisa assim, retorna a página "sobre"
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


# Função que retorna a página de cadastro
@app.route('/cadastro', methods=('GET', 'POST'))
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone = request.form['telefone']

        if nome and endereco and telefone:
            conn = get_db_connection()
            conn.execute('INSERT INTO users'
                         '(nome, endereco, telefone)'
                         'VALUES (?, ?, ?)',
                         (nome, endereco, telefone)
                         )
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

        else:
            flash('É preciso preencher todos os campos!')
            return render_template('cadastro.html')

    else:
        return render_template('cadastro.html')


# Função que retorna a página de edição do cadastro de um usuário
@app.route('/<int:id>/edicao', methods=('GET', 'POST'))
def edicao(id):
    user = get_user(id)
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone = request.form['telefone']

        if nome and endereco and telefone:
            conn = get_db_connection()
            conn.execute('UPDATE users SET nome = ?, endereco = ?, telefone = ?'
                         ' WHERE id = ?',
                         (nome, endereco, telefone, id)
                         )
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        else:
            flash('É preciso preencher todos os campos!')
            return render_template('edicao.html', user=user)

    return render_template('edicao.html', user=user)


# Função que exclui um usuário do banco de dados
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    user = get_user(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" foi excluído com sucesso!'.format(user['nome']))
    return redirect(url_for('index'))


# Run do programa para iniciar o servidor Flask
if __name__ == '__main__':
    app.run()