from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

import sys
sys.path.insert(0, '../')

from DAO.baseDAO import BaseDAO
from DAO.clienteDAO import ClienteDAO
from DAO.estabelecimentoDAO import EstabelecimentoDAO
from DAO.servicoDAO import ServicoDAO

from Model.cliente import Cliente
from Model.estabelecimento import Estabelecimento
from Model.servico import Servico

app = Flask(__name__, template_folder='../View')
app.config['SECRET_KEY'] = 'Uma_string_muito_grande'

database = "../database.db" #variável global que guarda o caminho do banco de dados


@app.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        user_ref = request.form['user_ref']
        senha = request.form['senha']

        if user_ref and senha:
            novoDAO = BaseDAO(database)
            logged = novoDAO.get_user_by_ref(user_ref)

            if not logged:
                flash('Usuario inexistente!')
                return render_template('login.html')

            elif senha != logged.senha:
                flash('Senha incorreta!')
                return render_template('login.html')

            else:
                return redirect(url_for('home', ref=logged.ref))

        else:
            flash('É preciso preencher todos os campos!')
            return render_template('login.html')

    else:
        return render_template('login.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/cadastro', methods=('GET', 'POST'))
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        ref = request.form['ref']
        senha = request.form['senha']
        tipo = request.form['tipo']
        cpf = request.form['cpf_cnpj']
        descricao = request.form['descricao']

        if nome and endereco and telefone and ref and senha and tipo and cpf:
            cliDAO = ClienteDAO(database)
            novo_cli = Cliente(nome, endereco, telefone, ref, senha, tipo, cpf)
            if not cliDAO.add_cliente(novo_cli):
                flash('Erro ao adicionar usuário!')
            else:
                flash('Usuário adicionado!')
                return redirect(url_for('login'))

        else:
            flash('É preciso preencher todos os campos!')
            return render_template('cadastro.html')

    else:
        return render_template('cadastro.html')


@app.route('/<ref>/home')
def home(ref):
    novoDAO = BaseDAO(database)
    user = novoDAO.get_user_by_ref(ref)
    cliDAO = ClienteDAO(database)
    estabDAO = EstabelecimentoDAO(database)
    if user.tipo == "cliente":
        estabelecimentos = estabDAO.list_estabelecimentos()
        return render_template("cliente_home.html", estabelecimentos=estabelecimentos, user=user)
    else:
        clientes = cliDAO.list_clientes()
        return render_template("sobre.html")


@app.route('/<ref>/horarios')
def horarios(ref):
    novoDAO = BaseDAO(database)
    user = novoDAO.get_user_by_ref(ref)
    servDAO = ServicoDAO(database)
    services = servDAO.list_services_for_user(user.ref)
    return render_template("horarios.html", services=services, user=user)


@app.route('/<ref_atual>/servico/<ref>', methods=('GET', 'POST'))
def novo_servico(ref, ref_atual):
    novoDAO = BaseDAO(database)
    estabDAO = EstabelecimentoDAO(database)
    servDAO = ServicoDAO(database)
    user = novoDAO.get_user_by_ref(ref_atual)
    estab = estabDAO.get_estabelecimento(ref)

    if request.method == 'POST':
        data = request.form['data']
        horario = request.form['horario']
        descricao = request.form['descricao']

        if data and horario and descricao:
            new_service = Servico(data, horario, descricao, user.ref, estab.ref)
            if not servDAO.new_service(new_service):
                flash('Erro ao agendar horario!')
            else:
                flash('Horário agendado!')
                return redirect(url_for('home', ref=user.ref))

        else:
            flash('É preciso preencher todos os campos!')
            return render_template('agendamento.html', estab=estab, user=user)

    else:
        return render_template('agendamento.html', estab=estab, user=user)


@app.route('/<ref_atual>/<ref>')
def perfil(ref, ref_atual):
    novoDAO = BaseDAO(database)
    user = novoDAO.get_user_by_ref(ref)
    user_atual = novoDAO.get_user_by_ref(ref_atual)
    if not user:
        abort(404)
    elif user.tipo == "cliente":
        cliDAO = ClienteDAO(database)
        cli = cliDAO.get_cliente(ref)
        if ref == ref_atual:
            return render_template("user_cliente.html", cli=cli, user=user_atual)
        else:
            return render_template("perfil_cliente.html", cli=cli, user=user_atual)
    else:
        estabDAO = EstabelecimentoDAO(database)
        estab = estabDAO.get_estabelecimento(ref)
        if ref == ref_atual:
            return render_template("user_estab.html", estab=estab, user=user_atual)
        else:
            return render_template("perfil_estab.html", estab=estab, user=user_atual)


@app.route('/<ref>/edicao', methods=('GET', 'POST'))
def edicao(ref):
    novoDAO = BaseDAO(database)
    user = novoDAO.get_user_by_ref(ref)
    if not user:
        abort(404)
    elif user.tipo == "cliente":
        cliDAO = ClienteDAO(database)
        cli = cliDAO.get_cliente(ref)
    else:
        estabDAO = EstabelecimentoDAO(database)
        estab = estabDAO.get_estabelecimento(ref)

    if request.method == 'POST':
        if user.tipo == "cliente":
            nome = request.form['nome']
            endereco = request.form['endereco']
            telefone = request.form['telefone']
            new_ref = request.form['ref']
            senha = request.form['senha']
            tipo = request.form['tipo']
            cpf = request.form['cpf']

            if nome and endereco and telefone and new_ref and senha and tipo and cpf:
                cliDAO = ClienteDAO(database)
                cli_editado = Cliente(nome, endereco, telefone, new_ref, senha, tipo, cpf)
                if not cliDAO.update_cliente(ref, cli_editado):
                    flash('Erro ao editar!')
                else:
                    flash('Registros editados com sucesso!')
                    return redirect(url_for('home', ref=cli_editado.ref, user=user))
            else:
                flash('É preciso preencher todos os campos!')
                return render_template("edicao_cliente.html", cli=cli, user=user)

        else:
            nome = request.form['nome']
            endereco = request.form['endereco']
            telefone = request.form['telefone']
            new_ref = request.form['ref']
            senha = request.form['senha']
            tipo = request.form['tipo']
            cnpj = request.form['cnpj']
            descricao = request.form['descricao']

            if nome and endereco and telefone and new_ref and senha and tipo and cnpj and descricao:
                estabDAO = EstabelecimentoDAO(database)
                estab_editado = Estabelecimento(nome, endereco, telefone, new_ref, senha, tipo, cnpj, descricao)
                if not estabDAO.update_estabelecimento(ref, estab_editado):
                    flash('Erro ao editar!')
                else:
                    flash('Registros editados com sucesso!')
                    return redirect(url_for('home', ref=estab_editado.ref, user=user))
            else:
                flash('É preciso preencher todos os campos!')
                return render_template("edicao_estab.html", estab=estab, user=user)

    else:
        if user.tipo == "cliente":
            return render_template("edicao_cliente.html", cli=cli, user=user)
        else:
            return render_template("edicao_estab.html", estab=estab, user=user)


@app.route('/<ref>/delete', methods=('POST',))
def delete(ref):
    novoDAO = BaseDAO(database)
    user_del = novoDAO.delete_user(ref)
    if user_del:
        flash('"{}", sua conta foi excluída com sucesso!'.format(user_del))
        return redirect(url_for('login'))
    else:
        flash('Erro ao excluir conta!')
        return redirect(url_for('home', ref))

if __name__ == '__main__':
    app.run()
