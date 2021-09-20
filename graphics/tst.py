from termcolor import cprint,colored
from os import system
system("cls")
recent1="Google"
recent2="Facebook"
recent3="Twitter"
recent4="Stack"
recent5="System"
recent6="Instagram"
recent7="GitHub"
recent8="IDs"
recent9="Linkedin"

status="Done"
status1="Error"
home_screen=(f'''
                                           _______________________________________________________________
          Commands                        |           ____                  __               __           |
                                          |          / __ \____ ___________/ /   ____  _____/ /__         |
    --help - for further help             |         / /_/ / __ `/ ___/ ___/ /   / __ \/ ___/ //_/         |
    --Exit - to exit                      |        / ____/ /_/ (__  |__  ) /___/ /_/ / /__/ ,<            |
    new    - to create a new password     |       /_/    \__,_/____/____/_____/\____/\___/_/|_|           |
    show   - to show saved password       |                                                               |
                                          |_______________________________________________________________|

   _________________________________________________________________________________________________________
        
     path_dir - E:\Passlock                            Process Monitor      Recent passwords   
     EKEY     - True
                                                        p1-{status}              {recent1}         
                                                        p2-{status}              {recent2}         
                                                        p3-{status1}             {recent3}         
                                                        p4-{status}              {recent4}         
                                                        p5-{status}              {recent5}         
                                                        p6-{status1}             {recent6}         
                                                        p7-{status1}             {recent7}                                 
                                                        p8-{status}              {recent8}                                  
                                                        p9-{status}              {recent9}                                 
''')
cprint(home_screen,"blue",attrs=["bold"])
input(colored("Enter input: ","green"))