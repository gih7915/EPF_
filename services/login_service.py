from bottle import request
from cryptography.fernet import Fernet
from models.login import LoginModel
from config import Config

class LoginService:
    def __init__(self):
        self.login_model = LoginModel()
        self.fernet = Fernet(Config.BYTES_KEY)
        

    def check(self, prof_service, aluno_service):
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        prof = prof_service.get_by_email(email)
        aluno = aluno_service.get_by_email(email)
        if prof:
            if senha == self.fernet.decrypt((prof.senha).encode('utf-8')).decode():
               return prof
            else:
                prof = None
        elif aluno:
            if senha == self.fernet.decrypt((aluno.senha).encode('utf-8')).decode():
               return aluno
            else:
                aluno = None
        else:
            raise IndexError("1")
    
        if not(aluno or prof):
            raise IndexError("2")