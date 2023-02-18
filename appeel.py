from function.header import *

if len(sys.argv) > 1:
	if sys.argv[1] == "start":
		subprocess.run(['python3', 'app.py'])

	else:
		print("Argumento "+sys.argv[1]+" nao encontrado")
else:

	def insert():
		leftstyle=b+"\n["+Ip+"]"
		query =input(leftstyle+ g+" Comando: "+w)
		option(query)

	def help():
		print('''
		Lista de Comandos	Fucao comando
		------------------	----------------
		0. start gui		Inicar app no modo grafico
		1. start ftp		Iniciar servidor ftp
		2. start scrcpy		Espelhar tela no dispositivo
		3. start beckup		Fazer uma copia de seguranca
		4. start reboot 	Reiniciar dispositivo
		5. exit			feichar programa
		
		''')

	def option(command):

		if command == "start gui":
			subprocess.run(['python3', 'app.py'])

		if command == "start scrcpy":
			subprocess.Popen(['x-terminal-emulator', '-e', 'python3 devices.py'])
			insert()

		if command == "start ftp":
			leftstyle=b+"\n[FTP]"
			user =input(leftstyle+ g+" Usuario: "+w)
			password =input(leftstyle+ g+" password: "+w)
			subprocess.Popen(['x-terminal-emulator', '-e', 'python3 ftp.py '+user+' '+password+' '+os.path.expanduser('~')])
			insert()

		if command == "start scrcpy wifi":
			leftstyle=b+"\n[scrcpy]"
			ip =input(leftstyle+ g+" IP: "+w)
			os.system('adb tcpip 5555 && adb connect '+ip)
			os.system('adb devices')
			insert()

		if command =="start beckup":
			subprocess.Popen(['x-terminal-emulator', '-e', 'python3 beckup.py'])
			insert()

		if command == "help":
			help()
			insert()

		if command == "exit":
			os.system("exit")

		else:
			os.system(command)
			insert()


	header()
	insert()
