import socket
import sys
import re


class Socket:

    def __init__(self):
        self.ip = ""


    def setIP(self, ip):
        set_ip = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')

        try:
            if set_ip.search(ip):
                self.ip = ip

        except:
            print("[!] You did not add any ip")
            exit()

    def getIP(self):
        return self.ip


    def checkPortSocket(self, port):
        ip = self.getIP()

        if ip != None and port != None:
            try:
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print("[*] Port {}: \t Open".format(port))
                else:
                    print("[*] Port {}: \t Closed".format(port))
                sock.close()
            except socket.error as error:
                print(str(error))
                print("[!] Conection error")

        else:
            print("[!] You did not add any port")