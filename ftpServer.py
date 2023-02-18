## Importando
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from function.system import *

def startFTP():
    ## Criando o gerenciador de conexões
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", "/home/walter", perm="elradfmwMT")

    ## Criando o manipulador
    handler = FTPHandler
    handler.authorizer = authorizer

    ## Criando o server
    with FTPServer((Meuip("local"), 21), handler) as server:
        server.max_cons = 5
        server.max_cons_per_ip = 2
        server.serve_forever()