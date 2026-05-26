# 📋 Escopo de Tarefas - EfeitoIma
## Métrica de Efeito do Jogador Sem Bola
**Versão Final | 26/05/2026**

---

## 🎯 Visão Geral do Projeto

**Objetivo:** Criar uma métrica unificada que mensure o efeito da movimentação de um jogador **sem a bola**, transformando esse valor em uma contribuição individual à **chance de gol** (xG incrementado) dependendo do espaço do campo.

**Escopo Final (1 mês):**
- ✅ Métrica **iSB** (incremental Shot Build value)
- ✅ Dashboard interativo Streamlit (10 jogadores)
- ✅ Código organizado + documentação
- ✅ Deploy online (Streamlit Cloud)


## 🗓️ ROADMAP DE 4 SEMANAS

### **SEMANA 1 - Fundação (4-5h)**

**Objetivos:** Exploração de dados + Zoneamento + Setup Streamlit

#### Card 1.1 - Explorar Dados (Rápido)
- [ ] Identificar e documentar estrutura tracking data
- [ ] Selecionar e filtrar os 10 jogadores
- [ ] Validar qualidade (gaps, ruídos)
- [ ] Criar script básico de carregamento

**Tempo:** 2-3h | **Com IA:** Gera exploração automática

---

#### Card 1.2 - Definir Zoneamento
- [ ] Dividir campo em 6 zonas estratégicas
- [ ] Definir valores xG por zona
- [ ] Criar funções de mapeamento (x,y) → zona

**Tempo:** 1-2h | **Com IA:** Template pronto

---

#### Card 1.3 - Setup Streamlit
- [ ] Instalar dependências
- [ ] Estrutura base do app
- [ ] Load dos dados dos 10 jogadores

**Tempo:** 1h | **Com IA:** Boilerplate pronto

---

### **SEMANA 2 - Features + Modelo (5-6h)**

**Objetivos:** Extrair features essenciais + Treinar baseline

#### Card 2.1 - Features Cinemáticas
- [ ] Velocidade instantânea
- [ ] Aceleração
- [ ] Distância para meta adversária
- [ ] Proximidade de defensores

**Tempo:** 4h | **Com IA:** Gera todo o código NumPy/Pandas

---

#### Card 3.1 - Modelo Baseline
- [ ] Treinar regressão logística (6-8 features)
- [ ] Feature importance
- [ ] Cross-validation (5-fold)
- [ ] Métricas: AUC, Brier Score

**Tempo:** 3-4h | **Com IA:** Código sklearn pronto

---

### **SEMANA 3 - Métrica + Dashboard Estrutura (5-6h)**

**Objetivos:** Métrica iSB + Abas do dashboard

#### Card 3.4 - Métrica iSB
- [ ] Fórmula: iSB = P(xG | movimento) vs baseline
- [ ] Normalizar para escala 0-100
- [ ] Calcular para os 10 jogadores

**Tempo:** 2-3h | **Com IA:** Implementação pronta

---

#### Card 4.2 - Dashboard: Abas Principais
**Aba 1 - Visão Geral:**
- [ ] Ranking dos 10 em iSB
- [ ] Cards com estatísticas principais
- [ ] Gráfico de distribuição por zona

**Aba 2 - Comparação:**
- [ ] Dropdown: selecionar 2-3 jogadores
- [ ] Gráfico comparativo (barras)
- [ ] Heatmaps lado a lado

**Aba 3 - Detalhes:**
- [ ] Dropdown: selecionar 1 jogador
- [ ] Mapa de calor (todas as posições)
- [ ] Série temporal (últimos 10 jogos)

**Tempo:** 6-7h | **Com IA:** Código Streamlit pronto

---

### **SEMANA 4 - Visualizações + Deploy (5-6h)**

**Objetivos:** Dashboard polido + Deploy online

