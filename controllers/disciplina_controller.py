from bottle import Bottle, request
from .base_controller import BaseController
from services.disciplina_service import DisciplinaService
import lists


class DisciplinaController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.disciplina_service = DisciplinaService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/disciplinas', method='GET', callback=self.list_disciplinas)
        self.app.route('/disciplinas/buscar', method=['GET', 'POST'], callback=self.buscar_disciplinas)
        self.app.route('/disciplinas/matricular/<disciplina_id:int>', method=['GET', 'POST'], callback=self.matricular)
        self.app.route('/disciplinas/minhas', method='GET', callback=self.minhas_disciplinas)
        self.app.route('/disciplinas/desmatricular/<disciplina_id:int>', method='POST', callback=self.desmatricular)

    def list_disciplinas(self):
        aluno_id = request.query.get('aluno_id')
        disciplinas = self.disciplina_service.get_all()
        
        disciplinas_matriculadas = []
        if aluno_id:
            disciplinas_matriculadas = self.disciplina_service.get_disciplinas_aluno(int(aluno_id))
            matriculadas_ids = [d.id for d in disciplinas_matriculadas]
        else:
            matriculadas_ids = []
        
        return self.render('disciplinas_list', 
                         disciplinas=disciplinas, 
                         aluno_id=aluno_id,
                         matriculadas_ids=matriculadas_ids,
                         nav_dict=lists.home_logged_nav_bar)

    def buscar_disciplinas(self):
        aluno_id = request.query.get('aluno_id') or request.forms.get('aluno_id')
        
        if request.method == 'POST':
            query = request.forms.get('query', '')
            disciplinas = self.disciplina_service.search(query)
        else:
            query = request.query.get('query', '')
            if query:
                disciplinas = self.disciplina_service.search(query)
            else:
                disciplinas = self.disciplina_service.get_all()
        
        if aluno_id:
            disciplinas_matriculadas = self.disciplina_service.get_disciplinas_aluno(int(aluno_id))
            matriculadas_ids = [d.id for d in disciplinas_matriculadas]
        else:
            matriculadas_ids = []
        
        return self.render('disciplinas_list', 
                         disciplinas=disciplinas,
                         aluno_id=aluno_id,
                         query=query,
                         matriculadas_ids=matriculadas_ids,
                         nav_dict=lists.home_logged_nav_bar)

    def matricular(self, disciplina_id):
        if request.method == 'GET':
            aluno_id = request.query.get('aluno_id')
            disciplina = self.disciplina_service.get_by_id(disciplina_id)
            
            if not disciplina:
                return "Disciplina não encontrada"
            
            return self.render('disciplina_matricular',
                             disciplina=disciplina,
                             aluno_id=aluno_id,
                             erro=None,
                             nav_dict=lists.home_logged_nav_bar)
        else:
            # POST - realizar matrícula
            aluno_id = request.forms.get('aluno_id')
            senha = request.forms.get('senha')
            
            try:
                self.disciplina_service.matricular_aluno(disciplina_id, int(aluno_id), senha)
                self.redirect(f'/disciplinas/minhas?aluno_id={aluno_id}')
            except Exception as e:
                disciplina = self.disciplina_service.get_by_id(disciplina_id)
                return self.render('disciplina_matricular',
                                 disciplina=disciplina,
                                 aluno_id=aluno_id,
                                 erro=str(e),
                                 nav_dict=lists.home_logged_nav_bar)

    def minhas_disciplinas(self):
        aluno_id = request.query.get('aluno_id')
        
        if not aluno_id:
            return "Aluno não informado"
        
        disciplinas = self.disciplina_service.get_disciplinas_aluno(int(aluno_id))
        
        return self.render('minhas_disciplinas',
                         disciplinas=disciplinas,
                         aluno_id=aluno_id,
                         nav_dict=lists.home_logged_nav_bar)

    def desmatricular(self, disciplina_id):
        aluno_id = request.forms.get('aluno_id')
        
        try:
            self.disciplina_service.desmatricular_aluno(disciplina_id, int(aluno_id))
        except Exception as e:
            print(f"Erro ao desmatricular: {e}")
        
        self.redirect(f'/disciplinas/minhas?aluno_id={aluno_id}')


disciplina_routes = Bottle()
disciplina_controller = DisciplinaController(disciplina_routes)
