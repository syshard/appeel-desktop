## Importando
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from function.system import *

def startFTP(user, senha, caminho):
    ## Criando o gerenciador de conexões
    authorizer = DummyAuthorizer()
    authorizer.add_user(user, senha, caminho, perm="elradfmwMT")

    ## Criando o manipulador
    handler = FTPHandler
    handler.authorizer = authorizer

    print("[USER] "+user)
    print("[PASS] "+senha)
    print("[FOLDER] "+caminho)

    ## Criando o server
    with FTPServer((Meuip("local"), 21), handler) as server:
        server.max_cons = 5
        server.max_cons_per_ip = 2
        server.serve_forever()