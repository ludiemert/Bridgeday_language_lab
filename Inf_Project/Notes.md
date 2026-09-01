Projeto:
BridgeDay — English + Deutsch Daily Language Lab
Vamos seguir exatamente esta ordem:

1. HTML + CSS + JavaScript
2. Python
3. Automação
4. IA

O método de estudo também fica definido:
- Um idioma principal por dia.
- O segundo idioma aparece como comparação.
- 60% frases de vida real.
- 40% inglês/alemão para TI.
- Estudar, ouvir, repetir, escrever e registrar progresso.

E as funções da versão 1 são:
- Áudio em inglês e alemão.
- Gravar e ouvir sua voz.
- Botão “Mark as studied”.
- Próxima lição.
- Frase diária.
- Progresso diário, sequência e resumo semanal.
- Dados locais e gratuitos.

__________________________________________
Método de estudo
Ciclo de 5 dias:
1. English
2. Deutsch
3. English
4. Deutsch
5. Review day
No dia normal, você estuda apenas um idioma principal. A tradução em português aparece como apoio; o outro idioma fica escondido e só pode ser aberto no final como comparação.
No dia 5, a revisão será de apenas um idioma por vez: o que tiver mais erros ou o que estiver há mais tempo sem revisão. Assim inglês e alemão não viram uma mistura.
__________________________________

Como medir aprendizado de verdade
“Marcar como estudado” não significa automaticamente “aprendi”. Teremos dois níveis:
- Completed: você terminou a lição.
- Learned: você acertou a mesma palavra/frase em revisões diferentes.
Uma palavra será considerada aprendida quando você acertá-la, por exemplo, 3 vezes em dias diferentes. A revisão vai reaparecer depois de alguns dias, não imediatamente.
Para cada idioma, o dashboard mostrará:
- Dias estudados.
- Tempo total de estudo.
- Lições concluídas.
- Palavras em revisão.
- Palavras aprendidas.
- Acertos.
- Erros.
- Taxa de acerto.
- Sequência de dias.
- Último dia estudado.
- Idioma com maior dificuldade.
E se você não estudar em um dia, tudo bem: o app não contará aquele dia como estudo e a sequência será interrompida. O histórico continua guardado — sem culpa e sem apagar seu progresso.
Exercícios
Teremos cards como:
Complete the word:

I use P _ _ _ _ n to automate tasks.

[ Digite sua resposta ]

Check answer
No dia de alemão:
Complete the word:

Ich lerne jeden T _ _ Deutsch.

[ Digite sua resposta ]

Check answer
O sistema guarda tentativa, acerto/erro, tempo e idioma.
Isso será o nosso dashboard mais tarde:
English
Study time: 4h 20m
Accuracy: 78%
Words learned: 32

Deutsch
Study time: 3h 10m
Accuracy: 65%
Words learned: 19

Next review:
Deutsch — vocabulary about daily routine
Você está pensando como alguém que cria produto de verdade. Vamos fazer com calma, mas com estrutura profissional.

______________________________________

Fase 0 — Estrutura profissional do projeto
Fase 1 — Página de estudo em inglês A2
Fase 2 — JavaScript: lições, áudio, respostas e progresso
Fase 3 — Python + Argos Translate:
          você escreve em português → gera inglês e alemão em lote
Fase 4 — Revisão, palavras incompletas e dashboard
Fase 5 — Automação do plano de estudo
Fase 6 — IA para adaptar conteúdo e sugerir frases

__________________________

id é o nome único de um elemento HTML.
document.getElementById() encontra esse elemento.
const guarda uma informação que não muda.
addEventListener("click") espera um clique.
hidden = false mostra o card.
hidden = true esconde o botão.
__________________________

instal env para usar o python

py --version

py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip

instala a biblioteca gratuita de tradução.
.\.venv\Scripts\python.exe -m pip install argostranslate

_____________________________

O dashboard terá dados separados:
English
- Time studied
- Correct answers
- Errors
- Words learned
- Speaking practice

Deutsch
- Time studied
- Correct answers
- Errors
- Words learned
- Speaking practice
E a cada cinco dias o app escolherá a revisão do idioma que estiver com mais erros ou há mais tempo sem revisão.

