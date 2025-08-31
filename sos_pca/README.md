# 🚗 SOS Crash Alert Simulator

Sistema de Alerta de Colisão com Resposta Automática de Emergência - Simulador Interativo

## 📁 Estrutura do Projeto

O projeto foi organizado em arquivos separados para melhor manutenção e organização:

```
sos_pca/
├── index.html          # Estrutura HTML principal
├── styles.css          # Estilos CSS organizados
├── sos-crash-alert.js  # Lógica JavaScript e classe principal
├── config.js           # Configurações centralizadas do sistema
└── README.md           # Documentação do projeto
```

## 🎯 Funcionalidades

### Sistema de Emergência SOS
- **Ativação Automática**: Simula detecção de colisão
- **Timer de Emergência**: Contador regressivo desde a ativação
- **Luzes de Emergência**: Setas piscando automaticamente
- **Iluminação Interna**: Ativação automática após 10 segundos

### Configuração de Portas
- **Modo Imediato**: Destrava portas instantaneamente
- **Modo Delayed**: Inibe portas por 6s, destrava após 10s total

### Controles de Reset
- **Hazard Switch**: Reset via interruptor de emergência
- **Keyfob Panic**: Reset via botão de pânico do chaveiro
- **Keyfob Unlock**: 
  - **Em emergência**: Reset do sistema (quando disponível)
  - **Em estado normal**: Toggle das portas (travadas ↔ destravadas)
- **Sistema de Inibição**: Bloqueia resets por 10 segundos após ativação

### Log de Eventos
- **Registro Automático**: Todos os eventos são registrados com timestamp
- **Exportação**: Salva log em arquivo TXT para análise
- **Histórico**: Mantém histórico completo da sessão

## 🚀 Como Usar

1. **Abrir o Simulador**: Abra `index.html` em qualquer navegador moderno
2. **Configurar Portas**: Escolha entre modo Imediato ou Delayed
3. **Simular Acidente**: Clique em "🚨 SIMULAR ACIDENTE"
4. **Observar Comportamento**: 
   - Setas piscam automaticamente
   - Portas seguem configuração escolhida
   - Timer conta tempo decorrido
   - Log registra todos os eventos
5. **Resetar Sistema**: Use qualquer botão de reset disponível
6. **Controle de Portas em Estado Normal**: Use Keyfob Unlock para alternar entre travadas/destravadas

## ⚙️ Configurações

### Modo de Portas
- **Imediato**: Portas destravam instantaneamente na ativação
- **Delayed**: Portas ficam inibidas por 6s, depois travadas por 4s, totalizando 10s
- **Após Reset**: Portas permanecem destravadas independente do modo anterior

### Comportamento do Keyfob Unlock
- **Em Estado de Emergência**: Funciona como botão de reset do sistema
- **Em Estado Normal**: Funciona como toggle das portas
  - Se portas estão travadas → destrava todas
  - Se portas estão destravadas → trava todas
- **Log Detalhado**: Registra cada ação com timestamp

### Sistema de Inibição
- **Período de Inibição**: 10 segundos após ativação
- **Botões Afetados**: Hazard Switch, Keyfob Panic, Keyfob Unlock
- **Comportamento**: Botões ficam desabilitados e mudam de cor

## 🎨 Interface

### Status Panel
- **Status do Sistema**: NORMAL/ATIVADO com indicadores visuais
- **Timer de Emergência**: Contador em tempo real

### Controles
- **Botão de Acidente**: Ativa o sistema SOS
- **Botões de Reset**: Reseta o sistema quando disponíveis
- **Configuração**: Seleção de modo de portas

### Elementos Visuais
- **Luzes de Emergência**: Setas dianteiras, traseiras e retrovisores
- **Status das Portas**: Indicadores visuais para cada porta
- **Iluminação Interna**: 4 pontos de luz simulados

### Log de Eventos
- **Registro em Tempo Real**: Todos os eventos com timestamp
- **Scroll Automático**: Sempre mostra eventos mais recentes
- **Exportação**: Botão para salvar log em arquivo

## 🔧 Tecnologias Utilizadas

- **HTML5**: Estrutura semântica e acessível
- **CSS3**: Estilos modernos com animações e responsividade
- **JavaScript ES6+**: Lógica orientada a objetos com classes
- **Design Responsivo**: Funciona em desktop e dispositivos móveis
- **Arquitetura Modular**: Código organizado em arquivos separados por responsabilidade

## 📱 Responsividade

O simulador é totalmente responsivo e se adapta a diferentes tamanhos de tela:
- **Desktop**: Layout em grid com 4 colunas para portas
- **Tablet**: Ajustes automáticos para telas médias
- **Mobile**: Layout em coluna única para melhor usabilidade

## 🚨 Casos de Uso

### Simulação de Treinamento
- **Instrutores**: Demonstração de sistemas de emergência
- **Estudantes**: Aprendizado sobre comportamento de sistemas SOS
- **Engenheiros**: Validação de lógica de controle

### Testes de Sistema
- **Validação**: Verificação de sequência de eventos
- **Timing**: Teste de tempos de resposta
- **Interface**: Validação de controles e indicadores

## 📋 Log de Eventos

O sistema registra automaticamente:
- Inicialização do sistema
- Ativação do SOS
- Mudanças de configuração
- Tentativas de reset
- Status das portas
- Ativação de iluminação
- Resets do sistema

## 💾 Exportação de Dados

- **Formato**: Arquivo TXT com timestamp
- **Conteúdo**: Todos os eventos da sessão atual
- **Nome**: Inclui data e hora da exportação
- **Download**: Automático via navegador

## 🔒 Segurança e Validação

- **Prevenção de Múltiplas Ativações**: Sistema não pode ser ativado duas vezes
- **Validação de Estados**: Verificações de estado antes de executar ações
- **Limpeza de Timers**: Todos os timers são limpos adequadamente
- **Tratamento de Erros**: Logs de tentativas inválidas

## 🚀 Melhorias Futuras

- [ ] Sistema de configurações salváveis
- [ ] Múltiplos perfis de veículo
- [ ] Simulação de falhas de sistema
- [ ] Integração com APIs de telemetria
- [ ] Modo de demonstração automática
- [ ] Relatórios estatísticos

## 👨‍💻 Desenvolvimento

### Arquitetura Modular
- **index.html**: Estrutura HTML limpa e semântica
- **styles.css**: Todos os estilos CSS organizados por seções
- **sos-crash-alert.js**: Classe principal com toda a lógica do sistema
- **config.js**: Configurações centralizadas para fácil manutenção

### Estrutura de Classes
- **SOSCrashAlert**: Classe principal que gerencia todo o sistema
- **Métodos Organizados**: Cada funcionalidade em método separado
- **Documentação JSDoc**: Comentários detalhados para cada método

### Padrões de Código
- **ES6+**: Uso de classes, arrow functions e template literals
- **Modular**: Código organizado em arquivos separados por responsabilidade
- **Responsivo**: CSS com media queries para diferentes dispositivos
- **Acessível**: HTML semântico e ARIA labels
- **Configurável**: Valores centralizados em arquivo de configuração

## 📄 Licença

Projeto desenvolvido para fins educacionais e de demonstração.

---

**Desenvolvido por Teixeira 2023** 🚗✨
