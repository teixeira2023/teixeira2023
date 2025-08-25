from flask import Flask, render_template, jsonify
import requests
import json
from datetime import datetime, timedelta
import pandas as pd
import plotly.graph_objs as go
import plotly.utils
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Configuração da API LLM Stats
LLM_STATS_URL = "https://llm-stats.com"
API_BASE_URL = "https://api.llm-stats.com"  # Se existir uma API
API_KEY = os.getenv('API_KEY', None)

class LLMDashboard:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        if app.config['API_KEY']:
            self.session.headers.update({'Authorization': f'Bearer {app.config["API_KEY"]}'})
    
    def get_llm_rankings(self):
        """Busca rankings de LLMs do LLM Stats"""
        try:
            # Simular dados baseados no site LLM Stats
            # Em um cenário real, você precisaria de uma API ou web scraping
            llm_data = [
                {
                    'name': 'Claude 3.7 Sonnet',
                    'provider': 'Anthropic',
                    'benchmark_score': 95.2,
                    'context_window': 200000,
                    'price_per_1k_tokens': 0.015,
                    'speed_tokens_per_sec': 120,
                    'model_size': 'Unknown',
                    'category': 'General Purpose'
                },
                {
                    'name': 'GPT-4o',
                    'provider': 'OpenAI',
                    'benchmark_score': 94.8,
                    'context_window': 128000,
                    'price_per_1k_tokens': 0.005,
                    'speed_tokens_per_sec': 150,
                    'model_size': 'Unknown',
                    'category': 'General Purpose'
                },
                {
                    'name': 'Claude 3.5 Sonnet',
                    'provider': 'Anthropic',
                    'benchmark_score': 92.5,
                    'context_window': 200000,
                    'price_per_1k_tokens': 0.003,
                    'speed_tokens_per_sec': 100,
                    'model_size': 'Unknown',
                    'category': 'General Purpose'
                },
                {
                    'name': 'Grok 3',
                    'provider': 'xAI',
                    'benchmark_score': 91.3,
                    'context_window': 100000,
                    'price_per_1k_tokens': 0.002,
                    'speed_tokens_per_sec': 80,
                    'model_size': 'Unknown',
                    'category': 'General Purpose'
                },
                {
                    'name': 'DeepSeek R1',
                    'provider': 'DeepSeek',
                    'benchmark_score': 89.7,
                    'context_window': 128000,
                    'price_per_1k_tokens': 0.001,
                    'speed_tokens_per_sec': 90,
                    'model_size': 'Unknown',
                    'category': 'General Purpose'
                },
                {
                    'name': 'GPT-4o Mini',
                    'provider': 'OpenAI',
                    'benchmark_score': 87.2,
                    'context_window': 128000,
                    'price_per_1k_tokens': 0.00015,
                    'speed_tokens_per_sec': 200,
                    'model_size': 'Unknown',
                    'category': 'General Purpose'
                },
                {
                    'name': 'Llama 4 Maverick',
                    'provider': 'Meta',
                    'benchmark_score': 85.1,
                    'context_window': 32768,
                    'price_per_1k_tokens': 0.0005,
                    'speed_tokens_per_sec': 60,
                    'model_size': 'Unknown',
                    'category': 'Open Source'
                },
                {
                    'name': 'Mistral Large',
                    'provider': 'Mistral AI',
                    'benchmark_score': 83.9,
                    'context_window': 32768,
                    'price_per_1k_tokens': 0.007,
                    'speed_tokens_per_sec': 70,
                    'model_size': 'Unknown',
                    'category': 'General Purpose'
                },
                {
                    'name': 'Gemini 1.5 Pro',
                    'provider': 'Google',
                    'benchmark_score': 82.4,
                    'context_window': 1000000,
                    'price_per_1k_tokens': 0.0035,
                    'speed_tokens_per_sec': 85,
                    'model_size': 'Unknown',
                    'category': 'General Purpose'
                },
                {
                    'name': 'Claude 3 Haiku',
                    'provider': 'Anthropic',
                    'benchmark_score': 80.1,
                    'context_window': 200000,
                    'price_per_1k_tokens': 0.00025,
                    'speed_tokens_per_sec': 110,
                    'model_size': 'Unknown',
                    'category': 'General Purpose'
                }
            ]
            return llm_data
        except Exception as e:
            print(f"Erro ao buscar dados de LLMs: {e}")
            return []
    
    def get_benchmark_data(self):
        """Busca dados de benchmarks"""
        try:
            benchmark_data = {
                'code_benchmarks': [
                    {'model': 'Claude 3.7 Sonnet', 'score': 95.2, 'category': 'Code Generation'},
                    {'model': 'GPT-4o', 'score': 94.8, 'category': 'Code Generation'},
                    {'model': 'Claude 3.5 Sonnet', 'score': 92.5, 'category': 'Code Generation'},
                    {'model': 'Grok 3', 'score': 91.3, 'category': 'Code Generation'},
                    {'model': 'DeepSeek R1', 'score': 89.7, 'category': 'Code Generation'}
                ],
                'reasoning_benchmarks': [
                    {'model': 'Claude 3.7 Sonnet', 'score': 94.1, 'category': 'Reasoning'},
                    {'model': 'GPT-4o', 'score': 93.8, 'category': 'Reasoning'},
                    {'model': 'Claude 3.5 Sonnet', 'score': 91.2, 'category': 'Reasoning'},
                    {'model': 'Grok 3', 'score': 89.5, 'category': 'Reasoning'},
                    {'model': 'DeepSeek R1', 'score': 87.9, 'category': 'Reasoning'}
                ],
                'general_knowledge': [
                    {'model': 'Claude 3.7 Sonnet', 'score': 96.3, 'category': 'General Knowledge'},
                    {'model': 'GPT-4o', 'score': 95.9, 'category': 'General Knowledge'},
                    {'model': 'Claude 3.5 Sonnet', 'score': 93.7, 'category': 'General Knowledge'},
                    {'model': 'Grok 3', 'score': 92.1, 'category': 'General Knowledge'},
                    {'model': 'DeepSeek R1', 'score': 90.5, 'category': 'General Knowledge'}
                ]
            }
            return benchmark_data
        except Exception as e:
            print(f"Erro ao buscar dados de benchmarks: {e}")
            return {}
    
    def get_provider_stats(self):
        """Busca estatísticas por provedor"""
        try:
            provider_stats = {
                'anthropic': {
                    'name': 'Anthropic',
                    'models_count': 3,
                    'avg_benchmark_score': 93.3,
                    'avg_price': 0.006,
                    'total_context_window': 600000
                },
                'openai': {
                    'name': 'OpenAI',
                    'models_count': 2,
                    'avg_benchmark_score': 91.0,
                    'avg_price': 0.002575,
                    'total_context_window': 256000
                },
                'xai': {
                    'name': 'xAI',
                    'models_count': 1,
                    'avg_benchmark_score': 91.3,
                    'avg_price': 0.002,
                    'total_context_window': 100000
                },
                'deepseek': {
                    'name': 'DeepSeek',
                    'models_count': 1,
                    'avg_benchmark_score': 89.7,
                    'avg_price': 0.001,
                    'total_context_window': 128000
                },
                'meta': {
                    'name': 'Meta',
                    'models_count': 1,
                    'avg_benchmark_score': 85.1,
                    'avg_price': 0.0005,
                    'total_context_window': 32768
                }
            }
            return provider_stats
        except Exception as e:
            print(f"Erro ao buscar estatísticas de provedores: {e}")
            return {}

