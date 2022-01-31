from usuario import Usuario
from servico import Servico

user = Usuario()
user.cadastro()

print("\nnome: ", user.nome, "\nendereco: ", user.endereco, "\ntelefone: ", user.telefone, "\nid: ", user.id, "\nsenha: ", user.senha, "\ntipo: ", user.tipo)
