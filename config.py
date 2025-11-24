import os
import base64

class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Configurações do servidor
    HOST = 'localhost'
    PORT = 8080
    DEBUG = True
    RELOADER = True

    # Paths
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'views')
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    DATA_PATH = os.path.join(BASE_DIR, 'data')

    # Outras configurações
    SECRET_KEY = 'sua-chave-secreta-aqui'
    BYTES_KEY = base64.urlsafe_b64encode(SECRET_KEY.encode("utf-8").ljust(32)[:32]) 