#### Card 4.3 - Visualizações Avançadas
- [ ] Heatmap 2D (kernel density)
- [ ] Scatter plots interativos (Plotly)
- [ ] Radar charts comparativos
- [ ] Ajustes estéticos (cores, fonts)

**Tempo:** 3-4h | **Com IA:** Gera gráficos, você integra

---

#### Card 6.2 - Deploy + Documentação
- [ ] README com instruções
- [ ] Guia de uso do dashboard
- [ ] Deploy Streamlit Cloud (1 clique)
- [ ] Documentação da métrica iSB

**Tempo:** 2-3h | **Com IA:** Redige docs, você edita

---

## 📊 RESUMO EXECUTIVO

### Entregáveis Finais

| Item | Status | Resultado |
|------|--------|-----------|
| **Dados** | ✅ | 10 jogadores explorados + limpos |
| **Features** | ✅ | 4 features essenciais extraídas |
| **Modelo** | ✅ | Regressão logística treinada + validada |
| **Métrica iSB** | ✅ | Calculada para 10 jogadores |
| **Dashboard** | ✅ | Streamlit interativo (3 abas) |
| **Visualizações** | ✅ | Heatmaps, scatter, radar, série temporal |
| **Deploy** | ✅ | Online em Streamlit Cloud |
| **Documentação** | ✅ | README + guia de uso |

### Tempo Total

| Semana | Atividade | Horas |
|--------|-----------|-------|
| **1** | Fundação | 4-5h |
| **2** | Features + Modelo | 5-6h |
| **3** | Métrica + Dashboard | 5-6h |
| **4** | Visualizações + Deploy | 5-6h |
| **TOTAL** | | **19-23h** |

**Tempo dedicado:** ~5h/semana = **Dentro do orçamento** ✅

---

## 🏗️ TECNOLOGIA DO DASHBOARD

### Framework: **Streamlit**

**Por que Streamlit?**
```
✅ Python puro (sem JS/HTML)
✅ Código simples (50-150 linhas)
✅ Deploy grátis em Streamlit Cloud
✅ Reloads automáticos (ótimo para dev)
✅ IA consegue gerar 100% do código
```

### Estrutura do App

```python
# streamlit_app.py (~150 linhas)

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Config
st.set_page_config(page_title="EfeitoIma", layout="wide")

# 2. Load data (10 jogadores)
@st.cache_data
def load_data():
    return pd.read_csv("data/players_10.csv")

df = load_data()

# 3. Sidebar navigation
page = st.sidebar.radio(
    "Escolha a visualização",
    ["📊 Visão Geral", "🔍 Comparação", "👤 Detalhes"]
)

# 4. Conteúdo por página
if page == "📊 Visão Geral":
    show_overview(df)
elif page == "🔍 Comparação":
    show_comparison(df)
else:
    show_details(df)
```

### Abas do Dashboard

```
┌─────────────────────────────────────┐
│ EfeitoIma - Análise de Movimento    │
├─────────────────────────────────────┤
│ 📊 Visão Geral | 🔍 Comparação | 👤 Detalhes │
└─────────────────────────────────────┘

📊 VISÃO GERAL:
├─ Ranking dos 10 (Tabela)
├─ Cards: iSB médio, top jogador, distribuição
└─ Gráfico: iSB por zona

🔍 COMPARAÇÃO:
├─ Dropdown 1: [João Silva]
├─ Dropdown 2: [Pedro Santos]
├─ Dropdown 3: [Opcional]
├─ Gráfico barras: Comparação iSB
├─ Heatmaps lado a lado
└─ Série temporal comparada

👤 DETALHES:
├─ Dropdown: [Selecionar jogador]
├─ Card perfil (nome, posição, minutos)
├─ Mapa de calor (grande)
├─ Série temporal (10 últimos jogos)
└─ Scatter plots (correlações)
```

---

## 💡 COMO USAR IA PARA SER RÁPIDO

### Pattern 1: Gerar Código

