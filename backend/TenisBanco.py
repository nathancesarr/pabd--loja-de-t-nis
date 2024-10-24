import psycopg2
from backend.Tenis import Tenis

class TenisBanco:
    def _ini_(self):
           pass
    def get_all_tenis(self):
        
        conexao=psycopg2.connect(dbname='20221214010040',
                                user='postgres',
                                password='pabd',
                                host='localhost',
                                port=5432)
        cursor=conexao.cursor()
        codigosql="SELECT * FROM tenis"
        cursor.execute(codigosql)

        result=cursor.fetchall()
        conexao.commit()
        lista=[]

        if result != None:
            for tenis in result:   
                modelo=tenis[0]
                preco=tenis[2]
                marca=tenis[1]
                ativo=tenis[3]
                cod=tenis[4]
                tenis=Tenis(modelo,preco,marca,ativo,cod) 
                lista.append(tenis)  
        else:
            lista=None
        return lista
   
    def create_tenis(self,modelo,preco,marca,ativo,):
        conexao=psycopg2.connect(dbname='20221214010040',
                                user='postgres',
                                password='pabd',
                                host='localhost',
                                port=5432)
        cursor= conexao.cursor()
        codigosql=F"INSERT INTO tenis(modelo,preco,marca,ativo) VALUES ('{modelo}',{preco}, '{marca}','{ativo}')"
        cursor.execute(codigosql)
        conexao.commit()
        
    def update_status_by_false(self,cod):
        conexao=psycopg2.connect(dbname='20221214010040',
                                user='postgres',
                                password='pabd',
                                host='localhost',
                                port=5432)
        cursor= conexao.cursor()
        codigosql=f"UPDATE tenis SET ativo='false' WHERE codigotenis={cod}"
        cursor.execute(codigosql)
        conexao.commit()
        
    
    def atualizar(self,cod,modelo,preco,marca):
        conexao=psycopg2.connect(dbname='20221214010040',
                                user='postgres',
                                password='pabd',
                                host='localhost',
                                port=5432)
        cursor= conexao.cursor()
        codigosql=F"UPDATE tenis SET modelo= '{modelo}', preco={preco}, marca='{marca}' WHERE codigotenis={cod}"
        cursor.execute(codigosql)
        conexao.commit()
        
        
    
         