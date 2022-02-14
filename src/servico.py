from datetime import datetime

class Servico:

    def __init__(self, paramData, paramHorario, paramDuracao, paramDescricao):
        self.__data = None #datetime.strptime(paramData, '%d/%m/%Y')
        self.__horario = None #datetime.strptime(paramHorario, '%H:%M')
        self.__duracao = None
        self.__descricao = None
        self.__cliente = None # Id do usuário que está requisitando um serviço
        self.__estabelecimento = None # Id do estabelecimento que realizará o serviço

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
        return self.__cliente

    @property
    def estabelecimento(self):
        return self.__estabelecimento

    @data.setter
    def data(self, newData):
        raise ValueError("Impossivel alterar a data diretamente. Use a funcao de novo servico/edicao.")

    @horario.setter
    def horario(self, newHorario):
        raise ValueError("Impossivel alterar o horario diretamente. Use a funcao de novo servico/edicao.")

    @duracao.setter
    def duracao(self, newDuracao):
        raise ValueError("Impossivel alterar a duracao diretamente. Use a funcao de novo servico/edicao.")

    @descricao.setter
    def descricao(self, newDescricao):
        raise ValueError("Impossivel alterar a descricao diretamente. Use a funcao de novo servico/edicao.")

    @cliente.setter
    def cliente(self, newCliente):
        raise ValueError("Impossivel alterar o cliente diretamente. Use a funcao de novo servico/edicao.")

    @estabelecimento.setter
    def estabelecimento(self, newEstabelecimento):
        raise ValueError("Impossivel alterar o estabelecimento diretamente. Use a funcao de novo servico/edicao.")

    def novoServico(self):
        print("Novo serviço\n")