import eel	
import os
import subprocess

from playsound import playsound

from function.system import *
from function.ftpServer import *
from function.nmap import *
from function.header import *


header()

criarAtalhoArquivos()
print("[servidor] Todas as ferramentas online")
print("[Info] Aguardando requisicoes...")


eel.init('web')                     


#playsound("./audio/audio.mp3")

@eel.expose
def startFtp(user,password):
	print(b+'\n['+Meuip('local')+']'+w+' Iniciando servidor: ftp://'+Meuip('local')+':21')
	subprocess.Popen(['x-terminal-emulator', '-e', 'python3 ftp.py '+user+' '+password+' '+os.path.expanduser('~')])

@eel.expose
def displayDevices():
	print(b+'\n['+Meuip('local')+']'+w+' Espelhando tela do celular')
	subprocess.Popen(['x-terminal-emulator', '-e', 'python3 devices.py'])		

@eel.expose
def closeFtp():
	print(b+'\n['+Meuip('local')+']'+w+' Servidor ftp feichado!')
	Ftpclose()

@eel.expose
def startdevices(ip):
	wificonnect(ip)
	return check_adb_device()

@eel.expose
def verficar():
	return check_adb_device()

@eel.expose
def Verif_FTP():
	return scan_ports(Meuip("local"))

@eel.expose
def adbpull():
	print(b+'\n['+Meuip('local')+']'+w+' Copiando imagens do celular')
	subprocess.Popen(['x-terminal-emulator', '-e', 'python3 adbpull.py'])	

@eel.expose
def reboot():
	print(b+'\n['+Meuip('local')+']'+w+' :( Reinicando celular ...')
	subprocess.Popen(['x-terminal-emulator', '-e', 'python3 reboot.py'])

@eel.expose
def keyboard(digitos):
	print(b+'\n['+Meuip('local')+']'+w+' Teclado digital iniciado: '+digitos)
	if digitos == "0":
		subprocess.Popen(['x-terminal-emulator', '-e', 'python3 keyboard.py ./wordlist/outros.txt'])	
	if digitos == "4":
		subprocess.Popen(['x-terminal-emulator', '-e', 'python3 keyboard.py ./wordlist/4digit.txt'])	
	if digitos == "6":
		subprocess.Popen(['x-terminal-emulator', '-e', 'python3 keyboard.py ./wordlist/6digit.txt'])	

@eel.expose
def apkinstaller(app):
	print(b+'\n['+Meuip('local')+']'+w+' Instalando o app '+app)
	subprocess.Popen(['x-terminal-emulator', '-e', 'python3 apkinstaller.py ./Apk/'+app+'.apk'])	

@eel.expose
def beckup():
	print(b+'\n['+Meuip('local')+']'+w+' Criando uma copia do sistema do celular')
	subprocess.Popen(['x-terminal-emulator', '-e', 'python3 beckup.py'])

eel.pythonSay("Servidor python conectado")

eel.ipLocal(Meuip("local"))    

eel.username(os.getlogin())


if Internet():
	eel.internet("online")
else:
	eel.internet("offline")     

eel.start('app.html', size=(800, 500))