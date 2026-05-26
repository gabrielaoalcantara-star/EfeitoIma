"""
Script para extrair dados StatsBomb em formato CSV
e preparar amostra para o projeto EfeitoIma
"""

import json
import csv
from pathlib import Path

# Função principal
def extract_game_data(match_id, output_dir="data"):
    """Extrai dados de um jogo e salva em CSV"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    # Carregar dados
    events_file = f"open-data/data/events/{match_id}.json"
    lineup_file = f"open-data/data/lineups/{match_id}.json"
    
    print(f"\n📂 Carregando jogo {match_id}...")
    
    try:
        with open(events_file) as f:
            events = json.load(f)
        with open(lineup_file) as f:
            lineups = json.load(f)
    except FileNotFoundError:
        print(f"❌ Jogo {match_id} não encontrado")
        return None
    
    # Extrair informações básicas
    print(f"✅ Total de eventos: {len(events)}")
    print(f"✅ Total de times: {len(lineups)}")
    
    # Mostrar times
    print(f"\n📋 TIMES:")
    for i, team in enumerate(lineups):
        print(f"  Time {i+1}: {team['team_name']} ({len(team['lineup'])} jogadores)")
    
    # Extrair eventos com posição
    print(f"\n🔄 Convertendo eventos para CSV...")
    
    csv_file = f"{output_dir}/game_{match_id}_events.csv"
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Headers
        writer.writerow([
            'event_id', 'timestamp', 'player_name', 'player_id',
            'team_name', 'event_type', 'x', 'y', 'period', 'minute'
        ])
        
        # Dados
        count = 0
        for event in events:
            if 'player' in event and 'location' in event:
                writer.writerow([
                    event.get('id', ''),
                    event.get('timestamp', ''),
                    event['player'].get('name', ''),
                    event['player'].get('id', ''),
                    event.get('team', {}).get('name', ''),
                    event['type'].get('name', ''),
                    event['location'][0],
                    event['location'][1],
                    event.get('period', ''),
                    event.get('minute', '')
                ])
                count += 1
        
        print(f"✅ {count} eventos com posição extraídos")
    
    # Extrair jogadores
    print(f"\n👥 Extraindo jogadores...")
    
    players_file = f"{output_dir}/game_{match_id}_players.csv"
    
    with open(players_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['player_id', 'player_name', 'team_name', 'jersey_number', 'position'])
        
        all_players = []
        for team in lineups:
            for player in team['lineup']:
                position = "Unknown"
                if player.get('positions'):
                    position = player['positions'][0].get('position', 'Unknown')
                
                all_players.append([
                    player['player_id'],
                    player['player_name'],
                    team['team_name'],
                    player.get('jersey_number', ''),
                    position
                ])
                writer.writerow(all_players[-1])
        
        print(f"✅ {len(all_players)} jogadores extraídos")
    
    # Mostrar primeiros 10 jogadores
    print(f"\n🎯 PRIMEIROS 10 JOGADORES (Time 1):")
    team1_players = [p for p in all_players if p[2] == lineups[0]['team_name']]
    for i, player in enumerate(team1_players[:10], 1):
        print(f"  {i}. {player[1]} (ID: {player[0]}, Pos: {player[4]})")
    
    print(f"\n✅ Dados salvos em:")
    print(f"   - {csv_file}")
    print(f"   - {players_file}")
    
    return {
        'events_file': csv_file,
        'players_file': players_file,
        'match_id': match_id,
        'team1': lineups[0]['team_name'],
        'team2': lineups[1]['team_name'],
        'event_count': count
    }

# MAIN
if __name__ == "__main__":
    print("="*60)
    print("📊 EXTRATOR DE DADOS STATSBOMB")
    print("="*60)
    
    # Lista jogos
    from pathlib import Path
    events_dir = Path("open-data/data/events")
    all_games = [f.stem for f in events_dir.glob("*.json")]
    
    print(f"\n✅ Total de jogos disponíveis: {len(all_games)}")
    print(f"\n📂 Primeiros 10 IDs:")
    for i, game_id in enumerate(all_games[:10], 1):
        print(f"   {i}. {game_id}")
    
    # Usar primeiro jogo
    print(f"\n{'='*60}")
    print(f"🚀 EXTRAINDO PRIMEIRO JOGO...")
    print(f"{'='*60}")
    
    result = extract_game_data(all_games[0])
    
    if result:
        print(f"\n{'='*60}")
        print(f"✅ PRÓXIMOS PASSOS:")
        print(f"{'='*60}")
        print(f"""
1. Os dados foram salvos em CSV:
   - Eventos: {result['events_file']}
   - Jogadores: {result['players_file']}

2. Agora você tem:
   - Time 1: {result['team1']}
   - Time 2: {result['team2']}
   - {result['event_count']} eventos com posição
   
3. Para usar outro jogo, edite o script e mude:
   result = extract_game_data('ID_DO_JOGO')
   
   Escolha um dos IDs acima!

4. Próximo: Compartilhe comigo os CSVs que vou criar o notebook!
        """)
