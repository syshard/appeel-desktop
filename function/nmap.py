import socket
from function.system import *

def scan_ports(host):
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            con = s.connect((host, 21))
            return "on"
            con.close()
        except:
            return "off"
