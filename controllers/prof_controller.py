from bottle import Bottle, request
from .base_controller import BaseController
from services.prof_service import ProfService
from models.prof import ProfModel
from services.tarefa_service import TarefaService
from services.video_service import VideoService
from services.disciplina_service import DisciplinaService

class ProfController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.prof_service = ProfService()
        self.prof_model = ProfModel()
        self.tarefa_service = TarefaService()
        self.video_service = VideoService()
        self.disciplina_service = DisciplinaService()
    
    def _get_logged_prof(self):
        """Helper para obter professor logado via login_controller"""
        from .login_controller import login_controller
        if login_controller.user_logged and login_controller.user_logged.entidade.__class__.__name__ == "Prof":
            return login_controller.user_logged.entidade
        return None


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
        self.app.route('/enviar_recado', method=['GET', 'POST'], callback=self.enviar_recado)

        self.app.route('/visualizar_turmas', method=['GET'], callback=self.visualizar_turmas)
        self.app.route('/visualizar_turmas', method='POST', callback=self.inscrever_docente)

        self.app.route('/avaliar_trabalhos', method=['GET'], callback=self.avaliar_trabalhos)

        self.app.route('/perfil_professor', method=['GET', 'POST'], callback=self.perfil_professor)

    def lancar_notas(self):
        prof = self._get_logged_prof()
        if not prof:
            return self.redirect('/login')
        
        minhas_turmas = self.disciplina_service.get_disciplinas_professor(prof.id)
        import lists
        
        if request.method == 'GET':
            disciplina_codigo = request.query.get('disciplina_codigo')
            disciplina_selecionada = None
            alunos = []
            
            if disciplina_codigo:
                disciplina_selecionada = next((d for d in minhas_turmas if d.codigo == disciplina_codigo), None)
                if disciplina_selecionada:
                    # Buscar alunos matriculados
                    from models.aluno import AlunoModel
                    aluno_model = AlunoModel()
                    todos_alunos = aluno_model.get_all()
                    alunos = [a for a in todos_alunos if a.id in disciplina_selecionada.alunos_matriculados]
            
            return self.render('lancar_notas', 
                             minhas_turmas=minhas_turmas, 
                             prof=prof,
                             disciplina_selecionada=disciplina_selecionada,
                             alunos=alunos,
                             mensagem=None,
                             nav_dict=lists.home_logged_nav_bar)
        else:
            # POST - salvar nota
            disciplina_codigo = request.forms.get('disciplina_codigo')
            aluno_id = int(request.forms.get('aluno_id'))
            avaliacao = request.forms.get('avaliacao')
            nota = float(request.forms.get('nota'))
            
            # Salvar nota no aluno
            from models.aluno import AlunoModel
            aluno_model = AlunoModel()
            aluno = aluno_model.get_by_id(aluno_id)
            
            if aluno:
                aluno.adicionar_nota(disciplina_codigo, nota)
                aluno_model.update_aluno(aluno)
                
                disciplina_selecionada = next((d for d in minhas_turmas if d.codigo == disciplina_codigo), None)
                todos_alunos = aluno_model.get_all()
                alunos = [a for a in todos_alunos if a.id in disciplina_selecionada.alunos_matriculados] if disciplina_selecionada else []
                
                return self.render('lancar_notas', 
                                 minhas_turmas=minhas_turmas, 
                                 prof=prof,
                                 disciplina_selecionada=disciplina_selecionada,
                                 alunos=alunos,
                                 mensagem=f"Nota {nota} lançada com sucesso para {aluno.name}!",
                                 nav_dict=lists.home_logged_nav_bar)
            
            self.redirect('/lancar_notas')

    def lancar_faltas(self):
        prof = self._get_logged_prof()
        if not prof:
            return self.redirect('/login')
        
        minhas_turmas = self.disciplina_service.get_disciplinas_professor(prof.id)
        import lists
        
        if request.method == 'GET':
            disciplina_codigo = request.query.get('disciplina_codigo')
            disciplina_selecionada = None
            alunos = []
            
            if disciplina_codigo:
                disciplina_selecionada = next((d for d in minhas_turmas if d.codigo == disciplina_codigo), None)
                if disciplina_selecionada:
                    # Buscar alunos matriculados
                    from models.aluno import AlunoModel
                    aluno_model = AlunoModel()
                    todos_alunos = aluno_model.get_all()
                    alunos = [a for a in todos_alunos if a.id in disciplina_selecionada.alunos_matriculados]
            
            return self.render('lancar_faltas', 
                             minhas_turmas=minhas_turmas, 
                             prof=prof,
                             disciplina_selecionada=disciplina_selecionada,
                             alunos=alunos,
                             mensagem=None,
                             nav_dict=lists.home_logged_nav_bar)
        else:
            # POST - salvar falta
            disciplina_codigo = request.forms.get('disciplina_codigo')
            aluno_id = int(request.forms.get('aluno_id'))
            data = request.forms.get('data')
            
            # Salvar falta no aluno
            from models.aluno import AlunoModel
            aluno_model = AlunoModel()
            aluno = aluno_model.get_by_id(aluno_id)
            
            if aluno:
                aluno.registrar_falta(disciplina_codigo, data)
                aluno_model.update_aluno(aluno)
                
                disciplina_selecionada = next((d for d in minhas_turmas if d.codigo == disciplina_codigo), None)
                todos_alunos = aluno_model.get_all()
                alunos = [a for a in todos_alunos if a.id in disciplina_selecionada.alunos_matriculados] if disciplina_selecionada else []
                
                return self.render('lancar_faltas', 
                                 minhas_turmas=minhas_turmas, 
                                 prof=prof,
                                 disciplina_selecionada=disciplina_selecionada,
                                 alunos=alunos,
                                 mensagem=f"Falta registrada com sucesso para {aluno.name} em {data}!",
                                 nav_dict=lists.home_logged_nav_bar)
            
            self.redirect('/lancar_faltas')

    def criar_atividade(self):
        prof = self._get_logged_prof()
        if not prof:
            return self.redirect('/login')
        
        if request.method == 'GET':
            minhas_turmas = self.disciplina_service.get_disciplinas_professor(prof.id)
            import lists
            return self.render('criar_atividade', minhas_turmas=minhas_turmas, nav_dict=lists.home_logged_nav_bar)
        else:
            titulo = request.forms.get('titulo')
            descricao = request.forms.get('descricao')
            disciplina_codigo = request.forms.get('disciplina_codigo')
            prazo = request.forms.get('prazo')

            last_id = max([t.id for t in self.tarefa_service.get_all()], default=0)
            new_id = last_id + 1

            from models.tarefa import Tarefa
            tarefa = Tarefa(id=new_id, titulo=titulo, descricao=descricao, disciplina=disciplina_codigo, prazo=prazo)
            self.tarefa_service.add_tarefa(tarefa)

            self.redirect('/dashboard_prof')

    def postar_videoaula(self):
        prof = self._get_logged_prof()
        if not prof:
            return self.redirect('/login')
        
        if request.method == 'GET':
            minhas_turmas = self.disciplina_service.get_disciplinas_professor(prof.id)
            import lists
            return self.render('postar_videoaula', minhas_turmas=minhas_turmas, nav_dict=lists.home_logged_nav_bar)
        else:
            titulo = request.forms.get('titulo')
            url = request.forms.get('link')
            disciplina_codigo = request.forms.get('disciplina_codigo')
            descricao = request.forms.get('descricao')

            last_id = max([v.id for v in self.video_service.get_all()], default=0)
            new_id = last_id + 1

            from models.videoaula import VideoAula
            video = VideoAula(id=new_id, titulo=titulo, url=url, descricao=descricao, 
                            disciplina=disciplina_codigo, disciplina_codigo=disciplina_codigo)
            self.video_service.add_video(video)

            self.redirect('/dashboard_prof')

    def enviar_recado(self):
        prof = self._get_logged_prof()
        if not prof:
            return self.redirect('/login')
        import lists
        from services.recado_service import RecadoService
        recado_service = RecadoService()
        minhas_turmas = self.disciplina_service.get_disciplinas_professor(prof.id)

        if request.method == 'GET':
            return self.render('recados', modo='professor', minhas_turmas=minhas_turmas, mensagem_sucesso=None, nav_dict=lists.home_logged_nav_bar)
        else:
            titulo = request.forms.get('titulo')
            mensagem = request.forms.get('mensagem')
            disciplina_codigo = request.forms.get('disciplina_codigo')
            # opcional direcionado para aluno específico
            aluno_id = request.forms.get('aluno_id')
            aluno_id_int = int(aluno_id) if aluno_id else None

            # gerar id simples
            last_id = max([r.id for r in recado_service.get_all()], default=0)
            new_id = last_id + 1
            from models.recado import Recado
            recado = Recado(id=new_id, titulo=titulo, mensagem=mensagem, disciplina_codigo=disciplina_codigo,
                            professor_id=prof.id, aluno_id=aluno_id_int)
            recado_service.add_recado(recado)
            return self.render('recados', modo='professor', minhas_turmas=minhas_turmas, mensagem_sucesso='Recado enviado!', nav_dict=lists.home_logged_nav_bar)

    def visualizar_turmas(self):
        prof = self._get_logged_prof()
        if not prof:
            return self.redirect('/login')
        
        todas = self.disciplina_service.get_all()
        minhas_turmas = [d for d in todas if d.docente_id == prof.id]
        disponiveis = [d for d in todas if d.docente_id is None or d.docente_id == 0]
        
        return self.render('visualizar_turmas', 
                         minhas_turmas=minhas_turmas, 
                         disponiveis=disponiveis,
                         prof=prof)

    def inscrever_docente(self):
        prof = self._get_logged_prof()
        if not prof:
            return self.redirect('/login')
        
        disciplina_id = int(request.forms.get('disciplina_id'))
        try:
            self.disciplina_service.atribuir_docente(disciplina_id, prof.id)
            return self.redirect('/visualizar_turmas')
        except Exception as e:
            return f"Erro: {str(e)}"

    def avaliar_trabalhos(self):
        return self.render('avaliar_trabalhos')


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

    def perfil_professor(self): #aq é similar ao meu_perfil do aluno controller
        prof_id = request.query.get('prof_id')
        if not prof_id:
            self.redirect("/")
            return
        prof = self.prof_model.get_by_id(int(prof_id))
        if request.method == 'GET':
            if prof:
                return self.render('perfil_professor', prof=prof)
            else:
                self.redirect("/")
        else: 
            if prof:
                self.prof_service.edit_prof_attribute(prof)
                self.redirect(f"/perfil_professor?prof_id={prof_id}")
            else:
                self.redirect("/")


prof_routes = Bottle()
prof_controller = ProfController(prof_routes)
