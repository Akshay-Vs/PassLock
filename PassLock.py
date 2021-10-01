import sys
clr='blue'
for i in range(3):#autofix with 3 iterations
    try:
        import os
        from addons import *
        from process import *

    except ModuleNotFoundError:
        if os.name=='posix':import posix as os
        print("\n\nInstalling requirements\nPlease wait.... \n")
        if 'termcolor' not in sys.modules:
            os.system('pip3 install termcolor')
        if 'pyperclip' not in sys.modules:
            os.system('pip3 install pyperclip')
        if 'Crypto' not in sys.modules:
            os.system('pip3 install Crypto')

while True:

    try:
        screen=Screen()
        try:
            entry=open('data/entry.psk','r')
            path_dir=open('data/path_dir','r')
        except FileNotFoundError:
            entry=open('data/entry.psk','w+')
            path_dir=open('data/path_dir','w+')
        if 'pass' in entry:
                                #<-- New Code write here
            path_dir=open("data/path_dir",'r')
            if screen.ui('master_password_screen') == 'proceed_to_login_screen':
                clear()
                key=screen.ui("login_screen")
                while True:
                    clear()
                    screen.ui('home_screen')
                    cprint('Enter Input',clr,attrs=['bold'])
                    input('\t\t\t : ')
                
            else:break
        else:
            screen.ui('create_login')
            cprint("Where do I store passwords?",clr)
            path=input("Enter path: ")
            path_dir.write(path)
            path_dir.close()
            entry.write('pass')
            entry.close()
            clear()
            
    except KeyError:cprint("Key Interupted, Try again",'red')
    
    except OSError as e:
        cprint(f"Error: {e} occured",'red')
        notify("Error Occured","Something went wrong that can't be fixed automatically")
        input("press enter to exit")
        os.system("exit()")
        break

    except ValueError as e:
        cprint(f"Value Error Occured: {e}, Try again",'red')
        input("press enter to exit")
        break

    except Exception:
        cprint("Something went wrong,Please Try again",'red',attrs=['bold'])
        sleep(1)
        input("press enter to exit")
        os.system("exit()")
        break

