Start API project terminal

# Start the API server.
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload

- http://127.0.0.1:8000/api/health
- http://127.0.0.1:8000/docs
A primeira mostra que a API está viva; a segunda é a documentação automática profissional do FastAPI.


Start backend => API - 1 terminal

# Start the API server.
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload

Start front - 2 terminal

# Start the front server.
.\.venv\Scripts\python.exe -m http.server 5500 --directory front

OR

# Start the front server.
..\.venv\Scripts\python.exe -m http.server 5500

open
http://127.0.0.1:5500

_____________________________________________
