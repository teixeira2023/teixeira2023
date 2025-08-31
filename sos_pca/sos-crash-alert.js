/**
 * SOS Crash Alert Simulator
 * Sistema de Alerta de Colisão com Resposta Automática de Emergência
 * 
 * @author Teixeira 2023
 * @version 1.0.0
 */

class SOSCrashAlert {
    constructor() {
        this.isActivated = false;
        this.timer = 0;
        this.timerInterval = null;
        this.lightInterval = null;
        this.internalLightTimer = null;
        this.doorUnlockTimer = null;
        this.doorConfig = 'immediate';
        this.doorsInhibited = false;
        this.doorsUnlocked = false; // Novo: controla se as portas estão destravadas em estado normal

        this.initializeElements();
        this.bindEvents();
        this.addLogEntry('Sistema inicializado', 'normal');
    }

    /**
     * Inicializa todos os elementos DOM necessários
     */
    initializeElements() {
        this.elements = {
            statusIndicator: document.getElementById('statusIndicator'),
            emergencyTimer: document.getElementById('emergencyTimer'),
            crashBtn: document.getElementById('crashBtn'),
            hazardSwitchBtn: document.getElementById('hazardSwitchBtn'),
            keyfobPanicBtn: document.getElementById('keyfobPanicBtn'),
            keyfobUnlockBtn: document.getElementById('keyfobUnlockBtn'),
            saveLogBtn: document.getElementById('saveLogBtn'),
            systemStatus: document.getElementById('systemStatus'),
            timerCard: document.getElementById('timerCard'),
            lights: {
                frontLeft: document.getElementById('frontLeft'),
                frontRight: document.getElementById('frontRight'),
                rearLeft: document.getElementById('rearLeft'),
                rearRight: document.getElementById('rearRight'),
                mirrorLeft: document.getElementById('mirrorLeft'),
                mirrorRight: document.getElementById('mirrorRight')
            },
            doors: {
                frontLeft: document.getElementById('doorFrontLeft'),
                frontRight: document.getElementById('doorFrontRight'),
                rearLeft: document.getElementById('doorRearLeft'),
                rearRight: document.getElementById('doorRearRight')
            },
            internalLights: [
                document.getElementById('internalLight1'),
                document.getElementById('internalLight2'),
                document.getElementById('internalLight3'),
                document.getElementById('internalLight4')
            ]
        };
    }

    /**
     * Configura todos os event listeners
     */
    bindEvents() {
        this.elements.crashBtn.addEventListener('click', () => this.activateSOS());
        
        this.elements.hazardSwitchBtn.addEventListener('click', () => {
            if (this.elements.hazardSwitchBtn.classList.contains('inhibited')) {
                this.addLogEntry('Tentativa de reset via Hazard Switch BLOQUEADA - sistema inibido por 10 segundos', 'warning');
                return;
            }
            this.resetSystem('Hazard Switch');
        });
        
        this.elements.keyfobPanicBtn.addEventListener('click', () => {
            if (this.elements.keyfobPanicBtn.classList.contains('inhibited')) {
                this.addLogEntry('Tentativa de reset via Keyfob Panic BLOQUEADA - sistema inibido por 10 segundos', 'warning');
                return;
            }
            this.resetSystem('Keyfob Panic');
        });
        
        this.elements.keyfobUnlockBtn.addEventListener('click', () => this.attemptDoorUnlock());
        this.elements.saveLogBtn.addEventListener('click', () => this.saveLogToFile());

        // Configuração das portas
        const doorConfigRadios = document.querySelectorAll('input[name="doorConfig"]');
        doorConfigRadios.forEach(radio => {
            radio.addEventListener('change', (e) => {
                this.doorConfig = e.target.value;
                this.addLogEntry(`Configuração das portas alterada para: ${this.doorConfig === 'immediate' ? 'Imediato' : 'Delayed'}`, 'config');
            });
        });
    }

