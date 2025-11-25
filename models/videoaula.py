import json
import os
from typing import Optional
from models.user import DATA_DIR


class VideoAula:
    def __init__(self, id, titulo, url, descricao: Optional[str] = None, 
                 disciplina: Optional[str] = None, duracao: Optional[int] = None,
                 disciplina_codigo: Optional[str] = None):
        self.id = id
        self.titulo = titulo
        self.url = url
        self.descricao = descricao
        self.disciplina = disciplina
        self.duracao = duracao
        self.disciplina_codigo = disciplina_codigo  # Código da disciplina (ex: FGA0030)

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'url': self.url,
            'descricao': self.descricao,
            'disciplina': self.disciplina,
            'duracao': self.duracao,
            'disciplina_codigo': self.disciplina_codigo,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            titulo=data.get('titulo'),
            url=data.get('url'),
            descricao=data.get('descricao'),
            disciplina=data.get('disciplina'),
            duracao=data.get('duracao'),
            disciplina_codigo=data.get('disciplina_codigo'),
        )
