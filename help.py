from addons import *
def help():
    clear()
    cprint("""\tCommands\n\n'new' to create new password\n'show' to show saved passwords\n\n--del to delete password\n--move to move passwords from default folder\n--copy to copy saved passwords\n--mkrec to save current state\n--p to change directory path\n--list to list all password IDs\n--Exit to exit console\n-c to copy password to clipboard\n--r n to generate a random password with n length, eg: --r (50) will generate a 40 bit long password.Default is 40""","cyan",attrs=["bold"])
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