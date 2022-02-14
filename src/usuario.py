class Usuario:

    def __init__(self, paramNome, paramEndereco, paramTelefone, paramId, paramSenha, paramTipo):
        self.nome = paramNome
        self.endereco = paramEndereco
        self.telefone = paramTelefone
        self.__id = paramId
        self.__senha = paramSenha
        self.__tipo = paramTipo

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
