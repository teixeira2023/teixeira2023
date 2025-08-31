/**
 * Configurações do Sistema SOS Crash Alert
 * Arquivo de configuração separado para facilitar manutenção
 * 
 * @author Teixeira 2023
 * @version 1.0.0
 */

const SOS_CONFIG = {
    // Configurações de Timing
    TIMING: {
        EMERGENCY_INHIBITION: 10000,    // 10 segundos de inibição
        DOOR_INHIBITION: 6000,          // 6 segundos de inibição de portas
        DOOR_TOTAL_DELAY: 10000,        // 10 segundos total para destravamento
        INTERNAL_LIGHTS_DELAY: 10000,   // 10 segundos para iluminação interna
        LIGHT_BLINK_INTERVAL: 500,      // 500ms para piscar das luzes
        TIMER_UPDATE_INTERVAL: 1000     // 1 segundo para atualização do timer
    },

    // Configurações de Interface
    UI: {
        ANIMATION_DURATION: '0.3s',
        PULSE_ANIMATION: '1s infinite',
        BLINK_ANIMATION: '1s infinite',
        CONTAINER_MAX_WIDTH: '900px',
        LOG_MAX_HEIGHT: '200px'
    },

    // Configurações de Cores
    COLORS: {
        PRIMARY: '#ff6b6b',
        SUCCESS: '#4CAF50',
        WARNING: '#ff9800',
        INFO: '#ffd700',
        DANGER: '#ff5252',
        BACKGROUND: 'linear-gradient(135deg, #1e3c72, #2a5298)',
        CONTAINER_BG: 'rgba(0, 0, 0, 0.8)',
        CARD_BG: 'rgba(255, 255, 255, 0.1)'
    },

    // Configurações de Texto
    TEXTS: {
        STATUS: {
            NORMAL: 'NORMAL',
            ACTIVATED: 'ATIVADO',
            INHIBITED: 'INIBIDO',
            LOCKED: 'TRAVADA',
            UNLOCKED: 'DESTRAVADA'
        },
        MESSAGES: {
            SYSTEM_INIT: 'Sistema inicializado',
            SOS_ACTIVATED: 'SOS Crash Alert ATIVADO!',
            LIGHTS_ACTIVATED: 'Setas piscando',
            INTERNAL_LIGHTS: 'Iluminação interna ativada (10s)',
            DOORS_IMMEDIATE: 'Portas destravadas imediatamente',
            DOORS_INHIBITED: 'Portas inibidas por 6 segundos',
            DOORS_UNLOCKED: 'Portas destravadas após período total de 10 segundos',
            RESET_ENABLED: 'Botões de reset habilitados após 10 segundos',
            DOORS_LOCKED_KEYFOB: 'Portas travadas via Keyfob Unlock',
            DOORS_UNLOCKED_KEYFOB: 'Portas destravadas via Keyfob Unlock',
            DOORS_MAINTAINED_UNLOCKED: 'Portas mantidas destravadas após reset'
        }
    },

    // Configurações de Log
    LOG: {
        TYPES: ['normal', 'emergency', 'warning', 'info', 'config'],
        EXPORT_HEADER: '=== SOS CRASH ALERT SIMULATOR - LOG DE EVENTOS ===',
        EXPORT_SEPARATOR: '================================================'
    },

    // Configurações de Responsividade
    RESPONSIVE: {
        MOBILE_BREAKPOINT: 768,
        MOBILE_MARGIN: '20px',
        MOBILE_PADDING: '20px'
    }
};

// Exportar configuração para uso em outros módulos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SOS_CONFIG;
}
