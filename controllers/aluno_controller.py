from bottle import Bottle, request
from .base_controller import BaseController
from services.video_service import VideoService
from services.tarefa_service import TarefaService
from services.submissao_service import SubmissaoService
from services.aluno_service import AlunoService
from services.disciplina_service import DisciplinaService
from models.aluno import AlunoModel
from models.submissao import Submissao
import lists


class AlunoController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.video_service = VideoService()
        self.tarefa_service = TarefaService()
        self.submissao_service = SubmissaoService()
        self.aluno_model = AlunoModel()
        self.aluno_service = AlunoService()
        self.disciplina_service = DisciplinaService()

        self.setup_routes()

    def setup_routes(self):
        self.app.route('/videoaulas', method=['GET'], callback=self.list_videos)
        self.app.route('/videoaulas/watch/<video_id>', method=['POST'], callback=self.watch_video)

        self.app.route('/tarefas', method=['GET'], callback=self.list_tarefas)
        self.app.route('/tarefas/submit/<tarefa_id>', method=['GET', 'POST'], callback=self.submit_tarefa)

        self.app.route('/meu_perfil', method=['GET', 'POST'], callback=self.meu_perfil)
        self.app.route('/minhas_notas', method=['GET', 'POST'], callback=self.mostra_notas)
        self.app.route('/minhas_faltas', method=['GET', 'POST'], callback=self.mostra_faltas)
        self.app.route('/recados', method=['GET'], callback=self.lista_recados)

    def list_videos(self):
        aluno_id = request.query.get('aluno_id')
        disciplina_codigo = request.query.get('disciplina_codigo')
        
        if not aluno_id:
            return "Aluno não informado"
        
        aluno = self.aluno_model.get_by_id(int(aluno_id))
        if not aluno:
            return "Aluno não encontrado"
        
        # Pegar disciplinas matriculadas
        disciplinas_matriculadas = self.disciplina_service.get_disciplinas_aluno(int(aluno_id))
        
        # Pegar todas as videoaulas
        todas_videos = self.video_service.get_all()
        
        # Filtrar vídeos pela disciplina selecionada ou mostrar todas
        if disciplina_codigo:
            videos = [v for v in todas_videos if v.disciplina_codigo == disciplina_codigo]
            disciplina_selecionada = next((d for d in disciplinas_matriculadas if d.codigo == disciplina_codigo), None)
        else:
            # Mostrar apenas vídeos das disciplinas matriculadas
            codigos_matriculados = [d.codigo for d in disciplinas_matriculadas]
            videos = [v for v in todas_videos if v.disciplina_codigo in codigos_matriculados]
            disciplina_selecionada = None
        
        return self.render('videoaulas', 
                         videos=videos, 
                         aluno=aluno,
                         disciplinas_matriculadas=disciplinas_matriculadas,
                         disciplina_selecionada=disciplina_selecionada,
                         nav_dict=lists.home_logged_nav_bar)

    def watch_video(self, video_id):
        aluno_id = request.forms.get('aluno_id')
        if not aluno_id:
            return "Aluno não informado"
        
        aluno = self.aluno_model.get_by_id(int(aluno_id))
        if not aluno:
            return "Aluno não encontrado"
        
        # Marcar vídeo como assistido
        if video_id not in aluno.videos_assistidos:
            aluno.assistir_video(video_id)
            self.aluno_model.update_aluno(aluno)
        
        # Redirecionar de volta para a página de vídeos
        disciplina_codigo = request.forms.get('disciplina_codigo', '')
        redirect_url = f"/videoaulas?aluno_id={aluno_id}"
        if disciplina_codigo:
            redirect_url += f"&disciplina_codigo={disciplina_codigo}"
        
        self.redirect(redirect_url)

    def list_tarefas(self):
        aluno_id = request.query.get('aluno_id')
        aluno = self.aluno_model.get_by_id(int(aluno_id)) if aluno_id else None
        
        # Filtrar tarefas apenas das disciplinas matriculadas
        if aluno:
            disciplinas_matriculadas = self.disciplina_service.get_disciplinas_aluno(int(aluno_id))
            codigos_matriculados = [d.codigo for d in disciplinas_matriculadas]
            todas_tarefas = self.tarefa_service.get_all()
            tarefas = [t for t in todas_tarefas if t.disciplina in codigos_matriculados]
        else:
            tarefas = []
        
        import lists
        return self.render('tarefas', tarefas=tarefas, aluno=aluno, nav_dict=lists.home_logged_nav_bar)

    def lista_recados(self):
        aluno_id = request.query.get('aluno_id')
        if not aluno_id:
            return "Aluno não informado"
        aluno = self.aluno_model.get_by_id(int(aluno_id))
        if not aluno:
            return "Aluno não encontrado"

        disciplinas_matriculadas = self.disciplina_service.get_disciplinas_aluno(int(aluno_id))
        codigos = [d.codigo for d in disciplinas_matriculadas]

        from services.recado_service import RecadoService
        recado_service = RecadoService()
        recados = recado_service.get_for_aluno(int(aluno_id), codigos)

        return self.render('recados', modo='aluno', recados=recados, aluno=aluno, disciplinas_matriculadas=disciplinas_matriculadas, nav_dict=lists.home_logged_nav_bar)

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

    def mostra_notas(self):
        if request.method == 'GET':
            aluno_id = request.query.get('aluno_id')
            disciplina_codigo = request.query.get('disciplina_codigo')

            aluno = self.aluno_model.get_by_id(int(aluno_id)) if aluno_id else None
            disciplinas_matriculadas = self.disciplina_service.get_disciplinas_aluno(int(aluno_id)) if aluno else []

            disciplina_selecionada = None
            notas_entries = []
            media = None

            if disciplina_codigo and aluno:
                disciplina_selecionada = next((d for d in disciplinas_matriculadas if d.codigo == disciplina_codigo), None)

                tarefas = [t for t in self.tarefa_service.get_all() if t.disciplina == disciplina_codigo]

                submissao_all = self.submissao_service.get_all()
                for t in tarefas:
                    sub = next((s for s in submissao_all if s.tarefa_id == t.id and s.aluno_id == int(aluno_id)), None)
                    notas_entries.append({'tarefa': t, 'submissao': sub})

                notas_vals = [s.nota for e in notas_entries for s in ([e['submissao']] if e['submissao'] else []) if s.nota is not None]
                if notas_vals:
                    media = sum(notas_vals) / len(notas_vals)
                else:
                    media = aluno.calcular_media(disciplina_codigo)

            return self.render('minhas_notas',
                               aluno=aluno,
                               disciplinas_matriculadas=disciplinas_matriculadas,
                               disciplina_selecionada=disciplina_selecionada,
                               notas_entries=notas_entries,
                               media=media,
                               nav_dict=lists.home_logged_nav_bar)
        else:
            self.redirect(f"/dashboard/aluno")

    def mostra_faltas(self):
        if request.method == 'GET':
            aluno_id = request.query.get('aluno_id')
            disciplina_codigo = request.query.get('disciplina_codigo')

            aluno = self.aluno_model.get_by_id(int(aluno_id)) if aluno_id else None
            disciplinas_matriculadas = self.disciplina_service.get_disciplinas_aluno(int(aluno_id)) if aluno else []

            # montar lista de entradas de faltas por disciplina
            faltas_entries = []

            disciplinas_map = {d.codigo: d for d in disciplinas_matriculadas}

            if aluno:
                codigo_set = set(list(aluno.faltas.keys()) + [d.codigo for d in disciplinas_matriculadas])
            else:
                codigo_set = set()

            for codigo in sorted(codigo_set):
                disc = disciplinas_map.get(codigo)
                datas = aluno.faltas.get(codigo, []) if aluno else []
                faltas_entries.append({
                    'codigo': codigo,
                    'nome': getattr(disc, 'nome', '—') if disc else '—',
                    'datas': datas,
                    'total': len(datas)
                })

            disciplina_selecionada = None
            if disciplina_codigo and aluno:
                disciplina_selecionada = next((d for d in disciplinas_matriculadas if d.codigo == disciplina_codigo), None)
                faltas_entries = [e for e in faltas_entries if e['codigo'] == disciplina_codigo]

            total_faltas = aluno.total_faltas() if aluno else 0

            return self.render('minhas_faltas',
                               aluno=aluno,
                               disciplinas_matriculadas=disciplinas_matriculadas,
                               disciplina_selecionada=disciplina_selecionada,
                               faltas_entries=faltas_entries,
                               total_faltas=total_faltas,
                               nav_dict=lists.home_logged_nav_bar)
        else:
            self.redirect(f"/dashboard/aluno")


    def meu_perfil(self):
        aluno_id = request.query.get('aluno_id')
        if not aluno_id:
            self.redirect("/")
            return
        aluno = self.aluno_model.get_by_id(int(aluno_id))
        if request.method == 'GET':
            if aluno:
                return self.render('meu_perfil', aluno=aluno, prof=None, cursos=lists.cursos)
            else:
                self.redirect("/")
        else: 
            if aluno:
                self.aluno_service.edit_aluno_attribute(aluno)
                self.redirect(f"/meu_perfil?aluno_id={aluno_id}")
            else:
                self.redirect("/")


aluno_routes = Bottle()
aluno_controller = AlunoController(aluno_routes)
