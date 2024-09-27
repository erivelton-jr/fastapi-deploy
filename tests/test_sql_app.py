from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database import Base
from main import app, get_db


# URL de conexão para o banco de dados de teste
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5433/fastapi_test"
engine = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()



app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# para gerar emails aleatorios
import random
import string

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

teste = random_char(7)+"@gmail.com"

def test_create_user():
    response = client.post("/alunos/",
                           json={"nome": "pedro", "email": teste}
                           )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == teste
    assert "id" in data
    user_id = data["id"]