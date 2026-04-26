import fs from 'fs';
import { 
  exchangeNpssoForCode, 
  exchangeCodeForAccessToken, 
  getUserTitles
} from "psn-api";

const NPSSO = process.env.psn_api;

if (!NPSSO) {
  console.error("Erro: A variável de ambiente 'psn_api' não está definida.");
  process.exit(1);
}

const DB_FILE = "games_db.json";

function normalizeTitle(title) {
  if (!title) return "";
  return title.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
}

async function run() {
  try {
    console.log("Authenticating with PSN...");
    const accessCode = await exchangeNpssoForCode(NPSSO);
    const authorization = await exchangeCodeForAccessToken(accessCode);
    console.log("Authenticated.");

    console.log("Fetching PSN titles...");
    let psnTitles = [];
    let offset = 0;
    while (true) {
      const response = await getUserTitles(authorization, "me", { limit: 100, offset: offset });
      psnTitles.push(...response.trophyTitles);
      if (response.nextOffset) {
        offset = response.nextOffset;
      } else {
        break;
      }
    }
    console.log(`Fetched ${psnTitles.length} games from PSN.`);

    // Load DB
    let gamesDb = [];
    if (fs.existsSync(DB_FILE)) {
      gamesDb = JSON.parse(fs.readFileSync(DB_FILE, 'utf-8'));
    }

    let updatedCount = 0;
    let addedCount = 0;

    for (const psnGame of psnTitles) {
      const normPsn = normalizeTitle(psnGame.trophyTitleName);
      
      // Look for a match in the DB
      let matchedGame = null;
      for (const dbGame of gamesDb) {
        // Only try to match if platform is PlayStation or Unknown
        const plat = (dbGame.platform || "").toLowerCase();
        if (plat.includes("ps") || plat.includes("playstation") || plat.includes("desconhecido")) {
          const normDb = normalizeTitle(dbGame.title);
          if (normDb === normPsn || (normDb.length > 5 && normPsn.length > 5 && (normDb.includes(normPsn) || normPsn.includes(normDb)))) {
            matchedGame = dbGame;
            break;
          }
        }
      }

      const psnStats = {
        name: psnGame.trophyTitleName,
        progress: psnGame.progress,
        trophies: psnGame.earnedTrophies,
        total_trophies: psnGame.definedTrophies,
        last_played: psnGame.lastUpdatedDateTime
      };

      if (matchedGame) {
        // Update existing
        matchedGame.psn_stats = psnStats;
        // Refactor/Fix missing cover
        if (!matchedGame.cover || matchedGame.cover.trim() === "") {
          matchedGame.cover = psnGame.trophyTitleIconUrl;
        }
        // Normalize platform if missing
        if (!matchedGame.platform || matchedGame.platform.toLowerCase() === "desconhecido") {
            matchedGame.platform = psnGame.trophyTitlePlatform;
        }
        updatedCount++;
      } else {
        // Add new game
        const newGame = {
          title: psnGame.trophyTitleName,
          platform: psnGame.trophyTitlePlatform,
          storage: "Digital / PSN",
          company: "Sony / Desconhecido",
          release_year: "",
          genre: "Geral",
          cover: psnGame.trophyTitleIconUrl,
          psn_stats: psnStats
        };
        gamesDb.unshift(newGame); // Add to the beginning of the list
        addedCount++;
      }
    }

    // Small Refactoring/Cleanup on the whole DB
    for (const game of gamesDb) {
       if (game.storage === "Padrão" || !game.storage) game.storage = "Digital / Outros";
       if (!game.cover) game.cover = "";
    }

    // Save DB
    fs.writeFileSync(DB_FILE, JSON.stringify(gamesDb, null, 2), 'utf-8');
    console.log(`Successfully updated DB! Modified ${updatedCount} existing games and added ${addedCount} new games from PSN.`);

  } catch (err) {
    console.error("Failed to run PSN update:", err);
  }
}

run();
