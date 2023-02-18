import os

print ('''

▄▄▄▄· ▄▄▄ . ▄▄· ▄ •▄ ▄• ▄▌ ▄▄▄·
▐█ ▀█▪▀▄.▀·▐█ ▌▪█▌▄▌▪█▪██▌▐█ ▄█
▐█▀▀█▄▐▀▀▪▄██ ▄▄▐▀▀▄·█▌▐█▌ ██▀·
██▄▪▐█▐█▄▄▌▐███▌▐█.█▌▐█▄█▌▐█▪·•
·▀▀▀▀  ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀   

''')

def backup_android():
    backup_dir = "./backup"
    os.makedirs(backup_dir, exist_ok=True)
    os.system(f"cd adb && adb backup -apk -shared -all -f {backup_dir}/backup.ab")

if __name__ == "__main__":
    backup_android()
