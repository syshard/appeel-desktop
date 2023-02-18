import sys
import subprocess
from function.color import *
from tqdm import tqdm

print (g+'''
    
▪   ▐ ▄ .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▌   ▄▄▄· ·▄▄▄▄        ▄▄▄  
██ •█▌▐█▐█ ▀. •██  ▐█ ▀█ ██•  ▐█ ▀█ ██▪ ██ ▪     ▀▄ █·
▐█·▐█▐▐▌▄▀▀▀█▄ ▐█.▪▄█▀▀█ ██▪  ▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄ 
▐█▌██▐█▌▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▌▐▌▐█ ▪▐▌██. ██ ▐█▌.▐▌▐█•█▌
▀▀▀▀▀ █▪ ▀▀▀▀  ▀▀▀  ▀  ▀ .▀▀▀  ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀

'''+w)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        apk_path = sys.argv[1]
        install_command = "cd adb && adb install " + apk_path
        print('Instalando '+apk_path)
        process = subprocess.Popen(install_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        for line in tqdm(iter(process.stdout.readline, b''), desc='Installing APK', unit=' lines'):
            pass
    else:
        print("Please specify the APK file path as an argument.")
