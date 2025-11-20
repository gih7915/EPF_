from bottle import request
from models.prof import ProfModel, Prof
from models.login import LoginModel, Login
from .prof_service import ProfService

class LoginService:
    def __init__(self):
        self.login_model = LoginModel()

    def check(self):
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        prof = self.prof_service.get_by_email(email)
        #adicionar o do aluno
        if prof:
            if senha == prof.senha:
               return prof
            else:
                raise IndexError("Senha incorreta.")
        #adicionar o else aluno
        else:
            raise IndexError("Usuário não cadastrado.")