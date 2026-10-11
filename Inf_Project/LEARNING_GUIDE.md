# BridgeDay — Learning Guide

Este arquivo reúne os principais conceitos aprendidos durante o desenvolvimento do BridgeDay.

## 1. O que é o BridgeDay

BridgeDay é um aplicativo de aprendizagem de idiomas.

O usuário pode estudar English ou Deutsch usando:

- lições;
- vocabulário;
- gramática;
- exercícios;
- escrita;
- progresso;
- revisões.

O projeto é um MVP local.

MVP significa **Minimum Viable Product**, ou Produto Mínimo Viável: uma versão pequena, útil e funcional, pronta para uso inicial e melhoria contínua.

## 2. Front-end

O front-end é a parte que o aluno vê e usa no navegador.

No BridgeDay, ele está na pasta:

```text
front/
```

Arquivos principais:

| Arquivo | Função |
| --- | --- |
| `index.html` | Estrutura da página |
| `styles.css` | Cores, tamanho, posição e responsividade |
| `app.js` | Regras principais da interface |
| `js/exercises.js` | Regras dos exercícios |

### HTML

HTML cria a estrutura da página.

Exemplos de elementos:

```html
<!-- A button lets the learner click an action. -->
<button type="button">Start lesson</button>

<!-- A section groups related page content. -->
<section class="study-content">
  <h2>Grammar</h2>
</section>
```

Conceitos importantes:

- `id`: nome único de um elemento.
- `class`: nome reutilizável para estilo ou JavaScript.
- `hidden`: esconde um elemento.
- `button`: cria botão.
- `section`: agrupa conteúdo relacionado.

### CSS

CSS controla a aparência do HTML.

Exemplo:

```css
/* This styles the main navigation menu. */
.main-nav {
  display: flex;
  gap: 6px;
}
```

Conceitos importantes:

- `display: flex`: organiza itens em linha ou coluna.
- `display: grid`: organiza itens em uma grade.
- `gap`: espaço entre itens.
- `padding`: espaço interno.
- `margin`: espaço externo.
- `border-radius`: arredonda cantos.
- `@media`: muda o layout para telas menores.

### Responsividade

Responsividade significa que a tela continua utilizável em celular, tablet e computador.

No BridgeDay, o menu mobile usa duas colunas para manter as quatro opções visíveis:

```text
Home     Study
Review   Progress
```

O front-end pode ser testado sem backend quando o objetivo é somente verificar HTML, CSS e JavaScript visual.

## 3. JavaScript

JavaScript faz a página reagir ao usuário.

Ele pode:

- trocar a trilha entre English e Deutsch;
- mostrar a próxima lição;
- chamar a API;
- mostrar progresso;
- enviar respostas de exercícios;
- atualizar feedback de acerto ou erro.

Exemplo:

```javascript
// Find the element with the selected CSS class.
const grammarText = document.querySelector(".grammar-content .page-help");

// Update text shown on the page.
grammarText.textContent = "Grammar will appear here.";
```

Conceitos importantes:

| Conceito | Significado |
| --- | --- |
| `const` | Guarda uma referência que não será trocada |
| `document.querySelector()` | Encontra um elemento HTML |
| `textContent` | Altera texto visível |
| `addEventListener()` | Espera uma ação, como clique |
| `fetch()` | Faz pedido para a API |
| `async` / `await` | Espera uma resposta da API |

## 4. Back-end

O back-end é a parte que roda no Python e protege as regras do sistema.

No BridgeDay, ele está em:

```text
backend/
```

O back-end:

- recebe pedidos do front-end;
- valida dados;
- protege senhas;
- consulta o banco;
- salva progresso;
- corrige exercícios;
- calcula revisões;
- devolve respostas ao navegador.

## 5. FastAPI

FastAPI é a ferramenta Python usada para criar a API do BridgeDay.

A aplicação principal está em:

```text
backend/app/main.py
```

FastAPI cria rotas, por exemplo:

```text
GET  /api/health
POST /api/auth/login
GET  /api/lessons/next
POST /api/exercises/{exercise_id}/attempts
GET  /api/progress/history
GET  /api/reviews
```

A documentação automática fica em:

