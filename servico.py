from datetime import datetime

class Servico:

    horario = "00/00/0000 00:00"
    duracao = 0
    descricao = "new"

    def __init__(self, paramHorario, paramDuracao, paramDescricao):
        self._horario = datetime.strptime(paramHorario, '%d/%m/%Y %H:%M') # Converte o horario passado em string para o tipo Date
        self._duracao = paramDuracao
        self._descricao = paramDescricao

    @property
    def horario(self):
        return self._horario
    def duracao(self):
        return self.duracao
    def descricao(self):
        return self._descricao