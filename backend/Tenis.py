class Tenis: 
    def __init__(self,modelo,preco,marca,ativo,cod):
        self.modelo=modelo
        self.preco=preco
        self.marca=marca
        self.cod=cod
        self.ativo=ativo

    def __str__(self):
        return f"modelo: {self.modelo}\npreco: {self.preco}\marca: {self.marca}\nStatus: {self.ativo}\nCodigo: {self.cod}"    
        
        