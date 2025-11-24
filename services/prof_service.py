from bottle import request
from cryptography.fernet import Fernet
from config import Config
from models.prof import ProfModel, Prof

class ProfService:
    def __init__(self):
        self.prof_model = ProfModel()
        self.fernet = Fernet(Config.BYTES_KEY)


    def get_all(self):
        profs = self.prof_model.get_all()
        return profs


    def save(self):
        last_id = max([p.id for p in self.prof_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        senha = self.fernet.encrypt(request.forms.get('senha').encode('utf-8')).decode()
        cargo = request.forms.get('cargo')

        prof = Prof(id=new_id, name=name, email=email, birthdate=birthdate, senha=senha, cargo=cargo)
        self.prof_model.add_prof(prof)
        
        return prof


    def get_by_id(self, prof_id):
        return self.prof_model.get_by_id(prof_id)
    

    def get_by_email(self, prof_email):
        return self.prof_model.get_by_email(prof_email)


    def edit_prof(self, prof):
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        senha = request.forms.get('senha')
        cargo = request.forms.get('cargo')

        prof.name = name
        prof.email = email
        prof.birthdate = birthdate
        prof.senha = senha
        prof.cargo = cargo

        self.prof_model.update_prof(prof)


    def delete_prof(self, prof_id):
        self.prof_model.delete_prof(prof_id)