# Instância global do dashboard
dashboard = LLMDashboard()

@app.route('/')
def index():
    """Página principal do dashboard"""
    return render_template('index.html')

@app.route('/api/dashboard-data')
def dashboard_data():
    """Endpoint para dados do dashboard"""
    try:
        # Buscar dados
        llm_data = dashboard.get_llm_rankings()
        benchmark_data = dashboard.get_benchmark_data()
        provider_stats = dashboard.get_provider_stats()
        
        # Processar dados
        processed_data = {
            'llm_data': llm_data,
            'benchmark_data': benchmark_data,
            'provider_stats': provider_stats,
            'last_updated': datetime.now().isoformat()
        }
        
        return jsonify(processed_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/charts')
def charts():
    """Endpoint para gráficos"""
    try:
        llm_data = dashboard.get_llm_rankings()
        
        if not llm_data:
            return jsonify({'error': 'Nenhum dado disponível'}), 404
        
        # Criar gráfico de barras para benchmark scores
        df = pd.DataFrame(llm_data)
        
        # Gráfico de Benchmark Scores
        benchmark_fig = go.Figure(data=[
            go.Bar(
                x=df['name'],
                y=df['benchmark_score'],
                text=[f"{score:.1f}" for score in df['benchmark_score']],
                textposition='auto',
                marker_color='rgb(55, 83, 109)'
            )
        ])
        benchmark_fig.update_layout(
            title='Top 10 LLMs por Benchmark Score',
            xaxis_title='Modelo',
            yaxis_title='Benchmark Score',
            height=400
        )
        
        # Gráfico de preços
        price_fig = go.Figure(data=[
            go.Bar(
                x=df['name'],
                y=df['price_per_1k_tokens'],
                text=[f"${price:.4f}" for price in df['price_per_1k_tokens']],
                textposition='auto',
                marker_color='rgb(26, 118, 255)'
            )
        ])
        price_fig.update_layout(
            title='Preços por 1K Tokens',
            xaxis_title='Modelo',
            yaxis_title='Preço (USD)',
            height=400
        )
        
        # Gráfico de velocidade
        speed_fig = go.Figure(data=[
            go.Bar(
                x=df['name'],
                y=df['speed_tokens_per_sec'],
                text=[f"{speed} t/s" for speed in df['speed_tokens_per_sec']],
                textposition='auto',
                marker_color='rgb(255, 193, 7)'
            )
        ])
        speed_fig.update_layout(
            title='Velocidade de Processamento',
            xaxis_title='Modelo',
            yaxis_title='Tokens por Segundo',
            height=400
        )
        
        charts_data = {
            'benchmark': json.dumps(benchmark_fig, cls=plotly.utils.PlotlyJSONEncoder),
            'price': json.dumps(price_fig, cls=plotly.utils.PlotlyJSONEncoder),
            'speed': json.dumps(speed_fig, cls=plotly.utils.PlotlyJSONEncoder)
        }
        
        return jsonify(charts_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats')
def stats():
    """Endpoint para estatísticas gerais"""
    try:
        llm_data = dashboard.get_llm_rankings()
        
        if not llm_data:
            return jsonify({'error': 'Nenhum dado disponível'}), 404
        
        df = pd.DataFrame(llm_data)
        
        stats = {
            'avg_benchmark_score': df['benchmark_score'].mean(),
            'avg_price': df['price_per_1k_tokens'].mean(),
            'avg_speed': df['speed_tokens_per_sec'].mean(),
            'top_performer': df.loc[df['benchmark_score'].idxmax()].to_dict(),
            'most_expensive': df.loc[df['price_per_1k_tokens'].idxmax()].to_dict(),
            'fastest': df.loc[df['speed_tokens_per_sec'].idxmax()].to_dict(),
            'total_models': len(df)
        }
        
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 