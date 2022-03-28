import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


# Função que abre a conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Encontra um usuário pela referencia
def get_user_by_ref(user_ref):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE ref = ?', (user_ref,)).fetchone()
    conn.close()
    if user is None:
        abort(404)
    return user


# Inicia a variavel app que conterá o site
app = Flask(__name__, template_folder='View')
app.config['SECRET_KEY'] = 'Uma_string_muito_grande'


# Render da tela inicial do programa, carrega todos os usuários do banco de dados
@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)


# Retorna a página pessoal de cada usuário, endereçada com sua respectiva id
@app.route('/<user_ref>')
def user(user_ref):
    user = get_user_by_ref(user_ref)
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
        ref = request.form['ref']
        senha = request.form['senha']
        tipo = request.form['tipo']
        cpf_cnpj = request.form['cpf_cnpj']
        descricao = request.form['descricao']

        if nome and endereco and telefone and ref and senha and tipo and cpf_cnpj:
            conn = get_db_connection()
            conn.execute('INSERT INTO users'
                         '(nome, endereco, telefone, ref, senha, tipo, cpf_cnpj, descricao)'
                         'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                         (nome, endereco, telefone, ref, senha, tipo, cpf_cnpj, descricao)
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
@app.route('/<ref>/edicao', methods=('GET', 'POST'))
def edicao(ref):
    user = get_user_by_ref(ref)
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        new_ref = request.form['ref']
        senha = request.form['senha']
        tipo = request.form['tipo']
        cpf_cnpj = request.form['cpf_cnpj']
        descricao = request.form['descricao']

        if nome and endereco and telefone and new_ref and senha and tipo and cpf_cnpj:
            conn = get_db_connection()
            conn.execute('UPDATE users SET nome = ?, endereco = ?, telefone = ?, ref = ?, senha = ?, tipo = ?, cpf_cnpj = ?, descricao = ?'
                         ' WHERE ref = ?',
                         (nome, endereco, telefone, new_ref, senha, tipo, cpf_cnpj, descricao, ref)
                         )
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        else:
            flash('É preciso preencher todos os campos!')
            return render_template('edicao.html', user=user)

    return render_template('edicao.html', user=user)


# Função que exclui um usuário do banco de dados
@app.route('/<ref>/delete', methods=('POST',))
def delete(ref):
    user = get_user_by_ref(ref)
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE ref = ?', (ref,))
    conn.commit()
    conn.close()
    flash('"{}" foi excluído com sucesso!'.format(user['nome']))
    return redirect(url_for('index'))


# Run do programa para iniciar o servidor Flask
if __name__ == '__main__':
    app.run()