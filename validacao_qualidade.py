"""
Módulo de Validação de Qualidade de Dados - Projeto Efeito Ímã
--------------------------------------------------------------
Objetivo: Identificar gaps (dados faltantes, eventos órfãos) 
e ruídos (coordenadas fora do campo, duplicatas) nos dados do StatsBomb.
"""

import pandas as pd

def validar_coordenadas_ruido(df, col_x='x', col_y='y'):
    """
    Identifica ruídos de coordenadas fora dos limites padrão do campo (120x80).
    """
    if col_x not in df.columns or col_y not in df.columns:
        return 0, pd.DataFrame()
        
    ruidos = df[(df[col_x] < 0) | (df[col_x] > 120) | (df[col_y] < 0) | (df[col_y] > 80)]
    return len(ruidos), ruidos

def validar_gaps_nulos(df, colunas_criticas):
    """
    Identifica gaps (valores nulos) em colunas fundamentais para a análise.
    """
    relatorio_nulos = {}
    for col in colunas_criticas:
        if col in df.columns:
            qtd_nulos = df[col].isnull().sum()
            relatorio_nulos[col] = qtd_nulos
    return relatorio_nulos

def validar_integridade_360(df_eventos, df_players, chave_evento='id', chave_player='event_id'):
    """
    Verifica eventos que não possuem correspondência de tracking data no frame 360.
    Isso é um 'gap' estrutural grave para o modelo de Pitch Control.
    """
    if chave_evento not in df_eventos.columns:
        return 0
        
    ids_com_tracking = df_players[chave_player].unique() if chave_player in df_players.columns else df_players['id'].unique()
    
    # Quantos eventos de passe não tem a 'foto' 360 dos jogadores?
    passes = df_eventos[df_eventos['type_name'] == 'Pass']
    passes_sem_tracking = passes[~passes[chave_evento].isin(ids_com_tracking)]
    
    return len(passes_sem_tracking)

def gerar_relatorio_qualidade(caminho_eventos, caminho_players):
    """
    Lê os CSVs locais e gera um relatório consolidado de qualidade.
    """
    print(f"--- Relatório de Qualidade de Dados ---")
    
    try:
        df_eventos = pd.read_csv(caminho_eventos)
        df_players = pd.read_csv(caminho_players)
    except FileNotFoundError:
        print("Erro: Arquivos CSV não encontrados no diretório.")
        return

    # 1. Checagem de Nulos (Gaps)
    colunas_importantes = ['id', 'type_name', 'player_name', 'x', 'y']
    nulos = validar_gaps_nulos(df_eventos, colunas_importantes)
    print("\n1. Gaps (Valores Nulos em Eventos):")
    for col, qtd in nulos.items():
        print(f"   - {col}: {qtd} registros vazios")
        
    # 2. Checagem de Coordenadas (Ruídos)
    qtd_ruidos, _ = validar_coordenadas_ruido(df_eventos)
    print(f"\n2. Ruídos (Coordenadas fora do campo 120x80):")
    print(f"   - Encontrados {qtd_ruidos} eventos com anomalias de posição.")
    
    # 3. Integridade 360 (Gaps Estruturais)
    qtd_passes_orfãos = validar_integridade_360(df_eventos, df_players)
    print(f"\n3. Integridade do Tracking 360 (Gaps Estruturais):")
    print(f"   - {qtd_passes_orfãos} passes estão sem os dados de posicionamento 360.")
    print("---------------------------------------")

if __name__ == "__main__":
    # Apontando para os arquivos que vocês já têm no repositório
    gerar_relatorio_qualidade('game_3890282_events.csv', 'game_3890282_players.csv'