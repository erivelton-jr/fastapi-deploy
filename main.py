# -*- coding: utf-8 -*-

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import Base, engine
from models import Aluno
from schemas import AlunoCreate, Aluno
from database import SessionLocal, engine

app = FastAPI()

#inicia a tabela
Base.metadata.create_all(bind=engine)

# Função que gerencia a sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#adicionar aluno
@app.post("/alunos", response_model=Aluno)
def post_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    aluno = Aluno(nome=aluno.nome, email=aluno.email)
    db.add(aluno)
    db.commit()
    db.refresh(aluno)
    return aluno


#Buscar um aluno
@app.get("/alunos/{aluno_id}", response_model=Aluno)
def read_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno


#Atualizar um aluno
@app.put("/alunos/{aluno_id}", response_model=Aluno)
def update_aluno(aluno_id: int, aluno_data: AlunoCreate, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    aluno.name = aluno_data.nome
    aluno.email = aluno_data.email
    db.commit()
    db.refresh(aluno)
    return aluno


#deletar aluno
@app.delete("/alunos/{aluno_id}", response_model=Aluno)
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if aluno is None:
        raise HTTPException(status_code=404,detail="Aluno não encontrado.")
    db.delete(aluno)
    db.commit()
    db.refresh(aluno)
    return {"detail": "Aluno deletado com sucesso"}


