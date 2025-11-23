from typing import Optional


class Tarefa:
    def __init__(self, id, titulo, descricao: Optional[str] = None, disciplina: Optional[str] = None, prazo: Optional[str] = None, max_points: Optional[float] = None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.disciplina = disciplina
        self.prazo = prazo
        self.max_points = max_points

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'disciplina': self.disciplina,
            'prazo': self.prazo,
            'max_points': self.max_points,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            titulo=data.get('titulo'),
            descricao=data.get('descricao'),
            disciplina=data.get('disciplina'),
            prazo=data.get('prazo'),
            max_points=data.get('max_points'),
        )
