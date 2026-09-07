O /docs é o Swagger UI gerado automaticamente pelo FastAPI. Ele não é banco de dados e não substitui o Beekeeper. Ele é uma página profissional para:
- ver todas as rotas disponíveis;
- entender que dados cada rota recebe e devolve;
- testar a API sem alterar o front;
- verificar erros e respostas reais;
- documentar o projeto para outra pessoa desenvolvedora.
Na sua tela:
- Authentication: criar conta, login e consultar usuário.
- Lessons: listar e abrir lições.
- Progress: salvar conclusão de uma lição.
- Dashboard: buscar métricas reais do usuário.
- Schemas: os “formatos de dados” que cada rota usa, como DashboardResponse.
É uma ferramenta muito usada no campo de TI. FastAPI gera essa documentação a partir do seu próprio código, seguindo o padrão OpenAPI. Por isso ela se mantém atualizada quando adicionamos novas rotas.

Para testar Dashboard:
1. Faça login em POST /api/auth/login e copie apenas o token — não envie nem salve print dele.
2. Clique em Authorize e informe o token.
3. Abra GET /api/dashboard.
4. Clique em Try it out e depois Execute.
A resposta deverá trazer seus números reais, como tempo total, lições concluídas e a lista com en-a2-work-routine-001.

____________________________________________

vamos usar /docs sempre que houver uma API nos projetos. É excelente para aprender, testar e demonstrar o backend. Em projetos que não usam FastAPI, existe a mesma ideia com OpenAPI/Swagger, Postman ou Insomnia.
O terminal também confirma tudo:
POST /api/auth/login ... 200 OK
GET /api/dashboard ... 200 OK

_________________________________