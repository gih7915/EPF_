import json
import os
from dataclasses import dataclass, asdict
from typing import List
from controllers.prof_controller import prof_controller
from controllers.aluno_controller import aluno_controller

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
            case "Aluno":
                permissions.append(["entregar"])
        return permissions

class LoginModel():
    def __init__(self):
        self.prof_service = prof_controller.prof_service
        self.aluno_service = aluno_controller.aluno_service