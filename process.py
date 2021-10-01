from os import remove
from addons import *
clear()
Master_password=str()

class PasswordManager:

	def __init__(self,id_name,password):
		self.id_name=id_name
		self.password=password
		
	def take_password(self):
		path_dir=open("path_dir","r+").read()
		path = f"{path_dir}\{self.id_name}"#path

		try:
			os.mkdir(path)
			typing("Encrypting...   ");sleep(.5)
			print(f"\nsaving done {path}");sleep(1)
		except Exception as error:
			cprint("Failed to create directory","red")
			cprint(f"could'nt find {path_dir}","yellow")
			print(f"\n{error}")

		#encryption and saving input passwords
		
		try:
			root=open(f"{path}\\password","w+")
			root.write(KeyProcess().encrypt_password(self.password))
		except Exception as e:
			print("Unable to save password\n",e)
			input()

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

class KeyProcess:
	def __init__(self):		
		try:
			self.path_dir=open("data/path_dir","r+").read()
		except:
				self.path_dir=open('data/path_dir','w+').read()
		#self.rootb=open("lib\ekey.psk","rb")
		#self.rootw=open("lib\.nomedia","r+")
		#except FileNotFoundError:
			
			#self.rootw=open("lib\ekey","w+")
			#self.rootb=open("lib\ekey","rb")

			#if self.new_raw_password==self.conferm_password:
			#	new_encrypted_password=AESCipher(self.new_raw_password).encrypt(self.new_raw_password)
			#
			#	t=str(new_encrypted_password)
			#	splited_encrypted_password=(t.split("'")[-2])#splitting encrypted key
			#	self.rootw.write(splited_encrypted_password)#saving encrypted password
			#	os.system("exit()")
			#
			#		
			#else:
			#	self.rootw.close()
			#	try:os.remove(f"{self.path_dir}lib\\ekey")
			#	except PermissionError as error:cprint(f"{error}\nplease manually delete empty 'lib/ekey' otherwise it will cause errors","yellow",attrs=["bold"])
			#	finally:raise ValueError("Passwords doesnt match")#fire value error 
	

			
		

	def encrypt_password(self,raw_password,key):
		aes=AESCipher(key)
		raw_encrypted_password=aes.encrypt(raw_password)
		t=str(raw_encrypted_password)
		splitted_encrypted_password=(t.split("'")[-2])#splitting raw_encrypted_password
		return splitted_encrypted_password
		

	def decrypt_password(self,key,path):
		aes=AESCipher(key)
		#path=open(f"{self.path_dir}\\{id}\\password")
		encrypted_password=open(path).read()#opening encrypted password from root
		decrypted_password=aes.decrypt(encrypted_password)
		if decrypted_password!='':return decrypted_password
		else:return 'Error'

	def reencrypt_password(self,id,password,key):
		aes=AESCipher(key)
		reencrypted_password=aes.encrypt(password)
		root=open(f"{self.path_dir}\\{id}\\password",'w')
		t=str(reencrypted_password)
		splitted_reencrypted_password=(t.split("'")[-2])#splitting raw_encrypted_password
		root.write(splitted_reencrypted_password)

		

