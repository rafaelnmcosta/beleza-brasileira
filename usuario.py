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
        endTemp = input()
        self.endereco = endTemp

        print("Informe o telefone: ")
        self.telefone = input()

        print("Informe a ID desejada: ")
        idTemp = input()
        while not validaId(idTemp):
            print("ID invalida! Informe outra!\n")
            idTemp = input()
        self.__id = idTemp

        print("Informe a senha a ser usada: ")
        senhaTemp = input()
        while not validaSenha(senhaTemp):
            print("Senha invalida! Informe outra!\n")
            senhaTemp = input()
        self.__senha = senhaTemp

        print("Informe o tipo de conta que deseja ser criada(C p/ cliente; E p/ estabelecimento):")
        tipoTemp = input()
        while tipoTemp != 'C' and tipoTemp != 'E':
            print("Informe apenas C p/ cliente ou E p/ estabelecimento")
            tipoTemp = input()
        self.__tipo = tipoTemp


def validaId(idTemp):
    return True


def validaSenha(senhaTemp):
    return True


user = Usuario()
user.cadastro()

print(user.nome, "\n", user.endereco, "\n", user.telefone, "\n", user.id, "\n", user.senha, "\n", user.tipo)
