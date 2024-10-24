import psycopg2 
from backend.Usuario import Usuario 


class UsuarioBanco:
    def _init_ (self):
        pass
    def get_usuario_por_nome(self,nome):
        banco_conexao=psycopg2.connect (dbname= '20221214010040',
                                        user= 'postgres',
                                        password= 'pabd',
                                        host= 'localhost',
                                        port= 5432
        )

        cursor=banco_conexao.cursor ()
        cod_sql= "SELECT * FROM usuario WHERE nome ='"+ nome+"';"
        cursor.execute(cod_sql)
        result=cursor.fetchone()
        banco_conexao.commit()
        banco_conexao.close()


        if result != None:
            nome_usuario= result[0]
            senha_usuario= result[1]
            cod_usuario= result[2]
            usuario= Usuario(nome_usuario,senha_usuario,cod_usuario)

        else:
            usuario= None 

        return usuario  

