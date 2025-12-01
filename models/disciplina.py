import json
import os
from typing import Optional, List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


class Disciplina:
    """Classe Disciplina para gerenciar as disciplinas oferecidas.
    
    Atributos:
    - codigo: código da disciplina (ex: FGA0003)
    - nome: nome da disciplina
    - turma: número da turma (ex: 01, 02)
    - ano_periodo: período letivo (ex: 2025.2)
    - docente: professor responsável
    - carga_horaria: carga horária total
    - horario: horário das aulas
    - vagas_ofertadas: total de vagas
    - vagas_ocupadas: vagas já preenchidas
    - local: sala/laboratório
    - senha: senha para matrícula (código de acesso)
    - alunos_matriculados: lista de IDs dos alunos matriculados
    """

    def __init__(
        self,
        id: int,
        codigo: str,
        nome: str,
        turma: str,
        ano_periodo: str,
        docente_id: Optional[int],
        carga_horaria: str,
        horario: str,
        vagas_ofertadas: int,
        vagas_ocupadas: int,
        local: str,
        senha: str,
        alunos_matriculados: Optional[List[int]] = None
    ):
        self.id = id
        self.codigo = codigo
        self.nome = nome
        self.turma = turma
        self.ano_periodo = ano_periodo
        self.docente_id = docente_id
        self.carga_horaria = carga_horaria
        self.horario = horario
        self.vagas_ofertadas = vagas_ofertadas
        self.vagas_ocupadas = vagas_ocupadas
        self.local = local
        self.senha = senha
        self.alunos_matriculados = alunos_matriculados or []

    def __repr__(self):
        return f"Disciplina(codigo='{self.codigo}', nome='{self.nome}', turma='{self.turma}')"

    def to_dict(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'nome': self.nome,
            'turma': self.turma,
            'ano_periodo': self.ano_periodo,
            'docente_id': self.docente_id,
            'carga_horaria': self.carga_horaria,
            'horario': self.horario,
            'vagas_ofertadas': self.vagas_ofertadas,
            'vagas_ocupadas': self.vagas_ocupadas,
            'local': self.local,
            'senha': self.senha,
            'alunos_matriculados': self.alunos_matriculados
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            codigo=data['codigo'],
            nome=data['nome'],
            turma=data['turma'],
            ano_periodo=data['ano_periodo'],
            docente_id=data.get('docente_id'),
            carga_horaria=data['carga_horaria'],
            horario=data['horario'],
            vagas_ofertadas=data['vagas_ofertadas'],
            vagas_ocupadas=data['vagas_ocupadas'],
            local=data['local'],
            senha=data['senha'],
            alunos_matriculados=data.get('alunos_matriculados', [])
        )

    def tem_vagas(self):
        """Verifica se ainda há vagas disponíveis."""
        return self.vagas_ocupadas < self.vagas_ofertadas

    def matricular_aluno(self, aluno_id: int):
        """Matricula um aluno na disciplina."""
        if not self.tem_vagas():
            raise Exception("Não há vagas disponíveis")
        if aluno_id in self.alunos_matriculados:
            raise Exception("Aluno já matriculado nesta disciplina")
        self.alunos_matriculados.append(aluno_id)
        self.vagas_ocupadas += 1

    def desmatricular_aluno(self, aluno_id: int):
        """Remove um aluno da disciplina."""
        if aluno_id not in self.alunos_matriculados:
            raise Exception("Aluno não está matriculado nesta disciplina")
        self.alunos_matriculados.remove(aluno_id)
        self.vagas_ocupadas -= 1


class DisciplinaModel:
    FILE_PATH = os.path.join(DATA_DIR, 'disciplinas.json')

    def __init__(self):
        self.disciplinas = self._load()
        # vínculo de disciplinas ao professor pode ser feito em services/controllers

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Disciplina.from_dict(d) for d in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([d.to_dict() for d in self.disciplinas], f, ensure_ascii=False, indent=2)

    def get_all(self):
        return self.disciplinas

    def get_by_id(self, disciplina_id: int):
        for disciplina in self.disciplinas:
            if disciplina.id == disciplina_id:
                return disciplina
        return None

    def search(self, query: str):
        """Busca disciplinas por código ou nome."""
        query_lower = query.lower()
        return [d for d in self.disciplinas 
                if query_lower in d.codigo.lower() or query_lower in d.nome.lower()]

    def add(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)
        self._save()

    def update(self, disciplina: Disciplina):
        for i, d in enumerate(self.disciplinas):
            if d.id == disciplina.id:
                self.disciplinas[i] = disciplina
                self._save()
                return True
        return False

    def delete(self, disciplina_id: int):
        self.disciplinas = [d for d in self.disciplinas if d.id != disciplina_id]
        self._save()
