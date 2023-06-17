import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="admin",
    password="admin"
)

class Client:

    def __init__(self,nome,sobrenome,cpf,telefone,nascimento,data_atual,id_typed):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.telefone = telefone
        self.nascimento = nascimento
        self.data_atual = data_atual
        self.id_typed = id_typed

    def __repr__(self):
        return f"nome:{self.nome}"\
                f"sobrenome:{self.sobrenome}"\
                f"cpf:{self.cpf}"\
                f"telefone:{self.telefone}"\
                f"nascimento:{self.nascimento}"\
                f"data atual:{self.data_atual}"\
                f"id digitado:{self.id_typed}"
                
    def add_client(self):
        sql = (f"INSERT INTO clientes( nome, sobrenome, cpf, telefone,"
                "data_de_nascimento, cliente_desde, status)"
                f"VALUES ('{self.nome}','{self.sobrenome}','{self.cpf}',"
                f"'{self.telefone}','{self.nascimento}'"
                f",'{self.data_atual}', 'TRUE');")
        cur.execute(sql)
        conn.commit()
        print("Cliente adicionado com sucesso")

    def update_client(self):
        cur.execute(f"UPDATE clientes SET nome = '{self.nome}',"
                    f"sobrenome = '{self.sobrenome}',"
                    f"cpf = '{self.cpf}', telefone = '{self.telefone}',"
                    f"data_de_nascimento = '{self.nascimento}'"
                    f"WHERE id = '{self.id_typed}';")
        conn.commit()
        print ("Cliente atualizado com sucesso")

    @staticmethod
    def delete_client():
        id_typed = int(input("Digite o ID do cliente para ser desativado:"))
        cur.execute(f"UPDATE clientes SET status = FALSE "
                    f"WHERE id = {id_typed}")
        conn.commit()
        print("Cliente desativado com sucesso")

    @staticmethod
    def activate_client():
        id_typed = int(input("Digite o ID do cliente para ser ativado:"))
        cur.execute(f"UPDATE clientes SET status = true "
                    f"WHERE id = {id_typed}")
        conn.commit()
        print("Cliente reativado com sucesso.")

    @staticmethod
    def show_options():
        print("[1] Para adicionar novos clientes")
        print("[2] Para listar todos os clientes ativos.")
        print("[3] Para listar todos os clientes desativados.")
        print("[4] Para reativar um cliente.")
        print("[5] Para desativar um cliente.")
        print("[6] Atualizar os clientes")
        print("[7] Para voltar ao menu principal")

    @staticmethod
    def list_ative_client():
        cur.execute("SELECT * FROM clientes WHERE status = true "
                    "ORDER BY id")
        result = cur.fetchall()
        for dados in result:
            data = datetime.strptime(f"{dados[5]}", '%Y-%m-%d')
            date = data.strftime('%d-%m-%Y')
            print (f"ID:{dados[0]} Nome:{dados[1]} Sobrenome:{dados[2]} "
                f"CPF:{dados[3]} Telefone:{dados[4]} Data de nascimento:{date} "
                f"Cliente desde {dados[6]}")

    @staticmethod  
    def list_desative_client():
        cur.execute("SELECT * FROM clientes WHERE status = false "
                    "ORDER BY id")
        result = cur.fetchall()
        for dados in result:
            data = datetime.strptime(f"{dados[5]}", '%Y-%m-%d')
            date = data.strftime('%d-%m-%Y')
            print (f"ID:{dados[0]} Nome:{dados[1]} Sobrenome:{dados[2]} "
                f"CPF:{dados[3]} Telefone:{dados[4]} Data de nascimento:{date} "
                f"Cliente desde {dados[6]}")

cur = conn.cursor()