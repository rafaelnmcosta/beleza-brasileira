from datetime import datetime

class Servico:

    def __init__(self, param_data, param_horario, param_duracao, param_descricao, param_cliente, param_estab):
        self.__data = param_data #datetime.strptime(paramData, '%d/%m/%Y')
        self.__horario = param_horario #datetime.strptime(paramHorario, '%H:%M')
        self.__duracao = param_duracao
        self.__descricao = param_descricao
        self.__ref_cliente = param_cliente # Referencia do usuário que está requisitando um serviço
        self.__ref_estab = param_estab # Referencia do estabelecimento que realizará o serviço

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @property
    def duracao(self):
        return self.__duracao

    @property
    def descricao(self):
        return self.__descricao

    @property
    def cliente(self):
        return self.__ref_cliente

    @property
    def estabelecimento(self):
        return self.__ref_estab

    @data.setter
    def data(self, new_data):
        raise ValueError("Impossivel alterar a data diretamente. Use a funcao de novo servico/edicao.")

    @horario.setter
    def horario(self, new_horario):
        raise ValueError("Impossivel alterar o horario diretamente. Use a funcao de novo servico/edicao.")

    @duracao.setter
    def duracao(self, new_duracao):
        raise ValueError("Impossivel alterar a duracao diretamente. Use a funcao de novo servico/edicao.")

    @descricao.setter
    def descricao(self, new_descricao):
        raise ValueError("Impossivel alterar a descricao diretamente. Use a funcao de novo servico/edicao.")

    @cliente.setter
    def cliente(self, new_cliente):
        raise ValueError("Impossivel alterar o cliente diretamente. Use a funcao de novo servico/edicao.")

    @estabelecimento.setter
    def estab(self, new_estab):
        raise ValueError("Impossivel alterar o estabelecimento diretamente. Use a funcao de novo servico/edicao.")

    def novo_servico(self):
        print("Novo serviço\n")