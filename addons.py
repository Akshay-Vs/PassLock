import string
import random
import os
import sys
from random import random,choice
from termcolor import cprint,colored
from time import sleep
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import pyperclip
import msvcrt

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
    symbols=['!','@','#','$','%','&','_','+','?','/']
    source = string.ascii_uppercase + string.ascii_lowercase + string.digits+choice(symbols)
    return ''.join(choice(f"{source},{choice(symbols)}{choice(symbols)}") for x in range(1,maxr))

def initialize(path):
    with open(path,"r") as rnf:
        exec(rnf.read())
        print("No errors found")
        clear()

def password_input(prompt=''):
    p_s = ''
    proxy_string = [' '] * 99
    while True:
        sys.stdout.write('\x0D' + prompt + ''.join(proxy_string))
        c = msvcrt.getch()
        if c == b'\r':
            break
        elif c == b'\x08':
            p_s = p_s[:-1]
            proxy_string[len(p_s)] = " "
        else:
            proxy_string[len(p_s)] = "*"
            p_s += c.decode()

    sys.stdout.write('\n')
    return p_s



if __name__=="__main__":
    password_input("Test password: ")
    print(generate_random_password())
    notify("notification","content")