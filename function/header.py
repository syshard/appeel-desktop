import os
import sys
import subprocess
from function.system import *



r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[0m"

Ip=Meuip('local')

def header():
    os.system('clear')
    print (g+"                        dP "+b+"                   oo                             "+w)
    print (g+"                        88 "+b+"                                                  "+w)
    print (g+" .d8888b. 88d888b. .d888b88"+b+" .d8888b. dP   .dP dP .d8888b. .d8888b. .d8888b.  "+w)
    print (g+" 88'  `88 88'  `88 88'  `88"+b+" 88ooood8 88   d8' 88 88'  `"" 88ooood8 Y8ooooo.  "+w) 
    print (g+" 88.  .88 88    88 88.  .88"+b+" 88.  ... 88 .88'  88 88.  ... 88.  ...       88  "+w) 
    print (g+" `88888P8 dP    dP `88888P8"+b+" `88888P' 8888P'   dP `88888P' `88888P' `88888P'  "+w) 
    print ("")


