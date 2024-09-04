# interface.py

import tkinter as tk
from tkinter import filedialog
from calculos import calcular_cloro, calcular_ajuste_ph, calcular_ajuste_alcalinidade
from utilitarios import on_enter, on_leave

def criar_interface():
    # Função principal para realizar todos os cálculos e exibir o resultado
    def calcular():
        try:
            volume = float(entry_volume.get())
            ph_atual = float(entry_ph.get())
            alcalinidade_atual = float(entry_alcalinidade.get())

            cloro = calcular_cloro(volume)
            produto_ph, quantidade_ph = calcular_ajuste_ph(ph_atual, volume)
            produto_alcalinidade, quantidade_alcalinidade = calcular_ajuste_alcalinidade(alcalinidade_atual, volume)

            if checkbox_pó.get() == 1:
                recomendacao_pó = (
                    "\nHá pó no fundo da piscina. Recomenda-se o seguinte procedimento:\n"
                    "1. **Aplicar o floculante:** Adicione a quantidade recomendada de floculante de acordo com o volume de água da piscina.\n"
                    "2. **Aguarde 6 a 12 horas:** Deixe a piscina em repouso durante esse tempo para que as partículas em suspensão se aglomerem e sedimentem no fundo.\n"
                    "3. **Aspiração:** Após o período de repouso, aspire cuidadosamente o fundo da piscina para remover os flocos que se formaram. Evite agitar a água durante a aspiração para não levantar novamente as partículas."
                )
            else:
                recomendacao_pó = ""

            resultado = (
                f"Quantidade de Cloro Necessária: {cloro:.2f} gramas\n"
                f"Produto para pH: {produto_ph} - Quantidade: {quantidade_ph:.2f} gramas\n"
                f"Produto para Alcalinidade: {produto_alcalinidade} - Quantidade: {quantidade_alcalinidade:.2f} gramas\n"
                f"{recomendacao_pó}"
            )
            text_resultado.delete(1.0, tk.END)
            text_resultado.insert(tk.END, resultado)

        except ValueError:
            text_resultado.delete(1.0, tk.END)
            text_resultado.insert(tk.END, "Erro: Por favor, insira valores numéricos válidos.")

    # Função para limpar os campos de entrada e o resultado
    def limpar():
        entry_volume.delete(0, tk.END)
        entry_ph.delete(0, tk.END)
        entry_alcalinidade.delete(0, tk.END)
        checkbox_pó.set(0)
        text_resultado.delete(1.0, tk.END)  # Limpa o resultado exibido

    # Função para salvar o resumo em um arquivo de texto
    def salvar_resumo():
        resumo = text_resultado.get(1.0, tk.END).strip()
        if resumo:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(resumo)

    # Criando a janela principal
    janela = tk.Tk()
    janela.title("Calculadora de Produtos Químicos para Piscinas")
    janela.geometry("1200x700")
    janela.resizable(False, False)
    janela.configure(bg='lightblue')

    # Carregar uma imagem de fundo relacionada com piscinas
    try:
        fundo_imagem = tk.PhotoImage(file="como-limpar-piscina.jpg")
        fundo_label = tk.Label(janela, image=fundo_imagem, bg='lightblue')
        fundo_label.place(relwidth=1, relheight=1)
    except tk.TclError:
        print("Erro ao carregar a imagem de fundo. Certifique-se de que o arquivo 'como-limpar-piscina.jpg' está no mesmo diretório do código.")

    titulo = tk.Label(janela, text="Calculadora de Gerenciamento de Piscina", bg='lightblue', fg='black', font=("Arial", 18, "bold"))
    titulo.pack(pady=(20, 10))

    frame_principal = tk.Frame(janela, bg='lightblue', width=1200, height=700)
    frame_principal.place(relx=0.5, rely=0.5, anchor='center')

    label_volume = tk.Label(frame_principal, text="Volume da Piscina (litros):", bg='lightblue', fg='black', font=("Arial", 12, "bold"))
    label_volume.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_volume = tk.Entry(frame_principal, width=25, font=("Arial", 12))
    entry_volume.grid(row=0, column=1, padx=10, pady=10)

    label_ph = tk.Label(frame_principal, text="pH Atual da Água:", bg='lightblue', fg='black', font=("Arial", 12, "bold"))
    label_ph.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_ph = tk.Entry(frame_principal, width=25, font=("Arial", 12))
    entry_ph.grid(row=1, column=1, padx=10, pady=10)

    label_alcalinidade = tk.Label(frame_principal, text="Alcalinidade Atual da Água (ppm):", bg='lightblue', fg='black', font=("Arial", 12, "bold"))
    label_alcalinidade.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_alcalinidade = tk.Entry(frame_principal, width=25, font=("Arial", 12))
    entry_alcalinidade.grid(row=2, column=1, padx=10, pady=10)

    checkbox_pó = tk.IntVar()
    checkbox_pó_botao = tk.Checkbutton(frame_principal, text="Piscina com pó no fundo?", variable=checkbox_pó, bg='lightblue', fg='black', font=("Arial", 12, "bold"))
    checkbox_pó_botao.grid(row=3, columnspan=2, padx=10, pady=10, sticky="w")

    frame_botoes = tk.Frame(frame_principal, bg='lightblue')
    frame_botoes.grid(row=4, columnspan=2, pady=10)

    botao_calcular = tk.Button(frame_botoes, text="Calcular", bg='#005f7f', fg='white', font=("Arial", 12, "bold"))
    botao_calcular.grid(row=0, column=0, padx=10)
    botao_calcular.bind("<Enter>", on_enter)
    botao_calcular.bind("<Leave>", on_leave)
    botao_calcular.config(command=calcular)

    botao_limpar = tk.Button(frame_botoes, text="Limpar", bg='#005f7f', fg='white', font=("Arial", 12, "bold"))
    botao_limpar.grid(row=0, column=1, padx=10)
    botao_limpar.bind("<Enter>", on_enter)
    botao_limpar.bind("<Leave>", on_leave)
    botao_limpar.config(command=limpar)

    botao_salvar = tk.Button(frame_botoes, text="Baixar Resumo", bg='#005f7f', fg='white', font=("Arial", 12, "bold"))
    botao_salvar.grid(row=0, column=2, padx=10)
    botao_salvar.bind("<Enter>", on_enter)
    botao_salvar.bind("<Leave>", on_leave)
    botao_salvar.config(command=salvar_resumo)

    text_resultado = tk.Text(frame_principal, height=15, width=80, wrap='word', bg='white', fg='black', font=("Arial", 12))
    text_resultado.grid(row=5, columnspan=2, padx=20, pady=10, sticky="n")

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
