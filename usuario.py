MIN_LEN_SENHA = 6 #Comprimento mínimo da senha de usuário

class Usuario:

    def __init__(self):
        self.nome = None
        self.endereco = None
        self.telefone = None
        self.__id = None
        self.__senha = None
        self.__tipo = None

    @property
    def id(self):
        return self.__id

    @property
    def senha(self):
        return self.__senha

    @property
    def tipo(self):
        return self.__tipo

    @id.setter
    def id(self, newId):
        raise ValueError("Impossivel alterar ID diretamente. Use a funcao de cadastro/edicao.")

    @senha.setter
    def senha(self, newSenha):
        raise ValueError("Impossivel alterar Senha diretamente. Use a funcao de cadastro/edicao.")

    @tipo.setter
    def tipo(self, newSenha):
        raise ValueError("Impossivel alterar Senha diretamente. Use a funcao de cadastro/edicao.")

    def cadastro(self):
        print("Dados do novo usuario\nInforme o nome: ")
        self.nome = input()

        print("Informe o endereco: ")
        self.endereco = input()

        print("Informe o telefone (11 dígitos): ")
        self.telefone = input()
        while len(self.telefone) != 11:
            print("Informe DDD e o dígito 9 no início do número:")
            self.telefone = input()
            self.telefone = str(self.telefone)

        self.telefone = '({}) {}-{}-{}'.format(self.telefone[0:2],
                                                self.telefone[2], self.telefone[3:7], self.telefone[7:])

        print("Informe a ID desejada: ")
        idTemp = input()
        while not validaId(idTemp):
            print("ID invalida! Informe outra!\n")
            idTemp = input()
        self.__id = idTemp

        print("Informe a senha a ser usada: ")
        senhaTemp = input()
        while not validaSenha(senhaTemp):
            print("Senha: ")
            senhaTemp = input()
        self.__senha = senhaTemp

        print("Informe o tipo de conta que deseja ser criada(C p/ cliente; E p/ estabelecimento):")
        tipoTemp = input().strip().upper()[0]
        while tipoTemp != 'C' and tipoTemp != 'E':
            print("Informe apenas C p/ cliente ou E p/ estabelecimento")
            tipoTemp = input()
        self.__tipo = tipoTemp


def validaId(idTemp):
    # Faz uma busca no banco de dados para verificar se essa ID já existe
    return True


def validaSenha(senhaTemp):
    if senhaTemp.isalpha():
        print("A senha precisa conter ao menos um numero!")
        return False
    if senhaTemp.isnumeric():
        print("A senha precisa conter ao menos uma letra!")
        return False
    if len(senhaTemp)<MIN_LEN_SENHA:
        print("A senha precisa ter ao menos 6 digitos!")
        return False
    return True
