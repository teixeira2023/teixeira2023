import json
import urllib.request
import urllib.parse
import time
import os

INPUT_FILE = "raw_games.json"
OUTPUT_FILE = "games_db.json"

def search_steam_game(game_name):
    query = urllib.parse.quote(game_name)
    url = f"https://store.steampowered.com/api/storesearch/?term={query}&l=portuguese&cc=BR"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
            if data.get('total', 0) > 0:
                first_item = data['items'][0]
                appid = first_item.get('id')
                # A imagem principal do jogo na Steam
                high_res_image = f"https://cdn.akamai.steamstatic.com/steam/apps/{appid}/header.jpg"
                
                return {
                    "cover": high_res_image,
                    # A API simples de storesearch não retorna o ano/empresa facilmente,
                    # mas já garantimos a capa perfeita.
                }
    except Exception as e:
        print(f"Erro ao buscar '{game_name}': {e}")
    
    return None

def main():
    print(f"Lendo {INPUT_FILE}...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        games = json.load(f)
        
    print(f"Total de jogos a processar: {len(games)}")
    
    updated_games = []
    
    # Se já existir o output, carregamos para continuar de onde parou
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            updated_games = json.load(f)
            print(f"Retomando progresso... {len(updated_games)} jogos já processados.")
            
    # Criar um set com os títulos já processados para evitar buscas duplicadas
    processed_titles = {g['title'] for g in updated_games}
    
    for i, game in enumerate(games):
        if game['title'] in processed_titles:
            continue
            
        print(f"[{i+1}/{len(games)}] Buscando imagens para: {game['title']}...")
        
        # Só buscamos se ainda não tiver capa
        if not game.get('cover'):
            steam_data = search_steam_game(game['title'])
            if steam_data:
                game['cover'] = steam_data['cover']
                print(f"  -> Capa encontrada!")
            else:
                print(f"  -> Capa não encontrada.")
            
            # Pequeno delay para não sobrecarregar a API (Rate Limit)
            time.sleep(1)
            
        updated_games.append(game)
        
        # Salva a cada 10 jogos para não perder o progresso se o script parar
        if (i + 1) % 10 == 0:
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_f:
                json.dump(updated_games, out_f, ensure_ascii=False, indent=2)
                
    # Salva o arquivo final
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_f:
        json.dump(updated_games, out_f, ensure_ascii=False, indent=2)
        
    print(f"\nConcluído! Banco de dados atualizado salvo em {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
