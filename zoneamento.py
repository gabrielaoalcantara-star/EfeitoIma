"""
Módulo de Zoneamento e Valoração de Espaço - Projeto Efeito Ímã
--------------------------------------------------------------
Objetivo: Dividir o campo em 6 zonas estratégicas e atribuir
valores base de xG (Expected Goals) para cada uma, mapeando 
as coordenadas (x, y) dos eventos do StatsBomb.
"""

import pandas as pd

# Dicionário com os valores base de xG por zona (Valores de referência)
XG_POR_ZONA = {
    'Z1_Defesa': 0.001,
    'Z2_Meio_Defensivo': 0.005,
    'Z3_Meio_Ofensivo': 0.015,
    'Z4_Flancos_Ofensivos': 0.030,
    'Z5_Intermediaria_Ofensiva': 0.060,
    'Z6_Area_Penalti': 0.150
}

def classificar_zona(x, y):
    """
    Mapeia coordenadas (X, Y) do padrão StatsBomb (120x80) 
    para as 6 zonas estratégicas do campo.
    """
    # Zonas de Defesa e Meio-Campo
    if x < 40:
        return 'Z1_Defesa'
    elif 40 <= x < 60:
        return 'Z2_Meio_Defensivo'
    elif 60 <= x < 80:
        return 'Z3_Meio_Ofensivo'
    
    # Terço Final (x >= 80)
    else:
        # Área de Pênalti (aproximadamente x >= 102 e y entre 18 e 62)
        if x >= 102 and 18 <= y <= 62:
            return 'Z6_Area_Penalti'
        # Intermediária / Zona 14 (x entre 80 e 102, faixa central)
        elif 80 <= x < 102 and 18 <= y <= 62:
            return 'Z5_Intermediaria_Ofensiva'
        # Flancos (Tudo fora da faixa central no terço final)
        else:
            return 'Z4_Flancos_Ofensivos'

def obter_xg_zona(zona_nome):
    """
    Retorna o valor do xG atrelado àquela zona.
    """
    return XG_POR_ZONA.get(zona_nome, 0.0)

def aplicar_zoneamento_dataframe(df, col_x='x', col_y='y'):
    """
    Aplica as funções de mapeamento ao dataframe de eventos.
    """
    df_copy = df.copy()
    
    # Aplica a função para criar a coluna de zonas
    df_copy['zona_campo'] = df_copy.apply(lambda row: classificar_zona(row[col_x], row[col_y]), axis=1)
    
    # Mapeia o valor de xG para cada zona
    df_copy['xg_base_zona'] = df_copy['zona_campo'].map(XG_POR_ZONA)
    
    return df_copy

if __name__ == "__main__":
    # Teste rápido do script
    eventos_teste = pd.DataFrame([
        {'id_lance': 1, 'x': 20, 'y': 40, 'desc': 'Saída de bola'},
        {'id_lance': 2, 'x': 85, 'y': 10, 'desc': 'Ponta esquerda'},
        {'id_lance': 3, 'x': 90, 'y': 40, 'desc': 'Passe na zona 14'},
        {'id_lance': 4, 'x': 110, 'y': 40, 'desc': 'Finalização na área'}
    ])
    
    print("--- Teste de Zoneamento ---")
    df_resultado = aplicar_zoneamento_dataframe(eventos_teste)
    print(df_resultado[['desc', 'zona_campo', 'xg_base_zona']])