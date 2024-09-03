import tkinter as tk

# Função para calcular a quantidade de cloro
def calcular_cloro(volume):
    concentracao_desejada = 2.0  # Exemplo de concentração desejada de cloro em mg/L
    cloro_necessario = volume * concentracao_desejada * 0.02
    return cloro_necessario

# Função para calcular o ajuste de pH
def calcular_ajuste_ph(ph_atual, volume):
    ph_ideal = 7.4
    if ph_atual < ph_ideal:
        ajuste = (ph_ideal - ph_atual) * volume * 0.001
        return 'barrilha', ajuste  # Barrilha é usada para elevar o pH
    elif ph_atual > ph_ideal:
        ajuste = (ph_atual - ph_ideal) * volume * 0.001
        return 'ácido', ajuste  # Ácido é usado para reduzir o pH
    else:
        return 'pH está ideal', 0

# Função para calcular o ajuste de alcalinidade
def calcular_ajuste_alcalinidade(alcalinidade_atual, volume):
    alcalinidade_ideal = 100  # PPM ideal de alcalinidade
    if alcalinidade_atual < 80:
        ajuste = (80 - alcalinidade_atual) * volume * 0.0015
        return 'bicarbonato de sódio', ajuste  # Bicarbonato de sódio eleva a alcalinidade
    elif alcalinidade_atual > 120:
        ajuste = (alcalinidade_atual - 120) * volume * 0.0015
        return 'ácido', ajuste  # Ácido reduz a alcalinidade
    else:
        return 'Alcalinidade está ideal', 0

# Função principal para realizar todos os cálculos e exibir o resultado
def calcular():
    try:
        # Obter os valores de entrada
        volume = float(entry_volume.get())
        ph_atual = float(entry_ph.get())
        alcalinidade_atual = float(entry_alcalinidade.get())
        
        # Calcular quantidade de cloro necessária
        cloro = calcular_cloro(volume)
        
        # Calcular ajuste de pH
        produto_ph, quantidade_ph = calcular_ajuste_ph(ph_atual, volume)
        
        # Calcular ajuste de alcalinidade
        produto_alcalinidade, quantidade_alcalinidade = calcular_ajuste_alcalinidade(alcalinidade_atual, volume)
        
        # Verificar se há pó no fundo da piscina
        if checkbox_pó.get() == 1:
            recomendacao_pó = (
                "\nHá pó no fundo da piscina. Recomenda-se o seguinte procedimento:\n"
                "1. **Aplicar o floculante:** Adicione a quantidade recomendada de floculante de acordo com o volume de água da piscina.\n"
                "2. **Aguarde 6 a 12 horas:** Deixe a piscina em repouso durante esse tempo para que as partículas em suspensão se aglomerem e sedimentem no fundo.\n"
                "3. **Aspiração:** Após o período de repouso, aspire cuidadosamente o fundo da piscina para remover os flocos que se formaram. Evite agitar a água durante a aspiração para não levantar novamente as partículas."
            )
        else:
            recomendacao_pó = ""
        
        # Exibir resultados no widget Text
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

# Função para adicionar efeitos de hover aos botões
def on_enter(e):
    e.widget.config(bg='white', fg='black')

def on_leave(e):
    e.widget.config(bg='#005f7f', fg='white')

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de Produtos Químicos para Piscinas")
janela.geometry("1200x700")  # Atualizando a altura da janela para 700px
janela.resizable(False, False)  # Impede a mudança de tamanho da janela

# Definir o fundo da janela
janela.configure(bg='lightblue')

# Carregar uma imagem de fundo relacionada com piscinas
try:
    fundo_imagem = tk.PhotoImage(file="como-limpar-piscina.jpg")
    fundo_label = tk.Label(janela, image=fundo_imagem, bg='lightblue')
    fundo_label.place(relwidth=1, relheight=1)
except tk.TclError:
    print("Erro ao carregar a imagem de fundo. Certifique-se de que o arquivo 'como-limpar-piscina.jpg' está no mesmo diretório do código.")

# Adicionar um título
titulo = tk.Label(janela, text="Calculadora de Gerenciamento de Piscina", bg='lightblue', fg='black', font=("Arial", 18, "bold"))
titulo.pack(pady=(20, 10))  # Espaço acima e abaixo do título

# Frame para centralizar o conteúdo
frame_principal = tk.Frame(janela, bg='lightblue', width=1200, height=700)  # Atualizando a altura do frame
frame_principal.place(relx=0.5, rely=0.5, anchor='center')

# Labels
label_volume = tk.Label(frame_principal, text="Volume da Piscina (litros):", bg='lightblue', fg='black', font=("Arial", 12, "bold"))
label_volume.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_volume = tk.Entry(frame_principal, width=25, font=("Arial", 12))  # Ajustado o tamanho do input
entry_volume.grid(row=0, column=1, padx=10, pady=10)

label_ph = tk.Label(frame_principal, text="pH Atual da Água:", bg='lightblue', fg='black', font=("Arial", 12, "bold"))
label_ph.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_ph = tk.Entry(frame_principal, width=25, font=("Arial", 12))  # Ajustado o tamanho do input
entry_ph.grid(row=1, column=1, padx=10, pady=10)

label_alcalinidade = tk.Label(frame_principal, text="Alcalinidade Atual da Água (ppm):", bg='lightblue', fg='black', font=("Arial", 12, "bold"))
label_alcalinidade.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_alcalinidade = tk.Entry(frame_principal, width=25, font=("Arial", 12))  # Ajustado o tamanho do input
entry_alcalinidade.grid(row=2, column=1, padx=10, pady=10)

# Checkbox para pó no fundo
checkbox_pó = tk.IntVar()
checkbox_pó_botao = tk.Checkbutton(frame_principal, text="Piscina com pó no fundo?", variable=checkbox_pó, bg='lightblue', fg='black', font=("Arial", 12, "bold"))
checkbox_pó_botao.grid(row=3, columnspan=2, padx=10, pady=10, sticky="w")

# Botão para realizar o cálculo
botao_calcular = tk.Button(frame_principal, text="Calcular", bg='#005f7f', fg='white', font=("Arial", 12, "bold"))
botao_calcular.grid(row=4, column=0, padx=10, pady=10)
botao_calcular.bind("<Enter>", on_enter)
botao_calcular.bind("<Leave>", on_leave)
botao_calcular.config(command=calcular)

# Botão para limpar os campos
botao_limpar = tk.Button(frame_principal, text="Limpar", bg='#005f7f', fg='white', font=("Arial", 12, "bold"))
botao_limpar.grid(row=4, column=1, padx=10, pady=10)
botao_limpar.bind("<Enter>", on_enter)
botao_limpar.bind("<Leave>", on_leave)
botao_limpar.config(command=limpar)

# Widget Text para exibir os resultados
text_resultado = tk.Text(frame_principal, height=15, width=80, wrap='word', bg='white', fg='black', font=("Arial", 12))
text_resultado.grid(row=5, columnspan=2, padx=20, pady=10, sticky="n")

# Iniciar o loop principal da janela
janela.mainloop()
