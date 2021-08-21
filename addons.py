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

def typing(text: str,color="yellow",typing_speed=50):
    for character in text:
        sys.stdout.write(colored(character,color))
        sys.stdout.flush()
        sleep(random() * 10.0 / typing_speed )

def clear():
   if os.name=='posix':_=os.system('clear')
   else:_=os.system('cls')

def generate_random_password():
    symbols=['!','@','#','$','%','&','_','+','?','/']
    source = string.ascii_uppercase + string.ascii_lowercase + string.digits+choice(symbols)
    return ''.join(choice(f"{source},{choice(symbols)}{choice(symbols)}") for x in range(1,40))

if __name__=="__main__":
    print(generate_random_password())