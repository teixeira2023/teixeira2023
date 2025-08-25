# Painel Interativo ZL

Um painel interativo responsivo que utiliza a imagem `features.jpg` como background, criado com HTML, CSS, JavaScript e **Streamlit**.

## 🚀 **Versões Disponíveis**

### 1. **Versão Web Pura** (HTML/CSS/JS)
- `index.html` - Aplicação web standalone
- `styles.css` - Estilos responsivos
- `script.js` - Funcionalidades interativas

### 2. **Versão Streamlit** (Python + Web)
- `app.py` - Aplicação Streamlit principal
- Interface web moderna com controles interativos
- Sidebar com configurações e estatísticas
- Integração perfeita com Python

## 🎯 **Características**

- **Background Responsivo**: A imagem `features.jpg` se ajusta automaticamente ao tamanho da tela sem distorção
- **Design Interativo**: 4 zonas clicáveis com informações detalhadas
- **Interface Responsiva**: Se adapta a diferentes tamanhos de tela e orientações
- **Efeitos Visuais**: Animações suaves e transições elegantes
- **Suporte Mobile**: Otimizado para dispositivos móveis com gestos touch
- **Integração Python**: Acesso completo às funcionalidades do Python via Streamlit

## 🚀 **Como Executar**

### **Opção 1: Aplicação Web Pura**
1. Abra o arquivo `index.html` em qualquer navegador moderno
2. Clique nas zonas interativas para explorar as funcionalidades

### **Opção 2: Aplicação Streamlit (Recomendado)**

#### **Instalação Rápida:**
```bash
# Execute o script de inicialização
python run_app.py
```

#### **Instalação Manual:**
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar o aplicativo
streamlit run app.py
```

#### **Execução Direta:**
```bash
# Se o Streamlit já estiver instalado
streamlit run app.py
```

## 📱 **Interface Streamlit**

### **Sidebar de Configurações:**
- 🎨 **Tema**: Escolha entre Padrão, Escuro ou Claro
- 📏 **Altura**: Ajuste a altura do painel (400-800px)
- 📋 **Informações**: Detalhes sobre o projeto e tecnologias

### **Painel Principal:**
- 🎯 **Painel Interativo**: Zonas clicáveis com a imagem de background
- 📊 **Estatísticas**: Métricas em tempo real
- 🔧 **Funcionalidades**: Lista de recursos disponíveis
- 🟢 **Status**: Indicadores do sistema

## 🛠️ **Estrutura dos Arquivos**

### **Versão Web:**
- `index.html` - Estrutura HTML principal
- `styles.css` - Estilos CSS responsivos
- `script.js` - Funcionalidades JavaScript interativas

### **Versão Streamlit:**
- `app.py` - Aplicação Streamlit principal
- `requirements.txt` - Dependências Python
- `.streamlit/config.toml` - Configuração do Streamlit
- `run_app.py` - Script de inicialização automática

### **Recursos:**
- `ZL imagens/features.jpg` - Imagem de background
- `README.md` - Documentação completa

## 🔧 **Funcionalidades**

### **Zonas Interativas:**
- **Zona 1**: Sistema de Iluminação Frontal
- **Zona 2**: Painel de Controle Central
- **Zona 3**: Sistema de Sensores
- **Zona 4**: Gerenciamento de Energia

### **Recursos Técnicos:**
- `object-fit: cover` para manter proporções da imagem
- Grid responsivo que se adapta ao tamanho da tela
- Media queries para diferentes breakpoints
- Efeitos de hover e transições CSS
- Suporte para gestos touch em dispositivos móveis
- **Integração Python** via Streamlit
- **Codificação Base64** para imagens
- **Componentes HTML** nativos do Streamlit

## 📱 **Responsividade**

O painel se adapta automaticamente a:
- **Desktop**: Layout em grid 2x2
- **Tablet**: Layout otimizado para telas médias
- **Mobile**: Layout em coluna única
- **Mobile Landscape**: Layout horizontal otimizado

## 🎨 **Personalização**

### **Via Interface Streamlit:**
1. Use a sidebar para ajustar altura e tema
2. Modifique as configurações no arquivo `.streamlit/config.toml`

### **Via Código:**
1. Edite o objeto `zone_data` no arquivo `app.py`
2. Modifique as cores e estilos no CSS inline
3. Adicione novas funcionalidades no JavaScript

## 🔌 **Compatibilidade**

- **Navegadores**: Chrome, Firefox, Safari, Edge (versões modernas)
- **Dispositivos**: iOS, Android, Desktop, Tablet
- **Python**: 3.7+
- **Streamlit**: 1.28.0+
- **PIL**: 10.0.0+

## 🚀 **Desenvolvimento**

### **Tecnologias Utilizadas:**
- **Frontend**: HTML5, CSS3 (Grid/Flexbox), JavaScript ES6+
- **Backend**: Python 3.7+, Streamlit
- **Imagens**: Base64 encoding para integração perfeita
- **Responsividade**: Media queries e CSS Grid

### **Arquitetura:**
- **Modular**: Separação clara entre frontend e backend
- **Responsivo**: Design adaptativo para todos os dispositivos
- **Interativo**: Eventos JavaScript e integração Python
- **Escalável**: Fácil adição de novas funcionalidades

## 📝 **Exemplos de Uso**

### **Demonstração:**
```bash
# Iniciar aplicação
python run_app.py

# Acessar via navegador
http://localhost:8501
```

### **Desenvolvimento:**
```bash
# Modo desenvolvimento
streamlit run app.py --server.runOnSave true

# Porta personalizada
streamlit run app.py --server.port 8080
```

## 🤝 **Contribuição**

Para contribuir com o projeto:
1. Clone o repositório
2. Crie uma branch para sua feature
3. Teste as funcionalidades
4. Envie um pull request

## 📄 **Licença**

Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes. 