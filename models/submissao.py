from typing import Optional


class Submissao:
    def __init__(self, id, tarefa_id, aluno_id, conteudo: Optional[str] = None, entregue_em: Optional[str] = None, nota: Optional[float] = None, feedback: Optional[str] = None):
        self.id = id
        self.tarefa_id = tarefa_id
        self.aluno_id = aluno_id
        self.conteudo = conteudo
        self.entregue_em = entregue_em
        self.nota = nota
        self.feedback = feedback

    def to_dict(self):
        return {
            'id': self.id,
            'tarefa_id': self.tarefa_id,
            'aluno_id': self.aluno_id,
            'conteudo': self.conteudo,
            'entregue_em': self.entregue_em,
            'nota': self.nota,
            'feedback': self.feedback,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            tarefa_id=data.get('tarefa_id'),
            aluno_id=data.get('aluno_id'),
            conteudo=data.get('conteudo'),
            entregue_em=data.get('entregue_em'),
            nota=data.get('nota'),
            feedback=data.get('feedback'),
        )
