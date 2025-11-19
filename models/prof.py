import json
import os
from dataclasses import dataclass, asdict
from typing import List
from .user import User

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Prof(User):
    def __init__(self, id, name, email, birthdate, cargo):
        super().__init__(id, name, email, birthdate)
        self.cargo = cargo


    def __repr__(self):
        return (f"Prof(id={self.id}, name='{self.name}', email='{self.email}', "
                f"birthdate='{self.birthdate}', cargo='{self.cargo}')")


    def to_dict(self):
        prof_dict = super().to_dict()
        prof_dict.update({
            'cargo': self.cargo
        })
        return prof_dict


    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            birthdate=data['birthdate'],
            cargo=data['cargo']
        )


class ProfModel:
    FILE_PATH = os.path.join(DATA_DIR, 'profs.json')

    def __init__(self):
        self.profs = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Prof(**item) for item in data]


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.profs], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.profs


    def get_by_id(self, prof_id: int):
        return next((p for p in self.profs if p.id == prof_id), None)


    def add_prof(self, prof: Prof):
        self.profs.append(prof)
        self._save()


    def update_prof(self, updated_prof: Prof):
        for i, prof in enumerate(self.profs):
            if prof.id == updated_prof.id:
                self.profs[i] = updated_prof
                self._save()
                break


    def delete_prof(self, prof_id: int):
        self.profs = [p for p in self.profs if p.id != prof_id]
        self._save()
