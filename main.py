from app import Menu_client
from app import Menu_endereco
import os


def menu_principal():
    print("[1] Para ir ao menu de clientes")
    print("[2] Para ir ao menu de endereços")
    print("[3] Para sair do programa")

while True:
    menu_principal()
    action = int(input("Digite um dos números indicados"
                        "para realizar alguma tarefa:"))
    if action == 1:
        os.system('cls')
        Menu_client.menu_client()
    elif action == 2:
        os.system('cls')
        Menu_endereco.menu_endereco()
    elif action == 3:
        os.system('cls')
        break
    else:
        os.system('cls')
        print("Ação invalida, veja uma ação válida abaixo:")

