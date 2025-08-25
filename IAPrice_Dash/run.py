#!/usr/bin/env python3
"""
Script de inicialização do Dashboard de Criptomoedas
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    if sys.version_info < (3, 7):
        print("❌ Erro: Python 3.7 ou superior é necessário")
        print(f"Versão atual: {sys.version}")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detectado")

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    try:
        import flask
        import requests
        import pandas
        import plotly
        print("✅ Todas as dependências estão instaladas")
        return True
    except ImportError as e:
        print(f"❌ Dependência não encontrada: {e}")
        print("Execute: pip install -r requirements.txt")
        return False

def install_dependencies():
    """Instala as dependências se necessário"""
    print("📦 Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar dependências")
        return False

def create_env_file():
    """Cria arquivo .env se não existir"""
    env_file = Path(".env")
    if not env_file.exists():
        print("📝 Criando arquivo .env...")
        env_content = """# Configurações da API LLM Stats
# Atualmente os dados são simulados baseados no site LLM Stats
# Para dados reais, seria necessário implementar web scraping ou usar uma API oficial
# Se você tiver uma chave API, descomente a linha abaixo
# API_KEY=sua_chave_api_aqui

# Configurações do Flask
FLASK_ENV=development
FLASK_DEBUG=True
"""
        with open(env_file, "w", encoding="utf-8") as f:
            f.write(env_content)
        print("✅ Arquivo .env criado")

def main():
    """Função principal"""
    print("🚀 Iniciando Dashboard de LLMs - LLM Stats")
    print("=" * 50)
    
    # Verificar versão do Python
    check_python_version()
    
    # Verificar dependências
    if not check_dependencies():
        print("\n📦 Tentando instalar dependências automaticamente...")
        if not install_dependencies():
            print("\n❌ Falha ao instalar dependências automaticamente")
            print("Execute manualmente: pip install -r requirements.txt")
            sys.exit(1)
    
    # Criar arquivo .env se necessário
    create_env_file()
    
    print("\n🎯 Iniciando servidor...")
    print("📱 Acesse: http://localhost:5000")
    print("🛑 Para parar o servidor, pressione Ctrl+C")
    print("=" * 50)
    
    # Executar a aplicação
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Servidor parado pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro ao iniciar servidor: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 