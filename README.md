# BridgeDay — Daily Language Lab

BridgeDay é um aplicativo local de aprendizagem diária para **English** e **Deutsch**.

O projeto oferece lições curtas, vocabulário, exercícios, escrita, progresso por idioma e revisão espaçada.

## Status

O MVP local está funcional.

- Login e sessão.
- Trilhas separadas: English A2 e Deutsch A1.
- Lições com texto, listening, grammar, vocabulary e speak & write.
- Exercícios `fill_blank` com correção e registro de tentativas.
- Progresso e histórico separados por idioma.
- Revisão espaçada em 1, 3, 7, 14 e 30 dias.
- Importação de lições revisadas em lote.
- Layout responsivo para celular.
- Banco SQLite local protegido do Git.

## MVP

MVP significa **Minimum Viable Product**: a menor versão útil e funcional de um produto.

O BridgeDay já permite que uma pessoa:

1. Crie uma conta e entre.
2. Escolha English ou Deutsch.
3. Estude lições reais.
4. Responda exercícios e veja a correção.
5. Salve uma resposta escrita.
6. Conclua lições.
7. Consulte progresso por idioma.
8. Faça revisões quando elas estiverem disponíveis.

## Tecnologias

| Área | Tecnologia |
| --- | --- |
| Front-end | HTML, CSS e JavaScript |
| Back-end | Python e FastAPI |
| Banco de dados | SQLite |
| ORM | SQLAlchemy |
| Migrações | Alembic |
| Autenticação | JWT, Passlib e bcrypt |
| Documentação da API | FastAPI Swagger Docs |
| Versionamento | Git e GitHub |

## Estrutura do projeto

```text
Bridgeday_language_lab/
├── front/                  # Interface mostrada ao aluno
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── js/
│       └── exercises.js
├── backend/                # API FastAPI
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── database.py
│   │   └── main.py
│   └── migrations/
│       └── versions/
├── data/
│   ├── bridgeday.db        # Banco SQLite ativo
│   └── batches/            # Lotes JSON de lições revisadas
├── scripts/                # Importadores e utilitários manuais
├── .env                    # Configurações privadas
├── .gitignore
├── alembic.ini
└── README.md
```

## Como iniciar o projeto

Abra dois terminais na pasta principal do projeto:

```text
C:\Users\user\Downloads\Bridgeday_language_lab
```

### 1. Iniciar o front-end

```powershell
# Serve the exact front folder used by the browser.
.\.venv\Scripts\python.exe -m http.server 5500 --directory front
```

Abra no navegador:

```text
http://localhost:5500
```

### 2. Iniciar o back-end

```powershell
# Start the FastAPI server and reload it after Python changes.
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa da API ficará em:

```text
http://127.0.0.1:8000/docs
```

## Banco de dados

O único banco ativo do projeto é:

```text
data\bridgeday.db
```

Não apague esse arquivo.

O banco guarda, entre outros dados:

- usuários;
- perfis de idioma;
- lições;
- traduções;
- vocabulário;
- exercícios;
- tentativas de exercícios;
- progresso das lições;
- revisões;
- textos escritos pelo usuário.

## Segurança local

O banco SQLite, ambiente virtual e configurações privadas não devem entrar no Git.

O `.gitignore` inclui:

```gitignore
# Ignore local databases and SQLite support files.
*.db
*.db-shm
*.db-wal

# Ignore local Python and private configuration files.
.venv/
**/__pycache__/
.env
```

## Conteúdo disponível

| Idioma | Nível | Lições |
| --- | --- | ---: |
| Deutsch | A1 | 16 |
| English | A2 | 17 |
| **Total** | — | **33** |

Lotes já importados:

```text
data\batches\de-a1-batch-02.json
data\batches\en-a2-batch-02.json
```

Cada lição possui:

- código único;
- idioma e nível;
- texto principal;
- traduções revisadas;
- nota gramatical;
- vocabulário;
- exercício `fill_blank`.

## Validar um lote de lições

```powershell
# Validate JSON syntax without changing the database.
.\.venv\Scripts\python.exe -m json.tool data\batches\NOME-DO-LOTE.json | Out-Null

