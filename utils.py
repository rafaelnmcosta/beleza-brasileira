from cliente import Cliente
from estabelecimento import Estabelecimento
from servico import Servico

MIN_LEN_SENHA = 6 #Comprimento mínimo da senha de usuário


class Utils:

    def formataTelefone(telTemp):
        while len(telTemp) != 11 or not telTemp.isnumeric():
            print("Informe DDD e o dígito 9 no início do número (PREENCHA APENAS COM NUMEROS!):")
            telTemp = str(input())

        telFormat = '({}) {}-{}-{}'.format(telTemp[0:2], telTemp[2], telTemp[3:7], telTemp[7:])

        return telFormat

    def validaId(idTemp):
        # Faz uma busca no banco de dados para verificar se essa ID já existe
        return True

    def validaSenha(senhaTemp):
        if senhaTemp.isalpha():
            print("A senha precisa conter ao menos um numero!")
            return False
        if senhaTemp.isnumeric():
            print("A senha precisa conter ao menos uma letra!")
            return False
        if len(senhaTemp) < MIN_LEN_SENHA:
            print("A senha precisa ter ao menos 6 digitos!")
            return False
        return True

    '''
    def cadastro():
        print("----- Cadastro de novo usuario -----\nInforme o nome: ")
        paramNome = input()
    
        print("Informe o endereco: ")
        paramEndereco = input()
    
        print("Informe o telefone (11 dígitos): ")
        telTemp = input()
        paramTelefone = formataTelefone(telTemp)
    
        print("Informe a ID desejada: ")
        idTemp = input()
        while not validaId(idTemp):
            print("ID invalida! Informe outra!\n")
            idTemp = input()
        paramId = idTemp
    
        print("Informe a senha a ser usada: ")
        senhaTemp = input()
        while not validaSenha(senhaTemp):
            print("Senha: ")
            senhaTemp = input()
        paramSenha = senhaTemp
    
        print("Informe o tipo de conta que deseja ser criada(C p/ cliente; E p/ estabelecimento):")
        tipoTemp = input().strip().upper()[0]
        while tipoTemp != 'C' and tipoTemp != 'E':
            print("Informe apenas C p/ cliente ou E p/ estabelecimento")
            tipoTemp = input()
        paramTipo = tipoTemp
    
        if paramTipo == 'E':
            print("Informe o CNPJ do seu estabelecimento: ")
            paramCnpj = input()
    
            print("Informe a categoria do estabelecimento: ")
            paramCategoria = input()
    
            return Estabelecimento(paramNome, paramEndereco, paramTelefone, paramId,
                                   paramSenha, paramTipo, paramCnpj, paramCategoria)
        else:
            print("Informe o seu CPF: ")
            paramCpf = input()
    
            return Cliente(paramNome, paramEndereco, paramTelefone,
                           paramId, paramSenha, paramTipo, paramCpf)
        

    def edicao():
        opcao = 99
        print("----- Edicao de um cadastro -----")
        while opcao != '0':
            print("Dados atuais:\n1 - Nome: ", self.nome, "\n2 - Endereco: ",
                  self.endereco, "\n3 - Telefone: ", self.telefone, "\n4 - Id: ", self.__id,
                  "\n5 - Senha: ", self.__senha, "\n6 - Tipo: ", self.__tipo)
            print("Informe o numero referente ao campo que deseja alterar (de 1 a 6) ou 0 para sair:")
            opcao = input()
    
            if opcao == '0':
                print("Fim da edicao")
    
            elif opcao == '1':
                print("Nome atual: ", self.nome)
                print("Informe o novo nome:")
                self.nome = input()
    
            elif opcao == '2':
                print("Endereco atual: ", self.endereco)
                print("Informe o novo endereco:")
                self.endereco = input()
    
            elif opcao == '3':
                print("Telefone atual: ", self.telefone)
                print("Informe o novo telefone:")
                telTemp = input()
                self.telefone = formataTelefone(telTemp)
    
            elif opcao == '4':
                print("Id atual: ", self.__id)
                print("Informe a nova Id:")
                idTemp = input()
                while not validaId(idTemp):
                    print("ID invalida! Informe outra!\n")
                    idTemp = input()
                self.__id = idTemp
    
            elif opcao == '5':
                print("Senha atual: ", self.__id)
                print("Informe a nova senha:")
                senhaTemp = input()
                while not validaSenha(senhaTemp):
                    print("Senha: ")
                    senhaTemp = input()
                self.__senha = senhaTemp
    
            elif opcao == '6':
                if(self.__tipo == 'C'):
                    print("Tipo atual: Cliente")
                    print("Deseja alterar o tipo de usuario para Estabelecimento? (s/n)")
                    loop = True
                    while loop:
                        verif = input()
                        if verif == 's' or verif == 'S':
                            self.__tipo = 'E'
                            loop = False
                        elif verif == 'n' or verif == 'N':
                            print("Tipo cliente mantido")
                            loop = False
                        else:
                            print("Informe apenas 's' para sim ou 'n' para nao")
                else:
                    print("Tipo atual: Estabelecimento")
                    print("Deseja alterar o tipo de usuario para Cliente? (s/n)")
                    loop = True
                    while loop:
                        verif = input()
                        if verif == 's' or verif == 'S':
                            self.__tipo = 'C'
                            loop = False
                        elif verif == 'n' or verif == 'N':
                            print("Tipo estabelecimento mantido")
                            loop = False
                        else:
                            print("Informe apenas 's' para sim ou 'n' para nao")
    
            else:
                print("Opcao invalida!")
    
        return
    '''
