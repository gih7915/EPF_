import json
import os
from typing import List, Optional
from models.recado import Recado
from models.user import DATA_DIR

class RecadoService:
    FILE_PATH = os.path.join(DATA_DIR, 'recados.json')

    def __init__(self):
        self.recados = self._load()

    def _load(self) -> List[Recado]:
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Recado.from_dict(item) for item in data]

    def _save(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([r.to_dict() for r in self.recados], f, indent=2, ensure_ascii=False)

    def add_recado(self, recado: Recado):
        self.recados.append(recado)
        self._save()

    def get_all(self) -> List[Recado]:
        return self.recados

    def get_by_disciplina(self, disciplina_codigo: str) -> List[Recado]:
        return [r for r in self.recados if r.disciplina_codigo == disciplina_codigo]

    def get_for_aluno(self, aluno_id: int, disciplinas_codigos: List[str]) -> List[Recado]:
        # Recados da(s) disciplinas do aluno + recados direcionados ao aluno
        return [r for r in self.recados if (r.disciplina_codigo in disciplinas_codigos) or (r.aluno_id == aluno_id)]
