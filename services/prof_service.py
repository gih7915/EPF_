from bottle import request
from models.prof import ProfModel, Prof

class ProfService:
    def __init__(self):
        self.prof_model = ProfModel()


    def get_all(self):
        profs = self.prof_model.get_all()
        return profs


    def save(self):
        last_id = max([p.id for p in self.prof_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        cargo = request.forms.get('cargo')

        prof = Prof(id=new_id, name=name, email=email, birthdate=birthdate, cargo=cargo)
        self.prof_model.add_prof(prof)


    def get_by_id(self, prof_id):
        return self.prof_model.get_by_id(prof_id)


    def edit_prof(self, prof):
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        cargo = request.forms.get('cargo')

        prof.name = name
        prof.email = email
        prof.birthdate = birthdate
        prof.cargo = cargo

        self.prof_model.update_prof(prof)


    def delete_prof(self, prof_id):
        self.prof_model.delete_prof(prof_id)
