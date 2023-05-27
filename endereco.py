import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="admin",
    password="admin"
)

class Endereco:
    
    def __init__(self,cep,endereco,numero,complemento,bairro,cidade,estado,cliente_id):
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cliente_id = cliente_id
        
    def __repre__(self):
        return f"CEP:{self.cep}"\
                f"Endereço:{self.endereco}"\
                f"Numero:{self.numero}"\
                f"Complemento:{self.complemento}"\
                f"Bairro:{self.bairro}"\
                f"Cidade:{self.cidade}"\
                f"Estado:{self.estado}"\
                f"ID do cliente:{self.cliente_id}"

    def add_address(self):
        sql = (f"INSERT INTO enderecos(cep,endereco,numero,complemento,\
               bairro,cidade,estado,cliente_id)"\
              f"VALUES ('{self.cep}','{self.endereco}','{self.numero}',\
              '{self.complemento}','{self.bairro}','{self.cidade}',\
              '{self.estado}','{self.cliente_id}');")
        cur.execute(sql)
        conn.commit()
        print("Endereço adicionado com sucesso")

    def update_address(self):
        cur.execute(f"UPDATE enderecos SET cep = '{self.cep}',"
                    f"endereco = '{self.endereco}',"
                    f"numero = '{self.numero}',"
                    f"complemento = '{self.complemento}',"
                    f"bairro = '{self.bairro}',"
                    f"cidade = '{self.cidade}', estado = '{self.estado}'"
                    f"WHERE cliente_id = '{self.cliente_id}'")
        conn.commit()
        print ("Cliente atualizado com sucesso")

    def delete_address():
        id_typed = int(input("Diga o ID do cliente "
                             "para deletar o seu enredeço:"))
        cur.execute(f"DELETE FROM enderecos WHERE cliente_id = {id_typed}")
        conn.commit()
        print("Endereço removido com sucesso")
        
    @staticmethod
    def list_address():
        cur.execute("SELECT * FROM enderecos")
        result = cur.fetchall()
        for dados in result:
            print(f"CEP:{dados[1]} Endereço:{dados[2]} "
                f"Numero:{dados[3]} Complemento:{dados[4]}\n"
                f"Bairro:{dados[5]} Cidade:{dados[6]} "
                f"Estado:{dados[7]} ID do cliente:{dados[8]}\n")
            
    @staticmethod
    def show_options():
        print("[1] Para adicionar novos endereços")
        print("[2] Para listar todos os endereços")
        print("[3] Para atualizar um endereços já cadastrado")
        print("[4] Para remover algum endereços")
        print("[5] Para voltar ao menu principal")

cur = conn.cursor()
