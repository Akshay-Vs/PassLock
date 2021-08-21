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
	cprint("Default path is not readable, Please create a new path",'yellow')
	path_dir=root.write(input("Enter path to the directory to save passwords: "))
try:key_process().encrypt_key()
except Exception as e:cprint(f"{e} restart requered\n",'red')