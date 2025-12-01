from models.disciplina import DisciplinaModel, Disciplina


class DisciplinaService:
    def __init__(self):
        self.disciplina_model = DisciplinaModel()

    def get_all(self):
        """Retorna todas as disciplinas."""
        return self.disciplina_model.get_all()

    def get_by_id(self, disciplina_id: int):
        """Retorna uma disciplina pelo ID."""
        return self.disciplina_model.get_by_id(disciplina_id)

    def search(self, query: str):
        """Busca disciplinas por código ou nome."""
        return self.disciplina_model.search(query)

    def matricular_aluno(self, disciplina_id: int, aluno_id: int, senha: str):
        """Matricula um aluno em uma disciplina.
        
        Args:
            disciplina_id: ID da disciplina
            aluno_id: ID do aluno
            senha: Senha da disciplina para validação
            
        Returns:
            bool: True se matrícula foi realizada com sucesso
            
        Raises:
            Exception: Se senha incorreta, sem vagas ou aluno já matriculado
        """
        disciplina = self.disciplina_model.get_by_id(disciplina_id)
        
        if not disciplina:
            raise Exception("Disciplina não encontrada")
        
        if disciplina.senha != senha:
            raise Exception("Senha incorreta")
        
        disciplina.matricular_aluno(aluno_id)
        self.disciplina_model.update(disciplina)
        return True

    def desmatricular_aluno(self, disciplina_id: int, aluno_id: int):
        """Remove um aluno de uma disciplina."""
        disciplina = self.disciplina_model.get_by_id(disciplina_id)
        
        if not disciplina:
            raise Exception("Disciplina não encontrada")
        
        disciplina.desmatricular_aluno(aluno_id)
        self.disciplina_model.update(disciplina)
        return True

    def get_disciplinas_aluno(self, aluno_id: int):
        """Retorna todas as disciplinas em que o aluno está matriculado."""
        todas = self.get_all()
        return [d for d in todas if aluno_id in d.alunos_matriculados]

    def atribuir_docente(self, disciplina_id: int, prof_id: int):
        """Atribui um docente à disciplina (professor se inscreve)."""
        disciplina = self.get_by_id(disciplina_id)
        if not disciplina:
            raise Exception("Disciplina não encontrada")
        if disciplina.docente_id:
            raise Exception("Disciplina já possui docente")
        disciplina.docente_id = prof_id
        self.disciplina_model.update(disciplina)
        return True
