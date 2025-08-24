# 🚗 SOS Crash Alert Simulator

Um simulador interativo da feature "SOS Crash Alert" que demonstra o comportamento automático de um sistema de segurança veicular em caso de acidente.

## 🎯 Funcionalidades

### ✅ Requisitos Implementados

1. **Timer Interno**: Inicia automaticamente quando um acidente é simulado
2. **Flag de Status**: Muda de "NORMAL" para "ATIVADO" em caso de emergência
3. **Setas Piscando**: 
   - Setas dianteiras (esquerda e direita)
   - Setas traseiras (esquerda e direita)
   - Luzes dos espelhos retrovisores
   - Todas piscam com intervalo de 1 segundo
4. **Configuração de Portas**: 
   - **Imediato**: Portas destravam instantaneamente após acidente
   - **Delayed**: Portas permanecem inibidas por 6 segundos antes de destravar
   - Durante a inibição, qualquer tentativa de destravar via keyfob ou switch é bloqueada
5. **Iluminação Interna**: Acende automaticamente após 10 segundos

### 🎮 Como Usar

1. **Abrir o Simulador**: Abra o arquivo `index.html` em qualquer navegador moderno
2. **Configurar Comportamento das Portas**:
   - **Imediato**: Portas destravam instantaneamente após acidente
   - **Delayed**: Portas ficam inibidas por 6 segundos antes de destravar
3. **Simular Acidente**: Clique no botão "🚨 SIMULAR ACIDENTE"
4. **Observar Comportamento**: 
   - Status muda para "ATIVADO"
   - Timer inicia contagem regressiva
   - Setas começam a piscar
   - Portas são destravadas conforme configuração
   - Após 10s, iluminação interna acende
5. **Resetar Sistema**: Use um dos botões de reset:
   - **⚠️ HAZARD SWITCH**: Reset simples do sistema
   - **🔑 KEYFOB PANIC**: Reset simples do sistema
   - **🔓 KEYFOB UNLOCK**: Reset imediato do sistema (bloqueado durante inibição de 6s)

### 🎨 Interface

- **Painel de Status**: Mostra o estado atual do sistema e timer
- **Luzes do Veículo**: Representação visual das setas e iluminação
- **Portas**: Status de travamento/destravamento de cada porta
- **Log de Eventos**: Registro cronológico de todas as ações do sistema
- **Design Responsivo**: Funciona em dispositivos móveis e desktop

### 🔧 Tecnologias

- **HTML5**: Estrutura semântica
- **CSS3**: Estilização moderna com animações e gradientes
- **JavaScript ES6+**: Lógica do sistema com classes e manipulação DOM
- **Grid Layout**: Layout responsivo usando CSS Grid
- **Animações CSS**: Efeitos visuais para luzes piscando e status

### 📱 Compatibilidade

- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Dispositivos móveis (responsivo)

### 🚀 Execução

1. Clone ou baixe os arquivos do projeto
2. Abra o arquivo `index.html` em seu navegador
3. O simulador carregará automaticamente
4. Clique em "SIMULAR ACIDENTE" para testar

### 📋 Log de Eventos

O sistema mantém um log detalhado de todos os eventos:
- Inicialização do sistema
- Alteração de configurações das portas
- Ativação do SOS
- Destravamento de portas (imediato ou após inibição)
- Inibição de portas (modo delayed)
- Tentativas de reset via keyfob (bloqueadas durante inibição)
- Ativação de setas
- Iluminação interna
- Reset do sistema (via Hazard Switch, Keyfob Panic ou Keyfob Unlock)

Cada entrada inclui timestamp e descrição do evento para facilitar o acompanhamento da sequência de ações.

---

**Desenvolvido para demonstração e teste da feature SOS Crash Alert**