    /**
     * Ativa o sistema SOS de emergência
     */
    activateSOS() {
        if (this.isActivated) return;

        this.isActivated = true;
        this.timer = 0;

        // Atualizar status
        this.elements.statusIndicator.textContent = 'ATIVADO';
        this.elements.statusIndicator.className = 'status-indicator status-activated';
        this.elements.systemStatus.classList.add('active');
        this.elements.timerCard.classList.add('active');

        // Iniciar timer
        this.startTimer();

        // Ativar setas (piscando a cada 1s)
        this.startLightBlinking();

        // Destravar portas conforme configuração
        if (this.doorConfig === 'immediate') {
            this.unlockAllDoors();
            this.addLogEntry('Portas destravadas imediatamente', 'info');
        } else {
            this.inhibitDoors();
            this.scheduleDoorUnlock();
            this.addLogEntry('Portas inibidas por 6 segundos', 'warning');
        }

        // Timer para iluminação interna (10s)
        this.scheduleInternalLights();

        // Inibir botões de reset por 10 segundos
        this.inhibitResetButtons();

        this.addLogEntry('SOS Crash Alert ATIVADO!', 'emergency');
        this.addLogEntry('Setas piscando', 'info');
    }

    /**
     * Inicia o timer de emergência
     */
    startTimer() {
        this.timerInterval = setInterval(() => {
            this.timer++;
            this.updateTimerDisplay();
        }, 1000);
    }

