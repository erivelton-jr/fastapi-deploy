# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco PostgreSQL
DATABASE_URL = 'postgresql://postgres:admin@db:5432/fastapi_db'

# Configurando o SQLAlchemy para se conectar ao banco
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para as classes do modelo
Base = declarative_base()
