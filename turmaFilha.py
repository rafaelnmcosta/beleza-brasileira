from turma import Turma

turma = 'Universidade'                  #global

class TurmaFilha(Turma):
    turma = 'vazia'
    ano = 0
    turno = 'xxxxxx'
    def __init__(self, paramTurma, paramAno, paramTurno):
        super().__init__(paramTurma) #instância
        self.ano = paramAno          #instância
        self.setTurno(paramTurno)    #instância
        TurmaFilha.ano += 4          #classe
        ano = 2023                   #local - nunca acessada

    def setTurno(self, numero):
        if numero == 1:
            self.turno = 'matutino'
        elif numero == 2:
            self.turno = 'vespertino'
        elif numero == 3:
            self.turno = 'noturno'

    
tA = TurmaFilha('BIA', 2022, 1)
tA.setTurno(2)
tB = TurmaFilha('BSI', 2022, 3)

print(TurmaFilha.turma,' ',TurmaFilha.ano) #variáveis de classe
print('\n')
print(tA.turma,' ',tA.ano,' ',tA.turno) #variáveis de instância
print(tB.turma,' ',tB.ano,' ',tB.turno) #variáveis de instância
print('\n')
print(turma)                            #variável global