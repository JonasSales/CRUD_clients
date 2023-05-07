import os
from client import Client, listar_clientes

Client.show_options()
while True:
    action = int(input("Digite um dos números indicados para realizar alguma tarefa:"))
    if action == 1:  # Adicionar novos clientes
        os.system('cls')
        Client.adicionar_clientes()
        Client.show_options()
    elif action == 2:  # Listar todos os clientes
        os.system('cls')
        listar_clientes()
        Client.show_options()
    elif action == 3:  # Atualizar um cliente já cadastrado
        os.system('cls')
        Client.atualizar_clientes()
        Client.show_options()
    elif action == 4:  # Remover um cliente
        os.system('cls')
        listar_clientes()
        Client.deletar_clientes()
        Client.show_options()
    elif action == 5:
        os.system('cls')
        break
    else:
        os.system('cls')
        print("Ação inválida,cheque ações válidas abaixo:")
        Client.show_options()
