import pandas as pd
import json

def excel_to_json(excel_path, json_path):
    print(f"Lendo {excel_path}...")
    xl = pd.ExcelFile(excel_path)
    
    games_list = []
    
    for sheet in xl.sheet_names:
        print(f"Processando aba: {sheet}")
        try:
            df = xl.parse(sheet, header=None) # Read without header to avoid missing data at row 0
        except Exception as e:
            print(f"  Erro ao ler {sheet}: {e}")
            continue
            
        for col in df.columns:
            current_storage = "Desconhecido"
            for val in df[col]:
                if pd.isna(val):
                    continue
                
                # Converter para string e limpar
                str_val = str(val).strip()
                
                # Ignorar números (índices)
                if str_val.replace('.', '', 1).isdigit():
                    continue
                
                lower_val = str_val.lower()
                
                # Checar se é um cabeçalho de HD
                if 'hd original' in lower_val or 'hd externo' in lower_val or 'hd backup' in lower_val:
                    if 'original' in lower_val: current_storage = "HD Original"
                    elif 'externo' in lower_val: current_storage = "HD Externo"
                    elif 'backup' in lower_val: current_storage = "HD Backup"
                    continue
                    
                # Ignorar textos de cabeçalho
                ignore_list = ['total', 'hd', 'físico', 'unnamed', 'psn']
                if lower_val in ignore_list or lower_val == "":
                    continue
                    
                if len(str_val) < 2: # Ignore single characters just to be safe
                    continue
                    
                # Se passou nos filtros, é um jogo
                games_list.append({
                    "title": str_val,
                    "platform": sheet.strip(),
                    "storage": current_storage if 'xbox 360' in sheet.strip().lower() else "Padrão",
                    # placeholder para o que for raspado futuramente:
                    "cover": "",
                    "company": "Desconhecido",
                    "release_year": "Desconhecido",
                    "genre": "Geral"
                })

    # Remover duplicatas baseadas no título e plataforma
    unique_games = []
    seen = set()
    for g in games_list:
        key = (g['title'], g['platform'])
        if key not in seen:
            seen.add(key)
            unique_games.append(g)

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(unique_games, f, ensure_ascii=False, indent=2)
        
    print(f"Extração concluída! {len(unique_games)} jogos salvos em {json_path}")

if __name__ == "__main__":
    excel_to_json("Joos360HDoriginal.xlsx", "raw_games.json")
