# 📨 Sistema de Envio de Notificações

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/Ruan342/Envio_notificacao_Opa)
![License](https://img.shields.io/badge/License-MIT-green)

Sistema automatizado para envio de notificações personalizadas via terminal, com integração a APIs externas.

## ✨ Funcionalidades
- Envio de notificações para múltiplos usuários simultaneamente
- Templates de mensagens personalizáveis
- Configuração simplificada via arquivo `.env`
- Interface CLI amigável com feedback visual

## 💻 Tecnologias Utilizadas
Desenvolvido em **Python 3.9+** com:
- `requests` para integração com APIs REST
- `python-dotenv` para gerenciamento de configurações
- `sqlite3` para armazenamento local de histórico
- `argparse` para construção da interface de linha de comando
- Git para controle de versão

## 🚀 Como Utilizar

1. Clone o repositório:
```bash
git clone https://github.com/Ruan342/Envio_notificacao_Opa.git
cd Envio_notificacao_Opa
```
2, configure o ambiente
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
pip install -r requirements.txt
