from usuario import Usuario


class Cliente:

    def __init__(self, paramNome, paramEndereco, paramTelefone, paramId, paramSenha, paramTipo, paramCpf):
        super().__init__(paramNome, paramEndereco, paramTelefone, paramId, paramSenha, paramTipo)
        self.__cpf = paramCpf
        self.__listaServicos = None

    @property

    def cpf(self):
        return self.cpf

    @cpf.setter

    def cpf(self, newCpf):
        raise ValueError("Impossivel alterar o cpf diretamente. Use a funcao de edicao.")
