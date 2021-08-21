from addons import *
def help():
    clear()
    typing("This password manager encrypts and save your passwords safely using Advanced Encryption Standards\nAn id_name is used to identify passwords, This names are not encrypted and able to see in the defiened directory\n",typing_speed=100)
    cprint(''' 
    path(C:\directory\data)
               |
               |-directory
                    |
                    |-data
                    |   |-id_name
                    |   |    |-encrypted_password(1IwYSXyl...wCy=)
                    |     
                    |-lib
                    |  |-ekey''','green',attrs=['bold'])
    cprint("\n\tcommands",'cyan',attrs=['bold'])
    cprint("'new' to create new password\n'show' to show saved passwords\n'--del' to edit passwords and identification name\n'-c' to copy password to clipboard\n\nleaving passwords blank will geanerete a random password",'cyan',attrs=['bold'])
    typing('\nNOTE:changing/deletion path.b or ekey.b will completly distroy your passwords',typing_speed=75)
    cprint("\tPython password manager\n\nversion 1.0\nEncryption:Advanced Encryption Standard (AES)\nAuthor: Akshay Vs\n\tgithub.com/Akshay-Vs/\n\tinstagram.com/__akshay_v5__/",'cyan')

    input()