```text
http://127.0.0.1:8000/docs
```

A página `/docs` é uma ferramenta de desenvolvimento. Ela não é a página usada pelo aluno.

## 6. API

API significa **Application Programming Interface**.

No BridgeDay, a API é a ponte entre a interface e o banco.

```text
Browser
  ↓ request
FastAPI API
  ↓ query or save
SQLite database
  ↓ response
Browser
```

Exemplo:

```text
Front-end asks:
“Which lesson is next?”

API checks the database.

API returns lesson data in JSON.

Front-end shows the lesson to the learner.
```

## 7. HTTP methods

| Método | Função |
| --- | --- |
| `GET` | Busca dados sem alterar nada |
| `POST` | Cria ou envia novos dados |
| `PUT` | Atualiza dados completos |
| `PATCH` | Atualiza parte dos dados |
| `DELETE` | Remove dados |

Exemplos no BridgeDay:

```text
GET  /api/lessons/next
POST /api/auth/login
POST /api/exercises/1/attempts
POST /api/reviews/lesson-code/complete
```

## 8. HTTP status codes

| Código | Significado |
| ---:| --- |
| `200 OK` | Pedido concluído com sucesso |
| `201 Created` | Novo item criado |
| `400 Bad Request` | Dados enviados estão incorretos |
| `401 Unauthorized` | Login ou token é necessário |
| `404 Not Found` | Rota ou dado não existe |
| `409 Conflict` | A ação não pode acontecer naquele momento |
| `500 Internal Server Error` | Erro interno do servidor |

No BridgeDay, `409 Conflict` ao concluir uma revisão cedo é correto. Ele protege a regra de revisão espaçada.

## 9. JSON

JSON é um formato de texto usado para trocar dados entre front-end, API e arquivos de conteúdo.

Exemplo:

```json
{
  "lesson_code": "de-a1-family-007",
  "language_code": "de",
  "level_code": "A1",
  "title": "Meine Familie"
}
```

Regras importantes:

- JSON não aceita comentários.
- Todo texto deve usar aspas duplas.
- Vírgulas devem estar no lugar correto.
- Cada objeto deve ter estrutura válida.
- O arquivo deve ser validado antes de importar.

## 10. SQLite

SQLite é o banco de dados local do BridgeDay.

Ele é um arquivo:

```text
data\bridgeday.db
```

O banco guarda dados organizados em tabelas.

Exemplos de tabelas:

```text
users
user_language_profiles
lessons
lesson_translations
vocabulary_items
exercises
exercise_attempts
lesson_progress
writing_entries
alembic_version
```

SQLite é uma boa escolha para o MVP porque:

- é gratuito;
- não precisa instalar um servidor de banco;
- funciona em um arquivo;
- é simples para desenvolvimento local.

## 11. SQLAlchemy

SQLAlchemy conecta o Python ao banco SQLite.

Em vez de escrever SQL em toda parte, o projeto usa modelos Python.

Exemplo de ideia:

```text
Python model Lesson
        ↓
SQLAlchemy
        ↓
SQLite table lessons
```

Os modelos ficam em:

```text
backend/app/models/
```

## 12. Schemas

Schemas definem e validam os dados enviados e recebidos pela API.

Eles ficam em:

```text
backend/app/schemas/
```

Exemplo:

```text
A request sends:
- email
- password

A schema checks:
- email format
- required fields
- password rules
```

Isso ajuda a API a não receber dados incompletos ou incorretos.

## 13. Autenticação

O BridgeDay usa login com:

- senha protegida;
- token JWT;
- usuário atual;
- sessão no navegador.

Fluxo:

```text
User enters email and password
        ↓
API checks the password
        ↓
API creates a token
        ↓
Browser saves the token
        ↓
Browser sends the token in protected requests
```

A senha nunca deve ser salva como texto normal.

## 14. CORS

O front-end usa a porta `5500`.

A API usa a porta `8000`.

Como são endereços diferentes, o navegador precisa de uma regra de segurança chamada CORS.

CORS permite:

```text
localhost:5500
        ↓
request allowed
        ↓
127.0.0.1:8000
```

Sem CORS, o navegador bloquearia os pedidos da interface para a API.