___________________________
BridgeDay
│
├── Home
│   └── Meta do dia, idioma do dia e resumo rápido
│
├── Study
│   ├── Text
│   ├── Listening
│   ├── Grammar
│   ├── Vocabulary
│   └── Speak & Write
│
├── Review
│   └── Exercícios, erros e revisão de 5 em 5 dias
│
└── Progress
    └── Tempo, acertos, erros, palavras e evolução

    _________________________________________

Lilás principal: #7C3AED
Lilás escuro:   #3B1764
Verde-limão:    #C6FF3C
Fundo lilás:    #F4F0FF
Texto escuro:   #21142F

_____________________________________

update linguage

.\.venv\Scripts\argospm.exe update
.\.venv\Scripts\argospm.exe install translate-pt_en
.\.venv\Scripts\argospm.exe install translate-en_de

________________________________________________

automação real em Python.
lessons-pt.json
      ↓
translate_lessons.py
      ↓
Argos Translate
      ↓
lessons-translated.json

_______________________________

instalar a biblioteca oficial do DeepL no ambiente virtual:
.\.venv\Scripts\python.exe -m pip install deepl

____________________________

instalamos uma biblioteca pequena para o Python ler o arquivo .env com segurança:
.\.venv\Scripts\python.exe -m pip install python-dotenv

___________________

No terminal, dentro da pasta principal Bridgeday_language_lab, execute:
.\.venv\Scripts\python.exe -m http.server 5500
Deixe esse terminal aberto. Depois abra no navegador:
http://localhost:5500/frontend/
Não use http://127.0.0.1:5000/frontend/index.html agora.
A mensagem esperada no terminal é parecida com:
Serving HTTP on :: port 5500 ...
Isso também permitirá que, no próximo passo, o JavaScript leia data/lessons-translated.json.
_________________________


____________________
estagio novo do projeto com login

terminal dentro da pasta principal do BridgeDay e rode:
# Check the Python version.
py --version

# Create the main folders.
New-Item -ItemType Directory -Force front, backend, data, scripts

# Create the Python environment.
py -m venv .venv

# Update pip.
.\.venv\Scripts\python.exe -m pip install --upgrade pip

# Install the backend tools.
.\.venv\Scripts\python.exe -m pip install fastapi "uvicorn[standard]" sqlalchemy alembic passlib[bcrypt] "pyth

__________________________________

Usaremos:
- FastAPI: API e documentação automática.
- SQLite: banco gratuito em data/bridgeday.db.
- SQLAlchemy: comunicação segura com o banco.
- Alembic: evolução do banco sem apagar dados.
- Passlib + bcrypt: senhas protegidas.
- JWT: login persistente.

_____________________________

# Show the Python path.
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"

# Show the installed FastAPI version.
.\.venv\Scripts\python.exe -c "import fastapi; print(fastapi.__version__)"

# Show the installed SQLAlchemy version.
.\.venv\Scripts\python.exe -c "import sqlalchemy; print(sqlalchemy.__version__)"
_________________________________________________________

# Open the backend folder.
Get-ChildItem backend -Recurse

Get-ChildItem é um comando seguro do PowerShell para listar o conteúdo de uma pasta.
- Get-ChildItem backend mostra o que existe dentro de backend.
- -Recurse pede para mostrar também as subpastas.
______________________________

Start project terminal

# Start the API server.
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload

- http://127.0.0.1:8000/api/health
- http://127.0.0.1:8000/docs
A primeira mostra que a API está viva; a segunda é a documentação automática profissional do FastAPI.
_____________________________________________

