class Usuario:

    def __init__(self, param_nome, param_endereco, param_telefone, param_ref, param_senha, param_tipo):
        self.nome = param_nome
        self.endereco = param_endereco
        self.telefone = param_telefone
        self.__ref = param_ref
        self.__senha = param_senha
        self.__tipo = param_tipo

    @property
    def ref(self):
        return self.__ref

    @property
    def senha(self):
        return self.__senha

    @property
    def tipo(self):
        return self.__tipo

    @ref.setter
    def ref(self, new_ref):
        raise ValueError("Impossivel alterar a Referência diretamente. Use a funcao de cadastro/edicao.")

    @senha.setter
    def senha(self, new_senha):
        raise ValueError("Impossivel alterar a Senha diretamente. Use a funcao de cadastro/edicao.")

    @tipo.setter
    def tipo(self, new_tipo):
        raise ValueError("Impossivel alterar o Tipo diretamente. Use a funcao de cadastro/edicao.")
