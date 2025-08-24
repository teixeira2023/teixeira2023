"""
Módulo de utilitários para o ZL Project
Contém funções auxiliares que podem ser reutilizadas em diferentes partes do app
"""

import streamlit as st
import base64
import os
from typing import Optional, Dict, Any

def load_image_base64(image_path: str) -> Optional[str]:
    """
    Carrega e converte imagem para base64
    
    Args:
        image_path: Caminho para a imagem
        
    Returns:
        String base64 da imagem ou None se erro
    """
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        return None
    except Exception as e:
        st.error(f"Erro ao carregar imagem: {e}")
        return None

def create_metric_card(title: str, value: str, delta: str = "", icon: str = "📊") -> None:
    """
    Cria um card de métrica padronizado
    
    Args:
        title: Título da métrica
        value: Valor principal
        delta: Variação (opcional)
        icon: Emoji do ícone
    """
    st.metric(
        label=f"{icon} {title}",
        value=value,
        delta=delta
    )

def show_status_indicator(status: str, message: str, status_type: str = "info") -> None:
    """
    Mostra um indicador de status padronizado
    
    Args:
        status: Texto do status
        message: Mensagem adicional
        status_type: Tipo do status (success, info, warning, error)
    """
    if status_type == "success":
        st.success(f"🟢 {status}")
    elif status_type == "warning":
        st.warning(f"🟡 {status}")
    elif status_type == "error":
        st.error(f"🔴 {status}")
    else:
        st.info(f"🔵 {status}")
    
    st.caption(message)

def create_expandable_section(title: str, content: str, expanded: bool = False) -> None:
    """
    Cria uma seção expansível
    
    Args:
        title: Título da seção
        content: Conteúdo da seção
        expanded: Se deve estar expandida por padrão
    """
    with st.expander(title, expanded=expanded):
        st.markdown(content)

def save_to_session_state(key: str, value: Any) -> None:
    """
    Salva valor no session state do Streamlit
    
    Args:
        key: Chave para armazenar
        value: Valor a ser armazenado
    """
    st.session_state[key] = value

def get_from_session_state(key: str, default: Any = None) -> Any:
    """
    Obtém valor do session state do Streamlit
    
    Args:
        key: Chave para buscar
        default: Valor padrão se não encontrado
        
    Returns:
        Valor armazenado ou default
    """
    return st.session_state.get(key, default)
