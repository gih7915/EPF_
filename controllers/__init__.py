from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.prof_controller import prof_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(prof_routes)
