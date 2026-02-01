Vou criar um documento Markdown completo com os comandos essenciais do Git para uso no terminal. Como não posso gerar arquivos para download diretamente, vou apresentar o conteúdo formatado que você pode copiar e salvar como git-commands.md.
Guia de Comandos Git Essenciais
📋 Índice
Configuração Inicial
Criar/Inicializar Repositórios
Fluxo de Trabalho Básico
Branches (Ramificações)
Repositórios Remotos
Desfazer Alterações
Inspeção e Comparação
Stash (Arquivo Temporário)
Tags (Etiquetas)
Comandos Úteis
Configuração Inicial
bash
Copy
# Configurar nome de usuário
git config --global user.name "Seu Nome"

# Configurar email
git config --global user.email "seu@email.com"

# Verificar configurações
git config --list

# Definir editor padrão (ex: VS Code)
git config --global core.editor "code --wait"

# Definir branch padrão como 'main'
git config --global init.defaultBranch main
Criar/Inicializar Repositórios
bash
Copy
# Inicializar novo repositório Git na pasta atual
git init

# Clonar repositório existente
git clone https://github.com/usuario/repositorio.git

# Clonar apenas uma branch específica
git clone -b nome-da-branch https://github.com/usuario/repositorio.git

# Clonar em pasta específica
git clone https://github.com/usuario/repositorio.git nome-da-pasta
Fluxo de Trabalho Básico
bash
Copy
# Verificar status do repositório
git status

# Adicionar arquivo específico para staging
git add arquivo.txt

# Adicionar todos os arquivos modificados
git add .

# Adicionar todos os arquivos de uma extensão
git add *.js

# Remover arquivo do staging (mantém alterações)
git reset HEAD arquivo.txt

# Comitar alterações com mensagem
git commit -m "Mensagem descritiva do commit"

# Comitar e adicionar simultaneamente (apenas arquivos rastreados)
git commit -am "Mensagem do commit"

# Ver histórico de commits
git log

# Histórico simplificado (uma linha por commit)
git log --oneline

# Histórico com gráfico de branches
git log --graph --oneline --all
Branches (Ramificações)
bash
Copy
# Listar branches locais
git branch

# Listar branches remotas
git branch -r

# Listar todas as branches (local e remoto)
git branch -a

# Criar nova branch
git branch nome-da-branch

# Criar e mudar para nova branch
git checkout -b nome-da-branch
# ou (Git 2.23+)
git switch -c nome-da-branch

# Mudar para branch existente
git checkout nome-da-branch
# ou (Git 2.23+)
git switch nome-da-branch

# Renomear branch atual
git branch -m novo-nome

# Deletar branch local (já mergeada)
git branch -d nome-da-branch

# Forçar deleção de branch (não mergeada)
git branch -D nome-da-branch

# Mesclar branch na branch atual
git merge nome-da-branch

# Rebase da branch atual com outra
git rebase nome-da-branch
Repositórios Remotos
bash
Copy
# Ver repositórios remotos configurados
git remote -v

# Adicionar repositório remoto
git remote add origin https://github.com/usuario/repositorio.git

# Remover repositório remoto
git remote remove origin

# Renomear repositório remoto
git remote rename antigo novo

# Buscar alterações do remoto (não aplica)
git fetch origin

# Buscar e mesclar alterações do remoto
git pull origin main

# Enviar commits para repositório remoto
git push origin main

# Enviar nova branch para remoto
git push -u origin nome-da-branch

# Deletar branch remota
git push origin --delete nome-da-branch

# Forçar push (cuidado!)
git push -f origin main
Desfazer Alterações
bash
Copy
# Desfazer alterações não staged (arquivo específico)
git checkout -- arquivo.txt

# Desfazer alterações não staged (todos os arquivos)
git checkout -- .

# Remover arquivo do staging (mantém modificações)
git reset HEAD arquivo.txt

# Desfazer último commit (mantém alterações staged)
git reset --soft HEAD~1

# Desfazer último commit (mantém alterações unstaged)
git reset --mixed HEAD~1