```
PROMPT:
"Cria função para calcular velocidade instantânea 
de cada jogador a partir de (x, y) por timestamp"

IA: [Gera 15 linhas de código pronto]

VOCÊ: Copia, testa, ajusta se necessário
```

### Pattern 2: Gerar Visualizações

```
PROMPT:
"Cria scatter plot interativo (Plotly) com:
- X: Velocidade média
- Y: iSB
- Cor: Posição
- Hover: Nome"

IA: [Código plotly pronto]

VOCÊ: Insere no Streamlit
```

### Pattern 3: Exploração de Dados

```
PROMPT:
"Explore esses dados de tracking e retorne:
- Estrutura (colunas, tipos)
- Distribuição de eventos
- Gaps/ruídos
- Estatísticas por jogador"

IA: [Análise completa com gráficos]

VOCÊ: Valida + toma decisões
```

### Pattern 4: Documentação

```
PROMPT:
"Documenta a métrica iSB de forma clara para 
usuários não-técnicos (explicar fórmula + interpretação)"

IA: [Redige seção inteira]

VOCÊ: Edita, melhora, aprova
```

---

## 🚀 DEPLOY EM STREAMLIT CLOUD

**Tempo total:** 15 minutos

```bash
# 1. Criar conta grátis em:
https://streamlit.io/cloud

# 2. Conectar seu GitHub
# 3. Selecionar repositório:
#    gabrielaoalcantara-star/EfeitoIma

# 4. Selecionar arquivo:
#    streamlit_app.py

# 5. Deploy automático!
# URL final: https://efeitoimadashboard.streamlit.app
```

**Benefícios:**
- ✅ Grátis (até 3 apps)
- ✅ Atualiza automaticamente ao fazer push
- ✅ HTTPS + SSL
- ✅ Compartilhável em qualquer lugar

---

## 📋 CHECKLIST FINAL

### Semana 1
- [ ] Dados explorados e filtrados (10 jogadores)
- [ ] Script de carregamento funcionando
- [ ] Zoneamento definido (6 zonas)
- [ ] Streamlit básico rodando

### Semana 2
- [ ] Features cinemáticas extraídas
- [ ] Modelo baseline treinado
- [ ] Feature importance documentada
- [ ] Validação cruzada 5-fold OK

### Semana 3
- [ ] Métrica iSB calculada
- [ ] Aba Visão Geral funcional
- [ ] Aba Comparação funcional
- [ ] Aba Detalhes funcional

### Semana 4
- [ ] Todas as visualizações integradas
- [ ] Dashboard polido (cores, layout)
- [ ] README completo
- [ ] Deploy em Streamlit Cloud live

---

## 🎯 PRÓXIMOS PASSOS (HOJE)

**Para começar agora, preciso de:**

1. **Os 10 jogadores:** Nomes, IDs ou posições
2. **Período dos dados:** Que temporada/competição
3. **Formato dos dados:** CSV, JSON, Parquet?
4. **Amostra dos dados:** Um arquivo sample para explorar

**Uma vez que tiver essas informações, vou criar:**
- ✅ Notebook exploratório completo
- ✅ Script de carregamento
- ✅ Primeiras visualizações

**Você executa e iteramos!**



## 📈 RESUMO DO QUE VOCÊ TERÁ EM 1 MÊS (COM DASHBOARD)

| Item | Status | Tempo |
|------|--------|-------|
| **Dados explorados (10 jogadores)** | ✅ | 2-3h |
| **Zoneamento definido** | ✅ | 1-2h |
| **Features (4 essenciais)** | ✅ | 4h |
| **Modelo baseline** | ✅ | 3-4h |
| **Métrica iSB** | ✅ | 2-3h |
| **Dashboard Streamlit interativo** | ✅ | 8-10h |
| **Visualizações avançadas** | ✅ | 3-4h |
| **Documentação + Deploy** | ✅ | 2-3h |
| **TOTAL** | | **25-29h** |

