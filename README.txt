Revisor Inteligente Dossel 🌳
=============================

Sistema web + pipeline em Python que revisa, avalia e analisa documentos **.docx** com auxílio da API OpenAI (GPT‑4o).

Principais modos
----------------

| Modo | Script chamado | O que faz |
|------|----------------|-----------|
| `completa` | `Processador_Unificado.py` | Revisão textual, bibliográfica, análise lógica/multimodal, relatório técnico e planilha de custos |
| `simples`  | `Revisor_Textual_Estruturado.py` | Correção gramatical rápida |
| `inconsistencias` | `verificador_contradicoes_globais.py` | Detecta contradições locais e globais (texto, tabelas, imagens) |

### Índice
1. Requisitos  
2. Instalação rápida  
3. Ambiente `.env`  
4. Estrutura de pastas  
5. Como rodar  
6. Arquitetura & Scripts  
7. E‑mails e planilha mestra  
8. Troubleshooting  
9. Escalabilidade & Dicas  
10. Licença  

---

### 1. Requisitos

* Python ≥ 3.11  
* Acesso à internet para chamadas OpenAI  
* Conta Gmail (ou SMTP similar) para envio de notificações  
* Sistema operacional testado: Windows 10/11 (funciona em Linux/macOS, ajuste paths)

Instale dependências:

```bash
python -m venv venv
source venv/Scripts/activate      # Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
```

---

### 2. Instalação rápida

```bash
git clone https://github.com/<sua-org>/dossel_project.git
cd dossel_project
cp .env.example .env            # ajuste variáveis
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse **http://127.0.0.1:8000** e faça login com o super‑usuário.

---

### 3. Ambiente `.env`

| Variável | Descrição |
|----------|-----------|
| `OPENAI_API_KEY` | chave da conta OpenAI |
| `EMAIL_REMETENTE` | endereço Gmail que envia alertas |
| `SENHA_APP` | *App Password* do Gmail |
| `DJANGO_SECRET_KEY` | chave secreta do Django |
| `DEBUG` | `True` / `False` |

> Gere uma *App Password* em **myaccount.google.com/apppasswords** se o 2FA estiver ativado.

---

### 4. Estrutura de pastas

```
dossel_project/
│
├─ manage.py
├─ dossel_project/          # settings.py (define PASTA_ENTRADA/SAIDA/CANCELAMENTO)
├─ revisor/                 # app Django: models, views, templates
├─ Scripts/
│   ├─ Gerenciador_Revisores_Estruturados.py
│   ├─ Processador_Unificado.py
│   ├─ Revisor_Textual_Estruturado.py
│   └─ verificador_contradicoes_globais.py
└─ media/
    ├─ entrada/             # upload recebido
    └─ saida/<nome>/        # resultados por documento
```

*Os scripts **não** movem arquivos para fora de `media/`; a view garante os caminhos corretos.*

---

### 5. Como rodar

#### Web (recomendado)

1. **Upload** do documento em `/upload/`.  
2. Escolha o **modo** (Completa, Simples ou Inconsistências).  
3. Acompanhe o progresso em `/acompanhamento/` (barra e %).  
4. Abra `/resultados/<id>/` para baixar arquivos finais.  
5. Consulte histórico em `/historico/`.

#### Linha de comando (debug / batch)

```bash
python Scripts/Gerenciador_Revisores_Estruturados.py   "Relatorio.docx" --id_revisao 1 --email user@dosselambiental.com.br --modo completa
```

---

### 6. Arquitetura & Scripts

```
Django view  ──▶  Gerenciador
                   │
                   ├──▶ Modo completa ─▶ Processador_Unificado.py
                   ├──▶ Modo simples  ─▶ Revisor_Textual_Estruturado.py
                   └──▶ Modo inconsist ─▶ verificador_contradicoes_globais.py
```

* **Gerenciador**: controla fila `QueueEntry`, dispara subprocessos, monitora cancelamento, envia e‑mail e grava planilha mestra.  
* **Processador_Unificado**: pipeline completo (mapeia + revisa + analisa + gera relatórios).  
* **Revisor_Textual_Estruturado**: revisão gramatical básica.  
* **Verificador_Contradicoes_Globais**: detecta erros lógicos/números, descreve imagens (GPT‑4o Vision).

---

### 7. E‑mails e planilha mestra

* Envio automático ao usuário quando a revisão atinge 100 %.  
* Planilha `relatorio_geral_revisoes.xlsx` consolida data, páginas, custo (R$), tokens, caminho de saída.

---

### 8. Troubleshooting

| Sintoma | Possível causa | Ação |
|---------|----------------|------|
| `OPENAI_API_KEY not found` | `.env` mal configurado | Verifique variável |
| Progresso parado | Exceção nos scripts | Cheque `logs/revisao_<id>_stderr.log` |
| E‑mail não chega | App Password ou SMTP bloqueado | Teste credenciais |
| Saída não aparece | Permissões ou caminho | Revise `MEDIA_ROOT`, `PASTA_SAIDA` |

---

### 9. Escalabilidade & Dicas

* **Multiprocessing**: ajuste `MAX_WORKERS` conforme CPU/RAM (24 GB atuais).  
* **Docker**: forneça `Dockerfile` e mapeie volume `media/`.  
* **Fila real**: para alto volume, considere Celery ou RQ.  
* **PostgreSQL**: troque SQLite por Postgres para concorrência melhor.

---

### 10. Licença

Projeto interno © 2025 **Dossel Ambiental**. Uso restrito; consulte o jurídico para distribuição externa.
