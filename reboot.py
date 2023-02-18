import os

print ('''  

▄▄▄  ▄▄▄ .▄▄▄▄·             ▄▄▄▄▄
▀▄ █·▀▄.▀·▐█ ▀█▪▪     ▪     •██  
▐▀▀▄ ▐▀▀▪▄▐█▀▀█▄ ▄█▀▄  ▄█▀▄  ▐█.▪
▐█•█▌▐█▄▄▌██▄▪▐█▐█▌.▐▌▐█▌.▐▌ ▐█▌·
.▀  ▀ ▀▀▀ ·▀▀▀▀  ▀█▄▀▪ ▀█▄▀▪ ▀▀▀ 
                               
''')

def reboot_to_fastboot():
    os.system("cd adb && adb reboot bootloader")

if __name__ == "__main__":
    reboot_to_fastboot()
