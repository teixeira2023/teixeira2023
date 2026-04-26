import os
import json
import requests
import re
from datetime import datetime

# Config
API_KEY = os.getenv("xbox_api")
if not API_KEY:
    print("ERRO: Variável de ambiente 'xbox_api' não definida.")
    exit(1)
DB_FILE = "games_db.json"
HEADERS = {
    "X-Authorization": API_KEY,
    "Accept": "application/json"
}

def normalize_title(title):
    # Remove special chars and make lowercase for better matching
    return re.sub(r'[^a-zA-Z0-9]', '', title).lower()

print("Fetching Xbox Title History...")
try:
    response = requests.get("https://xbl.io/api/v2/player/titleHistory", headers=HEADERS)
    response.raise_for_status()
    xbox_data = response.json()
except Exception as e:
    print(f"Failed to fetch Xbox data: {e}")
    exit(1)

titles_played = xbox_data.get("content", {}).get("titles", [])
print(f"Found {len(titles_played)} games in Xbox History.")

# Build a lookup dictionary using normalized names
xbox_history_lookup = {}
for t in titles_played:
    norm_name = normalize_title(t.get("name", ""))
    if norm_name:
        xbox_history_lookup[norm_name] = {
            "name": t.get("name"),
            "gamerscore_current": t.get("achievement", {}).get("currentGamerscore", 0),
            "gamerscore_total": t.get("achievement", {}).get("totalGamerscore", 0),
            "achievements_current": t.get("achievement", {}).get("currentAchievements", 0),
            "achievements_total": t.get("achievement", {}).get("totalAchievements", 0),
            "last_played": t.get("titleHistory", {}).get("lastTimePlayed", "")
        }

print("Loading local game database...")
with open(DB_FILE, "r", encoding="utf-8") as f:
    games_db = json.load(f)

updated_count = 0

for game in games_db:
    # Only try to match Xbox games
    if "Xbox" in game.get("platform", ""):
        norm_db_name = normalize_title(game.get("title", ""))
        
        # Check if we have history for this game
        if norm_db_name in xbox_history_lookup:
            game["xbox_stats"] = xbox_history_lookup[norm_db_name]
            updated_count += 1
            print(f"Matched and updated: {game['title']}")
        else:
            # Fallback fuzzy matching: if db name is inside xbox name or vice versa
            matched = False
            for xb_norm, xb_data in xbox_history_lookup.items():
                if len(norm_db_name) > 4 and len(xb_norm) > 4:
                    if norm_db_name in xb_norm or xb_norm in norm_db_name:
                        game["xbox_stats"] = xb_data
                        updated_count += 1
                        print(f"Fuzzy matched and updated: {game['title']} -> {xb_data['name']}")
                        matched = True
                        break

if updated_count > 0:
    print(f"Saving {updated_count} updates to {DB_FILE}...")
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(games_db, f, indent=2, ensure_ascii=False)
    print("Done!")
else:
    print("No matching games found between the database and Xbox History.")
