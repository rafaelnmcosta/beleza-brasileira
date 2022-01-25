class Usuario:

    nome = "new"
    endereco = "new"
    telefone = "new"
    id = "new"
    senha = "new"
    tipo = "new"

    def __init__(self, paramNome, paramEndereco, paramTelefone, paramId, paramSenha, paramTipo):
        self._nome = paramNome
        self._endereco = paramEndereco
        self._telefone = paramTelefone
        self._id = paramId
        self._senha = paramSenha
        self._tipo = paramTipo

    @property
    def nome(self):
        return self._nome
    def endereco(self):
        return  self._endereco
    def telefone(self):
        return self._telefone
    def id(self):
        return self._id
    def senha(self):
        return self._senha
    def tipo(self):
        return self._tipo