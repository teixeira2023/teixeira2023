let allGames = [];
let filteredGames = [];
let currentPage = 1;
const itemsPerPage = 12; // 12 jogos por página

const gamesGrid = document.getElementById('gamesGrid');
const searchInput = document.getElementById('searchInput');

const gameStats = document.getElementById('gameStats');
const paginationContainer = document.getElementById('paginationContainer');
const adminSection = document.getElementById('adminSection');
const adminTableBody = document.getElementById('adminTableBody');
const btnAdmin = document.getElementById('btnAdmin');
const btnAddRow = document.getElementById('btnAddRow');
const btnDownloadJson = document.getElementById('btnDownloadJson');

// Load Data
async function loadGames() {
    try {
        const response = await fetch('games_db.json');
        if (!response.ok) {
            // Se o arquivo ainda não existir, tenta carregar o raw_games.json
            const fallbackResponse = await fetch('raw_games.json');
            if (fallbackResponse.ok) {
                allGames = await fallbackResponse.json();
            } else {
                throw new Error("HTTP error " + response.status);
            }
        } else {
            allGames = await response.json();
        }
        filteredGames = [...allGames];

        generateFilters();
        renderGames();
    } catch (error) {
        console.error('Falha ao carregar jogos:', error);
        gamesGrid.innerHTML = `<div style="padding: 24px; color: #f87171;">
            Erro ao carregar os dados. Verifique se você executou o scraper e se games.json existe.
        </div>`;
    }
}

// Render Games
function renderGames() {
    gamesGrid.innerHTML = '';
    
    if (filteredGames.length === 0) {
        gamesGrid.innerHTML = `<div style="padding: 24px; color: #94a3b8;">Nenhum jogo encontrado com os filtros atuais.</div>`;
        gameStats.innerText = '0 jogos encontrados';
        paginationContainer.innerHTML = '';
        return;
    }

    const totalPages = Math.ceil(filteredGames.length / itemsPerPage);
    if (currentPage > totalPages) currentPage = totalPages;

    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const gamesToRender = filteredGames.slice(startIndex, endIndex);

    gamesToRender.forEach(game => {
        const card = document.createElement('div');
        card.className = 'game-card';
        
        const cover = game.cover ? game.cover : 'data:image/svg+xml;utf8,<svg width="200" height="300" xmlns="http://www.w3.org/2000/svg"><rect width="200" height="300" fill="%232d3748"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="sans-serif" font-size="16" fill="%23a0aec0">Sem Capa</text></svg>';

        card.innerHTML = `
            <div class="card-image-box">
                <img src="${cover}" alt="${game.title}" loading="lazy">
            </div>
            <div class="card-content">
                <div class="game-title">${game.title}</div>
                <div class="game-company">${game.company} • ${game.release_year || ''}</div>
                <div class="game-tags">
                    <span class="tag platform">${game.platform}</span>
                    <span class="tag">${game.genre}</span>
                    ${game.storage && game.storage !== "Padrão" ? `<span class="tag">${game.storage}</span>` : ''}
                </div>
            </div>
        `;
        // onClick to open on bdjogos if desired
        if(game.url) {
            card.style.cursor = 'pointer';
            card.onclick = () => window.open(game.url, '_blank');
        }
        
        gamesGrid.appendChild(card);
    });

    gameStats.innerText = `${filteredGames.length} jogo${filteredGames.length !== 1 ? 's' : ''} encontrados`;
    renderPagination(totalPages);
}

function renderPagination(totalPages) {
    if (totalPages <= 1) {
        paginationContainer.innerHTML = '';
        return;
    }

    paginationContainer.innerHTML = `
        <button class="page-btn" id="btnPrevPage" ${currentPage === 1 ? 'disabled' : ''}>Anterior</button>
        <span class="page-info">Página ${currentPage} de ${totalPages}</span>
        <button class="page-btn" id="btnNextPage" ${currentPage === totalPages ? 'disabled' : ''}>Próxima</button>
    `;

    const btnPrev = document.getElementById('btnPrevPage');
    const btnNext = document.getElementById('btnNextPage');

    if (btnPrev) {
        btnPrev.addEventListener('click', () => {
            if (currentPage > 1) {
                currentPage--;
                renderGames();
            }
        });
    }

    if (btnNext) {
        btnNext.addEventListener('click', () => {
            if (currentPage < totalPages) {
                currentPage++;
                renderGames();
            }
        });
    }
}

function generateFilters() {
    // Attach events to all filter inputs
    document.querySelectorAll('.filter-nested').forEach(cb => {
        cb.addEventListener('change', applyFilters);
    });
}

