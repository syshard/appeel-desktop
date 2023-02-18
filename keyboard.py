import sys
import subprocess
import time
from function.color import *

print (r+'''  

·▄▄▄      ▄▄▄   ▄▄· ▄▄▄ .▄▄▄▄· ▄▄▄        ▄▄▄▄▄▄▄▄ .
▐▄▄·▪     ▀▄ █·▐█ ▌▪▀▄.▀·▐█ ▀█▪▀▄ █·▪     •██  ▀▄.▀·
██▪  ▄█▀▄ ▐▀▀▄ ██ ▄▄▐▀▀▪▄▐█▀▀█▄▐▀▀▄  ▄█▀▄  ▐█.▪▐▀▀▪▄
██▌.▐█▌.▐▌▐█•█▌▐███▌▐█▄▄▌██▄▪▐█▐█•█▌▐█▌.▐▌ ▐█▌·▐█▄▄▌
▀▀▀  ▀█▄▀▪.▀  ▀·▀▀▀  ▀▀▀ ·▀▀▀▀ .▀  ▀ ▀█▄▀▪ ▀▀▀  ▀▀▀ 
                      ░                     ░                                  
'''+w)

def input_text(text):
    for char in text:
        cmd = "cd adb && adb shell input text '{}'".format(char)
        subprocess.run(cmd, shell=True)
        #time.sleep(0.05)

def press_enter():
    cmd = "cd adb && adb shell input keyevent 66"
    subprocess.run(cmd, shell=True)

def write_to_screen(wordlist_file):
    with open(wordlist_file, "r") as file:
        wordlist = file.readlines()

    line_counter = 0
    Count = 0
    for word in wordlist:
        print('[',b,Count,w,'] Typing: ['+d+ word.strip() +w+']')
        input_text(word.strip())
        press_enter()
        line_counter += 1
        Count+=1
        if line_counter == 3:
            print("\n "+d+"Waiting for 30 seconds \n"+w)  # Display the waiting message on the PC screen
            time.sleep(30)
            line_counter = 0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        write_to_screen(sys.argv[1])
    else:
        print("Please specify the file path as an argument.")
