from bottle import Bottle, request
from .base_controller import BaseController
from services.login_service import LoginService
from models.login import Login

class LoginController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.login_service = LoginService()

        self.erro=None
    
    #Rotas de login e sign-up
    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        #self.app.route('/signup', method=['GET', 'POST'], callback=self.signup)

    def login(self):
        if request.method == 'GET':
            print(self.erro)
            return self.render('login', email=None, senha=None, erro=self.erro, action=f"/login")
        else: #POST
            self.erro=None
            try:
                Login(self.login_service.check())
                self.redirect('/users')
            except IndexError as e:
                print(self.erro)
                self.erro=e
                self.redirect('/login')

login_routes = Bottle()
login_controller = LoginController(login_routes)