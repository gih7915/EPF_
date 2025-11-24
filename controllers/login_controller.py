from bottle import Bottle, request
import json
import os
from dataclasses import dataclass, asdict
from cryptography.fernet import Fernet
from .base_controller import BaseController
from services.login_service import LoginService
from models.login import Login
from .prof_controller import prof_controller
from .aluno_controller import aluno_controller
from lists import cursos
from lists import erro_mensagens


class LoginController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.login_service = LoginService()

        self.user_class_name=None
    
    #Rotas de login e sign-up
    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/signup', method=['GET', 'POST'], callback=self.signup)
        self.app.route('/signup/wipe', method=['GET', 'POST'], callback=self.signup_wipe)
        self.app.route('/home', method=['GET', 'POST'], callback=self.home)


    def login(self):
        if request.method == 'GET':
            erro_num = request.query.get('erro', '')
            erro = erro_mensagens.get(erro_num, '')
            return self.render('login', email=None, senha=None, erro=erro, action="/login")
        
        else:  # POST
            try:
                Login(self.login_service.check())
                self.redirect('/users')
            except IndexError as e:
                self.redirect(f'/login?erro={e}')

    def signup(self):
        if request.method == 'GET':
            return self.render('signup', user_class=self.user_class_name, action="/signup", cursos=cursos)
        else: #POST
            if self.user_class_name == "Prof":
                prof_controller.prof_service.save()
                self.redirect('/profs')
            elif self.user_class_name == "Aluno":
                aluno_controller.aluno_service.save()
                self.redirect('/users')
            else:
                self.user_class_name = request.forms.get('tipo')
                self.redirect(f'/signup?user_class={self.user_class_name}')

    def signup_wipe(self):
        self.user_class_name=None
        self.redirect('/signup')

    def home(self):
        if request.method == 'GET':
            return self.render('home', user_class=self.user_class_name, action="/home")

login_routes = Bottle()
login_controller = LoginController(login_routes)