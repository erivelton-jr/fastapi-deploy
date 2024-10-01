# Projeto de API de Alunos com FastAPI e PostgreSQL

Este projeto é uma API RESTful de gerenciamento de alunos, implementada usando [FastAPI](https://fastapi.tiangolo.com/) e conectada a um banco de dados PostgreSQL. A API permite adicionar, buscar, atualizar e deletar alunos, com autenticação para operações de alteração.

## Funcionalidades

- Criar um novo aluno
- Buscar aluno por ID
- Atualizar informações de um aluno existente
- Deletar um aluno
- Autenticação para operações de atualização e exclusão

## Tecnologias Utilizadas

- **Python 3.9+**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **PostgreSQL**
- **Docker e Docker Compose**
  
## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado em sua máquina:

- Python 3.9+
- PostgreSQL (ou você pode rodar o banco via Docker)
- Git

### Clone o repositório

```bash
git clone https://github.com/seu-usuario/projeto-api-alunos.git
cd projeto-api-alunos
```


---
## Rotas Disponíveis

| Método   | Rota	                 | Descrição                            |
|----------|-----------------------|--------------------------------------|
| _POST_   | `/login`              | Faz login na API                     |
| _POST_   | `/alunos`             | Cria um novo aluno                   |
| _GET_    | `/alunos/{aluno_id}`  | Busca um aluno pelo ID               |
| _GET_    | `/lista-alunos/`      | Lista todos os alunos                |
| _PUT_    | `/alunos/{aluno_id}`  | Atualiza as informações de um aluno  |
| _DELETE_ | `/alunos/{aluno_id}`  | Deleta um aluno                      |

---

## Updates

- Implantação de lista de todos os alunos
- Sistema de login para alteração do banco de dados
- Containerização da api e do banco de dados.