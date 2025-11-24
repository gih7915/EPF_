import json
import os
from typing import Optional, Dict, List
from models.user import User, DATA_DIR


class Aluno(User):
    """Classe Aluno (herda de User).

    Atributos principais:
    - id, name, email, birthdate, senha : herdados de User
    - matricula: número de matrícula
    - curso: nome do curso
    - notas: dict disciplina -> list[float]
    - faltas: dict disciplina -> list[str] (datas como 'YYYY-MM-DD')
    - turma: identificador da turma
    - ativo: bool (aluno ativo/inativo)
    """

    def __init__(
        self,
        id,
        name,
        email,
        birthdate,
        senha,
        matricula: Optional[str] = None,
        curso: Optional[str] = None,
        notas: Optional[Dict[str, List[float]]] = None,
        faltas: Optional[Dict[str, List[str]]] = None,
        turma: Optional[str] = None,
        ativo: bool = True,
    ):
        super().__init__(id, name, email, birthdate, senha)
        self.matricula = matricula
        self.curso = curso
        self.notas = notas or {}
        self.faltas = faltas or {}
        self.turma = turma
        self.ativo = ativo
        # Histórico de vídeos assistidos (lista de ids de VideoAula)
        self.videos_assistidos: List[str] = []
        # Entregas locais: mapa tarefa_id -> submissao_id (ou dados mínimos)
        self.entregas: Dict[str, dict] = {}

    def adicionar_nota(self, disciplina: str, nota: float):
        self.notas.setdefault(disciplina, []).append(float(nota))

    def calcular_media(self, disciplina: Optional[str] = None) -> Optional[float]:
        """Calcula média de uma disciplina específica ou média geral.

        - Se `disciplina` for informado, retorna a média daquela disciplina.
        - Se não informado, retorna média simples entre as médias das disciplinas.
        - Retorna None se não houver notas.
        """
        if disciplina:
            notas = self.notas.get(disciplina, [])
            if not notas:
                return None
            return sum(notas) / len(notas)

        # média geral: média das médias por disciplina
        medias = [sum(v) / len(v) for v in self.notas.values() if v]
        if not medias:
            return None
        return sum(medias) / len(medias)

    def registrar_falta(self, disciplina: str, data_str: str):
        """Registra uma falta para uma disciplina na data (string 'YYYY-MM-DD')."""
        self.faltas.setdefault(disciplina, []).append(data_str)

    def assistir_video(self, video_id: str):
        """Marca que o aluno assistiu uma videoaula (id)."""
        if video_id not in self.videos_assistidos:
            self.videos_assistidos.append(video_id)

    def registrar_entrega(self, tarefa_id: str, submissao_info: dict):
        """Registra localmente uma entrega (serviço de submissões deve persistir)."""
        # submissao_info pode conter id, entregue_em, conteudo, etc.
        self.entregas[str(tarefa_id)] = submissao_info

    def total_faltas(self, disciplina: Optional[str] = None) -> int:
        if disciplina:
            return len(self.faltas.get(disciplina, []))
        return sum(len(v) for v in self.faltas.values())

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'matricula': self.matricula,
            'curso': self.curso,
            'notas': self.notas,
            'faltas': self.faltas,
            'turma': self.turma,
            'ativo': self.ativo,
            'videos_assistidos': self.videos_assistidos,
            'entregas': self.entregas,
        })
        return d

    @classmethod
    def from_dict(cls, data: dict):
        obj = cls(
            id=data.get('id'),
            name=data.get('name'),
            email=data.get('email'),
            birthdate=data.get('birthdate'),
            senha=data.get('senha'),
            matricula=data.get('matricula'),
            curso=data.get('curso'),
            notas=data.get('notas', {}),
            faltas=data.get('faltas', {}),
            turma=data.get('turma'),
            ativo=data.get('ativo', True),
        )
        # restore optional fields that aren't constructor args
        videos = data.get('videos_assistidos')
        if isinstance(videos, list):
            obj.videos_assistidos = videos
        entregas = data.get('entregas')
        if isinstance(entregas, dict):
            obj.entregas = entregas
        return obj

    def __repr__(self):
        return (
            f"Aluno(id={self.id}, name='{self.name}', matricula='{self.matricula}', "
            f"curso='{self.curso}', turma='{self.turma}', ativo={self.ativo})"
        )


# Compatibilidade: manter nomes em inglês caso o resto do projeto use-os
Student = Aluno


class AlunoModel:
    FILE_PATH = os.path.join(DATA_DIR, 'alunos.json')

    def __init__(self):
        self.alunos: List[Aluno] = self._load()

    def _load(self) -> List[Aluno]:
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Aluno.from_dict(item) for item in data]

    def _save(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a in self.alunos], f, indent=4, ensure_ascii=False)

    def get_all(self) -> List[Aluno]:
        return self.alunos

    def get_by_id(self, aluno_id):
        return next((a for a in self.alunos if a.id == aluno_id), None)
    
    def get_by_email(self, aluno_email):
        return next((a for a in self.alunos if a.email == aluno_email), None)

    def add_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)
        self._save()

    # compatibilidade com nomes em inglês
    add_student = add_aluno

    def update_aluno(self, updated_aluno: Aluno):
        for i, a in enumerate(self.alunos):
            if a.id == updated_aluno.id:
                self.alunos[i] = updated_aluno
                self._save()
                break

    update_student = update_aluno

    def delete_aluno(self, aluno_id):
        self.alunos = [a for a in self.alunos if a.id != aluno_id]
        self._save()

    delete_student = delete_aluno