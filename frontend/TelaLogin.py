import tkinter as tk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.UsuarioBanco import UsuarioBanco
from frontend.TelaHome import run

def verificar_login():
    usuario_digitado = entrada_usuario.get()
    senha_digitada = entrada_senha.get()

    userBanc=UsuarioBanco()

    result=userBanc.get_usuario_por_nome(usuario_digitado)

    if result != None and result.senha==senha_digitada:
        run()
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x200")

# Criar os elementos da tela
rotulo_usuario = tk.Label(janela, text="Nome:")
rotulo_usuario.pack(pady=10)

entrada_usuario = tk.Entry(janela)
entrada_usuario.pack(pady=5)

rotulo_senha = tk.Label(janela, text="Senha:")
rotulo_senha.pack(pady=10)

entrada_senha = tk.Entry(janela, show='*')
entrada_senha.pack(pady=5)

botao_login = tk.Button(janela, text="Login", command=verificar_login)
botao_login.pack(pady=20)




janela.mainloop()
