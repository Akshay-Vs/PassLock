from hashlib import new
import sys

for i in range(3):
    try:
        import os
        import help
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


def passlock(user_choice):

    if user_choice =='new':
        clear()
        screen.ui('create_new')

    elif 'show' in user_choice:
        clear()
        id_name=user_choice.replace("show ","")
        id_name=id_name.replace(" ","_")
        try:screen.ui('show_screen',option=id_name)
        except FileNotFoundError:
            if id_name=='show':
                cprint('Error: Identification expected',error)
                cprint('Please provide Identification name eg: show name','yellow')
                cprint('Press Enter to continue',secondary)
                input()
            
            else:
                cprint('Error: Invalid ID name',error)
                cprint('File not found, Enter another id','yellow')
                cprint('Press Enter to continue',secondary)
                input()

    elif user_choice=="list":
        dirs=os.listdir(open('data/path_dir','r').read())
        cprint('\n\n\t\t\t\tList of saved passwords\n',secondary,attrs=['bold'])
        for x in dirs:cprint(f'\t\t\t\t\t{x}',secondary,attrs=['bold'])
        input()

    elif user_choice=="move":
        old_path=open("data/path_dir",'r').read()
        cprint("\tEnter destination path: ",secondary,attrs=['bold'])
        destination_path=input('\t\t\t: ')
        shutil.move(old_path,destination_path)
        cprint("\tDo you want to set new path as default?[y/n]: ",secondary,attrs=['bold'])
        set_default=input('\t\t\t: ')
        if set_default == "y" or "Y":
            open("path_dir",'w').write(destination_path)
            cprint("\tFiles moved successfully",secondary,attrs=['bold'])
            sleep(1.748)
        else:
            os.mkdir(path_dir.read())
            cprint("\tFiles moved successfully",'yellow',attrs=['bold'])
            sleep(1.748)

    elif user_choice=='mkrec':
        cprint("This feature is not available at the moment",error,attrs=["bold"])
        sleep(1.748)
        '''cprint("\tEnter a name for recovery point",secondary,attrs=["bold"])
        name=input("\t\t\t: ")
        cprint("\tEnter a folder path to save recovery point",secondary,attrs=['bold'])
        recovery_path=input("\t\t\t: ")
        compress(f"{recovery_path}",f'{name}.rec','passlock')'''

    elif 'del' in user_choice:
        if user_choice !="--del" or "--del ":                      
            user_choice=user_choice.replace("--del ","")
            user_choice=user_choice.replace(" ","_")
            cprint("\tEnter Master password",secondary,attrs=['bold'])
            raw_password= password_input("\t\t\t: ")
            master_password=KeyProcess().decrypt(raw_password,'lib/ekey.psk')
            trash_file=f"{path_dir.read()}/{user_choice}"

            if master_password==raw_password:
                try:
                    os.remove(f"{trash_file}/iterables")
                    os.remove(f"{trash_file}/password.psl")
                    os.remove(f"{trash_file}/readables.json")
                    os.rmdir(trash_file)
                    cprint(f"\t{user_choice} deleted successfully",secondary,attrs=['bold'])
                    sleep(1.748)
                except FileNotFoundError:
                    cprint("\tFile not found, Skipping Process",error,attrs=['bold'])
                    sleep(1.748)
                except OSError:
                    cprint(f"\tError: Foreign files found in {user_choice}",error,attrs=['bold'])
                    sleep(1.748)
            else:
                cprint("\tInvalid password, Skipping process",error,attrs=['bold'])

        else:
            cprint("\tInvalid Input: Expected identification name after command",error,attrs=['bold'])
            sleep(1.748)

    elif "set path".lower() in user_choice:
        new_path=user_choice.replace("set path ","")
        open('data\path_dir','w+').write(f"{new_path}\Passlock")
        try:
            os.mkdir(f'{new_path}\Passlock')
            cprint("\tpath changed successfully",secondary,attrs=['bold'])
            sleep(0.83)
        except FileExistsError:
            cprint("\tpath changed successfully",secondary,attrs=['bold'])
            sleep(0.83)
        except Exception:
            cprint("\tSomething went wrong",error,attrs=['bold'])
            sleep(1.748)
    
    elif "restart with " in user_choice:
        user_choice=user_choice.replace("restart with ","")
        #print(user_choice)
        screen.ui("restart_with",option=user_choice)

    elif user_choice=='help':
        help.help()

    elif user_choice=='exit':
        screen.ui("end_screen")
        notify("You are protected","Thanks for using PassLock")
        sys.exit()

    else:
        cprint('\n\t\t\t⚠ Invalid Input\n',error,attrs=['bold'])
        sleep(1.748)
            
            
while True:

    try:
        screen=Screen()
        try:
            entry=open('data/entry.psk','r+')
            path_dir=open('data/path_dir','r+')
        except FileNotFoundError:
            entry=open('data/entry.psk','w+')
            path_dir=open("data/path_dir","w+")
            
        if 'pass' in entry:
            path_dir=open("data/path_dir",'r+')

            if screen.ui('master_password_screen') == 'proceed_to_login_screen':
                clear()
                key=screen.ui("login_screen")
                clear()
                print('\n\n\n\n')
                typing('\t\t\tloading...\t\t\t',secondary)
                while True:    
                    clear()
                    screen.ui('home_screen')
                    cprint('\t\t\bEnter Input',secondary,attrs=['bold'])
                    user_choice=str(input('\t\t\t : ')).lower()

                    passlock(user_choice) #commands -> passlock() --> none
            else:break

        else:
            cprint("Enter a folder location to store passwords",secondary)
            path=input("Enter path: ")
            for i in range(3):
                try:
                    if not path:
                        path=__file__
                        print(path)
                        path=path.replace("\PassLock.py","")
                        print(path)
                        try:os.mkdir(f"{path}\passlock")
                        except:pass
                        path_dir.write(f"{path}\passlock")
                        break
                    open('data/path_dir','w+').write(f'{path}/Passlock')
                    os.mkdir(f'{path}\Passlock')
                except FileExistsError as e:
                    cprint(f'{e}; Skipping path exists','yellow')
            clear()
            path_dir.close()
            screen.ui('create_login')
            entry.write('pass')
            entry.close()
            clear()
        
            
    except KeyError:cprint("Key Interupted, Try again",error)
    
    except FileNotFoundError as e:
        cprint(f'Files Missing: {e} Occured',error,attrs=['bold'])
        notify('\tCritical','Mission files or Broken files were found',5)

        user_choice=input("Enter recovery commands: ")
        passlock(user_choice)

        if not user_choice:
            notify('report us',"feel free to report this issue")
            break
        sleep(2)
         
    except FileExistsError:
        cprint("\tFile Exist Error occured",'yellow')
        sleep(1.23)
    except OSError as e:
        cprint(f"\tError: {e} error occured",error)
        notify("\tError Occured","Something went wrong that can't be fixed automatically")
        input("\tpress enter to exit")
        sys.exit()

    except ValueError as e:
        cprint(f"\tValue Error Occured: {e}, Try again",error)
        cprint("\n\tpress enter to restart",secondary,attrs=['bold'])
        input()

    except Exception:
        cprint("Something went wrong,Please Try again",error,attrs=['bold'])
        sleep(1)
        input("press enter to exit")
        sys.exit()
        
