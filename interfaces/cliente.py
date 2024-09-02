import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
from services.excel_service import carregar_produtos

def interface_cliente():
    janela_cliente = tk.Tk()
    janela_cliente.title("Cliente")
    
    try:
        df = carregar_produtos()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar produtos: {e}")
        return

    tk.Label(janela_cliente, text="Lista de Produtos", font=("Arial", 16)).pack(pady=10)
    
    selecoes = {}
    
    frame_produtos = tk.Frame(janela_cliente)
    frame_produtos.pack()
    
    for idx, row in df.iterrows():
        frame_produto = tk.Frame(frame_produtos, bd=2, relief="ridge", padx=10, pady=10)
        frame_produto.pack(fill="x", padx=10, pady=5)
        
        label_produto = tk.Label(frame_produto, text=f"{row['Produto']} - R${row['Preço']:.2f}", font=("Arial", 14))
        label_produto.pack(side="left")
        
        entry_quantidade = tk.Entry(frame_produto, width=5)
        entry_quantidade.pack(side="right")
        selecoes[row['Produto']] = entry_quantidade
    
    def gerar_relatorio():
        total = 0
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for produto, entry in selecoes.items():
            quantidade = int(entry.get()) if entry.get() else 0
            if quantidade > 0:
                preco = df.loc[df['Produto'] == produto, 'Preço'].values[0]
                subtotal = quantidade * preco
                total += subtotal
                pdf.cell(200, 10, txt=f"{produto} - {quantidade} x R${preco:.2f} = R${subtotal:.2f}", ln=True)
        pdf.cell(200, 10, txt=f"Total: R${total:.2f}", ln=True)
        pdf.output("relatorio.pdf")
        messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")

    tk.Button(janela_cliente, text="Gerar Relatório", command=gerar_relatorio).pack(pady=20)
    
    janela_cliente.mainloop()
