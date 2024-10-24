class Usuario:
    def __init__(self,nome,senha,codigo):
        self.nome=nome
        self.senha=senha
        self.codigo=codigo

    def __str__(self):
        return f"Nome: {self.nome}\nSenha: {self.senha}\nCodigo: {self.codigo}"