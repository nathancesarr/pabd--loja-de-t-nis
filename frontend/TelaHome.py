import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.TenisBanco import TenisBanco
from backend.fornecedorBanco import fornecedorBanco



def criar_tabela():

    # Criação da janela principal
        root = tk.Tk()
        root.title("Tabela de Produtos")

        # Criação da tabela
        columns = ("modelo", "preco", "marca", "codigo")
        tree = ttk.Treeview(root, columns=columns, show="headings")
        tree.heading("modelo", text="Modelo")
        tree.heading("preco", text="Preço")
        tree.heading("marca", text="Marca")
        tree.heading("codigo", text="Codigo")

        # Ajuste das larguras das colunas
        tree.column("modelo", width=100)
        tree.column("preco", width=100)
        tree.column("marca", width=100)
        tree.column("codigo", width=100)

        # Inserindo valores pré-definidos na tabela
        tb=TenisBanco()
        dados=tb.get_all_tenis()

        for item in dados:
            if item.ativo==True:
                tree.insert("", tk.END, values=(item.modelo,item.preco,item.marca,item.cod))

        tree.pack(pady=10)

        # Iniciar a aplicação
        root.mainloop()

def adicionarTenis():

    global entry_marca
    global entry_modelo
    global entry_preco
    global entry_fornecedor

    janela=tk.Tk()
    label_modelo=tk.Label(janela,text="modelo ")
    label_modelo.pack()

    entry_modelo=tk.Entry(janela)
    entry_modelo.pack()

    label_preco=tk.Label(janela,text="preço ")
    label_preco.pack()

    entry_preco=tk.Entry(janela)
    entry_preco.pack()

    label_marca=tk.Label(janela,text="marca ")
    label_marca.pack()

    entry_marca=tk.Entry(janela)
    entry_marca.pack()

    #label=tk.Label(janela,text="codigo do fornecedor")
    #label.pack()

    #entry_fornecedor=tk.Entry(janela)
    #entry_fornecedor.pack()

    botao=tk.Button (janela,text="adicionar",command=add_tenis)
    botao.pack()

    janela.geometry("300x200")
    janela.mainloop()

def add_tenis():
    global entry_marca
    global entry_modelo
    global entry_preco

    marca= entry_marca.get()
    modelo= entry_modelo.get()
    preco= entry_preco.get()
    status='true'

    tb= TenisBanco()
    try:
        criar=tb.create_tenis(modelo,preco,marca,status)
        messagebox.showinfo('ADCIONADO','tênis adicionado com sucesso')
    except:
        messagebox.showerror('NAO ADICIONADO','ERROR')

def deletarTenis(): 
    global entry_cod
    janela=tk.Tk()
    janela.title("deletar")
    labelcod=tk.Label(janela,text="Digite o codigo do tenis que você quer remover")
    labelcod.pack()

    entry_cod=tk.Entry(janela)
    entry_cod.pack()

    botao=tk.Button (janela,text="deletar",command=remover_tenis)
    botao.pack()

    janela.geometry("300x200")
    janela.mainloop()

def remover_tenis():
    global entry_cod
    cod=entry_cod.get()

    tb=TenisBanco()
    try:
        remover=tb.update_status_by_false(cod)
        messagebox.showinfo("DELETE", "tênis removido")
    except: 
        messagebox.showerror("error","ERROR")

def atualizarTenis():
    global entry_marca
    global entry_modelo
    global entry_preco
    global entry_cod

    janela=tk.Tk()
    janela.title("atualizar")
    label_codigo=tk.Label(janela,text="Digite o codigo do tenis que você quer atualizar ")
    label_codigo.pack()

    entry_cod=tk.Entry(janela)
    entry_cod.pack()

    label_modelo=tk.Label(janela,text="modelo ")
    label_modelo.pack()

    entry_modelo=tk.Entry(janela)
    entry_modelo.pack()

    label_preco=tk.Label(janela,text="preço ")
    label_preco.pack()

    entry_preco=tk.Entry(janela)
    entry_preco.pack()

    label_marca=tk.Label(janela,text="marca ")
    label_marca.pack()

    entry_marca=tk.Entry(janela)
    entry_marca.pack()

    botao=tk.Button (janela,text="atualizar",command=atualizar)
    botao.pack()

    janela.geometry("300x200")
    janela.mainloop()

def atualizar():
    global entry_marca
    global entry_modelo
    global entry_preco
    global entry_cod

    marca= entry_marca.get()
    modelo=entry_modelo.get()
    preco=entry_preco.get()
    cod=entry_cod.get()

    tb=TenisBanco()
    try:
        atualizar=tb.atualizar(cod,modelo,preco,marca)
        messagebox.showinfo("atualizado", " Tenis atualizado com sucesso")
    except:
        messagebox.showerror("error", "ERROR")

def tabelafornecedores():
    root = tk.Tk()
    root.title("Tabela de Produtos")

    # Criação da tabela
    columns = ("nome", "codigo_tenis", "codigo")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("nome", text="nome")
    tree.heading("codigo_tenis", text="codigo_tenis")
    tree.heading("codigo", text="codigo")


    # Ajuste das larguras das colunas
    tree.column("nome", width=100)
    tree.column("codigo_tenis", width=100)
    tree.column("codigo", width=100)
    
    # Inserindo valores pré-definidos na tabela
    fornecedor=fornecedorBanco()
    dados=fornecedor.get_all_fornecedor()



    for item in dados:
        tree.insert("", tk.END, values=(item.nome,item.codigotenis,item.codigo))

    tree.pack(pady=10)

    # Iniciar a aplicação
    root.mainloop()

def run():
    janela=tk.Tk()
    label= tk.Label(janela, text=" bem vindo a minha loja de tênis ")
    label.pack(pady=5)
    janela.geometry("300x200")
    janela.title("Loja de Tênis ")

    tabela=tk.Button (janela, text=" ver lista de tênis ", command=criar_tabela)
    tabela.pack()

    criar=tk.Button (janela, text=" adicionar tenis ", command=adicionarTenis)
    criar.pack()

    deletar=tk.Button (janela, text=" deletar tenis ", command=deletarTenis)
    deletar.pack()

    atualizar=tk.Button (janela, text=" atualizar tenis ", command=atualizarTenis)
    atualizar.pack()

    botao_fornecedor = tk.Button(janela, text= "fornecedores", command=tabelafornecedores)
    botao_fornecedor.pack()

    #botao_adicionarF = tk.Button(janela, text=) "fo"

    janela.mainloop()
 
 