**COM IA:** Você faz ~50% desse trabalho (o resto é IA gerando código/análises)

---

## 🎬 ROADMAP DE 1 MÊS (4-6h/semana) — DASHBOARD FIRST

```
SEMANA 1 (4-5h) ⚡ FUNDAÇÃO
├─ Seg-Ter: Card 1.1 Explorar Dados → 2-3h
│           (Selecionar 10 jogadores chave)
├─ Qua-Qui: Card 1.2 Zoneamento → 1-2h
└─ Sex: Setup inicial Streamlit → 1h

SEMANA 2 (5-6h) 🔧 FEATURES + MODELO
├─ Seg-Qua: Card 2.1 Features → 4h
│           (Velocidade, aceleração, distância, defesa)
├─ Qui-Sex: Card 3.1 Baseline Model → 3-4h
│           (Treina, valida, feature importance)
└─ Fim de semana: Testes + ajustes → 1-2h

SEMANA 3 (5-6h) 📊 DASHBOARD ESTRUTURA
├─ Seg-Ter: Card 3.4 Métrica iSB → 2-3h
│           (Calcula scores 10 jogadores)
├─ Qua-Sex: Card 4.2 Dashboard Streamlit → 6-7h
│           ├─ Aba 1: Ranking dos 10 (iSB, estatísticas)
│           ├─ Aba 2: Comparação entre 2-3 jogadores
│           ├─ Aba 3: Detalhes individuais (heatmap, série)
│           └─ Testes + deploy local
└─ Fim de semana: Primeira versão funcional → 1-2h

SEMANA 4 (5-6h) 🎨 DASHBOARD FINAL
├─ Seg-Ter: Card 4.3 Visualizações → 3-4h
│           (Heatmaps, scatter, radar charts)
├─ Qua-Sex: Integrar visualizações + ajustes estéticos → 3-4h
│           (Cores, layout, responsividade)
├─ Sábado: Documentação + README → 2h
│          (Como usar o dashboard, limites, próximos passos)
└─ Domingo: Deploy Streamlit Cloud → 1h
            (Live e acessível)


TEMPO TOTAL: ~25h em 4 semanas = 6h/semana (cabe no seu orçamento!)
```

---

## � DASHBOARD STREAMLIT — ESCOPO COM 10 JOGADORES

### Por que é bem mais rápido?

| Aspecto | 100+ jogadores | 10 jogadores | Economia |
|--------|---|---|---|
| **Tamanho dados** | ~2GB tracking data | ~500MB | -75% |
| **Cálculos** | Otimização necessária | Direto em memória | -90% |
| **Filtros** | 50+ opções de filtro | Dropdown simples | -95% |
| **Cache/DB** | Redis/Postgres necessário | CSV/Parquet local | -100% |
| **Testes** | 2-3h por versão | 10-15 min | -90% |
| **Deploy** | Server dedicado | Streamlit Cloud grátis | -100% |

**Resultado:** Dashboard implementável em **8-10h em vez de 20-25h**

---

### 🎯 Escopo do Dashboard (10 Jogadores)

#### **ABAs do Dashboard:**

**1️⃣ VISÃO GERAL**
```
┌─────────────────────────────────────┐
│ EfeitoIma - Análise de Movimento    │
├─────────────────────────────────────┤
│                                     │
│ 📊 Ranking dos 10 Jogadores         │
│                                     │
│ Nome        | iSB | iSB/90 | Posição│
│ João Silva  | 8.5 |  2.1   | Atacante
│ ...         |     |        |        │
│                                     │
│ 📈 Distribuição por Zona            │
│ [Gráfico: iSB_ataque vs meio vs def]│
│                                     │
└─────────────────────────────────────┘
```

