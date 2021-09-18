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
    path_dir.write(path)
    path_dir.close()

try:KeyProcess(raw_key=input_key).encrypt_key()
except FileNotFoundError as e:print("path intrupted, Try to open AES-Encrypted-Password-manager folder as home directory\n")
except NameError:initialize(__file__)
except ValueError or KeyError as e:
    cprint("Key Interupted, Try again",e)
    os.system("exit()")
except Exception:
    try:
        cprint("Something went wrong\nTrying Auto-restart")
        sleep(1)
        initialize(__file__)
    except:
        cprint("kill current terminal and run this again\n",'yellow')
  
