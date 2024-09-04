# calculos.py

def calcular_cloro(volume):
    concentracao_desejada = 2.0  # Exemplo de concentração desejada de cloro em mg/L
    return volume * concentracao_desejada * 0.02

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
