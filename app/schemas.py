# -*- coding: utf-8 -*-
import uuid

from pydantic import BaseModel


class AlunoBase(BaseModel):
    nome: str
    email: str

class AlunoCreate(AlunoBase):
    pass

class Aluno(AlunoBase):
    id: int

    class ConfigDict:
        from_attributes = True


