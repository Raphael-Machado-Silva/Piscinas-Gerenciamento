import tkinter as tk
from tkinter import messagebox
import pandas as pd
from gerar_relatorio_pdf import gerar_relatorio_pdf

def verificar_login():
    nome = entry_nome.get()
    senha = entry_senha.get()
    
    df = pd.read_excel('usuarios.xlsx')
    
    if (df['Nome'] == nome).any() and (df['Senha'] == senha).any():
        if df[df['Nome'] == nome]['Tipo'].values[0] == 'cliente':
            abrir_interface_cliente()
        else:
            abrir_interface_proprietario()
    else:
        messagebox.showerror("Erro", "Nome ou senha incorretos")

def abrir_interface_cliente():
    root.destroy()
    
    cliente_window = tk.Tk()
    cliente_window.title("Cliente")

    tk.Label(cliente_window, text="Produto").grid(row=0)
    tk.Label(cliente_window, text="Quantidade").grid(row=1)
    
    produto_entry = tk.Entry(cliente_window)
    quantidade_entry = tk.Entry(cliente_window)

    produto_entry.grid(row=0, column=1)
    quantidade_entry.grid(row=1, column=1)

    produtos = []

    def adicionar_produto():
        produto = produto_entry.get()
        quantidade = quantidade_entry.get()
        produtos.append((produto, quantidade))
        messagebox.showinfo("Info", "Produto adicionado")

    def gerar_relatorio():
        if produtos:
            gerar_relatorio_pdf(produtos)
            messagebox.showinfo("Info", "Relatório gerado com sucesso")
        else:
            messagebox.showwarning("Aviso", "Nenhum produto adicionado")
    
    tk.Button(cliente_window, text="Adicionar Produto", command=adicionar_produto).grid(row=2, columnspan=2)
    tk.Button(cliente_window, text="Gerar Relatório", command=gerar_relatorio).grid(row=3, columnspan=2)

    cliente_window.mainloop()

def abrir_interface_proprietario():
    root.destroy()
    
    proprietario_window = tk.Tk()
    proprietario_window.title("Proprietário")

    tk.Label(proprietario_window, text="Produto").grid(row=0)
    tk.Label(proprietario_window, text="Preço").grid(row=1)
    
    produto_entry = tk.Entry(proprietario_window)
    preco_entry = tk.Entry(proprietario_window)

    produto_entry.grid(row=0, column=1)
    preco_entry.grid(row=1, column=1)

    def adicionar_produto():
        produto = produto_entry.get()
        preco = preco_entry.get()
        adicionar_produto_excel(produto, float(preco))
        messagebox.showinfo("Info", "Produto adicionado")

    def remover_produto():
        produto = produto_entry.get()
        remover_produto_excel(produto)
        messagebox.showinfo("Info", "Produto removido")
    
    tk.Button(proprietario_window, text="Adicionar Produto", command=adicionar_produto).grid(row=2, column=0)
    tk.Button(proprietario_window, text="Remover Produto", command=remover_produto).grid(row=2, column=1)
    
    proprietario_window.mainloop()

def adicionar_produto_excel(nome, preco):
    df = pd.read_excel('produtos.xlsx')
    df = df.append({'Nome': nome, 'Preço': preco}, ignore_index=True)
    df.to_excel('produtos.xlsx', index=False)

def remover_produto_excel(nome):
    df = pd.read_excel('produtos.xlsx')
    df = df[df['Nome'] != nome]
    df.to_excel('produtos.xlsx', index=False)

# Interface de login
root = tk.Tk()
root.title("Login")

tk.Label(root, text="Nome:").grid(row=0)
tk.Label(root, text="Senha:").grid(row=1)

entry_nome = tk.Entry(root)
entry_senha = tk.Entry(root, show="*")

entry_nome.grid(row=0, column=1)
entry_senha.grid(row=1, column=1)

tk.Button(root, text="Entrar", command=verificar_login).grid(row=2, columnspan=2)

root.mainloop()
