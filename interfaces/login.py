import tkinter as tk
from tkinter import messagebox
from services.excel_service import carregar_usuarios
from interfaces.cliente import interface_cliente
from interfaces.proprietario import interface_proprietario

def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    try:
        df = carregar_usuarios()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar usuários: {e}")
        return
    
    if usuario in df['Usuario'].values:
        senha_correta = df.loc[df['Usuario'] == usuario, 'Senha'].values[0]
        if senha == senha_correta:
            tipo_usuario = df.loc[df['Usuario'] == usuario, 'Tipo'].values[0]
            janela_login.destroy()
            if tipo_usuario == 'Proprietário':
                interface_proprietario()
            else:
                interface_cliente()
        else:
            messagebox.showerror("Erro", "Senha incorreta")
    else:
        messagebox.showerror("Erro", "Usuário não encontrado")

def interface_login():
    global janela_login, entry_usuario, entry_senha
    janela_login = tk.Tk()
    janela_login.title("Login")
    
    janela_login.geometry("300x200")  # Ajusta o tamanho da janela
    
    tk.Label(janela_login, text="Usuário").pack(pady=(20, 5))
    entry_usuario = tk.Entry(janela_login, width=30)
    entry_usuario.pack(pady=(0, 10))
    
    tk.Label(janela_login, text="Senha").pack(pady=(0, 5))
    entry_senha = tk.Entry(janela_login, show="*", width=30)
    entry_senha.pack(pady=(0, 20))
    
    tk.Button(janela_login, text="Entrar", command=verificar_login).pack()
    
    janela_login.mainloop()
