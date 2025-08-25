import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class Config:
    """Configurações da aplicação"""
    
    # Configurações da API LLM Stats
    API_BASE_URL = "https://api.llm-stats.com"  # Se existir uma API
    LLM_STATS_URL = "https://llm-stats.com"
    API_KEY = os.getenv('API_KEY', None)
    
    # Configurações do Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    # Configurações de timeout
    REQUEST_TIMEOUT = 30  # segundos
    
    # Configurações de cache
    CACHE_TIMEOUT = 300  # 5 minutos
    
    # Configurações de rate limiting
    RATE_LIMIT = 50  # requisições por minuto 