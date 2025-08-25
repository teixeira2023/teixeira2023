# Dashboard de LLMs - LLM Stats

Um dashboard moderno e interativo que consome dados do site LLM Stats para exibir informações sobre modelos de linguagem (LLMs) em tempo real.

## 🚀 Funcionalidades

- **Dados em Tempo Real**: Consome dados do site LLM Stats
- **Gráficos Interativos**: Visualizações com Plotly.js
- **Estatísticas Gerais**: Score médio, preços, modelos mais rápidos/caros
- **Tabela de LLMs**: Top 10 modelos com benchmarks e preços
- **Interface Moderna**: Design responsivo com tema escuro
- **Atualização Automática**: Dados atualizados a cada 5 minutos
- **Botão de Refresh**: Atualização manual dos dados

## 📊 Informações Exibidas

### Cards de Estatísticas
- Score Médio (Benchmark)
- Preço Médio por 1K Tokens
- Modelo Mais Rápido
- Modelo Mais Caro

### Gráficos
- Benchmark Scores dos Top 10 LLMs
- Preços por 1K Tokens
- Velocidade de Processamento

### Tabela de Dados
- Ranking
- Nome e Categoria
- Provedor
- Benchmark Score
- Preço por 1K Tokens
- Velocidade (tokens/seg)

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Gráficos**: Plotly.js
- **UI Framework**: Bootstrap 5
- **Ícones**: Font Awesome
- **API**: LLM Stats (simulado)

## 📦 Instalação

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd IAPrice_Dash
```

2. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**:
```bash
python app.py
```

4. **Acesse o dashboard**:
```
http://localhost:5000
```

## 🔧 Configuração

### Variáveis de Ambiente (Opcional)

Crie um arquivo `.env` na raiz do projeto:

```env
API_KEY=sua_chave_api_aqui
```

> **Nota**: Atualmente os dados são simulados baseados no site LLM Stats. Para dados reais, seria necessário implementar web scraping ou usar uma API oficial.

## 📁 Estrutura do Projeto

```
IAPrice_Dash/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
├── templates/
│   └── index.html        # Template HTML principal
└── static/               # Arquivos estáticos (CSS/JS)
    ├── css/
    └── js/
```

## 🔌 Endpoints da API

### `/`
- **Método**: GET
- **Descrição**: Página principal do dashboard

### `/api/dashboard-data`
- **Método**: GET
- **Descrição**: Retorna dados dos LLMs, benchmarks e estatísticas de provedores

### `/api/charts`
- **Método**: GET
- **Descrição**: Retorna dados para os gráficos (Benchmark Scores, Preços, Velocidade)

### `/api/stats`
- **Método**: GET
- **Descrição**: Retorna estatísticas gerais (médias, modelos mais rápidos/caros)

## 🎨 Características da Interface

- **Tema Escuro**: Design moderno com cores escuras
- **Responsivo**: Funciona em desktop, tablet e mobile
- **Animações**: Transições suaves e efeitos hover
- **Loading States**: Indicadores de carregamento
- **Auto-refresh**: Atualização automática a cada 5 minutos

## 🔄 Atualização de Dados

- **Automática**: A cada 5 minutos
- **Manual**: Botão de refresh no canto superior direito
- **Tempo Real**: Timestamp da última atualização

## 🚨 Tratamento de Erros

- **API Indisponível**: Mensagens de erro amigáveis
- **Dados Ausentes**: Fallbacks para dados não disponíveis
- **Timeout**: Timeouts configurados para requisições

## 📈 Dados da API

O dashboard consome dados baseados no site LLM Stats:

- Rankings de LLMs por benchmark score
- Preços por 1K tokens
- Velocidade de processamento
- Estatísticas por provedor
- Dados de benchmarks (código, raciocínio, conhecimento geral)

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- [LLM Stats](https://llm-stats.com/) pela referência de dados
- [Plotly](https://plotly.com/) pelos gráficos interativos
- [Bootstrap](https://getbootstrap.com/) pelo framework CSS
- [Font Awesome](https://fontawesome.com/) pelos ícones

## 📞 Suporte

Se você encontrar algum problema ou tiver sugestões, abra uma issue no repositório.

---

**Desenvolvido com ❤️ usando Python e Flask para análise de LLMs** 