**2️⃣ COMPARAÇÃO (2-3 jogadores)**
```
Selecione 2-3 jogadores para comparar:
[Dropdown 1: João Silva]
[Dropdown 2: Pedro Santos]

📊 Comparativo iSB
[Gráfico de barras]

🔥 Heatmaps lado a lado
[Mapa 1] [Mapa 2]

📉 Série temporal (últimos 10 jogos)
[Gráfico linha: iSB ao longo do tempo]
```

**3️⃣ DETALHES DO JOGADOR**
```
Selecione um jogador:
[Dropdown: Todos os 10]

👤 João Silva
📍 Posição: Atacante
⏱️ Minutos: 1.245
📊 iSB: 8.5 | iSB/90: 2.1

🗺️ Mapa de calor (últimas 5 partidas)
[Heatmap grande]

📈 Série temporal
[Gráfico: iSB por jogo]

📊 Features correlacionadas
[Scatter: iSB vs velocidade média]
[Scatter: iSB vs proximidade defesa]
```

---

### 💻 Tecnologia: Streamlit

**Por que Streamlit?**
- ✅ Python puro (sem JS/HTML)
- ✅ Código fica simples (50-100 linhas)
- ✅ Deploy grátis em Streamlit Cloud
- ✅ Reloads automáticos (ótimo para desenvolvimento)
- ✅ IA consegue gerar 100% do código

**Estrutura do arquivo:**
```python
# streamlit_app.py (~120 linhas)

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Load data (10 jogadores apenas)
df = load_data()  # Rápido!

# 2. Sidebar com navegação
page = st.sidebar.radio("Escolha a visualização", 
    ["Visão Geral", "Comparação", "Detalhes"])

# 3. Mostrar conteúdo
if page == "Visão Geral":
    show_overview(df)
elif page == "Comparação":
    show_comparison(df)
else:
    show_details(df)
```

---

### 📋 Checklist Dashboard (Semana 3-4)

**Semana 3 (Estrutura):**
- [ ] Setup Streamlit básico
- [ ] Carregar dados dos 10 jogadores
- [ ] Aba 1: Ranking + estatísticas
- [ ] Testes com dados reais

**Semana 4 (Completo):**
- [ ] Aba 2: Comparação entre jogadores
- [ ] Aba 3: Detalhes individuais
- [ ] Heatmaps + visualizações
- [ ] Ajustes estéticos (cores, fonts)
- [ ] Deploy Streamlit Cloud
- [ ] README com instruções

---

### 🎨 Estilo e Design

**Paleta de cores recomendada:**
```python
st.set_page_config(
    page_title="EfeitoIma",
    layout="wide",  # Maximiza espaço
    initial_sidebar_state="expanded"
)

# Verde (campo) + Azul (dados) + Laranja (destaques)
primary_color = "#1f77b4"     # Azul
secondary_color = "#2ca02c"   # Verde
accent_color = "#ff7f0e"      # Laranja
```

---

### 🚀 Deploy (15 minutos)

```bash
# 1. Criar conta grátis em: https://streamlit.io/cloud
# 2. Conectar seu GitHub
# 3. Deploy com 1 clique:
#    - Repositório: gabrielaoalcantara-star/EfeitoIma
#    - Arquivo: streamlit_app.py
# 4. Compartilhar link para qualquer um acessar
```

**URL final:** `https://efeitoimadashboard.streamlit.app`

---

### 1️⃣ **Use IA para gerar 80% do código**
```
Você: "Cria um script que carrega dados de tracking,
calcula velocidade instantânea e plota heatmap"

IA: [Gera 150 linhas de código]

Você: [Testa, corrige edge cases, valida output]
```

### 2️⃣ **Use IA para exploração dados**
```
Você: "Explore esses dados de tracking e me diga:
- Estrutura
- Gaps/ruídos
- Distribuição de eventos"

IA: [Análise completa em 10 min]

Você: [Lê, valida, toma decisões]
```