    /**
     * Atualiza a exibição do timer
     */
    updateTimerDisplay() {
        const minutes = Math.floor(this.timer / 60);
        const seconds = this.timer % 60;
        this.elements.emergencyTimer.textContent =
            `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }

    /**
     * Inicia o piscar das luzes de emergência
     */
    startLightBlinking() {
        this.lightInterval = setInterval(() => {
            // Alternar estado das luzes
            const isOn = (this.timer % 2) === 0;

            Object.values(this.elements.lights).forEach(light => {
                if (isOn) {
                    light.classList.add('blinking');
                } else {
                    light.classList.remove('blinking');
                }
            });
        }, 500); // Mudança a cada 500ms para piscar a cada 1s
    }

    /**
     * Destrava todas as portas imediatamente
     */
    unlockAllDoors() {
        Object.values(this.elements.doors).forEach(door => {
            door.classList.remove('inhibited');
            door.classList.add('unlocked');
            const statusElement = door.querySelector('.door-status');
            statusElement.textContent = 'DESTRAVADA';
            statusElement.className = 'door-status door-unlocked';

            // Remover descrição de tempo
            const doorTitle = door.querySelector('h4');
            if (doorTitle.innerHTML.includes('<br><small')) {
                doorTitle.innerHTML = doorTitle.textContent;
            }
        });
        this.doorsInhibited = false;
        this.doorsUnlocked = true; // Marcar portas como destravadas

        // Remover inibição do botão de destravamento
        this.elements.keyfobUnlockBtn.classList.remove('inhibited');
        this.elements.keyfobUnlockBtn.title = '';
    }

    /**
     * Inibe as portas por 6 segundos
     */
    inhibitDoors() {
        Object.values(this.elements.doors).forEach(door => {
            door.classList.add('inhibited');
            const statusElement = door.querySelector('.door-status');
            statusElement.textContent = 'INIBIDO';
            statusElement.className = 'door-status door-locked';

            // Adicionar descrição com informações de tempo
            const doorTitle = door.querySelector('h4');
            if (this.doorConfig === 'delayed') {
                doorTitle.innerHTML = `${doorTitle.textContent}<br><small style="color: #ffd700; font-size: 0.8em;">🔒 Inibido por 6s | 🔓 Destrava em 10s</small>`;
            }
        });
        this.doorsInhibited = true;

        // Inibir o botão de destravamento
        this.elements.keyfobUnlockBtn.classList.add('inhibited');
        this.elements.keyfobUnlockBtn.title = 'Portas inibidas - aguarde 6 segundos';
    }

    /**
     * Agenda o destravamento das portas após 10 segundos
     */
    scheduleDoorUnlock() {
        this.doorUnlockTimer = setTimeout(() => {
            // Após 6 segundos, remover inibição mas manter travadas por mais 4 segundos
            this.removeDoorInhibition();
            this.addLogEntry('Inibição das portas removida após 6 segundos', 'info');

            // Agendar destravamento total após 10 segundos
            setTimeout(() => {
                this.unlockAllDoors();
                this.addLogEntry('Portas destravadas após período total de 10 segundos', 'info');
            }, 4000); // 4 segundos adicionais (6s + 4s = 10s total)
        }, 6000); // 6 segundos
    }

    /**
     * Remove a inibição das portas após 6 segundos
     */
    removeDoorInhibition() {
        Object.values(this.elements.doors).forEach(door => {
            door.classList.remove('inhibited');
            const statusElement = door.querySelector('.door-status');
            statusElement.textContent = 'TRAVADA';
            statusElement.className = 'door-status door-locked';

            // Atualizar descrição para mostrar que ainda está travada
            const doorTitle = door.querySelector('h4');
            if (this.doorConfig === 'delayed') {
                doorTitle.innerHTML = `${doorTitle.textContent.split('<br>')[0]}<br><small style="color: #ffd700; font-size: 0.8em;">🔓 Destrava em 4s</small>`;
            }
        });
        this.doorsInhibited = false;

        // Remover inibição do botão de destravamento
        this.elements.keyfobUnlockBtn.classList.remove('inhibited');
        this.elements.keyfobUnlockBtn.title = '';
    }

    /**
     * Tenta destravar portas via keyfob ou faz toggle quando sistema está normal
     */
    attemptDoorUnlock() {
        // Se o sistema está ativado (emergência)
        if (this.isActivated) {
            if (this.doorsInhibited) {
                this.addLogEntry('Tentativa de reset via keyfob BLOQUEADA - portas inibidas', 'warning');
                return;
            }

            // Verificar se o botão ainda está inibido (primeiros 10 segundos)
            if (this.elements.keyfobUnlockBtn.classList.contains('inhibited')) {
                this.addLogEntry('Tentativa de reset via keyfob BLOQUEADA - sistema inibido por 10 segundos', 'warning');
                return;
            }

            // Se o sistema está ativado e as portas não estão inibidas, resetar o sistema
            this.addLogEntry('Sistema resetado via Keyfob Unlock', 'info');
            this.resetSystem('Keyfob Unlock');
            return;
        }

        // Se o sistema está em estado normal, fazer toggle das portas
        if (this.doorsUnlocked) {
            this.lockAllDoors();
            this.addLogEntry('Portas travadas via Keyfob Unlock', 'info');
        } else {
            this.unlockAllDoors();
            this.addLogEntry('Portas destravadas via Keyfob Unlock', 'info');
        }
    }

    /**
     * Trava todas as portas (para uso em estado normal)
     */
    lockAllDoors() {
        Object.values(this.elements.doors).forEach(door => {
            door.classList.remove('unlocked');
            const statusElement = door.querySelector('.door-status');
            statusElement.textContent = 'TRAVADA';
            statusElement.className = 'door-status door-locked';
        });
        this.doorsUnlocked = false;
    }

    /**
     * Agenda a ativação da iluminação interna após 10 segundos
     */
    scheduleInternalLights() {
        this.internalLightTimer = setTimeout(() => {
            this.activateInternalLights();
        }, 10000); // 10 segundos
    }

    /**
     * Ativa a iluminação interna
     */
    activateInternalLights() {
        this.elements.internalLights.forEach(light => {
            light.classList.add('on');
        });
        this.addLogEntry('Iluminação interna ativada (10s)', 'info');
    }

    /**
     * Reseta todo o sistema
     * @param {string} source - Fonte do reset (Manual, Hazard Switch, Keyfob Panic, etc.)
     */
    resetSystem(source = 'Manual') {
        this.isActivated = false;
        this.timer = 0;

        // Limpar timers
        if (this.timerInterval) clearInterval(this.timerInterval);
        if (this.lightInterval) clearInterval(this.lightInterval);
        if (this.internalLightTimer) clearTimeout(this.internalLightTimer);
        if (this.doorUnlockTimer) clearTimeout(this.doorUnlockTimer);

        // Resetar status
        this.elements.statusIndicator.textContent = 'NORMAL';
        this.elements.statusIndicator.className = 'status-indicator status-normal';
        this.elements.systemStatus.classList.remove('active');
        this.elements.timerCard.classList.remove('active');
        this.elements.emergencyTimer.textContent = '00:00';

        // Resetar luzes
        Object.values(this.elements.lights).forEach(light => {
            light.classList.remove('blinking');
        });

        // Resetar iluminação interna
        this.elements.internalLights.forEach(light => {
            light.classList.remove('on');
        });

        // Resetar portas - manter destravadas após reset
        Object.values(this.elements.doors).forEach(door => {
            door.classList.remove('inhibited');
            door.classList.add('unlocked');
            const statusElement = door.querySelector('.door-status');
            statusElement.textContent = 'DESTRAVADA';
            statusElement.className = 'door-status door-unlocked';

            // Remover descrição de tempo
            const doorTitle = door.querySelector('h4');
            if (doorTitle.innerHTML.includes('<br><small')) {
                doorTitle.innerHTML = doorTitle.textContent;
            }
        });
        this.doorsInhibited = false;
        this.doorsUnlocked = true; // Portas permanecem destravadas após reset

        // Remover inibição do botão de destravamento
        this.elements.keyfobUnlockBtn.classList.remove('inhibited');
        this.elements.keyfobUnlockBtn.title = '';

        // Remover inibição dos outros botões de reset
        this.elements.hazardSwitchBtn.classList.remove('inhibited');
        this.elements.hazardSwitchBtn.title = '';
        this.elements.keyfobPanicBtn.classList.remove('inhibited');
        this.elements.keyfobPanicBtn.title = '';

        this.addLogEntry(`Sistema resetado via ${source}`, 'normal');
        this.addLogEntry('Portas mantidas destravadas após reset', 'info');
    }

    /**
     * Adiciona uma entrada no log de eventos
     * @param {string} message - Mensagem do evento
     * @param {string} type - Tipo do evento (normal, emergency, warning, info, config)
     */
    addLogEntry(message, type) {
        const logContainer = document.getElementById('logContainer');
        const timestamp = new Date().toLocaleTimeString();

        const logEntry = document.createElement('div');
        logEntry.className = 'log-entry';
        logEntry.innerHTML = `
            <span class="log-time">[${timestamp}]</span>
            <span class="log-event">${message}</span>
        `;

        logContainer.appendChild(logEntry);
        logContainer.scrollTop = logContainer.scrollHeight;
    }

    /**
     * Salva o log de eventos em um arquivo TXT
     */
    saveLogToFile() {
        const logContainer = document.getElementById('logContainer');
        const logEntries = logContainer.querySelectorAll('.log-entry');

        if (logEntries.length === 0) {
            this.addLogEntry('Nenhum evento para salvar', 'warning');
            return;
        }

        // Criar conteúdo do arquivo
        let fileContent = '=== SOS CRASH ALERT SIMULATOR - LOG DE EVENTOS ===\n';
        fileContent += `Data/Hora: ${new Date().toLocaleString('pt-BR')}\n`;
        fileContent += '================================================\n\n';

        logEntries.forEach(entry => {
            const time = entry.querySelector('.log-time').textContent;
            const event = entry.querySelector('.log-event').textContent;
            fileContent += `${time} ${event}\n`;
        });

        // Criar blob e download
        const blob = new Blob([fileContent], { type: 'text/plain;charset=utf-8' });
        const url = URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.href = url;
        a.download = `sos_crash_alert_log_${new Date().toISOString().slice(0, 19).replace(/:/g, '-')}.txt`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        URL.revokeObjectURL(url);

        this.addLogEntry('Log salvo com sucesso em arquivo TXT', 'info');
    }

    /**
     * Inibe os botões de reset por 10 segundos
     */
    inhibitResetButtons() {
        this.elements.hazardSwitchBtn.classList.add('inhibited');
        this.elements.hazardSwitchBtn.title = 'Sistema inibido - aguarde 10 segundos';
        this.elements.keyfobPanicBtn.classList.add('inhibited');
        this.elements.keyfobPanicBtn.title = 'Sistema inibido - aguarde 10 segundos';
        this.elements.keyfobUnlockBtn.classList.add('inhibited');
        this.elements.keyfobUnlockBtn.title = 'Sistema inibido - aguarde 10 segundos';

        // Remover inibição após 10 segundos
        setTimeout(() => {
            this.enableResetButtons();
        }, 10000);
    }

    /**
     * Habilita os botões de reset após 10 segundos
     */
    enableResetButtons() {
        this.elements.hazardSwitchBtn.classList.remove('inhibited');
        this.elements.hazardSwitchBtn.title = '';
        this.elements.keyfobPanicBtn.classList.remove('inhibited');
        this.elements.keyfobPanicBtn.title = '';

        // Para o keyfob unlock, verificar se as portas ainda estão inibidas
        if (!this.doorsInhibited) {
            this.elements.keyfobUnlockBtn.classList.remove('inhibited');
            this.elements.keyfobUnlockBtn.title = '';
        }

        this.addLogEntry('Botões de reset habilitados após 10 segundos', 'info');
    }
}

// Inicializar o sistema quando a página carregar
document.addEventListener('DOMContentLoaded', () => {
    new SOSCrashAlert();
});
