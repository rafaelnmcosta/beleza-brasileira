from usuario import Usuario


class Estabelecimento:

    def __init__(self, paramNome, paramEndereco, paramTelefone, paramId, paramSenha, paramTipo, paramCnpj, paramCategoria):
        super().__init__(paramNome, paramEndereco, paramTelefone, paramId, paramSenha, paramTipo)
        self.__cnpj = paramCnpj
        self.categoria = paramCategoria
        self.__listaServicos = None

    @property

    def cnpj(self):
        return self.cnpj

    @cnpj.setter

    def cnpj(self, newCnpj):
        raise ValueError("Impossivel alterar o CNPJ diretamente. Use a funcao de edicao.")
