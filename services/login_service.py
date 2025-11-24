from bottle import request
from models.prof import ProfModel, Prof
from models.login import LoginModel, Login
from .prof_service import ProfService
from controllers.prof_controller import prof_controller
from controllers.aluno_controller import aluno_controller

class LoginService:
    def __init__(self):
        self.login_model = LoginModel()

    def check(self):
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        prof = prof_controller.prof_service.get_by_email(email)
        aluno = aluno_controller.aluno_service.get_by_email(email)
        if prof:
            if senha == prof.senha:
               return prof
            else:
                prof = None
        elif aluno:
            if senha == aluno.senha:
               return aluno
            else:
                aluno = None
        else:
            raise IndexError("1")
    
        if not(aluno or prof):
            raise IndexError("2")