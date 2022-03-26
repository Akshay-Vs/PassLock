import string
import base64
import hashlib
import json
import msvcrt
import shutil
import sys
import time
import zipfile
import help
import pyperclip

from Crypto import Random
from Crypto.Cipher import AES
from termcolor import colored, cprint
from random import choice, random
from time import sleep

try:import posix as os
except:import os

class Theme:

    def __init__(self,path):
        self.path = path
        self.fetch()

    def fetch(self):
        with open(self.path,'r') as f:
            data_read=json.loads(f.read())


        #colors
        
        self.color_primary = data_read["color_primary"]
        self.color_secondary = data_read["color_secondary"]
        self.color_error = data_read["color_error"]
        self.color_logo = data_read["color_logo"]
        self.color_divider = data_read["color_divider"]
        self.color_bg = data_read["color_bg"]
        self.color_warn = data_read["color_warn"]

        #attributes
        self.primary = data_read["primary"]
        self.error = data_read["error"]
        self.logo = data_read["logo"]
        self.divider = data_read["divider"]

        #render
        self.speed = data_read["speed"]
        self.size = data_read["size"]
        self.placeholder = data_read["password_placeholder"]
        self.max_index = data_read["max_index"]

    def refresh():
        pass

theme=Theme("data\\user_data\\themes\\default.json")

password_placeholder = theme.placeholder
max_index=theme.max_index
warn=theme.color_warn
error=theme.color_error
primary_color=theme.color_primary
secondary=theme.color_secondary


if os.name=='posix':pass
else:from notify import notify
def typing(text: str,color="yellow",typing_speed=50):
    for character in text:
        sys.stdout.write(colored(character,color))
        sys.stdout.flush()
        sleep(random() * 10.0 / typing_speed )

def clear():
   if os.name=='posix':_=os.system('clear')
   else:_=os.system('cls')

def generate_random_password(maxr=40):
    symbols=['!','@','#','$','%','&','_','+','?','/','*',"'",'"']
    source = string.ascii_uppercase + string.ascii_lowercase + string.digits+choice(symbols)
    return ''.join(choice(f"{source},{choice(symbols)}{choice(symbols)}") for x in range(1,maxr))

def initialize(path):
    with open(path,"r") as rnf:
        exec(rnf.read())
        clear()

def password_input(prompt=''):
    p_s = ''
    proxy_string = [' '] * max_index
    while True:
        sys.stdout.write('\x0D' + prompt + ''.join(proxy_string))
        c = msvcrt.getch()
        if c == b'\r':break
        elif c == b'\x08':
            p_s = p_s[:-1]
            proxy_string[len(p_s)] = " "
        else:
            proxy_string[len(p_s)] = password_placeholder
            p_s += c.decode()

    sys.stdout.write('\n')
    return p_s

def compress(files,archive,password):
    with zipfile.ZipFile(archive, "w") as zf:
        for file in files:
            zf.write(file)

        zf.setpassword(password)

    with zipfile.ZipFile(archive, "r") as zf:
        crc_test = zf.testzip()
        if crc_test is not None:
            print(f"Bad CRC or file headers: {crc_test}")

        info = zf.infolist() 

        file = info[0]
        with zf.open(file) as f:
            f.read().decode()


        #zf.extract(file, "/tmp", pwd=password)

if __name__=="__main__":
    clear()
    print('Password: ',password_input("Enter password: "))
    print('Generated Random password (70-bit):',generate_random_password(70))
    print('Generated Random password (Default):',generate_random_password())
    notify("Tite","This is a notification")