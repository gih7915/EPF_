from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.prof_controller import prof_routes
from controllers.login_controller import login_routes
from controllers.aluno_controller import aluno_routes
from controllers.disciplina_controller import disciplina_routes

def init_controllers(app: Bottle):
    app.merge(login_routes)
    app.merge(user_routes)
    app.merge(prof_routes)
    app.merge(aluno_routes)
    app.merge(disciplina_routes)
