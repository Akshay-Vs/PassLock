from hashlib import new
import sys
clr='blue'
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
            os.system('pip3 install pycrypto')

while True:

    try:
        screen=Screen()
        try:
            entry=open('data/entry.psk','r+')
            path_dir=open('data/path_dir','r+')
        except FileNotFoundError:
            entry=open('data/entry.psk','w+')
            
        if 'pass' in entry:
            path_dir=open("data/path_dir",'r+')

            if screen.ui('master_password_screen') == 'proceed_to_login_screen':
                clear()
                key=screen.ui("login_screen")
                clear()
                print('\n\n\n\n')
                typing('\t\t\tloading...\t\t\t',clr)
                while True:    
                    clear()
                    screen.ui('home_screen')
                    cprint('\t\t\bEnter Input',clr,attrs=['bold'])
                    user_choice=str(input('\t\t\t : '))

                    if user_choice =='new':
                        clear()
                        screen.ui('create_new')

                    elif 'show' in user_choice:
                        clear()
                        id_name=user_choice.replace("show ","")
                        id_name=id_name.replace(" ","_")
                        #print(type(splitted_choice),splitted_choice)
                        #input()
                        try:screen.ui('show_screen',show=id_name)
                        except FileNotFoundError:
                            if id_name=='show':
                                cprint('Error: Identification expected','red')
                                cprint('Please provide Identification name eg: show name','yellow')
                                cprint('Press Enter to continue',clr)
                                input()
                            
                            else:
                                cprint('Error: Invalid ID name','red')
                                cprint('File not found, Enter a different id','yellow')
                                cprint('Press Enter to continue',clr)
                                input()

                    elif user_choice=="--list":
                        dirs=os.listdir(open('data/path_dir','r').read())
                        cprint('\n\n\t\t\t\tList of saved passwords\n',clr,attrs=['bold'])
                        for x in dirs:cprint(f'\t\t\t\t\t{x}',clr,attrs=['bold'])
                        input()

                    elif user_choice=="--move":
                        old_path=open("data/path_dir",'r').read()
                        cprint("\tEnter destination path: ",clr,attrs=['bold'])
                        destination_path=input('\t\t\t: ')
                        shutil.move(old_path,destination_path)
                        cprint("\tDo you want to set new path as default?[y/n]: ",clr,attrs=['bold'])
                        set_default=input('\t\t\t: ')
                        if set_default == "y" or "Y":
                            open("path_dir",'w').write(destination_path)
                            cprint("Files moved successfully",clr,attrs=['bold'])
                            sleep(1.748)
                        else:
                            os.mkdir(path_dir.read())
                            cprint("Files moved successfully",'yellow',attrs=['bold'])
                            sleep(1.748)

                    elif user_choice=='--help':
                        help.help()

                    elif user_choice=='--Exit':
                        screen.ui("end_screen")
                        notify("You are protected","Thanks for using PassLock")
                        sys.exit()

                    else:
                        cprint('\n\t\t\t⚠ Invalid Input\n','red',attrs=['bold'])
                        sleep(1.748)
        
                    ##########################################################
            else:break

        else:
            cprint("Where do I store passwords?",clr)
            path=input("Enter path: ")
            for i in range(3):
                try:
                    open('data/path_dir','w+').write(f'{path}/Passlock')
                    os.mkdir(f'{path}/Passlock')
                except FileExistsError as e:
                    cprint(f'{e}; Skipping path exists','yellow')
            clear()
            path_dir.close()
            screen.ui('create_login')
            entry.write('pass')
            entry.close()
            clear()
            
    except KeyError:cprint("Key Interupted, Try again",'red')
    
    except FileNotFoundError as e:
        cprint(f'Files Missing: {e} Occured\nMake sure to make a recovery point next time','red',attrs=['bold'])
        cprint('Please wait...','yellow')
        notify('\tCritical','Some Files Found Missing\nUse -r-rec command to read your recovery point',5)

        rec=input("Enter path to recovery point: ")
        if not rec:
            notify('report us',"feel free to report this issue")
            break
        sleep(2)
        

    except FileExistsError:
        cprint("File Exist Error occured",'yellow')
        sleep(1.23)
    except OSError as e:
        cprint(f"Error: {e} error occured",'red')
        notify("Error Occured","Something went wrong that can't be fixed automatically")
        input("press enter to exit")
        sys.exit()

    except ValueError as e:
        cprint(f"Value Error Occured: {e}, Try again",'red')
        cprint("\npress enter to restart",clr,attrs=['bold'])
        input()
        

    except Exception:
        cprint("Something went wrong,Please Try again",'red',attrs=['bold'])
        sleep(1)
        input("press enter to exit")
        sys.exit()
        