## 15. Migrations

Migration é um arquivo que registra mudanças na estrutura do banco.

Exemplo:

```text
Add review_count to lesson_progress
```

Alembic cria e aplica migrations.

Isso permite alterar tabelas sem apagar os dados existentes.

Fluxo:

```text
Change SQLAlchemy model
        ↓
Create migration
        ↓
Review migration file
        ↓
Apply migration
        ↓
SQLite structure is updated
```

A migration atual do BridgeDay é:

```text
b883e40f21a4 (head)
```

## 16. Revisão espaçada

Revisão espaçada significa revisar uma lição depois de alguns dias, e não imediatamente.

No BridgeDay:

```text
Lesson completed
        ↓
Review after 1 day
        ↓
Review after 3 days
        ↓
Review after 7 days
        ↓
Review after 14 days
        ↓
Review after 30 days
```

A coluna `review_count` registra quantas revisões uma lição teve.

## 17. Importação de lições

As lições ficam em arquivos JSON dentro de:

```text
data\batches/
```

Fluxo:

```text
Create reviewed JSON batch
        ↓
Validate JSON
        ↓
Run import script
        ↓
New lessons go to SQLite
        ↓
API can return the lessons
        ↓
Front-end can show the lessons
```

O importador ignora códigos repetidos. Isso evita duplicar lições.

## 18. Git

Git registra a história do código.

Conceitos:

| Conceito | Significado |
| --- | --- |
| Repository | Pasta do projeto com histórico |
| Commit | Foto salva de uma mudança |
| Branch | Linha de desenvolvimento |
| `main` | Branch principal |
| `git status` | Mostra mudanças locais |
| `git add` | Prepara arquivos para commit |
| `git commit` | Salva uma mudança no histórico |
| `git push` | Envia commits ao GitHub |

Fluxo seguro:

```text
Change files
        ↓
git status --short
        ↓
git add specific-file
        ↓
git commit
        ↓
git push
```

## 19. .gitignore

`.gitignore` diz ao Git quais arquivos locais não devem ser enviados ao GitHub.

No BridgeDay, ele protege:

```text
.env
.venv/
*.db
*.db-shm
*.db-wal
__pycache__/
```

Por que isso importa:

- `.env` pode ter chaves privadas;
- `.venv` é recriada localmente;
- bancos SQLite podem conter dados pessoais de estudo;
- caches Python não precisam ficar no Git.

## 20. Beekeeper Studio

Beekeeper Studio é uma ferramenta visual para abrir e consultar o banco SQLite.

Ele ajuda a:

- ver tabelas;
- verificar colunas;
- executar SQL;
- confirmar dados salvos;
- investigar problemas de banco.

Ele não substitui a API. Ele é uma ferramenta de desenvolvimento.

## 21. Responsividade

A interface deve funcionar em telas pequenas.

Para testar:

```text
Chrome DevTools
  ↓
Device toolbar
  ↓
320 × 750 or 375 × 812
```

Verificar:

- menu acessível;
- botões visíveis;
- cards dentro da largura;
- sem rolagem horizontal;
- ações clicáveis.

## 22. Regra para conteúdo de idiomas

Para criar lições com qualidade:

1. Escrever primeiro no idioma estudado.
2. Usar nível adequado, como A1 ou A2.
3. Criar traduções naturais, não palavra por palavra.
4. Revisar sentido, tom, gramática e contexto.
5. Criar vocabulário útil.
6. Criar exercício coerente com a lição.
7. Validar o JSON.
8. Importar o lote.
9. Testar a lição pela API e pelo front-end.

## 23. Próximo nível do projeto

Quando o MVP estiver maduro, o BridgeDay pode evoluir com:

- mais idiomas;
- mais conteúdo;
- tipos novos de exercício;
- testes automatizados;
- perfil de usuário;
- recuperação de senha;
- áudio avançado;
- publicação online;
- recursos de IA para personalizar estudo.

## Regra principal

Sempre trabalhar com cuidado:

```text
Read first
        ↓
Understand the real problem
        ↓
Change one thing
        ↓
Test the result
        ↓
Save with Git
```

Isso protege o projeto e evita alterações por tentativa.