import cloudscraper
import urllib.parse
from bs4 import BeautifulSoup
import re
import json

def scrape_bdjogos(game_name):
    scraper = cloudscraper.create_scraper()
    query = urllib.parse.quote(game_name)
    search_url = f"https://bdjogos.com.br/busca.php?busca={query}"
    print(f"Buscando: {game_name}")
    try:
        r = scraper.get(search_url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # Procura o primeiro link de um jogo no retorno da busca
        game_links = soup.find_all('a', href=re.compile(r'jogo\.php\?id='))
        if not game_links:
            # Talvez a busca redirecionou direto se achou só 1?
            if 'jogo.php?id=' in r.url:
                return extract_game_data(soup, r.url)
            print(f"  -> Nenhum jogo encontrado para: {game_name}")
            return None

        first = game_links[0]['href']
        game_url = f"https://bdjogos.com.br/{first}" if not first.startswith('http') else first

        r_game = scraper.get(game_url)
        game_soup = BeautifulSoup(r_game.text, 'html.parser')
        return extract_game_data(game_soup, game_url)
    except Exception as e:
        print(f"Erro em {game_name}: {e}")
        return None

def extract_game_data(soup, url):
    title = soup.title.text.replace(' - BD Jogos', '').strip() if soup.title else "Desconhecido"
    
    # Capa (usualmente src contendo /capas/ ou /img/)
    cover = ""
    imgs = soup.find_all('img')
    for img in imgs:
        src = img.get('src', '')
        if 'capa' in src.lower() or '/capas/' in src.lower():
            cover = src
            break
    if cover and not cover.startswith('http'):
        if cover.startswith('/'): cover = "https://bdjogos.com.br" + cover
        else: cover = "https://bdjogos.com.br/" + cover
    
    # Fallback to any larger image if capa not found
    if not cover:
        for img in imgs:
            if 'img-fluid' in img.get('class', []):
                src = img.get('src', '')
                if src:
                    if src.startswith('/'): cover = "https://bdjogos.com.br" + src
                    else: cover = "https://bdjogos.com.br/" + src
                    break

    company = "Várias"
    year = "Desconhecido"
    genres = ["Ação"] # defaulters
    
    # Try looking for texts in the page
    for span in soup.find_all('span'):
        txt = span.text.strip()
        if 'Desenvolvedor' in txt or 'Publicadora' in txt:
            nxt = span.find_next_sibling()
            if nxt: company = nxt.text.strip()
        if 'Lançamento' in txt:
            nxt = span.find_next_sibling()
            if nxt: year = nxt.text.split('-')[0].split('/')[-1].strip()

    # Some fallback for simple HTML parsing
    for b in soup.find_all('b'):
        if 'Desenvolvedor' in b.text or 'Empresa' in b.text:
            text_lines = b.parent.text.replace(b.text, '').strip().split('\n')
            if text_lines: company = text_lines[0].strip()
        if 'Ano' in b.text or 'Lançamento' in b.text:
            text_lines = b.parent.text.replace(b.text, '').strip().split('\n')
            if text_lines: year = text_lines[0].strip()[:4]
    
    return {
        "title": title,
        "cover": cover,
        "company": company,
        "release_year": year,
        "url": url,
        "platform": "Xbox 360", # hardcoded for this demo
        "genre": genres[0]
    }

def run():
    # Ler o CSV de exemplo
    games_to_scrape = []
    with open('Joos360HDoriginal.csv', 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines[1:15]): # pular o cabeçalho e pegar as primeiras 14
            columns = line.strip().split(';')
            # As colunas com nomes parecem ser 1, 7 e 13
            for col_idx in [1, 7, 13]:
                if col_idx < len(columns):
                    name = columns[col_idx].strip()
                    if name and not name.isdigit():
                        games_to_scrape.append(name)
    
    # limitar para ~5 jogos de teste no JSON para ser rápido
    games_to_scrape = list(set(games_to_scrape))[:5]
    print(f"Jogos que tentaremos buscar: {games_to_scrape}")
    
    results = []
    for g in games_to_scrape:
        data = scrape_bdjogos(g)
        if data:
            results.append(data)
    
    if len(results) == 0:
        # mock data if fallback
         results = [
            {"id": "mock_1", "title": "Alan Wake", "cover": "https://bdjogos.com.br/capas/4084-alan-wake-xbox-360-capa-1.jpg", "company": "Remedy", "platform": "Xbox 360", "genre": "Ação"},
        ]
            
    with open('games.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("Salvo em games.json!")

if __name__ == "__main__":
    run()
