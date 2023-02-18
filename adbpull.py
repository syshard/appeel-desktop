import os
from function.color import *

print (b,'''

 ▄▄·        ▄▄▄· ▄· ▄▌·▄▄▄▪  ▄▄▌  ▄▄▄ ..▄▄ · 
▐█ ▌▪▪     ▐█ ▄█▐█▪██▌▐▄▄·██ ██•  ▀▄.▀·▐█ ▀. 
██ ▄▄ ▄█▀▄  ██▀·▐█▌▐█▪██▪ ▐█·██▪  ▐▀▀▪▄▄▀▀▀█▄
▐███▌▐█▌.▐▌▐█▪·• ▐█▀·.██▌.▐█▌▐█▌▐▌▐█▄▄▌▐█▄▪▐█
·▀▀▀  ▀█▄▀▪.▀     ▀ • ▀▀▀ ▀▀▀.▀▀▀  ▀▀▀  ▀▀▀▀ 

''',w)

def copy_screenshots_from_device():
    # Verifica se a pasta arquivos existe, caso contrário, cria
    if not os.path.exists("./arquivos"):
        os.makedirs("./arquivos")

    # Obtém o caminho das capturas de tela no dispositivo
    path_on_device = "/sdcard/Pictures/"
    # Copia as capturas de tela para a pasta arquivos no PC
    os.system(f"adb pull {path_on_device} ./arquivos")

    # Obtém o caminho das capturas de tela no dispositivo
    path_on_device = "/sdcard/DCIM/"
    # Copia as capturas de tela para a pasta arquivos no PC
    os.system(f"cd adb && adb pull {path_on_device} ./arquivos")

# Executa a função de copiar capturas de tela
copy_screenshots_from_device()
