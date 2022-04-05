from .usuario import Usuario


class Estabelecimento(Usuario):

    def __init__(self,param_nome,param_endereco,param_telefone,param_ref,param_senha,param_tipo,param_cnpj,param_descricao):
        super().__init__(param_nome, param_endereco, param_telefone, param_ref, param_senha, param_tipo)
        self.__cnpj = param_cnpj
        self.descricao = param_descricao
        #self.__lista_servicos = None

    @property

    def cnpj(self):
        return self.__cnpj

    @cnpj.setter

    def cnpj(self, new_cnpj):
        raise ValueError("Impossivel alterar o CNPJ diretamente. Use a funcao de edicao.")
