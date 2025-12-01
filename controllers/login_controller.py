from bottle import Bottle, request
from dataclasses import dataclass, asdict
from cryptography.fernet import Fernet
from .base_controller import BaseController
from services.login_service import LoginService
from models.login import Login
from .prof_controller import prof_controller
from .aluno_controller import aluno_controller
import lists


class LoginController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.login_service = LoginService()
        self.user_logged = None

        self.user_class_name = None
    
    #Rotas de login e sign-up
    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/signup', method=['GET', 'POST'], callback=self.signup)
        self.app.route('/signup/wipe', method=['GET', 'POST'], callback=self.signup_wipe)
        self.app.route('/home', method=['GET', 'POST'], callback=self.home)
        self.app.route('/sair', method='GET', callback=self.sair)
        self.app.route('/dashboard/aluno', method='GET', callback=self.dashboard_aluno)
        self.app.route('/dashboard/professor', method='GET', callback=self.dashboard_professor)


    def login(self):
        if request.method == 'GET':
            erro_num = request.query.get('erro', '')
            erro = lists.erro_mensagens.get(erro_num, '')
            return self.render('login', email=None, senha=None, erro=erro, action="/login")
        
        else:  # POST
            try:
                # Inject services to avoid circular imports
                from .prof_controller import prof_controller
                from .aluno_controller import aluno_controller
                self.user_logged = Login(self.login_service.check(
                    prof_controller.prof_service,
                    aluno_controller.aluno_service
                ))
                
                # Redirecionar para dashboard específico baseado no tipo de usuário
                user_type = self.user_logged.entidade.__class__.__name__
                if user_type == "Prof":
                    self.redirect('/dashboard/professor')
                elif user_type == "Aluno":
                    self.redirect('/dashboard/aluno')
                else:
                    self.redirect('/home')
            except IndexError as e:
                self.redirect(f'/login?erro={e}')

    def signup(self):
        if request.method == 'GET':
            return self.render('signup', user_class=self.user_class_name, action="/signup", cursos=lists.cursos)
        else: #POST
            if self.user_class_name == "Prof":
                saved_prof = prof_controller.prof_service.save()
                self.user_logged = Login(saved_prof)
                self.redirect('/dashboard/professor')
            elif self.user_class_name == "Aluno":
                saved_aluno = aluno_controller.aluno_service.save()
                self.user_logged = Login(saved_aluno)
                self.redirect('/dashboard/aluno')
            else:
                self.user_class_name = request.forms.get('tipo')
                self.redirect(f'/signup?user_class={self.user_class_name}')

    def signup_wipe(self):
        self.user_class_name=None
        self.redirect('/signup')

    def home(self):
        if request.method == 'GET':
            # Redirecionar para login se não estiver autenticado
            if self.user_logged is None:
                self.redirect('/login')
            else:
                # Redirecionar para dashboard apropriado
                user_type = self.user_logged.entidade.__class__.__name__
                if user_type == "Prof":
                    self.redirect('/dashboard/professor')
                elif user_type == "Aluno":
                    self.redirect('/dashboard/aluno')
                else:
                    return self.render('home', action="/home", nav_dict=lists.home_logged_nav_bar)
            
    def sair(self):
        if not self.user_logged == None:
            self.user_logged = None
        self.redirect('/login')

    def dashboard_aluno(self):
        if self.user_logged is None:
            self.redirect('/login')
        else:
            aluno = self.user_logged.entidade
            return self.render('dashboard_aluno', aluno=aluno, nav_dict=lists.home_logged_nav_bar)

    def dashboard_professor(self):
        if self.user_logged is None:
            self.redirect('/login')
        else:
            prof = self.user_logged.entidade
            return self.render('dashboard_prof', prof=prof, nav_dict=lists.home_logged_nav_bar)


login_routes = Bottle()
login_controller = LoginController(login_routes)