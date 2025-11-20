import json
import os
from models.user import User, DATA_DIR

class Student(User):
    def __init__(self, id, name, email, birthdate, senha, grades=None, attendance=None):
        super().__init__(id, name, email, birthdate, senha)
        self.grades = grades or {}       # ex: {'math': [8.5, 9.0]}
        self.attendance = attendance or {}  # ex: {'2025-03-10': 'present'}

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'grades': self.grades,
            'attendance': self.attendance
        })
        return d

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            birthdate=data['birthdate'],
            senha=data.get('senha'),
            grades=data.get('grades', {}),
            attendance=data.get('attendance', {})
        )

class StudentModel:
    FILE_PATH = os.path.join(DATA_DIR, 'students.json')

    def __init__(self):
        self.students = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Student.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.students

    def get_by_id(self, student_id):
        return next((s for s in self.students if s.id == student_id), None)

    def add_student(self, student):
        self.students.append(student)
        self._save()

    def update_student(self, updated_student):
        for i, s in enumerate(self.students):
            if s.id == updated_student.id:
                self.students[i] = updated_student
                self._save()
                break

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.id != student_id]
        self._save()