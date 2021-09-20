from os import DirEntry
import sys
from typing import Dict
try:import posix as os
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
    path_dir=open("path_dir",'r')
    path_dir.close()
    input_key=cprint("Enter Input: ")
except:
    print("Where do I store passwords?")
    #cprint("Be sure to enter an existing path, 1.0 doesn't deals with that issue, FIX: Edit path_dir with a valid path",'yellow')#This will get omitted after a couple of updates.
    path=input("Enter path: ")
    path_dir=open("path_dir","w")
    path_dir.write(f"{path}\passlock")
    path_dir.close()
    os.mkdir(open("path_dir",'r').read())

try:KeyProcess(raw_key=input_key).encrypt_key()
except FileNotFoundError as e:print("path intrupted, Try to open AES-Encrypted-Password-manager folder as home directory\n")
except NameError:initialize(__file__)
except ValueError as e:
    notify("Key Interupted","Something unexpected happened\nRun PassLock code once again",15)
    cprint("Key Interupted, Try again",e)
    os.system("exit()")
except KeyError:
    notify("Key Processing unit crashed","Something unexpected happened\nRun System diagnostics")
    try:initialize()
    except:
        notify("Auto Restart Failed","System initializer almost fixed all isses, but failed to restart. Run PassLock once again")
        os.system("exit()")
except Exception as e:
    print(e)
    os.system("exit()")