esponde:
{"status":"ok","app":"BridgeDay API"}
Isso confirma três coisas:
- O servidor FastAPI iniciou.
- O endereço da rota funciona.
- O navegador consegue receber dados da API.
Ela é usada por desenvolvedores, serviços de hospedagem e também pelo próprio time para verificar rapidamente se o sistema está ativo. Mais tarde, ela poderá confirmar também se o banco SQLite está acessível.
A página /docs é a documentação interativa criada automaticamente pelo FastAPI. É uma ferramenta muito boa porque, quando criarmos rotas como login, lição diária, registrar resposta e dashboard, todas aparecerão ali automaticamente.
Na sua tela:
- GET /api/health: é a rota existente.
- GET: significa “buscar informação”, sem alterar dados.
- Try it out: permite testar a rota dentro da própria documentação.
- 200 Successful Response: significa que o servidor respondeu com sucesso.
- /openapi.json: é a versão técnica dessa documentação, usada por ferramentas e pelo front se necessário.
O exemplo "string" que aparece na documentação não é um problema agora. A API está retornando o objeto correto na página Health. Nas próximas rotas vamos declarar modelos de resposta, e a documentação mostrará exatamente os campos reais, por exemplo usuário, idioma, nível, sequência e métricas.
Neste momento, você tem:
Front existente → pronto para receber dados
FastAPI         → funcionando
Docs interativas → funcionando
Banco SQLite    → próxima etapa
Login           → próxima etapa após o banco
__________________________________________

criar duas tabelas fundamentais:
users
└── conta, e-mail, senha protegida, data de criação

user_language_profiles
└── idioma escolhido, nível escolhido e vínculo com o usuário
_____________________________
uma mesma pessoa poderá ter, por exemplo:
English → A2
Deutsch → A1
____________________________________

projeto realmente gratuito, minha recomendação é:
BridgeDay API   → FastAPI + SQLite
Traduções       → Argos Translate, local e gratuito
DeepL           → não usar na versão 1

_____________________________________

FastAPI          → API do BridgeDay
SQLite           → banco local
Alembic          → histórico seguro das tabelas
DeepL API Free   → geração em lote de traduções
Argos Translate  → não usar

_______________________________

aplicar a migração ao SQLite:
# Create the first database tables.
.\.venv\Scripts\alembic.exe upgrade head

# Show the current database version.
.\.venv\Scripts\alembic.exe current

# Show the database table names.
.\.venv\Scripts\python.exe -c "from sqlalchemy import inspect; from backend.app.database import engine; print(inspect(engine).get_table_names())"

____________________________________

instale a validação de e-mail e gere uma chave secreta.
# Install email validation.
.\.venv\Scripts\python.exe -m pip install email-validator

# Create a secret key.
.\.venv\Scripts\python.exe -c "import secrets; print(secrets.token_urlsafe(32))"

______________________

cada parte faz.
Bridgeday_language_lab/
│
├── .venv/
├── .env
├── alembic.ini
├── front/
├── backend/
├── data/
└── scripts/
Pasta ou arquivo	Função
.venv/	Ambiente Python isolado. Guarda FastAPI, SQLAlchemy e bibliotecas do projeto.
.env	Guarda dados privados, como SECRET_KEY. Nunca vai para Git ou para o front.
alembic.ini	Configuração geral do Alembic.
front/	Seu HTML, CSS e JavaScript. É a tela que o aluno usa.
backend/	Todo o servidor Python/FastAPI.
data/	Banco bridgeday.db e arquivos JSON de conteúdo.
scripts/	Programas que você executa manualmente para importar lições ou preparar conteúdo.


Dentro de backend/:
backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── database.py
│   └── main.py
└── migrations/
    └── versions/
Pasta ou arquivo	Função
app/main.py	Inicia a API e conecta todas as rotas.
app/database.py	Define onde está o SQLite, cria conexões e sessões do banco.
app/api/	Rotas da API: login, lições, progresso e dashboard. auth.py contém cadastro, login e usuário atual.
app/core/	Configurações globais e segurança.
core/config.py	Lê a chave secreta do .env e define duração do token.
core/security.py	Protege senhas e cria/lê tokens de login.
app/models/	Desenhos das tabelas SQLite usando Python/SQLAlchemy.
models/user.py	Tabela users: e-mail, senha protegida e status da conta.
models/language_profile.py	Tabela de níveis: English e Deutsch para cada usuário.
app/schemas/	Define e valida dados recebidos/enviados pela API.
schemas/auth.py	Valida cadastro, login e resposta segura do usuário.
app/services/	Regras de negócio. Depois ficará aqui a regra de ciclo de 5 dias, revisão e cálculo de métricas.
migrations/	Histórico das mudanças no banco.
migrations/versions/	Arquivos de cada versão do banco, como a criação das tabelas atuais.
migrations/env.py	Liga o Alembic aos modelos e ao SQLite.


O caminho dos dados ficará assim:
Front
  ↓
API route: auth.py
  ↓
