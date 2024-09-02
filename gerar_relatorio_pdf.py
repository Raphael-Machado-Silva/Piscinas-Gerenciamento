from fpdf import FPDF
import pandas as pd

def gerar_relatorio_pdf(produtos):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Relatório de Produtos", ln=True, align='C')
    
    total = 0
    for produto, quantidade in produtos:
        # Buscar o preço do produto no arquivo Excel
        df_produtos = pd.read_excel('produtos.xlsx')
        preco = df_produtos[df_produtos['Nome'] == produto]['Preço'].values[0]
        total += preco * int(quantidade)
        linha = f"Produto: {produto}, Preço: {preco}, Quantidade: {quantidade}"
        pdf.cell(200, 10, txt=linha, ln=True)
    
    pdf.cell(200, 10, txt=f"Total: {total}", ln=True)
    
    pdf.output("relatorio.pdf")