# Show success only after valid JSON syntax.
if ($LASTEXITCODE -eq 0) {
    Write-Host "JSON valid."
}
```

## Importar um lote de lições

```powershell
# Import only lesson codes that do not already exist in SQLite.
.\.venv\Scripts\python.exe scripts\import_lessons.py --file data\batches\NOME-DO-LOTE.json
```

O importador ignora códigos de lições que já existem no banco.

## Revisão espaçada

Depois que uma lição é concluída, ela entra no ciclo de revisão:

```text
1 dia → 3 dias → 7 dias → 14 dias → 30 dias
```

Uma revisão não pode ser concluída antes da data prevista. A API retorna `409 Conflict` quando alguém tenta concluir uma revisão antecipadamente.

## Migrações do banco

A migração atual é:

```text
b883e40f21a4 (head)
```

Para conferir:

```powershell
# Show the migration applied to the active SQLite database.
.\.venv\Scripts\python.exe -m alembic current
```

Para aplicar novas migrações:

```powershell
# Apply every migration not yet applied to the local database.
.\.venv\Scripts\python.exe -m alembic upgrade head
```

## Verificações concluídas

- API iniciada sem erros.
- Banco SQLite conectado.
- Migrações aplicadas.
- Login testado.
- Lição diária carregada pela API.
- Exercícios testados com respostas certas e erradas.
- Tentativas salvas no banco.
- Histórico por idioma testado.
- Revisão antecipada bloqueada corretamente.
- Lotes German A1 e English A2 validados e importados.
- Responsividade testada em tela de celular.
- Menu mobile com Home, Study, Review e Progress acessíveis.
- Banco local removido do controle do Git.

## Próximas evoluções

1. Criar novos lotes de lições revisadas.
2. Adicionar testes automatizados para a API.
3. Adicionar exercícios de múltipla escolha.
4. Adicionar exercícios de ordenar palavras.
5. Adicionar compreensão de áudio.
6. Melhorar perfil e recuperação de senha.
7. Criar validações adicionais.
8. Preparar deploy público.

## Arquitetura de exercícios

```text
Exercise engine
├── fill_blank               # Implementado
├── multiple_choice          # Futuro
├── word_order               # Futuro
└── audio_comprehension      # Futuro
```

## Arquitetura de conteúdo

```text
Content
├── English lessons
├── Deutsch lessons
└── Future languages
```

## Licença

Projeto em desenvolvimento para fins educacionais e de portfólio.

________________________________________


---------

#### 🤝 Contributing
If you would like to contribute to this project, feel free to open an issue or submit a pull request! 🚀
________________________________________
#### 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
👩💻 Developed with 💙 by [[LuDiemert](https://www.linkedin.com/in/lucianadiemert/)]

________________________________________
- #### My LinkedIn - [![Linkedin Badge](https://img.shields.io/badge/-LucianaDiemert-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lucianadiemert/)](https://www.linkedin.com/in/lucianadiemert/)

________________________________________
## 🌐 **Contact**
<img align="left" src="https://www.github.com/ludiemert.png?size=150">

#### [**Luciana Diemert**](https://github.com/ludiemert)

🛠 Full-Stack Developer <br>
🖥️ Python | Computer Vision | AI Integrations <br>
📍 Cork - Irland
☎ +353 87 243 8690

<a href="https://www.linkedin.com/in/lucianadiemert" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;
<a href="mailto:lucianadiemert@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white" alt="Gmail Badge" height="25"></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white" title="LuDiem#0654" alt="Discord Badge" height="25"></a>&nbsp;
<a href="https://www.github.com/ludiemert" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub Badge" height="25"></a>&nbsp;

<br clear="left"/>

---
Developed with ❤ by [ludiemert](https://github.com/ludiemert).

