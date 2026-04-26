import urllib.request
import urllib.parse
import json

def search_steam_image(game_name):
    # Encode game name for URL
    query = urllib.parse.quote(game_name)
    url = f"https://store.steampowered.com/api/storesearch/?term={query}&l=portuguese&cc=BR"
    
    print(f"Buscando '{game_name}' na API do Steam...")
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
            if data.get('total', 0) > 0:
                # Get the first result
                first_item = data['items'][0]
                title = first_item.get('name')
                # Usually Steam returns a small capsule image in the search
                image_url = first_item.get('tiny_image') 
                
                # To get a high-res image, we can use the appid
                appid = first_item.get('id')
                high_res_image = f"https://cdn.akamai.steamstatic.com/steam/apps/{appid}/header.jpg"
                
                print(f"Encontrado: {title}")
                print(f"Imagem miniatura: {image_url}")
                print(f"Imagem alta resolução: {high_res_image}")
                
                return {
                    "title": title,
                    "image": high_res_image
                }
            else:
                print("Nenhum jogo encontrado.")
                return None
    except Exception as e:
        print(f"Erro ao buscar na API: {e}")
        return None

if __name__ == "__main__":
    search_steam_image("Alan Wake")
    print("-" * 40)
    search_steam_image("Gears of War")