# Desfazer último commit (remove alterações)
git reset --hard HEAD~1

# Reverter commit criando novo commit
git revert hash-do-commit

# Ver reflog (histórico de referências)
git reflog
Inspeção e Comparação
bash
Copy
# Ver diferenças não staged
git diff

# Ver diferenças staged (próximo commit)
git diff --staged
# ou
git diff --cached

# Ver diferenças entre branches
git diff branch1..branch2

# Ver conteúdo de arquivo em commit específico
git show hash-do-commit:arquivo.txt

# Ver informações sobre objeto Git
git show hash-do-commit

# Ver quem modificou cada linha (blame)
git blame arquivo.txt

# Ver conteúdo de arquivo em branch específica
git show branch:arquivo.txt
Stash (Arquivo Temporário)
bash
Copy
# Salvar alterações temporariamente
git stash

# Salvar com descrição
git stash push -m "descrição das alterações"

# Listar stashes salvos
git stash list

# Aplicar último stash (mantém na lista)
git stash apply

# Aplicar stash específico
git stash apply stash@{2}

# Aplicar e remover último stash
git stash pop

# Remover último stash
git stash drop

# Remover todos os stashes
git stash clear

# Criar branch a partir de stash
git stash branch nome-da-branch
Tags (Etiquetas)
bash
Copy
# Listar tags existentes
git tag

# Criar tag anotada
git tag -a v1.0.0 -m "Versão 1.0.0"

# Criar tag leve
git tag v1.0.0

# Criar tag em commit específico
git tag -a v1.0.0 hash-do-commit -m "Mensagem"

# Enviar tag específica para remoto
git push origin v1.0.0

# Enviar todas as tags para remoto
git push origin --tags

# Deletar tag local
git tag -d v1.0.0

# Deletar tag remota
git push origin --delete v1.0.0
Comandos Úteis
bash
Copy
# Limpar arquivos não rastreados (dry-run primeiro)
git clean -n

# Remover arquivos não rastreados
git clean -f

# Remover diretórios não rastreados
git clean -fd

# Arquivar repositório em formato zip
git archive --format=zip --output=projeto.zip HEAD

# Ver estatísticas do repositório
git shortlog -sn

# Ver log em formato customizado
git log --pretty=format:"%h - %an, %ar : %s"

# Ver branches mergeadas
git branch --merged

# Ver branches não mergeadas
git branch --no-merged

# Atualizar submódulos
git submodule update --init --recursive

# Bisect (busca binária para encontrar bugs)
git bisect start
git bisect bad
git bisect good hash-do-commit-bom
🚀 Fluxo de Trabalho Típico
bash
Copy
# 1. Atualizar repositório local
git pull origin main

# 2. Criar branch para nova feature
git checkout -b feature/nova-funcionalidade

# 3. Fazer alterações e commitar
git add .
git commit -m "feat: adiciona nova funcionalidade"

# 4. Atualizar com main (se necessário)
git pull origin main

# 5. Enviar para repositório remoto
git push -u origin feature/nova-funcionalidade

# 6. Criar Pull Request via interface web
# 7. Após merge, voltar para main e atualizar
git checkout main
git pull origin main

# 8. Deletar branch local
git branch -d feature/nova-funcionalidade
💡 Dicas Importantes
Table
Copy
Situação	Comando
Ver aliases configurados	git config --get-regexp alias
Criar alias	git config --global alias.st status
Ignorar arquivos	Criar arquivo .gitignore
Ver configuração local	cat .git/config
Ver objetos do Git	git count-objects -vH
📄 Arquivo .gitignore Exemplo
gitignore
Copy
# Dependências
node_modules/
vendor/

# Arquivos de ambiente
.env
.env.local

# IDEs
.vscode/
.idea/
*.swp

# Sistema operacional
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Build
dist/
build/
Nota: Substitua main pelo nome da sua branch principal se for diferente (antigamente era master).
Para salvar este documento, copie todo o conteúdo acima, cole em um editor de texto e salve como git-commands.md.