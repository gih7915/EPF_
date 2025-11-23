import json
import os
from models.tarefa import Tarefa
from models.user import DATA_DIR


class TarefaService:
    FILE_PATH = os.path.join(DATA_DIR, 'tarefas.json')

    def __init__(self):
        self.tarefas = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Tarefa.from_dict(item) for item in data]

    def _save(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self.tarefas], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.tarefas

    def get_by_id(self, tid):
        return next((t for t in self.tarefas if t.id == tid), None)

    def add_tarefa(self, tarefa: Tarefa):
        self.tarefas.append(tarefa)
        self._save()
