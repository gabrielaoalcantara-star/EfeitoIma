"""
Dashboard Efeito Ímã - Métrica iSB
Integração do pipeline de dados (Extração -> Zoneamento -> Visualização)
Execução: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import os

# Importando o módulo estrutural que criamos
import zoneamento

st.set_page_config(page_title="Efeito Ímã | iSB Metric", page_icon="⚽", layout="wide")

# --- Pipeline de Dados Integrado ---
@st.cache_data
def carregar_e_processar_dados(caminho_eventos, caminho_players):
    """
    Unifica a leitura dos dados locais e aplica as regras de negócio dos módulos externos.
    """
    # Verifica se os arquivos gerados pelo extract_statsbomb.py existem
    if not os.path.exists(caminho_eventos) or not os.path.exists(caminho_players):
        st.error(f"Arquivos CSV não encontrados. Rode o pipeline de extração primeiro.")
        return pd.DataFrame(), pd.DataFrame()
        
    # 1. Leitura dos CSVs base
    df_events = pd.read_csv(caminho_eventos)
    df_players = pd.read_csv(caminho_players)
    
    # 2. Aplicação do módulo de Zoneamento (x,y -> Zona e Valor xG)
    # Filtramos apenas eventos que possuem coordenadas X e Y para evitar erros
    df_com_xy = df_events.dropna(subset=['x', 'y']).copy()
    df_processado = zoneamento.aplicar_zoneamento_dataframe(df_com_xy, col_x='x', col_y='y')
    
    # 3. (Futuro) Aqui faremos o merge com df_players para rodar o cálculo Voronoi da Aula 7
    
    return df_processado, df_players

# Carregando os dados da base de testes (Jogo 3890282)
# O cache do Streamlit garante que isso rode rápido após a 1ª vez
df_eventos, df_jogadores = carregar_e_processar_dados('game_3890282_events.csv', 'game_3890282_players.csv')

# --- Interface do Dashboard ---
st.sidebar.title("Configurações do Pipeline")
st.sidebar.info("Base Estrutural: Conectada")

st.title("⚽ O Efeito Ímã: Ambiente de Teste")
st.markdown("Dashboard conectado ao pipeline de processamento. Abaixo, a validação da integração dos módulos.")

if not df_eventos.empty:
    aba1, aba2 = st.tabs(["Validação do Zoneamento", "Explorador de Dados Brutos"])
    
    with aba1:
        st.subheader("Distribuição de Eventos por Zona")
        st.write("Validação do módulo `zoneamento.py` aplicado à base de eventos.")
        
        # Conta quantos eventos ocorreram em cada zona e plota um gráfico nativo
        contagem_zonas = df_eventos['zona_campo'].value_counts().reset_index()
        contagem_zonas.columns = ['Zona do Campo', 'Quantidade de Eventos']
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.dataframe(contagem_zonas, use_container_width=True)
        with col2:
            st.bar_chart(data=contagem_zonas, x='Zona do Campo', y='Quantidade de Eventos')
            
    with aba2:
        st.subheader("Dataset Processado")
        st.write("Visão direta de como os dados saem do pipeline, já com o *xG base* atrelado.")
        # Mostra colunas chave, incluindo as novas colunas geradas pelo zoneamento
        colunas_display = ['id', 'type_name', 'player_name', 'x', 'y', 'zona_campo', 'xg_base_zona']
        
        # Filtra para mostrar apenas colunas que existem no dataframe
        colunas_existentes = [col for col in colunas_display if col in df_eventos.columns]
        st.dataframe(df_eventos[colunas_existentes].head(50), use_container_width=True)

else:
    st.warning("Aguardando carregamento dos dados para habilitar visualizações.")