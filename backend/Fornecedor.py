class Fornecedor:
    def __init__(self,nome,codigotenis,codigo):
        self.nome=nome
        self.codigotenis=codigotenis
        self.codigo=codigo
    def __str__(self):
        return f'nome: {self.nome}\ncodigotenis {self.codigotenis}\ncodigo {self.codigo}'