class Screen:

	def __init__(self) -> None:
		pass

	def home_elements(self):

		while True:
			clear()
			cprint("\tWelcome To PassLock\n\n--help  for help\n--Exit to exit console\n","green",attrs=["bold"])
			cprint("new  - create new passwords\nshow - show currently saved pasword\n","green",attrs=["bold","blink"])
			user_input=input("Enter input: ")

			if user_input == "--p":
				old_path=open("path_dir","r").read()
				self.new_path=input("Enter new path: ")
				path_dir=open("path_dir","w")
				path_dir.write(self.new_path)
				path_dir.close()
				cprint("Path updated","yellow")
				


			if user_input=="--Exit":
				clear()
				typing("\tThanks for using",'cyan',typing_speed=40)
				pyperclip.copy("Your passwords are protected by passlock")
				notify("Your Passwords are protected","Hold on, We are verifiying your passwords once again\nThanks For Using PassLock")
				clear()
				sleep(0.739)
				os.system("exit()")
				break

			elif user_input=="new":
				id=input("Create an identification name: ")
				mgr_input_password=input(f"Enter {id} password: ")
				if '-r' in mgr_input_password or mgr_input_password=='':
					splited_input=mgr_input_password.split()
					try:value = int(splited_input[1])
					except:
						cprint("Invalid input, Excepted a number after -r. eg: -r 40")
						input("press enter to continue")
					mgr_input_password=generate_random_password(value)
					cprint(f"Generated password: {mgr_input_password}")
					sleep(1)
				elif mgr_input_password=="":
					mgr_input_password=generate_random_password(40)
					cprint(f"Generated password: {mgr_input_password}")

				manager=PasswordManager(id,mgr_input_password)
				manager.take_password()
				sleep(1.792)

				

			elif user_input=="show":
				id=input("Enter identification name: ")
				decrypter=KeyProcess()
				try:
					decrypted_final_password=decrypter.decrypt_password(id)
					typing("Decrypting...  ","cyan")
					clear()
					if decrypted_final_password !='':
						cprint(f'Name: {id}\nPassword: {decrypted_final_password}\n\n\tpress enter to continue, -c to copy',"cyan",attrs=['bold'])
					elif decrypted_final_password=='':
						cprint(f'Name: {id}\nPassword: *******\nYour passwords are kept safe\nTry to enter the correct 	\n\n\tpress enter to continue, -c to copy',"cyan",attrs=['bold'])
					c=input()
					decrypter.reencrypt_password(id,decrypted_final_password)
					if c=="-c":
						if decrypted_final_password !='':
							pyperclip.copy(decrypted_final_password)
						elif decrypted_final_password=='':
							pyperclip.copy("You are using PassLock")
				except FileNotFoundError:
					clear()
					typing("searching...",'cyan',60);sleep(1)
					clear()
					cprint("INVALID IDENTIFICATION NAME","red",attrs=["bold"])
					cprint(f"couldn't find {id}",'yellow',attrs=['bold']);sleep(3)

			elif user_input=="--del":
				id_name=input("Enter identification name: ")
				ver=input(f"Are you sure to delete {id_name}?[y/n]: ")
				if ver=="y":
					try:
						os.remove(f"{KeyProcess().path_dir}\\{id_name}\\password")
						os.rmdir(f"{KeyProcess().path_dir}\\{id_name}")
						cprint(f"Successfully deleted {id_name}",'yellow')
						sleep(1.7)
					except OSError as e:
						cprint(f"No Such directory {e}",'red')
						sleep(1.7)
				else:
					cprint('Skipping process','yellow')
					sleep(1.7)
				
			elif user_input=="--help":
				import help
				help.help()

			elif user_input=="--list":
				dirs=os.listdir(open('data/path_dir','r').read())
				listToStr = ' '.join(map(str, dirs))
				print(listToStr.replace(' ', '\n'))
				input()

			elif user_input=="--move":
				old_path=open("path_dir",'r').read()
				destination_path=input("Enter destination path: ")
				shutil.move(old_path,destination_path)
				set_default=input("Do you want to set new path as default?[y/n]: ")
				if set_default == "y" or "Y":open("path_dir",'w').write(destination_path)
				else:cprint("Files moved successfully")
				
			else:
				cprint("Invalid input","red",attrs=['bold'])
				sleep(2)

	def ui(self,name,clr="green",attr='bold'):
		recent1='Screen'
		recent2="Facebook"
		recent3="Twitter"
		recent4="Stack"
		recent5="System"
		recent6="Instagram"
		recent7="GitHub"
		recent8="IDs"
		recent9="Linkedin"
		lists="n"
		status="Done"
		status1="Error"
		encryption_state="Decrypting"
		method="AES124"
		last_view='12/09/2021'
		created_date="12/09/2021"
		generation_type="Random"
		bitrate='60'
		encoder='Built-In AES124'
		success_preview=2
		failed_preview=0
		self.error_message=''

		id_name="Goolge"
		encrypted_password="wfd43,jkh6rgdf2qsrfd9iuyg8uytr5=c_"
		decrypted_password="Google_password"
		path="E:/Passlock/Google/"

				
		homescreen=(f'''
                                    	             _______________________________________________________________
                        Commands                    |           ____                  __               __           |
                                                    |          / __ \____ ___________/ /   ____  _____/ /__         |
                --help - for further help           |         / /_/ / __ `/ ___/ ___/ /   / __ \/ ___/ //_/         |
                --Exit - to exit                    |        / ____/ /_/ (__  |__  ) /___/ /_/ / /__/ ,<            |
                                                    |       /_/    \__,_/____/____/_____/\____/\___/_/|_|           |
                show   - to show saved password     |                                                               |
                new    - to create a new password   |_______________________________________________________________|
		path_dir -{os}
	_____________________________________________________________________________________________________________
																													
		TRs   -True                                       Process Monitor      Recent passwords                    
		EKEY  -True
															p1-{status}              {recent1}                      
		--list  to list password IDs                        p2-{status}              {recent2}                      
		--r n   to generate n bit password                  p3-{status1}             {recent3}                       
		--p     to change currrent path_dir                 p4-{status}              {recent4}                      
		--move  to move passwords                           p5-{status}              {recent5}                     
		--mkrec to make recovery point                      p6-{status1}             {recent6}                     
															p7-{status1}             {recent7}                               
															p8-{status}              {recent8}                                 
															p9-{status}              {recent9}                      
		
	_______________________________________________________________________________________________________________    
		''')


		################################################################################################################################


		show_screen=(f'''

		{encryption_state}  |  Last View   : {last_view   }  |  Password Type : {generation_type}  |   Success Previews: {success_preview}   | BitRate: {bitrate}
		{method}          |  Created Date: {created_date}  |  Encoder :{encoder } |   Failed Previews : {failed_preview}
	_______________________________________________________________________________________________________________


		Identification Name: {id_name}
		Encrypted Password : {encrypted_password}
		Saved path         : {path}

		Decrypted Password : {decrypted_password}

		-c to copy password to clipboard


		''')

		##############################################################################################################################################

		show_screen_failed_top=(f'''
		Identification Name: {id_name}
		Encrypted Password : {encrypted_password}
		Saved Path         : {path}
		Decrypted Password : *********
	''')
		show_screen_failed_middle=(f'''
         ______________
     ___/Preview failed\___________________________________________________________________________________________________
	|                                                                                                                      |
	|  Invalid_Key: Entered key doesn't seems right. So we safely reencrypted it. To recover, Restart Passlock with right  |
	|  key.                                                                                                                |
	|                                                                                                                      |
	|      Preview state: Failed         |   Preview Time  : {time.ctime()}                                      |
	|      Key state    : Invalid        |   Total Failures: {failed_preview}                                                             |
	|______________________________________________________________________________________________________________________|

		''')

		###############################################################################################################################################

		end_screen=(f'''

                                                 _______________________________________________________________
                Thanks For Using                |           ____                  __               __           |
                                                |          / __ \____ ___________/ /   ____  _____/ /__         |
        Hold On...                          	|         / /_/ / __ `/ ___/ ___/ /   / __ \/ ___/ //_/         |
        Reencrypting Passwords...           	|        / ____/ /_/ (__  |__  ) /___/ /_/ / /__/ ,<            |
                                                |       /_/    \___,/____/____/_____/\____/\___/_/|_|           |
                                                |                                                               |
                                                |_______________________________________________________________|

	Process Time: {time.process_time_ns()}
		''')

		################################################################################################################################################

		login_screen_top=(f"""                               _________________________
______________________________/WELCOME TO PASSLOCK LOGIN\______________________________________________________________

		Enter Login Details to continue

			
		""")

		create_login=(f"""                               _________________________
______________________________/WELCOME TO PASSLOCK LOGIN\______________________________________________________________
		{self.error_message}
		Create a username and private key to continue

			
		""")

		create_new=(f'''

		{encryption_state}  |  Password Type : {generation_type}  |  Created Date: {created_date}  |  Encoder :{encoder }
		{method}           
	_______________________________________________________________________________________________________________

			Enter Requered Fields To Continue

	''')

		master_password_screen=(f'''			       _________________________
______________________________/WELCOME TO PASSLOCK LOGIN\______________________________________________________________
										{time.process_time_ns()} at {time.ctime()}
                                                 _______________________________________________________________
                Welcome Back                    |           ____                  __               __           |
                                                |          / __ \____ ___________/ /   ____  _____/ /__         |
        Please Verify it's you                  |         / /_/ / __ `/ ___/ ___/ /   / __ \/ ___/ //_/         |
    Enter Master password to continue       	|        / ____/ /_/ (__  |__  ) /___/ /_/ / /__/ , <           |
                                                |       /_/    \___,/____/____/_____/\____/\___/_/|_|           |
                                                |                                                               |
                                                |_______________________________________________________________|

	''')

		if name=='login_screen':
			cprint(login_screen_top,color=clr,attrs=[attr])
			cprint("\tEnter username ",color=clr,attrs=[attr])
			username=input("\t\t\t:")								#<<--UPDATE IN NEAR FUTURE
			cprint("\tEnter secret key",color=clr,attrs=[attr])
			self.private_key=password_input('\t\t\t:')
			return self.private_key

			#######<<<<FUTURE USERNAME IMPLEMENTATION WILL COME HERE!>>>>#######



		elif name=='create_login':
			cprint(create_login,color=clr,attrs=[attr])
			cprint('\n\tCreate a username',color=clr,attrs=[attr])
			self.new_username=input("\t\t\t:")
			cprint('\tCreate a password',color=clr,attrs=[attr])
			self.new_password=input("\t\t\t:")
			cprint("\tConfirm password",color=clr,attrs=[attr])
			confirm_password=password_input("\t\t\t:")
			cprint("\tCreate a private key\t\t\t\bNOTE: You can't change private key but can use multiple keys at same time",color=clr,attrs=[attr])
			self.private_key=password_input("\t\t\t: ")
			encrypter=KeyProcess()

			#username section
			os.mkdir('data/users')
			open(f'data/users/{self.new_username}.psu','w+').write(encrypter.encrypt_password(self.new_username,self.new_username))

			#password section
			if self.new_password==confirm_password:
				root=open('lib/ekey.psk','w+')
				encrypt_password=encrypter.encrypt_password(confirm_password,self.new_password)
				root.write(encrypt_password)

			else:
				clear()
				cprint("Passwords doesnt match",'red',attrs=['bold'])
				sleep(1)
				clear()
				self.error_message="Try again"
				Screen().ui('create_login')

		elif name=='create_new':
			cprint(create_new,color=clr,attrs=[attr])
			cprint("Enter Identification name",color=clr,attrs=[attr])
			id=input('\t\t\t: ')
			cprint("Enter Password\t\t\t\t-r to generate random password",color=clr,attrs=[attr])
			raw_password=password_input('\t\t\t: ')
			encrypter=KeyProcess()
			path_dir=open('data/path_dir','w+').read()
			try:
				if '-r' in raw_password or raw_password == '':
					t=str(raw_password)
					r=(t.split(" ")[-1])
					if r =='-r':raw_password=generate_random_password()
					else:raw_password=generate_random_password(int(r))
					typing(f"\nGenerated Password:{raw_password}",'cyan',typing_speed=len(raw_password)/0.045)
					os.mkdir(f'{path_dir}/{id}')
					open(f'{path_dir}/{id}/password.psw','w+').write(encrypted_password)
					

				else:
					encrypted_password=encrypter.encrypt_password(raw_password,'key')
					print(encrypted_password)
					os.mkdir(f'{path_dir}/{id}')
					open(f'{path_dir}/{id}/password.psw','w+').write(encrypted_password)

			except FileExistsError:
				clear()
				cprint(create_new,color=clr,attrs=[attr])
				cprint('ID Exists: Entered id alredy exixts. Please enter another id','red',attrs=[attr])
				cprint("Enter identification name",clr,attrs=[attr])
				id=input('\t\t\t: ')
				os.mkdir(f'{path_dir}/{id}')
				open(f'{path_dir}/{id}/password.psw','w+').write(encrypted_password)
				cprint(f"Saving Done {id} at {path_dir}",'yellow',attrs=['bold'])
				sleep(1.638)

			except ValueError as e:
				error=str(e)
				if 'invalid literal' in error:
					cprint("\nOperation cancelled\nInvalid Literal Found: Entered value doesn't seems correct. Try to enter initializer<space>max_range\n\t\t\teg: -r 20, will generate a 20 bit long password",'red','on_grey',attrs=['bold'])
				else:cprint("\nSomething went wrong, please try again",'red')

			except Exception:cprint("\nSomething went wrong, please try again",'red')

		elif name=='master_password_screen':
			clear()
			cprint(master_password_screen,clr,attrs=[attr])
			cprint('Enter Maser password',clr,attrs=[attr])
			raw_password = password_input('\t\t\t: ')
			decrypted_master_password=KeyProcess().decrypt_password(key=raw_password,path='lib\ekey.psk')
			if decrypted_master_password==raw_password:return 'proceed_to_login_screen'
			else:
				cprint("Invalid password\nExiting Application",'red',attrs=['bold'])
				sleep(1.638)

		elif name=='home_screen':cprint(homescreen,color=clr,attrs=[attr])
		elif name=='show_screen_failed_middle':cprint(show_screen_failed_middle,color=clr,attrs=[attr])
		elif name=='show_screen_failed_top':cprint(show_screen_failed_top,color=clr,attrs=[attr])
		elif name=='show_screen':cprint(show_screen,color=clr,attrs=[attr])
		elif name=='end_screen':cprint(end_screen)


if __name__=="__main__":
	clear()
	screen=Screen()
	screen.ui('login_screen')
	#print(screen.ui("master_password_screen"))
	#screen.ui('create_new',clr='blue')
	