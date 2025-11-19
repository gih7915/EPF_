from bottle import Bottle, request
from .base_controller import BaseController
from services.prof_service import ProfService

class ProfController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.prof_service = ProfService()


    # Rotas Prof
    def setup_routes(self):
        self.app.route('/profs', method='GET', callback=self.list_profs)
        self.app.route('/profs/add', method=['GET', 'POST'], callback=self.add_prof)
        self.app.route('/profs/edit/<prof_id:int>', method=['GET', 'POST'], callback=self.edit_prof)
        self.app.route('/profs/delete/<prof_id:int>', method='POST', callback=self.delete_prof)


    def list_profs(self):
        profs = self.prof_service.get_all()
        return self.render('profs', profs=profs)


    def add_prof(self):
        if request.method == 'GET':
            return self.render('prof_form', prof=None, action="/profs/add")
        else:
            # POST - salvar usuário
            self.prof_service.save()
            self.redirect('/profs')


    def edit_prof(self, prof_id):
        prof = self.prof_service.get_by_id(prof_id)
        if not prof:
            return "Professor não encontrado"

        if request.method == 'GET':
            return self.render('prof_form', prof=prof, action=f"/profs/edit/{prof_id}")
        else:
            # POST - salvar edição
            self.prof_service.edit_prof(prof)
            self.redirect('/profs')


    def delete_prof(self, prof_id):
        self.prof_service.delete_prof(prof_id)
        self.redirect('/profs')


prof_routes = Bottle()
prof_controller = ProfController(prof_routes)
