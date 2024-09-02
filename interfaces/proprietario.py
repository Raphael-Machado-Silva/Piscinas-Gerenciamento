import tkinter as tk
from tkinter import messagebox
from services.excel_service import carregar_produtos, salvar_produtos
import pandas as pd

# Declara a variável global df
df = pd.DataFrame()

def interface_proprietario():
    global df  # Declara df como global para garantir que a função possa modificá-la
    
    janela_proprietario = tk.Tk()
    janela_proprietario.title("Proprietário")
    
    try:
        df = carregar_produtos()  # Carrega os produtos
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar produtos: {e}")
        return

    tk.Label(janela_proprietario, text="Lista de Produtos", font=("Arial", 16)).pack(pady=10)
    
    frame_produtos = tk.Frame(janela_proprietario)
    frame_produtos.pack()
    
    def atualizar_interface():
        for widget in frame_produtos.winfo_children():
            widget.destroy()
        
        for idx, row in df.iterrows():
            frame_produto = tk.Frame(frame_produtos, bd=2, relief="ridge", padx=10, pady=10)
            frame_produto.pack(fill="x", padx=10, pady=5)
            
            label_produto = tk.Label(frame_produto, text=f"{row['Produto']} - R${row['Preço']:.2f}", font=("Arial", 14))
            label_produto.pack(side="left")
    
    atualizar_interface()
    
    tk.Label(janela_proprietario, text="Nome do Produto").pack()
    entry_nome = tk.Entry(janela_proprietario, width=30)
    entry_nome.pack()
    
    tk.Label(janela_proprietario, text="Preço do Produto").pack()
    entry_preco = tk.Entry(janela_proprietario, width=30)
    entry_preco.pack()
    
    def adicionar_produto():
        global df
        nome = entry_nome.get()
        preco = entry_preco.get()
        if not preco:
            messagebox.showerror("Erro", "O preço não pode estar vazio.")
            return
        try:
            preco = float(preco)
        except ValueError:
            messagebox.showerror("Erro", "O preço deve ser um número.")
            return
        
        if nome in df['Produto'].values:
            messagebox.showerror("Erro", "Produto já existe.")
            return
        
        novo_produto = pd.DataFrame({"Produto": [nome], "Preço": [preco]})
        df = pd.concat([df, novo_produto], ignore_index=True)
        salvar_produtos(df)
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        atualizar_interface()
    
    def remover_produto():
        global df
        nome = entry_nome.get()
        if nome not in df['Produto'].values:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return
        df = df[df['Produto'] != nome]
        salvar_produtos(df)
        messagebox.showinfo("Sucesso", "Produto removido com sucesso!")
        atualizar_interface()
    
    def alterar_preco():
        global df
        nome = entry_nome.get()
        preco = entry_preco.get()
        if not preco:
            messagebox.showerror("Erro", "O preço não pode estar vazio.")
            return
        try:
            preco = float(preco)
        except ValueError:
            messagebox.showerror("Erro", "O preço deve ser um número.")
            return
        
        if nome not in df['Produto'].values:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return
        
        df.loc[df['Produto'] == nome, 'Preço'] = preco
        salvar_produtos(df)
        messagebox.showinfo("Sucesso", "Preço alterado com sucesso!")
        atualizar_interface()
    
    tk.Button(janela_proprietario, text="Adicionar Produto", command=adicionar_produto).pack(pady=5)
    tk.Button(janela_proprietario, text="Remover Produto", command=remover_produto).pack(pady=5)
    tk.Button(janela_proprietario, text="Alterar Preço", command=alterar_preco).pack(pady=5)
    
    janela_proprietario.mainloop()
