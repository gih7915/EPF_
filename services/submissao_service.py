import json
import os
from models.submissao import Submissao
from models.user import DATA_DIR


class SubmissaoService:
    FILE_PATH = os.path.join(DATA_DIR, 'submissoes.json')

    def __init__(self):
        self.submissoes = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Submissao.from_dict(item) for item in data]

    def _save(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([s.to_dict() for s in self.submissoes], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.submissoes

    def get_by_id(self, sid):
        return next((s for s in self.submissoes if s.id == sid), None)

    def add_submissao(self, submissao: Submissao):
        self.submissoes.append(submissao)
        self._save()
