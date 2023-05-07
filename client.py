import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="admin",
    password="admin"
)

class Client:

    def show_options():
        print("[1] Para adicionar novos clientes")
        print("[2] Para listar todos os clientes")
        print("[3] Para atualizar um cliente já cadastrado")
        print("[4] Para remover algum cliente")
        print("[5] Para sair do programa")

    def adicionar_clientes():
        name = input("Digite o novo nome do usuário:")
        surname = input("Digite o novo sobrenome do usuário:")
        age = input("Digite a nova idade do usuário:")
        fone = input("Digite o novo telefone do usuário:")
        sql = (f"INSERT INTO public.clientes( nome, sobrenome, idade, telefone) VALUES ('{name}','{surname}',{age},'{fone}');")
        cur.execute(sql)
        conn.commit()
        print("Cliente adicionado com sucesso")

    def atualizar_clientes():
        id_typed = int(input("Digite o id do usuário:"))
        name = input("Digite o novo nome do usuário:")
        surname = input("Digite o novo sobrenome do usuário:")
        age = input("Digite a nova idade do usuário:")
        fone = input("Digite o novo telefone do usuário:")
        cur.execute(f"UPDATE clientes SET nome = '{name}', sobrenome = '{surname}',idade = '{age}', telefone = '{fone}' WHERE id = '{id_typed}';")
        conn.commit()
        print ("Cliente atualizado com sucesso")

    def deletar_clientes():
        id_typed = int(input("Diga o ID do cliente para ser deletado:"))
        cur.execute(f"DELETE FROM clientes WHERE id = {id_typed}")
        conn.commit()
        print("Cliente removido com sucesso")

def listar_clientes():
    cur.execute("SELECT * FROM clientes")
    result = cur.fetchall()
    for dados in result:
        print (f"ID:{dados[0]} Nome:{dados[1]} Sobrenome:{dados[2]} Idade:{dados[3]} Telefone:{dados[4]}")
cur = conn.cursor()