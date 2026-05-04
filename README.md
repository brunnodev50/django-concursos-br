# ConcursosBR — Sistema de Gestão de Concursos Públicos

Sistema web completo desenvolvido em **Django + SQLite** para cadastro, publicação e candidatura em concursos públicos, com pagamento integrado via **Mercado Pago** (PIX e Boleto) e recuperação de senha por **e-mail** e **WhatsApp**.

---

## Índice

1. [Visão Geral](#visão-geral)
2. [Screenshots](#screenshots)
3. [Funcionalidades](#funcionalidades)
4. [Tecnologias](#tecnologias)
5. [Estrutura do Projeto](#estrutura-do-projeto)
6. [Requisitos](#requisitos)
7. [Instalação](#instalação)
8. [Configuração do .env](#configuração-do-env)
9. [Rodando o Projeto](#rodando-o-projeto)
10. [Criando o Superusuário](#criando-o-superusuário)
11. [Painel Administrativo](#painel-administrativo)
12. [Rotas do Sistema](#rotas-do-sistema)
13. [Modelos de Dados](#modelos-de-dados)
14. [Integrações Externas](#integrações-externas)
15. [Deploy em Produção](#deploy-em-produção)
16. [Perguntas Frequentes](#perguntas-frequentes)

---

## Screenshots

> Todas as telas foram capturadas nas versões **Desktop** e **Mobile**.

---

### Tela Inicial — Lista de Concursos

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Tela Home Desktop.png" width="640" alt="Home Desktop"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Tela Home Mobile parte 1.png" width="280" alt="Home Mobile 1"/>
      <br/>
      <img src="docs/screenshots/Tela Home Mobile parte 2.png" width="280" alt="Home Mobile 2"/>
    </td>
  </tr>
</table>

---

### Login

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Tela Login Desktop.png" width="640" alt="Login Desktop"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Tela Login Celular.png" width="280" alt="Login Mobile"/>
    </td>
  </tr>
</table>

---

### Redefinir Senha

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Redefinir senha desktop.png" width="640" alt="Redefinir Senha Desktop"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Redefinir senha mobile.png" width="280" alt="Redefinir Senha Mobile"/>
    </td>
  </tr>
</table>

---

### Cadastro de Candidato

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Criar conta de candidato Desktop Parte 1.png" width="640" alt="Cadastro Candidato Desktop 1"/>
      <br/><br/>
      <img src="docs/screenshots/Criar conta de candidato Desktop Parte 2.png" width="640" alt="Cadastro Candidato Desktop 2"/>
      <br/><br/>
      <img src="docs/screenshots/Criar conta de candidato Desktop Parte 3.png" width="640" alt="Cadastro Candidato Desktop 3"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Criar conta de candidato Mobile Parte 1.png" width="280" alt="Cadastro Candidato Mobile 1"/>
      <br/>
      <img src="docs/screenshots/Criar conta de candidato Mobile Parte 2.png" width="280" alt="Cadastro Candidato Mobile 2"/>
      <br/>
      <img src="docs/screenshots/Criar conta de candidato Mobile Parte 3.png" width="280" alt="Cadastro Candidato Mobile 3"/>
    </td>
  </tr>
</table>

---

### Dashboard do Candidato

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Tela Dashboard Candidato.png" width="640" alt="Dashboard Candidato Desktop"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Tela Dashboard Candidato mobile.png" width="280" alt="Dashboard Candidato Mobile"/>
    </td>
  </tr>
</table>

---

### Lista de Concursos (logado)

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Dashboard menu Concursos Desktop.png" width="640" alt="Concursos Desktop"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Dashboard menu Concursos Mobile.png" width="280" alt="Concursos Mobile"/>
    </td>
  </tr>
</table>

---

### Detalhe do Concurso

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Dashboard empresa veja mais desktop parte 1.png" width="640" alt="Detalhe Concurso Desktop 1"/>
      <br/><br/>
      <img src="docs/screenshots/Dashboard empresa veja mais desktop parte 2.png" width="640" alt="Detalhe Concurso Desktop 2"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Dashboard empresa veja mais mobile parte 1.png" width="280" alt="Detalhe Concurso Mobile 1"/>
      <br/>
      <img src="docs/screenshots/Dashboard empresa veja mais mobile parte 2.png" width="280" alt="Detalhe Concurso Mobile 2"/>
    </td>
  </tr>
</table>

---

### Tela de Inscrição no Concurso

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Tela de inscrição desktop.png" width="640" alt="Inscrição Desktop"/>
    </td>
  </tr>
</table>

---

### Pagamento da Taxa (PIX / Boleto)

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Tela de pagamento de inscrição via desktop.png" width="640" alt="Pagamento Desktop"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Tela de pagamento de inscrição via mobile.png" width="280" alt="Pagamento Mobile"/>
    </td>
  </tr>
</table>

---

### Minhas Candidaturas

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Tela de minhas candidaturas desktop.png" width="640" alt="Candidaturas Desktop"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Tela de minhas candidaturas mobile.png" width="280" alt="Candidaturas Mobile"/>
    </td>
  </tr>
</table>

---

### Cadastro de Empresa

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Cadastro de empresa desktop 1.png" width="640" alt="Cadastro Empresa Desktop 1"/>
      <br/><br/>
      <img src="docs/screenshots/Cadastro de empresa desktop 2.png" width="640" alt="Cadastro Empresa Desktop 2"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Cadastro de empresa mobile 1.png" width="280" alt="Cadastro Empresa Mobile 1"/>
      <br/>
      <img src="docs/screenshots/Cadastro de empresa mobile 2.png" width="280" alt="Cadastro Empresa Mobile 2"/>
    </td>
  </tr>
</table>

---

### Dashboard da Empresa

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Dashboard empresa desktop.png" width="640" alt="Dashboard Empresa Desktop"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Dashboard empresa mobile.png" width="280" alt="Dashboard Empresa Mobile 1"/>
      <br/>
      <img src="docs/screenshots/Dashboard empresa mobile parte 2.png" width="280" alt="Dashboard Empresa Mobile 2"/>
    </td>
  </tr>
</table>

---

### Cadastrar Novo Concurso (Empresa)

<table>
  <tr>
    <th align="center">🖥️ Desktop</th>
    <th align="center">📱 Mobile</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Cadastrar novo concurso tela parte 1 desktop.png" width="640" alt="Novo Concurso Desktop 1"/>
      <br/><br/>
      <img src="docs/screenshots/Cadastrar novo concurso tela parte 2 desktop.png" width="640" alt="Novo Concurso Desktop 2"/>
      <br/><br/>
      <img src="docs/screenshots/Cadastrar novo concurso tela parte 3 desktop.png" width="640" alt="Novo Concurso Desktop 3"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Cadastrar novo concurso tela parte 1 mobile.png" width="280" alt="Novo Concurso Mobile 1"/>
      <br/>
      <img src="docs/screenshots/Cadastrar novo concurso tela parte 2 mobile.png" width="280" alt="Novo Concurso Mobile 2"/>
      <br/>
      <img src="docs/screenshots/Cadastrar novo concurso tela parte 3 mobile.png" width="280" alt="Novo Concurso Mobile 3"/>
    </td>
  </tr>
</table>

---

### Painel Administrativo (Django Admin)

<table>
  <tr>
    <th align="center">Login Admin</th>
    <th align="center">Admin Logado</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/screenshots/Administração do Django.png" width="640" alt="Admin Login"/>
    </td>
    <td align="center">
      <img src="docs/screenshots/Administração do Django logado.png" width="640" alt="Admin Logado"/>
    </td>
  </tr>
</table>

---

## Visão Geral

O **ConcursosBR** é uma plataforma que conecta **candidatos** a **empresas/órgãos** que publicam concursos públicos. O candidato cria seu perfil completo, navega pelos concursos abertos com filtros por estado e cidade, se candidata e paga a taxa de inscrição diretamente pela plataforma.

```
Candidato  →  Cadastro  →  Login  →  Busca Concursos  →  Se Candidata  →  Paga (PIX ou Boleto)
Empresa    →  Cadastro  →  Login  →  Cria Concurso  →  Publica Editais  →  Acompanha Inscrições
```

---

## Funcionalidades

### Candidato
- Cadastro com foto, CPF, RG + órgão emissor, nome completo, nome da mãe e do pai, renda mensal, data de nascimento
- Até **2 telefones** (celular e/ou fixo), cada um com indicação de WhatsApp
- Login por e-mail e senha
- Recuperação de senha via **e-mail** ou **WhatsApp**
- Busca e filtro de concursos por estado, cidade e palavra-chave
- Candidatura em concursos abertos com escolha de cargo
- Pagamento da taxa por **PIX** (QR Code + copia e cola) ou **Boleto Bancário**
- Acompanhamento de candidaturas com número de inscrição único

### Empresa / Órgão
- Cadastro com razão social, CNPJ, responsável
- Dashboard com todos os concursos cadastrados
- Criação e edição de concursos com múltiplos cargos (vagas, salário, PCD)
- Publicação de **editais em PDF** com suporte a retificações
- Controle de status do concurso: Rascunho → Aberto → Encerrado / Suspenso

### Administrador
- Painel admin completo (`/admin/`) com gestão de todos os modelos
- Ações em lote: publicar e encerrar concursos
- Visualização de pagamentos e status de candidaturas

---

## Tecnologias

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.10+ | Linguagem base |
| Django | 6.x | Framework web |
| SQLite | — | Banco de dados |
| Bootstrap | 5.3 | Interface |
| Bootstrap Icons | 1.11 | Ícones |
| django-crispy-forms | 2.x | Formulários |
| crispy-bootstrap5 | — | Tema Bootstrap 5 |
| django-localflavor | 4.x | Validação BR |
| Pillow | 10.x | Upload de fotos |
| python-decouple | 3.x | Variáveis de ambiente |
| Mercado Pago SDK | 2.x | Pagamentos PIX/Boleto |
| Twilio | 9.x | WhatsApp API |
| Celery + Redis | 5.x / — | Tarefas assíncronas (opcional) |

---

## Estrutura do Projeto

```
sistema concurso/
│
├── manage.py                   # Ponto de entrada Django
├── requirements.txt            # Dependências Python
├── .env                        # Variáveis de ambiente (não versionar)
├── .env.example                # Modelo do .env
├── .gitignore
├── iniciar.bat                 # Script de inicialização (Windows)
│
├── core/                       # Configuração central do projeto
│   ├── __init__.py
│   ├── celery.py               # Configuração Celery
│   ├── urls.py                 # URLs raiz
│   ├── wsgi.py
│   └── settings/
│       ├── base.py             # Configurações compartilhadas
│       ├── development.py      # Desenvolvimento (DEBUG=True)
│       └── production.py       # Produção (HTTPS, segurança)
│
├── apps/
│   ├── accounts/               # Autenticação e usuários
│   │   ├── models.py           # Usuario, TokenRedefinicaoSenha
│   │   ├── views.py            # Login, logout, reset de senha
│   │   ├── forms.py
│   │   ├── backends.py         # Autenticação por e-mail
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── candidatos/             # Perfil do candidato
│   │   ├── models.py           # Candidato, Telefone
│   │   ├── views.py            # Cadastro, edição de perfil
│   │   ├── forms.py            # Formulários + formset de telefones
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── empresas/               # Perfil da empresa
│   │   ├── models.py           # Empresa
│   │   ├── views.py            # Cadastro, dashboard
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── concursos/              # Concursos, cargos e editais
│   │   ├── models.py           # Concurso, Cargo, Edital
│   │   ├── views.py            # CRUD de concursos, upload de edital
│   │   ├── forms.py            # Formulários + formset de cargos + filtro
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── candidaturas/           # Inscrições dos candidatos
│   │   ├── models.py           # Candidatura
│   │   ├── views.py            # Candidatar, listar candidaturas
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   └── pagamentos/             # Pagamentos via Mercado Pago
│       ├── models.py           # Pagamento
│       ├── views.py            # Checkout, confirmação, webhook
│       ├── urls.py
│       └── admin.py
│
├── utils/
│   ├── validators.py           # Validação de CPF e CNPJ
│   ├── whatsapp.py             # Envio via Twilio WhatsApp
│   └── mercadopago_client.py   # Criação de PIX e Boleto
│
├── templates/
│   ├── base.html               # Layout base com navbar e footer
│   ├── 404.html / 500.html     # Páginas de erro
│   ├── registration/           # Login
│   ├── accounts/               # Reset de senha
│   ├── candidatos/             # Cadastro e perfil
│   ├── empresas/               # Dashboard e formulário de concurso
│   ├── concursos/              # Lista e detalhe
│   ├── candidaturas/           # Confirmação e lista
│   └── pagamentos/             # Checkout PIX/Boleto e confirmação
│
├── static/
│   ├── css/style.css           # Estilos customizados
│   └── js/main.js              # Máscaras CPF/CNPJ/telefone, preview foto
│
└── media/
    ├── fotos_candidatos/       # Fotos de perfil
    └── editais/                # PDFs dos editais
```

---

## Requisitos

- **Python 3.10 ou superior**
- **pip**
- Windows, Linux ou macOS

Para funcionalidades opcionais:
- **Redis** (tarefas assíncronas com Celery)
- Conta **Mercado Pago** (pagamentos PIX e Boleto)
- Conta **Twilio** (reset de senha via WhatsApp)
- Conta de e-mail com SMTP (reset de senha por e-mail)

---

## Instalação

### Passo 1 — Clone ou extraia o projeto

Se tiver o Git:
```bash
git clone <url-do-repositorio> sistema-concurso
cd sistema-concurso
```

Ou apenas extraia o ZIP na pasta desejada e abra o terminal nela.

---

### Passo 2 — Crie o ambiente virtual

**Windows:**
```bat
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

> Após ativar, o terminal mostrará `(.venv)` no início da linha.

---

### Passo 3 — Instale as dependências

```bash
pip install -r requirements.txt
```

Para habilitar **pagamentos** (Mercado Pago):
```bash
pip install mercadopago==2.2.3
```

Para habilitar **WhatsApp** (Twilio):
```bash
pip install twilio==9.3.2
```

Para habilitar **tarefas assíncronas** (Celery):
```bash
pip install celery==5.4.0 redis==5.1.1
```

---

### Passo 4 — Configure o arquivo `.env`

Copie o arquivo de exemplo:

**Windows:**
```bat
copy .env.example .env
```

**Linux / macOS:**
```bash
cp .env.example .env
```

Edite o `.env` com suas configurações (veja a seção [Configuração do .env](#configuração-do-env)).

---

### Passo 5 — Aplique as migrations

```bash
python manage.py migrate
```

---

### Passo 6 — Crie o superusuário (administrador)

```bash
python manage.py createsuperuser
```

Informe e-mail e senha quando solicitado. Ou rode o comando abaixo substituindo os dados:

```bash
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser(email='admin@email.com', password='suasenha')
print('Superusuário criado!')
"
```

---

### Passo 7 — Inicie o servidor

**Windows (duplo clique ou terminal):**
```bat
iniciar.bat
```

**Ou manualmente:**
```bash
python manage.py runserver
```

Acesse: **`http://localhost:8000`**

---

## Configuração do .env

O arquivo `.env` fica na raiz do projeto e contém todas as variáveis sensíveis. **Nunca versione este arquivo.**

```env
# ─── OBRIGATÓRIO ──────────────────────────────────────────────
SECRET_KEY=sua-chave-secreta-unica-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# ─── E-MAIL (para reset de senha por e-mail) ──────────────────
# Em desenvolvimento, deixe DEBUG=True e os e-mails aparecem no console.
# Para Gmail: ative "Senhas de App" em myaccount.google.com/security
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu@gmail.com
EMAIL_HOST_PASSWORD=xxxx-xxxx-xxxx-xxxx   # senha de app, NÃO sua senha normal

# ─── MERCADO PAGO (pagamentos PIX e Boleto) ───────────────────
# Obtenha em: https://www.mercadopago.com.br/developers/panel
MP_ACCESS_TOKEN=APP_USR-000...
MP_PUBLIC_KEY=APP_USR-000...
MP_WEBHOOK_SECRET=sua-chave-webhook

# ─── TWILIO (reset de senha via WhatsApp) ─────────────────────
# Obtenha em: https://www.twilio.com/console
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886

# ─── URL BASE DO SISTEMA ──────────────────────────────────────
# Em produção: https://seudominio.com.br
BASE_URL=http://localhost:8000

# ─── CELERY / REDIS (opcional) ────────────────────────────────
CELERY_BROKER_URL=redis://localhost:6379/0
```

### Como gerar a SECRET_KEY

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## Rodando o Projeto

### Desenvolvimento

```bash
# Ativar ambiente virtual
.venv\Scripts\activate          # Windows
source .venv/bin/activate        # Linux/macOS

# Iniciar servidor
python manage.py runserver
```

Servidor disponível em `http://localhost:8000`

### Porta diferente

```bash
python manage.py runserver 8080
```

### Verificar se há erros de configuração

```bash
python manage.py check
```

### Criar novas migrations após alterar models

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Criando o Superusuário

O superusuário tem acesso total ao painel administrativo.

### Opção 1 — Interativo

```bash
python manage.py createsuperuser
```

Preencha:
```
Email: admin@exemplo.com
Password: ********
Password (again): ********
```

### Opção 2 — Por comando (sem interação)

```bash
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@exemplo.com').exists():
    User.objects.create_superuser(email='admin@exemplo.com', password='suasenha')
    print('Criado!')
else:
    print('Já existe.')
"
```

---

## Painel Administrativo

Acesse `http://localhost:8000/admin/` com as credenciais do superusuário.

### O que você pode fazer no admin

| Seção | Ações |
|---|---|
| **Usuários** | Listar, criar, bloquear usuários |
| **Candidatos** | Ver perfis completos, telefones |
| **Empresas** | Gerenciar empresas cadastradas |
| **Concursos** | Publicar, encerrar, suspender concursos em lote |
| **Cargos** | Gerenciar cargos inline no concurso |
| **Editais** | Ver e baixar PDFs publicados |
| **Candidaturas** | Ver todas as inscrições e status |
| **Pagamentos** | Ver pagamentos, status, IDs do Mercado Pago |
| **Tokens de Senha** | Ver tokens de redefinição usados/expirados |

### Ações em lote (concursos)

No admin de Concursos, selecione vários registros e use:
- **Publicar concursos selecionados** → status muda para "Aberto"
- **Encerrar concursos selecionados** → status muda para "Encerrado"

---

## Rotas do Sistema

### Públicas

| Método | URL | Descrição |
|---|---|---|
| GET | `/` | Redireciona para `/concursos/` |
| GET | `/concursos/` | Lista de concursos abertos com filtros |
| GET | `/concursos/<id>/` | Detalhe do concurso |
| GET | `/accounts/login/` | Login |
| GET | `/accounts/redefinir-senha/solicitar/` | Solicitar reset de senha |
| GET | `/accounts/redefinir-senha/<token>/` | Formulário de nova senha |
| GET | `/candidatos/cadastro/` | Cadastro de candidato |
| GET | `/empresas/cadastro/` | Cadastro de empresa |

### Autenticadas — Candidato

| Método | URL | Descrição |
|---|---|---|
| GET/POST | `/candidatos/perfil/` | Editar perfil |
| GET/POST | `/candidaturas/concurso/<id>/candidatar/` | Se inscrever em um concurso |
| GET | `/candidaturas/minhas/` | Listar minhas candidaturas |
| GET/POST | `/pagamentos/checkout/<id>/` | Pagamento da taxa |
| GET | `/pagamentos/confirmacao/<id>/` | Confirmação PIX / Boleto |

### Autenticadas — Empresa

| Método | URL | Descrição |
|---|---|---|
| GET | `/empresas/dashboard/` | Dashboard da empresa |
| GET/POST | `/concursos/criar/` | Criar novo concurso |
| GET/POST | `/concursos/<id>/editar/` | Editar concurso |
| GET/POST | `/concursos/<id>/edital/` | Publicar edital PDF |

### Webhook

| Método | URL | Descrição |
|---|---|---|
| POST | `/pagamentos/webhook/mercadopago/` | Notificação de pagamento (Mercado Pago) |

---

## Modelos de Dados

### Usuario (`accounts`)
| Campo | Tipo | Descrição |
|---|---|---|
| id | UUID | Chave primária |
| email | EmailField | Login único |
| tipo | CharField | `candidato`, `empresa` ou `admin` |
| is_active | BooleanField | Conta ativa |
| criado_em | DateTimeField | Data de cadastro |

### Candidato (`candidatos`)
| Campo | Tipo | Descrição |
|---|---|---|
| usuario | OneToOne → Usuario | Vínculo com a conta |
| foto | ImageField | Foto de perfil |
| nome_completo | CharField | Nome completo |
| cpf | CharField | CPF (validado) |
| rg | CharField | Número do RG |
| orgao_emissor | CharField | Ex: SSP/SP |
| nome_mae | CharField | Nome da mãe |
| nome_pai | CharField | Nome do pai |
| renda_mensal | DecimalField | Renda em R$ |
| data_nascimento | DateField | Data de nascimento |

### Telefone (`candidatos`)
| Campo | Tipo | Descrição |
|---|---|---|
| candidato | FK → Candidato | Vínculo |
| numero | CharField | Número com máscara |
| tipo | CharField | `celular` ou `fixo` |
| tem_whatsapp | BooleanField | Possui WhatsApp? |

### Empresa (`empresas`)
| Campo | Tipo | Descrição |
|---|---|---|
| usuario | OneToOne → Usuario | Vínculo |
| razao_social | CharField | Razão social |
| nome_fantasia | CharField | Nome fantasia |
| cnpj | CharField | CNPJ (validado) |
| responsavel | CharField | Nome do responsável |
| telefone | CharField | Telefone de contato |

### Concurso (`concursos`)
| Campo | Tipo | Descrição |
|---|---|---|
| empresa | FK → Empresa | Empresa responsável |
| titulo | CharField | Título do concurso |
| orgao | CharField | Órgão realizador |
| estado | CharField | UF (sigla) |
| cidade | CharField | Cidade |
| vagas_total | IntegerField | Total de vagas |
| taxa_inscricao | DecimalField | Valor da taxa em R$ |
| data_abertura | DateField | Início das inscrições |
| data_fechamento | DateField | Fim das inscrições |
| data_prova | DateField | Data da prova |
| status | CharField | `rascunho`, `aberto`, `encerrado`, `suspenso` |

### Cargo (`concursos`)
| Campo | Tipo | Descrição |
|---|---|---|
| concurso | FK → Concurso | Vínculo |
| nome | CharField | Nome do cargo |
| nivel_escolaridade | CharField | Nível exigido |
| salario | DecimalField | Salário em R$ |
| vagas | IntegerField | Número de vagas |
| vagas_pcd | IntegerField | Vagas para PCD |

### Edital (`concursos`)
| Campo | Tipo | Descrição |
|---|---|---|
| concurso | FK → Concurso | Vínculo |
| titulo | CharField | Título do edital |
| arquivo | FileField | PDF do edital |
| data_publicacao | DateField | Data da publicação |
| retificacao | BooleanField | É retificação? |

### Candidatura (`candidaturas`)
| Campo | Tipo | Descrição |
|---|---|---|
| candidato | FK → Candidato | Candidato inscrito |
| concurso | FK → Concurso | Concurso |
| cargo | FK → Cargo | Cargo escolhido |
| status | CharField | `pendente`, `aguardando_pagamento`, `paga`, `cancelada` |
| numero_inscricao | CharField | Número único gerado automaticamente |

### Pagamento (`pagamentos`)
| Campo | Tipo | Descrição |
|---|---|---|
| candidatura | OneToOne → Candidatura | Vínculo |
| metodo | CharField | `pix` ou `boleto` |
| valor | DecimalField | Valor pago |
| status | CharField | `pendente`, `pago`, `cancelado`, `expirado` |
| mp_payment_id | CharField | ID do Mercado Pago |
| pix_qr_code | TextField | QR Code em base64 |
| pix_qr_code_texto | TextField | Código Pix copia e cola |
| boleto_url | URLField | Link do boleto PDF |
| boleto_barcode | CharField | Código de barras |
| pago_em | DateTimeField | Data/hora do pagamento |

---

## Integrações Externas

### Mercado Pago (Pagamentos)

1. Crie uma conta em [mercadopago.com.br/developers](https://www.mercadopago.com.br/developers)
2. Acesse **Suas integrações → Credenciais**
3. Copie o **Access Token** e **Public Key** de **produção**
4. Cole no `.env`
5. Configure o **Webhook** no painel do Mercado Pago:
   - URL: `https://seudominio.com.br/pagamentos/webhook/mercadopago/`
   - Evento: `payment`
6. Copie a chave secreta do webhook para `MP_WEBHOOK_SECRET` no `.env`

> Em desenvolvimento, use as credenciais de **teste** (Sandbox) para não cobrar de verdade.

---

### Twilio — Reset de Senha via WhatsApp

1. Crie uma conta em [twilio.com](https://www.twilio.com)
2. Acesse o **Console** e copie **Account SID** e **Auth Token**
3. Ative o **WhatsApp Sandbox** (gratuito para testes)
4. Cole as credenciais no `.env`
5. O candidato precisa ter um telefone com WhatsApp cadastrado no perfil

---

### E-mail (Reset de Senha)

Para usar o Gmail:

1. Acesse [myaccount.google.com/security](https://myaccount.google.com/security)
2. Ative **Verificação em duas etapas**
3. Vá em **Senhas de App** e gere uma senha para "Outro (nome personalizado)"
4. Use essa senha (16 caracteres) em `EMAIL_HOST_PASSWORD` no `.env`

> Em desenvolvimento (`DEBUG=True`), os e-mails são exibidos no console do terminal automaticamente, sem precisar configurar SMTP.

---

## Deploy em Produção

### 1. Variáveis de ambiente

```env
DEBUG=False
SECRET_KEY=chave-muito-longa-e-aleatoria
ALLOWED_HOSTS=seudominio.com.br,www.seudominio.com.br
BASE_URL=https://seudominio.com.br
```

### 2. Use as configurações de produção

```bash
export DJANGO_SETTINGS_MODULE=core.settings.production
```

### 3. Colete os arquivos estáticos

```bash
python manage.py collectstatic --noinput
```

### 4. Use Gunicorn como servidor WSGI

```bash
pip install gunicorn
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

### 5. Configure o Nginx como proxy reverso

```nginx
server {
    listen 80;
    server_name seudominio.com.br;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name seudominio.com.br;

    ssl_certificate /etc/letsencrypt/live/seudominio.com.br/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/seudominio.com.br/privkey.pem;

    location /static/ {
        alias /caminho/para/staticfiles/;
    }

    location /media/ {
        alias /caminho/para/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 6. Banco de dados para produção (recomendado)

Para produção, migre de SQLite para **PostgreSQL**:

```bash
pip install psycopg2-binary
```

Em `core/settings/production.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'concursosdb',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Perguntas Frequentes

**O sistema funciona sem Mercado Pago configurado?**
Sim. Os imports são carregados apenas quando o pagamento é acionado. O restante do sistema funciona normalmente.

**O sistema funciona sem Twilio configurado?**
Sim. O reset por WhatsApp exibirá erro apenas se o candidato escolher essa opção sem as credenciais configuradas. O reset por e-mail continuará funcionando.

**Como mudar a porta do servidor?**
```bash
python manage.py runserver 8080
```

**Como redefinir o banco de dados do zero?**
```bash
# Apagar o banco
del db.sqlite3           # Windows
rm db.sqlite3            # Linux/macOS

# Recriar
python manage.py migrate
python manage.py createsuperuser
```

**Como habilitar o Celery para tarefas em segundo plano?**
```bash
# Em um terminal separado (Redis deve estar rodando)
celery -A core worker -l info
```

**Os arquivos de mídia (fotos, editais) são servidos em produção?**
Não pelo Django. Configure o Nginx para servir `/media/` diretamente (veja a configuração de Nginx acima).

---

## Licença

Este projeto foi desenvolvido para uso interno/educacional. Adapte conforme necessário.

---

*Desenvolvido com Django — Python Web Framework*
