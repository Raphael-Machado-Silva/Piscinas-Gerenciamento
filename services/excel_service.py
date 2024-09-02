import pandas as pd

def carregar_usuarios():
    try:
        df = pd.read_excel('data/usuarios.xlsx')
        if 'Senha' not in df.columns or 'Usuario' not in df.columns or 'Tipo' not in df.columns:
            raise ValueError("O arquivo de usuários deve conter as colunas 'Usuario', 'Senha' e 'Tipo'.")
        return df
    except Exception as e:
        raise Exception(f"Erro ao carregar usuários: {e}")

def carregar_produtos():
    try:
        df = pd.read_excel('data/produtos.xlsx')
        if 'Produto' not in df.columns or 'Preço' not in df.columns:
            raise ValueError("O arquivo de produtos deve conter as colunas 'Produto' e 'Preço'.")
        df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')  # Garante que os preços sejam numéricos
        return df
    except Exception as e:
        raise Exception(f"Erro ao carregar produtos: {e}")

def salvar_produtos(df):
    try:
        df.to_excel('data/produtos.xlsx', index=False)
    except Exception as e:
        raise Exception(f"Erro ao salvar produtos: {e}")
