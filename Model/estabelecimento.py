from .usuario import Usuario


class Estabelecimento:

    def __init__(self, param_nome, param_endereco, param_telefone, param_ref, param_senha, param_tipo, param_cnpj, param_categoria):
        super().__init__(param_nome, param_endereco, param_telefone, param_ref, param_senha, param_tipo)
        self.__cnpj = param_cnpj
        self.categoria = param_categoria
        self.__lista_servicos = None

    @property

    def cnpj(self):
        return self.cnpj

    @cnpj.setter

    def cnpj(self, newCnpj):
        raise ValueError("Impossivel alterar o CNPJ diretamente. Use a funcao de edicao.")
