import psycopg2
from backend.Fornecedor import Fornecedor


class fornecedorBanco:
    def __init__(self):
          pass

    def get_all_fornecedor(self):

        conexao=psycopg2.connect(dbname='20221214010040',
                                user='postgres',
                                password='pabd',
                                host='localhost',
                                port=5432)
        cursor=conexao.cursor()
        codigosql="SELECT * FROM fornecedor"
        cursor.execute(codigosql)

        result=cursor.fetchall()
        conexao.commit()
        lista=[]

        if result != None:
            for fornecedor in result:   
                nome=fornecedor[0]
                codigotenis=fornecedor[1]
                codigo=fornecedor[2]
                forn=Fornecedor(nome,codigotenis,codigo)
                lista.append(forn)  
        else:
            lista=None
        return lista
