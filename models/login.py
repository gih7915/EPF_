import json
import os
from dataclasses import dataclass, asdict
from typing import List
from .user import User
from .prof import Prof, ProfModel
from services.prof_service import ProfService

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Login():
    def __init__(self, entidade):
        self.entidade = entidade
        self.permissions = self.set_permissions()

    def set_permissions(self):
        permissions=["comentar"]
        match self.entidade.__class__.__name__:
            case "Prof":
                permissions.append(["postar", "add_aluno_turma", "remover_aluno_turma", "criar_turma"])
            #adicionar case "Aluno":
        return permissions

class LoginModel():

    def __init__(self):
        self.prof_service = ProfService()
        #adicionar a parte de alunos


