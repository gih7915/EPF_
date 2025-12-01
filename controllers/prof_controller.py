from bottle import Bottle, request
from .base_controller import BaseController
from services.prof_service import ProfService
from services.tarefa_service import TarefaService
from services.video_service import VideoService
from services.disciplina_service import DisciplinaService

class ProfController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.prof_service = ProfService()
        self.tarefa_service = TarefaService()
        self.video_service = VideoService()
        self.disciplina_service = DisciplinaService()


    # Rotas Prof
    def setup_routes(self):
        self.app.route('/profs', method='GET', callback=self.list_profs)
        self.app.route('/profs/add', method=['GET', 'POST'], callback=self.add_prof)
        self.app.route('/profs/edit/<prof_id:int>', method=['GET', 'POST'], callback=self.edit_prof)
        self.app.route('/profs/delete/<prof_id:int>', method='POST', callback=self.delete_prof)
        self.app.route('/lancar_notas', method=['GET', 'POST'], callback=self.lancar_notas)
        self.app.route('/lancar_faltas', method=['GET', 'POST'], callback=self.lancar_faltas)
        self.app.route('/criar_atividade', method=['GET', 'POST'], callback=self.criar_atividade)
        self.app.route('/postar_videoaula', method=['GET', 'POST'], callback=self.postar_videoaula)
        self.app.route('/enviar_recado', method=['GET'], callback=self.enviar_recado)
            self.app.route('/visualizar_turmas', method=['GET'], callback=self.visualizar_turmas)
            self.app.route('/visualizar_turmas', method='POST', callback=self.inscrever_docente)
        self.app.route('/avaliar_trabalhos', method=['GET'], callback=self.avaliar_trabalhos)
        self.app.route('/relatorios', method='GET', callback=self.relatorios)
    def lancar_notas(self):
        if request.method == 'GET':
            return self.render('lancar_notas')
        else:
            # Aqui você pode adicionar a lógica para salvar a nota
            # Exemplo: disciplina = request.forms.get('disciplina')
            # aluno = request.forms.get('aluno')
            # nota = request.forms.get('nota')
            # self.prof_service.lancar_nota(disciplina, aluno, nota)
            self.redirect('/dashboard_prof')

    def lancar_faltas(self):
        if request.method == 'GET':
            return self.render('lancar_faltas')
        else:
            # Aqui você pode adicionar a lógica para salvar as faltas
            # Exemplo: disciplina = request.forms.get('disciplina')
            # aluno = request.forms.get('aluno')
            # faltas = request.forms.get('faltas')
            # self.prof_service.lancar_falta(disciplina, aluno, faltas)
            self.redirect('/dashboard_prof')

    def criar_atividade(self):
        if request.method == 'GET':
            return self.render('criar_atividade')
        else:
            titulo = request.forms.get('titulo')
            descricao = request.forms.get('descricao')
            disciplina = request.forms.get('disciplina')
            prazo = request.forms.get('prazo')

            last_id = max([t.id for t in self.tarefa_service.get_all()], default=0)
            new_id = last_id + 1

            from models.tarefa import Tarefa
            tarefa = Tarefa(id=new_id, titulo=titulo, descricao=descricao, disciplina=disciplina, prazo=prazo)
            self.tarefa_service.add_tarefa(tarefa)

            self.redirect('/tarefas')

    def postar_videoaula(self):
        if request.method == 'GET':
            return self.render('postar_videoaula')
        else:
            titulo = request.forms.get('titulo')
            url = request.forms.get('link')
            disciplina = request.forms.get('disciplina')
            descricao = request.forms.get('descricao')

            last_id = max([v.id for v in self.video_service.get_all()], default=0)
            new_id = last_id + 1

            from models.videoaula import VideoAula
            video = VideoAula(id=new_id, titulo=titulo, url=url, descricao=descricao, disciplina=disciplina)
            self.video_service.add_video(video)

            self.redirect('/videoaulas')

    def enviar_recado(self):
        return self.render('recados')

    def visualizar_turmas(self):
        disciplinas = self.disciplina_service.get_all()
        return self.render('visualizar_turmas', disciplinas=disciplinas)

    def inscrever_docente(self):
        disciplina_id = int(request.forms.get('disciplina_id'))
        prof_id = int(request.forms.get('prof_id'))
        try:
            self.disciplina_service.atribuir_docente(disciplina_id, prof_id)
            return self.redirect('/visualizar_turmas')
        except Exception as e:
            return f"Erro: {str(e)}"

    def avaliar_trabalhos(self):
        return self.render('avaliar_trabalhos')

    def relatorios(self):
        return self.render('relatorios')


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
