from typing import Optional

class Recado:
    def __init__(self, id: int, titulo: str, mensagem: str, 
                 disciplina_codigo: Optional[str] = None,
                 professor_id: Optional[int] = None,
                 aluno_id: Optional[int] = None,
                 criado_em: Optional[str] = None):
        self.id = id
        self.titulo = titulo
        self.mensagem = mensagem
        self.disciplina_codigo = disciplina_codigo
        self.professor_id = professor_id
        self.aluno_id = aluno_id
        self.criado_em = criado_em

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'mensagem': self.mensagem,
            'disciplina_codigo': self.disciplina_codigo,
            'professor_id': self.professor_id,
            'aluno_id': self.aluno_id,
            'criado_em': self.criado_em,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            titulo=data.get('titulo'),
            mensagem=data.get('mensagem'),
            disciplina_codigo=data.get('disciplina_codigo'),
            professor_id=data.get('professor_id'),
            aluno_id=data.get('aluno_id'),
            criado_em=data.get('criado_em'),
        )
