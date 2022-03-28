from .usuario import Usuario

class Cliente(Usuario):

    def __init__(self,param_nome,param_endereco,param_telefone,param_ref,param_senha,param_tipo,param_cpf):
        super().__init__(param_nome, param_endereco, param_telefone, param_ref, param_senha, param_tipo)
        self.__cpf = param_cpf
        #self.__lista_servicos = []

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, newCpf):
        raise ValueError("Impossivel alterar o cpf diretamente. Use a funcao de edicao.")
