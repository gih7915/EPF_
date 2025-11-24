from bottle import Bottle, request
from .base_controller import BaseController
from services.video_service import VideoService
from services.tarefa_service import TarefaService
from services.submissao_service import SubmissaoService
from services.aluno_service import AlunoService
from models.aluno import AlunoModel
from models.submissao import Submissao


class AlunoController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.video_service = VideoService()
        self.tarefa_service = TarefaService()
        self.submissao_service = SubmissaoService()
        self.aluno_model = AlunoModel()
        self.aluno_service = AlunoService()

        self.setup_routes()

    def setup_routes(self):
        self.app.route('/videoaulas', method=['GET'], callback=self.list_videos)
        self.app.route('/videoaulas/watch/<video_id>', method=['POST'], callback=self.watch_video)

        self.app.route('/tarefas', method=['GET'], callback=self.list_tarefas)
        self.app.route('/tarefas/submit/<tarefa_id>', method=['GET', 'POST'], callback=self.submit_tarefa)

    def list_videos(self):
        aluno_id = request.query.get('aluno_id')
        aluno = self.aluno_model.get_by_id(int(aluno_id)) if aluno_id else None
        videos = self.video_service.get_all()
        return self.render('videoaulas', videos=videos, aluno=aluno)

    def watch_video(self, video_id):
        aluno_id = request.forms.get('aluno_id')
        if not aluno_id:
            return "Aluno não informado"
        aluno = self.aluno_model.get_by_id(int(aluno_id))
        if not aluno:
            return "Aluno não encontrado"
        aluno.assistir_video(video_id)
        self.aluno_model.update_aluno(aluno)
        self.redirect(f"/videoaulas?aluno_id={aluno_id}")

    def list_tarefas(self):
        aluno_id = request.query.get('aluno_id')
        aluno = self.aluno_model.get_by_id(int(aluno_id)) if aluno_id else None
        tarefas = self.tarefa_service.get_all()
        return self.render('tarefas', tarefas=tarefas, aluno=aluno)

    def submit_tarefa(self, tarefa_id):
        if request.method == 'GET':
            aluno_id = request.query.get('aluno_id')
            tarefa = self.tarefa_service.get_by_id(tarefa_id)
            return self.render('tarefa_submit', tarefa=tarefa, aluno_id=aluno_id)
        else:
            aluno_id = request.forms.get('aluno_id')
            conteudo = request.forms.get('conteudo')
            entregue_em = request.forms.get('entregue_em')

            # gerar id simples
            last_id = max([s.id for s in self.submissao_service.get_all()], default=0)
            new_id = last_id + 1
            submissao = Submissao(id=new_id, tarefa_id=tarefa_id, aluno_id=int(aluno_id), conteudo=conteudo, entregue_em=entregue_em)
            self.submissao_service.add_submissao(submissao)

            # atualizar o registro do aluno
            aluno = self.aluno_model.get_by_id(int(aluno_id))
            if aluno:
                aluno.registrar_entrega(tarefa_id, {'submissao_id': new_id, 'entregue_em': entregue_em})
                self.aluno_model.update_aluno(aluno)

            self.redirect(f"/tarefas?aluno_id={aluno_id}")


aluno_routes = Bottle()
aluno_controller = AlunoController(aluno_routes)
