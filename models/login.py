import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Login():
    def __init__(self, entidade):
        self.entidade = entidade

class LoginModel():
    def __init__(self):
        pass