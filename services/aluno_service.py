from bottle import request
from cryptography.fernet import Fernet
from config import Config
from models.aluno import AlunoModel, Aluno

class AlunoService:
    def __init__(self):
        self.aluno_model = AlunoModel()
        self.fernet = Fernet(Config.BYTES_KEY)


    def get_all(self):
        alunos = self.aluno_model.get_all()
        return alunos


    def save(self):
        last_id = max([p.id for p in self.aluno_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        senha = self.fernet.encrypt(request.forms.get('senha').encode('utf-8')).decode()
        matricula = request.forms.get('matricula')
        curso = request.forms.get('curso')

        aluno = Aluno(id=new_id, name=name, email=email, birthdate=birthdate, senha=senha, matricula=matricula, curso=curso)
        self.aluno_model.add_aluno(aluno)

        return aluno


    def get_by_id(self, aluno_id):
        return self.aluno_model.get_by_id(aluno_id)
    

    def get_by_email(self, aluno_email):
        return self.aluno_model.get_by_email(aluno_email)


    def edit_aluno(self, aluno):
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        senha = request.forms.get('senha')
        matricula = request.forms.get('matricula')
        curso = request.forms.get('curso')

        aluno.name = name
        aluno.email = email
        aluno.birthdate = birthdate
        aluno.senha = senha
        aluno.matricula = matricula
        aluno.curso = curso

        self.aluno_model.update_aluno(aluno)


    def delete_aluno(self, aluno_id):
        self.aluno_model.delete_aluno(aluno_id)