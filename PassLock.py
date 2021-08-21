import sys
try:import posix
except:import os
if 'termcolor' not in sys.modules:
    os.system('pip3 install termcolor')
if 'pyperclip' not in sys.modules:
    os.system('pip3 install pyperclip')
if 'Crypto' not in sys.modules:
    os.system('pip3 install Crypto')

from addons import *
from backend import *

clear()
try:
    path_dir=open("path_dir")
    path_dir.close()
except:
    root=open("path_dir",'w+')
    print("Where do I store passwords?")
    cprint("Be sure to enter an existing path, 1.0 doesn't deals with that issue, FIX: Edit path_dir with a valid path",'yellow')#This will get omitted after a couple of updates.
    path_dir=root.write(input("Enter path to the directory: "))
try:key_process().encrypt_key()
except FileNotFoundError as e:print("Invalid file path, Try to open AES-Encrypted-Password-manager folder as home directory\n")
except Exception:cprint(f"Something went wrong restart requered\n",'red')