Schema: auth.py valida os dados
  ↓
Security: protege senha ou lê token
  ↓
Model + database: salva ou busca no SQLite
  ↓
API responde ao front

________________________________________

Sobre os imports de main.py:
# Import the FastAPI app class.
from fastapi import FastAPI
FastAPI cria a aplicação servidor. É o objeto principal do backend.
# Import the browser access tool.
from fastapi.middleware.cors import CORSMiddleware
CORSMiddleware permite que o navegador aberto em localhost:5500 — onde estará seu front — faça pedidos à API em localhost:8000. Sem isso, o navegador bloquearia a comunicação por segurança.
# Import simple SQL text.
from sqlalchemy import text
text permite enviar uma consulta SQL simples. Usamos isso apenas no Health para executar SELECT 1 e confirmar que o SQLite está acessível.
# Import the login route group.
from .api.auth import router as auth_router
- . significa “a pasta atual”, ou seja, backend/app/.
- .api.auth aponta para backend/app/api/auth.py.
- router é o grupo com as rotas de cadastro, login e usuário atual.
- as auth_router renomeia esse objeto para ficar claro no main.py.
# Add the login routes.
app.include_router(auth_router)
Essa linha registra as rotas de auth.py dentro da API principal. Sem ela, o arquivo existiria, mas /api/auth/register, /api/auth/login e /api/auth/me não apareceriam nem funcionariam.
__________________________________________________

O /docs não é uma tela do aluno. É uma ferramenta de desenvolvimento gerada automaticamente pelo FastAPI para testar e documentar sua API.
Na sua página aparecem:
- POST /api/auth/register: cria uma conta com e-mail, senha e níveis de English/Deutsch.
- POST /api/auth/login: verifica a senha e devolve um token de acesso.
- GET /api/auth/me: mostra o usuário conectado. O cadeado significa que precisa de token.
- GET /api/health: confirma que API e banco estão ativos.
- Schemas: os formatos de dados aceitos e devolvidos, como RegisterRequest e TokenResponse.
Como ela funciona:
1. Clique em uma rota.
2. Clique em Try it out.
3. Preencha os dados de teste.
4. Clique em Execute.
5. A Docs mostra o pedido enviado, o código da resposta e os dados devolvidos.
O botão Authorize serve para informar seu token à Docs. Depois disso, ela envia esse token automaticamente ao testar a rota protegida /api/auth/me.
As imagens provam que as rotas, os schemas e a documentação foram criados corretamente. Elas ainda não comprovam que cadastro e login foram executados; isso será confirmado quando aparecer 201 Created no cadastro e 200 OK no login.

______________________________________________

tudo funcionando corretamente.
- Application startup complete.: FastAPI iniciou sem erro.
- GET /api/health 200 OK: a Health respondeu com sucesso; API e SQLite estão ativos.
- GET /docs 200 OK: a documentação abriu.
- GET /openapi.json 200 OK: FastAPI gerou o contrato técnico usado pela Docs.
- 404 /.well-known/appspecific/com.chrome.devtools.json: é uma tentativa automática do Chrome/DevTools de procurar um arquivo opcional. Ele não existe no BridgeDay e não afeta nada.

________________________________________

O /docs não é banco de dados. Ele é uma página de teste e documentação da API.
A separação é esta:
Front            → tela que o aluno vê
FastAPI          → ferramenta Python que cria o servidor
API              → regras/endpoints que o front pode chamar
SQLite           → arquivo que guarda os dados
Docs             → painel para testar e entender a API
Uma comparação simples:
- SQLite é o caderno onde os dados ficam guardados.
- API é o atendente que recebe pedidos e devolve respostas.
- FastAPI é a ferramenta Python usada para construir esse atendente.
- Docs é o painel de treinamento do atendente: mostra o que ele sabe fazer e permite testar cada pedido.
“API” é um conceito, não um programa específico. Poderíamos criar uma API com Flask, Django, Node.js, Java ou outras tecnologias. Escolhemos FastAPI porque é rápido, gratuito, organizado e cria essa documentação automaticamente.
Você também poderia usar Postman ou Insomnia para testar a API, mas não precisa agora: a página /docs já faz esse trabalho muito bem, sem instalar outro aplicativo.
_______________________________________
