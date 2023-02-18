import sys
from function.system import *
from function.ftpServer import *

print ('''
·▄▄▄▄▄▄▄▄ ▄▄▄·.▄▄ · ▄▄▄ .▄▄▄   ▌ ▐·▄▄▄ .▄▄▄  
▐▄▄·•██  ▐█ ▄█▐█ ▀. ▀▄.▀·▀▄ █·▪█·█▌▀▄.▀·▀▄ █·
██▪  ▐█.▪ ██▀·▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ 
██▌. ▐█▌·▐█▪·•▐█▄▪▐█▐█▄▄▌▐█•█▌ ███ ▐█▄▄▌▐█•█▌
▀▀▀  ▀▀▀ .▀    ▀▀▀▀  ▀▀▀ .▀  ▀. ▀   ▀▀▀ .▀  ▀

''')
startFTP(sys.argv[1],sys.argv[2],sys.argv[3])