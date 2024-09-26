# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from database import Base


# Modelo de Aluno (tabela Aluno)
class Aluno(Base):
    __tablename__ = "aluno"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)



