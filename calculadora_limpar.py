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
            recomendacao_pó = """
            Há pó no fundo da piscina. Recomenda-se o seguinte procedimento:
            1. **Aplicar o floculante:** Adicione a quantidade recomendada de floculante de acordo com o volume de água da piscina.
            2. **Aguarde 6 a 12 horas:** Deixe a piscina em repouso durante esse tempo para que as partículas em suspensão se aglomerem e sedimentem no fundo.
            3. **Aspiração:** Após o período de repouso, aspire cuidadosamente o fundo da piscina para remover os flocos que se formaram. Evite agitar a água durante a aspiração para não levantar novamente as partículas.
            """
        else:
            recomendacao_pó = ""
        
        # Exibir resultados no Label
        resultado = f"""
        Quantidade de Cloro Necessária: {cloro:.2f} gramas
        Produto para pH: {produto_ph} - Quantidade: {quantidade_ph:.2f} gramas
        Produto para Alcalinidade: {produto_alcalinidade} - Quantidade: {quantidade_alcalinidade:.2f} gramas
        {recomendacao_pó}
        """
        label_resultado.config(text=resultado)
    
    except ValueError:
        label_resultado.config(text="Erro: Por favor, insira valores numéricos válidos.")

# Função para limpar os campos de entrada e o resultado
def limpar():
    entry_volume.delete(0, tk.END)
    entry_ph.delete(0, tk.END)
    entry_alcalinidade.delete(0, tk.END)
    checkbox_pó.set(0)
    label_resultado.config(text="")  # Limpa o resultado exibido

# Função para adicionar efeitos de hover aos botões
def on_enter(e):
    e.widget.config(bg='white', fg='black', font=("Arial", 12, "bold"))
    e.widget.config(width=20, height=2)

def on_leave(e):
    e.widget.config(bg='#005f7f', fg='white', font=("Arial", 12, "bold"))
    e.widget.config(width=15, height=1)

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de Produtos Químicos para Piscinas")
janela.geometry("600x500")  # Define o tamanho da janela
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

# Labels
label_volume = tk.Label(janela, text="Volume da Piscina (litros):", bg='lightblue', fg='black', font=("Arial", 12, "bold"))
label_volume.grid(row=0, column=0, padx=10, pady=10)
entry_volume = tk.Entry(janela)
entry_volume.grid(row=0, column=1, padx=10, pady=10)

label_ph = tk.Label(janela, text="pH Atual da Água:", bg='lightblue', fg='black', font=("Arial", 12, "bold"))
label_ph.grid(row=1, column=0, padx=10, pady=10)
entry_ph = tk.Entry(janela)
entry_ph.grid(row=1, column=1, padx=10, pady=10)

label_alcalinidade = tk.Label(janela, text="Alcalinidade Atual da Água (ppm):", bg='lightblue', fg='black', font=("Arial", 12, "bold"))
label_alcalinidade.grid(row=2, column=0, padx=10, pady=10)
entry_alcalinidade = tk.Entry(janela)
entry_alcalinidade.grid(row=2, column=1, padx=10, pady=10)

# Checkbox para pó no fundo
checkbox_pó = tk.IntVar()
checkbox_pó_botao = tk.Checkbutton(janela, text="Piscina com pó no fundo?", variable=checkbox_pó, bg='lightblue', fg='black', font=("Arial", 12, "bold"))
checkbox_pó_botao.grid(row=3, columnspan=2, padx=10, pady=10)

# Botão para realizar o cálculo
botao_calcular = tk.Button(janela, text="Calcular", bg='#005f7f', fg='white', font=("Arial", 12, "bold"))
botao_calcular.grid(row=4, column=0, padx=10, pady=10)
botao_calcular.bind("<Enter>", on_enter)
botao_calcular.bind("<Leave>", on_leave)
botao_calcular.config(command=calcular)

# Botão para limpar os campos
botao_limpar = tk.Button(janela, text="Limpar", bg='#005f7f', fg='white', font=("Arial", 12, "bold"))
botao_limpar.grid(row=4, column=1, padx=10, pady=10)
botao_limpar.bind("<Enter>", on_enter)
botao_limpar.bind("<Leave>", on_leave)
botao_limpar.config(command=limpar)

# Label para exibir os resultados
label_resultado = tk.Label(janela, text="", justify="left", anchor="w", bg='lightblue', fg='black', font=("Arial", 12))
label_resultado.grid(row=5, columnspan=2, padx=10, pady=10)

# Iniciar o loop principal da janela
janela.mainloop()