### 3️⃣ **Use IA para acelerar modelagem**
```
Você: "Treina regressão logística com essas features,
faz cross-validation e retorna feature importance"

IA: [Código + gráficos]

Você: [Interpreta resultados]
```

### 4️⃣ **Use IA para documentação**
```
Você: "Documenta essa metodologia iSB de forma clara"

IA: [Redige seção inteira]

Você: [Edita, corrige, melhora]
```

---

## 💡 ESTRATÉGIA COM IA PARA DASHBOARD

### IA gera tudo isso em 30 minutos:

```
PROMPT 1:
"Cria um script Streamlit com:
- 3 abas (Visão Geral, Comparação, Detalhes)
- Dropdown para selecionar jogador
- Gráfico de ranking iSB em barras
- 2 colunas para lado a lado"

IA: [Gera 150 linhas de código Streamlit pronto]

VOCÊ: Copia, testa, ajusta cores
```

### Específico para Dashboard:

**Heatmaps:**
```
PROMPT: "Cria heatmap 2D de movimento do jogador
usando density plot, com campo do futebol como background"

IA: [Código com matplotlib/plotly pronto]
```

**Scatter plots:**
```
PROMPT: "Cria scatter interativo (Plotly) com:
- X: Velocidade média
- Y: iSB
- Cor: Posição do jogador
- Hover: Nome do jogador"

IA: [Código pronto em 5 linhas]
```

**Série temporal:**
```
PROMPT: "Gera gráfico de linha (Plotly) mostrando
iSB ao longo dos últimos 10 jogos"

IA: [Código pronto]
```

**Radar chart:**
```
PROMPT: "Cria radar chart comparando 2 jogadores em:
- Velocidade média
- Aceleração
- Proximidade defesa
- iSB por zona"

IA: [Código com Plotly pronto]
```

---

## 🎯 RESUMO FINAL - 1 MÊS COM DASHBOARD

### ✅ Você entrega:

1. **Dashboard Streamlit** - Interativo, online, compartilhável
2. **Métrica iSB** - Calculada para 10 jogadores
3. **Análise completa** - Features, modelo, insights
4. **Documentação** - README + guia de uso
5. **Deploy** - Streamlit Cloud (grátis, sem servidor)

### ⏱️ Tempo necessário:

- **25-29 horas** em 4 semanas
- **~6h/semana** (bem próximo do seu limite)
- **50% com IA** (você faz revisão/ajustes)

### 📊 Comprovação:

| Tarefa | Com IA | Sem IA | Economia |
|--------|--------|--------|----------|
| Features | 4h | 10h | -60% |
| Modelo | 3-4h | 8-10h | -60% |
| Dashboard | 8-10h | 25h | -68% |
| Total | 25-29h | 50-60h | -55% |

### 🚀 Próximas fases (Mês 2-3):

- Expandir para 50+ jogadores
- Redes Neurais LSTM
- Validação em múltiplas competições
- Pipeline automático

---

## 💬 PRÓXIMOS PASSOS (HOJE)

**1. Confirme os 10 jogadores:**
- [ ] Quais 10 jogadores analisar?
- [ ] De qual time?
- [ ] Qual período de dados?

**2. Confirme a estrutura dos dados:**
- [ ] Tem dados de tracking (x, y, t)?
- [ ] Tem dados de eventos (passe, chute)?
- [ ] Em que formato? (CSV, JSON, Parquet?)
- [ ] Quantos jogos?

**3. Comece agora:**
```
Tarefa 1: Compartilhe um arquivo de amostra dos dados
Tarefa 2: Me diga os 10 jogadores
Tarefa 3: Vou criar o notebook exploratório

→ Você executa, vamos iterar
```

---

**CONCLUSÃO:** Com escopo de 10 jogadores + Streamlit, você consegue um **dashboard interativo profissional em 1 mês, dedicando 4-6h/semana, com ajuda de IA**. É viável e realista! 🎯