// Apply Filters
function applyFilters() {
    const term = searchInput.value.toLowerCase();
    
    // Check nested combinations: e.g. [{platform: 'PS4', storage: 'HD Interno'}, ...]
    const nestedCheckboxes = Array.from(document.querySelectorAll('.filter-nested:checked'));
    
    // Se nenhum filtro de console/armazenamento estiver marcado, mostramos tudo da busca/empresa
    // Se tiver marcado, o jogo precisa corresponder a pelo menos uma das combinações plataforma+armazenamento marcadas.
    const isAnyNestedChecked = nestedCheckboxes.length > 0;

    filteredGames = allGames.filter(game => {
        const matchSearch = game.title.toLowerCase().includes(term);
        
        let matchNested = true;
        if (isAnyNestedChecked) {
            matchNested = nestedCheckboxes.some(cb => {
                // To support fuzzy matching for storage, since raw_games.json has 'HD Original', 'HD externo', etc.
                const cbPlatform = cb.getAttribute('data-platform').toLowerCase();
                const cbStorage = cb.value.toLowerCase(); // 'hd interno', 'hd externo', 'biblioteca'
                
                const gamePlatform = (game.platform || "").toLowerCase();
                const gameStorage = (game.storage || "padrão").toLowerCase();
                
                const platformMatch = gamePlatform.includes(cbPlatform);
                
                // Mapeamento solto: se JSON tem "hd original" e filtro é "hd interno" (ou similar)
                // O usuário colocou hd interno, hd externo, biblioteca
                let storageMatch = false;
                if (gameStorage.includes(cbStorage)) {
                    storageMatch = true;
                } else if (cbStorage === "hd interno" && (gameStorage.includes("original") || gameStorage.includes("interno"))) {
                    storageMatch = true;
                } else if (cbStorage === "hd externo" && gameStorage.includes("externo")) {
                    storageMatch = true;
                } else if (cbStorage === "biblioteca" && (gameStorage.includes("backup") || gameStorage.includes("biblioteca") || gameStorage === "padrão")) {
                    // Assuming 'padrão' or 'backup' could be considered 'biblioteca' if no other match
                    storageMatch = true;
                } else if (cbStorage === "mídia física" && gameStorage.includes("físic")) {
                    storageMatch = true;
                }
                
                return platformMatch && storageMatch;
            });
        }

        return matchSearch && matchNested;
    });

    currentPage = 1; // Reset to first page when filtering
    renderGames();
}

// Listeners
searchInput.addEventListener('input', applyFilters);

// Admin Logic
let isAdminMode = false;

btnAdmin.addEventListener('click', () => {
    isAdminMode = !isAdminMode;
    if (isAdminMode) {
        gamesGrid.style.display = 'none';
        paginationContainer.style.display = 'none';
        adminSection.style.display = 'flex';
        btnAdmin.classList.add('active');
        btnAdmin.innerText = 'Voltar ao Catálogo';
        renderAdminTable();
    } else {
        gamesGrid.style.display = ''; 
        paginationContainer.style.display = 'flex';
        adminSection.style.display = 'none';
        btnAdmin.classList.remove('active');
        btnAdmin.innerText = 'Gerenciar Biblioteca';
        generateFilters();
        applyFilters();
    }
});

function renderAdminTable() {
    adminTableBody.innerHTML = '';
    
    allGames.forEach((game, index) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><input type="text" value="${game.title || ''}" data-index="${index}" data-field="title"></td>
            <td><input type="text" value="${game.platform || ''}" data-index="${index}" data-field="platform"></td>
            <td><input type="text" value="${game.storage || ''}" data-index="${index}" data-field="storage"></td>
            <td><input type="text" value="${game.company || ''}" data-index="${index}" data-field="company"></td>
            <td><input type="text" value="${game.release_year || ''}" data-index="${index}" data-field="release_year"></td>
            <td><input type="text" value="${game.genre || ''}" data-index="${index}" data-field="genre"></td>
            <td><input type="text" value="${game.cover || ''}" data-index="${index}" data-field="cover"></td>
            <td><button class="action-button danger-button" onclick="deleteGame(${index})">Excluir</button></td>
        `;
        adminTableBody.appendChild(tr);
    });

    // Attach input listeners
    document.querySelectorAll('#adminTableBody input').forEach(input => {
        input.addEventListener('change', (e) => {
            const index = e.target.getAttribute('data-index');
            const field = e.target.getAttribute('data-field');
            allGames[index][field] = e.target.value;
        });
    });
}

window.deleteGame = function(index) {
    if (confirm("Tem certeza que deseja remover este jogo?")) {
        allGames.splice(index, 1);
        renderAdminTable();
    }
}

btnAddRow.addEventListener('click', () => {
    allGames.unshift({
        title: "Novo Jogo",
        platform: "Desconhecido",
        storage: "Padrão",
        company: "Desconhecido",
        release_year: "Desconhecido",
        genre: "Geral",
        cover: ""
    });
    renderAdminTable();
});

btnDownloadJson.addEventListener('click', () => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(allGames, null, 2));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", "games_db.json");
    document.body.appendChild(downloadAnchorNode);
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
});

// Init
loadGames();
