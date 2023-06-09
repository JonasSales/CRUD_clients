import os
from client import Client, list_client
from endereco import Endereco
from datetime import datetime



class Menu_client:
    os.system('cls')
    def menu_client():
        Client.show_options()
        while True:
            action = int(input("Digite um dos números indicados"
                                "para realizar alguma tarefa:"))
            if action == 1:  # Adicionar novos clientes
                os.system('cls')
                dados = (dados_cliente())
                cliente = Client(dados[0],dados[1],dados[2],dados[3],
                    dados[4],dados[5],'')
                cliente.add_client()
                Client.show_options()
            elif action == 2:  # Listar todos os clientes
                os.system('cls')
                list_client()
                Client.show_options()
            elif action == 3:  # Atualizar um cliente já cadastrado
                os.system('cls')
                list_client()
                id_typed = int(input("Digite o ID do cliente "
                                     "para atualizamos os dados:"))
                dados = (dados_cliente())
                cliente = Client(dados[0],dados[1],dados[2],dados[3],
                    dados[4],'',id_typed)
                os.system('cls')
                cliente.update_client()
                Client.show_options()
            elif action == 4:  # Remover um cliente
                os.system('cls')
                list_client()
                Client.delete_client()
                Client.show_options()
            elif action == 5:
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Ação inválida,cheque ações válidas abaixo:")
                Client.show_options()



class Menu_endereco:

    def menu_endereco():
        os.system('cls')
        Endereco.show_options()
        while True:
            action = int(input("Digite um dos números indicados "
                                "para realizar alguma tarefa:"))
            if action == 1:  # Adicionar novos clientes
                os.system('cls')
                list_client()
                id_typed = int(input("Digite o ID do cliente para "
                                      "adicionamos o endereço:"))
                dados = (dados_enderecos())
                endereco = Endereco(dados[0],dados[1],dados[2],dados[3],
                    dados[4],dados[5],dados[6],id_typed)
                os.system('cls')
                endereco.add_address()
                Endereco.show_options()
            elif action == 2: # Listar todos os endereços
                os.system('cls')
                Endereco.list_address()
                Endereco.show_options()
            elif action == 3: #Atualizar um endereço
                os.system('cls')
                Endereco.list_address()
                id_typed = input("Digite o id do cliente para atualizamos o seu endereço:")
                dados = (dados_enderecos())
                endereco = Endereco(dados[0],dados[1],dados[2],dados[3],
                    dados[4],dados[5],dados[6],id_typed)
                os.system('cls')
                endereco.update_address()
                Endereco.show_options()
            elif action == 4: #Remover um endereço
                os.system('cls')
                Endereco.list_address()
                Endereco.delete_address()
                Endereco.show_options()
            elif action == 5:
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Ação inválida,cheque ações válidas abaixo:")
                Endereco.show_options()



def dados_enderecos():
    try:
        while True:
            try:
                cep = int(input("Digite o novo CEP:"))
                if len(str(cep)) != 8:
                    os.system('cls')
                    print("O CEP deve ter 8 números")
                else:
                    break
            except ValueError:
                    os.system('cls')
                    print("Apenas números")

        while True:
            numero = input("Digite o novo número:")
            try:
                numero = int(numero)
                break
            except ValueError:
                os.system('cls')
                print("Apenas números.")
    except:
        pass

    endereco = input("Digite o novo endereço:")
    complemento = input("Digite o novo complemento:")
    bairro = input("Digite o novo bairro:")
    cidade = input("Digite a nova cidade:")
    estado = input("Digite o novo estado:")
    return (cep,endereco,numero,complemento,
            bairro,cidade,estado)
       


def dados_cliente():   
    nome = input("Digite o novo nome do usuário:")
    sobrenome = input("Digite o novo sobrenome do usuário:")
    try:
        while True:
            try:
                cpf = int(input("Digite o novo CPF do usuário:"))
                if len(str(cpf)) == 11:
                    break
                else:
                    os.system('cls')
                    print("CPF inválido, ele deve conter 11 digitos.")
            except ValueError:
                    print("Apenas números.")
                    
        while True:
            try:
                fone = int(input("Digite o novo telefone do usuário, no formato (DD+Número):"))
                if len(str(fone)) == 11 and 12:
                    break
                else:
                    os.system('cls')
                    print("Telefone inválido! o número deve conter 11 ou 12 "
                            "números no formato (DD+Número).")
            except ValueError:
                os.system('cls')
                print("Telefone inválido! Digite apenas "
                        "números.")
    except:
        pass
        
    data_atual = datetime.now()
    data_atual = data_atual.strftime('%Y%m%d')
            
    while True:
        try:
            data_string = input("Digite a data de seu nascimento (formato dd/mm/aaaa):")
            data = datetime.strptime(data_string, '%d/%m/%Y')
            nascimento = data.strftime('%Y%m%d')
            break
        except ValueError:
            os.system('cls')
            print("Data inválida! Digite novamente no formato dd/mm/aaaa.\n"
                    "Reinicie o processo novamente.")
            
    return (nome, sobrenome, cpf, fone,
            nascimento, data_atual)
        
