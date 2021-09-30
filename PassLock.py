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
        if 'pass' in open('data/entry.psk','r'):
            #<-- New Code write here
            path_dir=open("path_dir",'r')
            screen.ui("login_screen_top")

        else:
            screen.ui('create_login')
            clear()
            open('data/entry.psk','w+').write("pass")

    except IOError:

        #IO_PATH_SECTION

        cprint("Where do I store passwords?",clr)
        path=input("Enter path: ")
        clear()
        path_dir=open("path_dir","w")
        path_dir.write(f"{path}\passlock")
        path_dir.close()
        os.mkdir(open("path_dir",'r').read())
        Screen().ui('create_login')
        open("data/entry.psk",'w+').write("pass")

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
        cprint("Something went wrong, Try again")
        sleep(1)
        input("press enter to exit")
        os.system("exit()")
        break

