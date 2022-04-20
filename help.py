from addons import *
def help():
    clear()
    cprint("""\tCommands\n\n'new' to create new password\n'show' to show saved passwords\n\ndel to delete password\nmove to move passwords from default folder\ncopy to copy saved passwords\nmkrec to save current state\np to change directory path\nlist to list all password IDs\nExit to exit console\n-c to copy password to clipboard\nr n to generate a random password with n length, eg: r (50) will generate a 40 bit long password.Default is 40""","cyan",attrs=["bold"])
    typing('''\nRecomended way to store passwords 
    path(C:\directory\data)
               |
               |-directory
                    |
                    |-data
                    |   |-id_name
                    |   |    |-encrypted_password(1IwYSXyl...wCy=)
                    |     
                    |-lib
                    |  |-ekey''',typing_speed=150)
    cprint("\n\Passlock password manager\n\nversion 2.0\nEncryption: Advanced Encryption Standard (AES)\nDeveloper: Akshay Vs\n\tgithub.com/Akshay-Vs/\n\tinstagram.com/__akshay_v5__/",'cyan')

    input()

if __name__=="__main__":
    help()