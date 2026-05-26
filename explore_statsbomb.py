"""
Script para explorar dados StatsBomb e prepará-los para análise
Execução: python explore_statsbomb.py
"""

import json
import os
from pathlib import Path

# Função para carregar um jogo
def load_game_data(match_id, statsbomb_path="open-data"):
    """Carrega dados de um jogo específico"""
    
    events_file = f"{statsbomb_path}/data/events/{match_id}.json"
    lineup_file = f"{statsbomb_path}/data/lineups/{match_id}.json"
    
    if not os.path.exists(events_file):
        return None, None
    
    with open(events_file) as f:
        events = json.load(f)
    
    with open(lineup_file) as f:
        lineups = json.load(f)
    
    return events, lineups

# Lista alguns IDs de jogos disponíveis
def list_available_games(statsbomb_path="open-data", limit=5):
    """Lista alguns IDs de jogos disponíveis"""
    events_dir = f"{statsbomb_path}/data/events"
    game_ids = [f.replace('.json', '') for f in os.listdir(events_dir)][:limit]
    return game_ids

# Analisa estrutura de um jogo
def analyze_game(match_id, statsbomb_path="open-data"):
    """Analisa estrutura de um jogo"""
    
    events, lineups = load_game_data(match_id, statsbomb_path)
    
    if events is None:
        print(f"❌ Jogo {match_id} não encontrado")
        return
    
    print(f"\n{'='*60}")
    print(f"📊 ANÁLISE DO JOGO ID: {match_id}")
    print(f"{'='*60}\n")
    
    # Info básica
    print(f"✅ Total de eventos: {len(events)}")
    print(f"✅ Total de times: {len(lineups)}")
    
    # Times
    print(f"\n📋 TIMES:")
    for team in lineups:
        print(f"  - {team['team']['name']}: {len(team['lineup'])} jogadores")
    
    # Tipos de eventos
    event_types = {}
    for event in events:
        event_type = event['type']['name']
        event_types[event_type] = event_types.get(event_type, 0) + 1
    
    print(f"\n🎯 TIPOS DE EVENTOS:")
    for event_type, count in sorted(event_types.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  - {event_type}: {count}")
    
    # Amostra de evento com posição
    print(f"\n📍 EXEMPLO DE EVENTO COM POSIÇÃO:")
    for event in events[:50]:
        if 'location' in event and 'player' in event:
            print(f"""
  Player: {event['player']['name']}
  Tipo: {event['type']['name']}
  Posição: x={event['location'][0]:.1f}, y={event['location'][1]:.1f}
  Timestamp: {event['timestamp']}
            """)
            break
    
    # Extrai 10 jogadores aleatórios do primeiro time
    print(f"\n👥 PRIMEIROS 10 JOGADORES DO TIME 1:")
    team1_players = lineups[0]['lineup'][:10]
    for i, player in enumerate(team1_players, 1):
        print(f"  {i}. {player['player_name']} (ID: {player['player_id']}, Posição: {player['player_nickname']})")
    
    return events, lineups, team1_players

# EXECUÇÃO
if __name__ == "__main__":
    
    print("🔍 EXPLORANDO DADOS STATSBOMB\n")
    
    # Lista jogos disponíveis
    print("📂 LISTANDO JOGOS DISPONÍVEIS...")
    game_ids = list_available_games(limit=10)
    print(f"\nPrimeiros 10 IDs de jogos: {game_ids}\n")
    
    # Analisa primeiro jogo
    if game_ids:
        first_game_id = game_ids[0]
        events, lineups, players = analyze_game(first_game_id)
        
        print(f"\n{'='*60}")
        print(f"✅ PRÓXIMO PASSO:")
        print(f"{'='*60}")
        print(f"""
1. Copie um dos IDs de jogo acima
2. Rode novamente: python explore_statsbomb.py
3. Digite qual jogo quer analisar
4. Vou extrair amostra dos dados e seus 10 jogadores

Sugestão: Use o jogo ID: {first_game_id}
        """)
