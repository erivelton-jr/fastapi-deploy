# -*- coding: utf-8 -*-

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine
from models import Aluno as AlunoModel  # Evita conflito de nome
from schemas import AlunoCreate, Aluno
from database import SessionLocal

app = FastAPI()

# Inicia a tabela
Base.metadata.create_all(bind=engine)

# Função que gerencia a sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Adicionar aluno
@app.post("/alunos", response_model=Aluno)
def post_aluno(aluno_data: AlunoCreate, db: Session = Depends(get_db)):
    # Cria instância do modelo SQLAlchemy
    novo_aluno = AlunoModel(nome=aluno_data.nome, email=aluno_data.email)
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)  # Obtém o id gerado automaticamente pelo banco de dados
    return novo_aluno  # Retorna o objeto com o id incluído

# Buscar um aluno
@app.get("/alunos/{aluno_id}", response_model=Aluno)
def read_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(AlunoModel).filter(AlunoModel.id == aluno_id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno


# Atualizar um aluno
@app.put("/alunos/{aluno_id}", response_model=Aluno)
def update_aluno(aluno_id: int, aluno_data: AlunoCreate, db: Session = Depends(get_db)):
    aluno = db.query(AlunoModel).filter(AlunoModel.id == aluno_id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    aluno.nome = aluno_data.nome  # Corrigido de "aluno.name" para "aluno.nome"
    aluno.email = aluno_data.email
    db.commit()
    db.refresh(aluno)
    return aluno

# Deletar aluno
@app.delete("/alunos/{aluno_id}", response_model=dict)
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(AlunoModel).filter(AlunoModel.id == aluno_id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    db.delete(aluno)
    db.commit()
    return {"detail": "Aluno deletado com sucesso"}
