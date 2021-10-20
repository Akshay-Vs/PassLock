from os import remove
from addons import *
clear()
Master_password=str()
primary_color='cyan'

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b85encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b85decode(enc)
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
		self.path_dir=open("data/path_dir","r").read()

	def encrypt(self,raw_password,key):
		aes=AESCipher(key)
		raw_encrypted_password=aes.encrypt(raw_password)
		t=str(raw_encrypted_password)
		splitted_encrypted_password=(t.split("'")[-2])#splitting raw_encrypted_password
		return splitted_encrypted_password

	def decrypt(self,key,path):
		aes=AESCipher(key)
		path=open(path,'r')
		encrypted_password=path.read()#opening encrypted password from root
		decrypted_password=aes.decrypt(encrypted_password)
		if decrypted_password:return decrypted_password #return if the string is not empty
		return '********'

	def encrypt_password(self,raw_password,key,path):

		aes=AESCipher(key)
		iteration=choice(['6','5','6','7','8','9','10'])

		encrypted_password=raw_password
		for i in range(int(iteration)):
			encrypted_password=aes.encrypt(encrypted_password)
			encrypted_password=str(encrypted_password)
			encrypted_password=(encrypted_password.split("'")[-2])
		
		encrypted_iteration=aes.encrypt(iteration)
		encrypted_iteration=str(encrypted_iteration)
		encrypted_iteration=(encrypted_iteration.split("'")[-2])

		open(f"{path}/iterables",'w+').write(encrypted_iteration)
		open(f"data/exc.pyc",'w+').write(f'|?~p~;{encrypted_password}|?~p~;')

		compress(['data/exc.pyc'],f'{path}/password.psl',b"passlock")
		os.remove("data/exc.pyc")

		return encrypted_password
		

	def decrypt_password(self,key,path):
		try:
			aes=AESCipher(key)
			iteration=open(f"{path}/iterables",'r').read()
			iteration=aes.decrypt(iteration)
			iteration=int(iteration)
			password=open(f"{path}/password.psl",'rb').read()
			password=str(password)
			decrypted_password=(password.split("|?~p~;")[-2])	

			for i in range(iteration):
				decrypted_password=aes.decrypt(decrypted_password)
				decrypted_password=str(decrypted_password)

			if decrypted_password:return decrypted_password #return if the string is not empty
			return '********'
		except ValueError:return '********'

	def reencrypt_password(self,id,password,key):
		aes=AESCipher(key)
		reencrypted_password=aes.encrypt(password)
		root=open(f"{self.path_dir}\\{id}\\password",'w')
		t=str(reencrypted_password)
		splitted_reencrypted_password=(t.split("'")[-2])
		root.write(splitted_reencrypted_password)

		

class Screen:

	def __init__(self) -> None:
		#self.path=open('data/path_dir','r').read()
		try:
			open("data/user_data/.nomedia",'r')
		except FileNotFoundError:
			os.mkdir('data/user_data')
			open('data/user_data/.nomedia','w+')

	def ui(self,name,clr=primary_color,attr='blink',option=None):
	
		ids=os.listdir(open('data/path_dir','r').read())
		recent=[None,None,None,None,None,None,None,None,None]
		for x in ids:recent.append(x)
		recent.reverse()
		del recent[9:]
		
		status="Done"
		status1="Error"
		self.encryption_state="Success\t  "
		method="AES124"
		last_view=''
		created_date=""
		generation_type="Random"
		self.bitrate=None
		encoder='Built-in AES124'
		success_preview=2
		failed_preview=0
		self.error_message=''
		id_name=""
		encrypted_password=""
		decrypted_password=""

				
		home_screen_top=(f'''
                                    	             _______________________________________________________________
                                                    |           ____                  __               __           |
                                                    |          / __ \____ ___________/ /   ____  _____/ /__         |
                --help - to get help                |         / /_/ / __ `/ ___/ ___/ /   / __ \/ ___/ //_/         |
                --Exit - to exit                    |        / ____/ /_/ (__  |__  ) /___/ /_/ / /__/ ,<            |
                                                    |       /_/    \__,_/____/____/_____/\____/\___/_/|_|           |
                                                    |                                                               |
                                                    |_______________________________________________________________|
		\n
	_____________________________________________________________________________________________________________
																													
		TRs   -True                                       Process Monitor      Recent passwords                    
		EKEY  -True
                                                            	    p1-{status}              {recent[0]}                      
		--list  to list password IDs                        p2-{status}              {recent[1]}                      
		--r n   to generate n bit password                  p3-{status1}             {recent[2]}                       
		--p     to change currrent path_dir                 p4-{status}              {recent[3]}                      
		--move  to move passwords                           p5-{status}              {recent[4]}                     
		--del   to delete a password                        p6-{status1}             {recent[5]}                     
		                                                    p7-{status1}             {recent[6]}  
		                                                    p8-{status}              {recent[7]}
                                                                    p9-{status}              {recent[8]} ''')                     
		
		home_screen_bottom=('''
	_______________________________________________________________________________________________________________    
		''')

		home_screen_text=('''
		\t\t new    - to create a new password
		\t\t show <name>  - to show saved password
		''')


		################################################################################################################################


		def show_screen():
			return f'''

        {self.encryption_state}  |  Last View   : {last_view   }  |  Password Type : {generation_type}   |   Success Previews: {success_preview}   | Total Bits : {self.bitrate}
        {method}      |  Created Date: {created_date}  |  Encoder :{encoder } |   Failed Previews : {failed_preview}
	_______________________________________________________________________________________________________________


		'''

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
	Process Ended in {time.time()}
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

		{self.encryption_state}  |  Password Type : {generation_type}  |  Created Date: {created_date}  |  Encoder :{encoder }
		{method}           
	_______________________________________________________________________________________________________________

			Enter Requered Details

	''')

		master_password_screen=(f'''			       _________________________
______________________________/WELCOME TO PASSLOCK LOGIN\______________________________________________________________
										{time.process_time_ns()} on {time.ctime()}
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
			try:os.mkdir('data/users')
			except FileExistsError:pass
			username=open(f'data/users/{self.new_username}.psu','w+')
			username.write(encrypter.encrypt(self.new_username,self.new_username))
			username.close()

			#password section
			if self.new_password==confirm_password:
				root=open('lib/ekey.psk','w+')
				encrypt_password=encrypter.encrypt(confirm_password,self.new_password)
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
			cprint("\t\tEnter Identification name",color=clr,attrs=[attr])
			id=input('\t\t\t: ')
			id=id.replace(" ","_")
			cprint("Enter Password (-r n to generate random password)",color=clr,attrs=[attr])
			raw_password=password_input('\t\t\t: ')
			encrypter=KeyProcess()
			path_dir=open('data/path_dir','r').read()
			path=f'{path_dir}/{id}'
			os.mkdir(path)
			
			#print(path)

			try:
				if '-r' in raw_password or raw_password == '':
					t=str(raw_password)
					r=(t.split(" ")[-1])

					if r =='-r':raw_password=generate_random_password()
					else:raw_password=generate_random_password(int(r))
					

					typing(f"\nGenerated Password:{raw_password}\n",'cyan',typing_speed=len(raw_password)/0.045)
					encrypted_password=encrypter.encrypt_password(raw_password,self.private_key,path)
					cprint(f"Encrypted password: {encrypted_password}",clr,attrs=[attr])
		
					cprint(f'Saving {id} at {path_dir}/{id}...','yellow',attrs=['bold'])
					sleep(0.596)
					cprint("Done",'yellow')
					sleep(1.232629)
					

				else:
					encrypted_password=encrypter.encrypt_password(raw_password,self.private_key,path)
					cprint(f'Encrypted password: {encrypted_password}')
					cprint(f'\nSaving {id} at {path_dir}/{id}...','yellow',attrs=['bold'])
					sleep(0.596)
					cprint("Done",'yellow')
					sleep(1.232629)

			except FileExistsError:
				clear()
				cprint(create_new,color=clr,attrs=[attr])
				cprint('ID Exists: Entered id alredy exixts. Please enter another id','red',attrs=[attr])
				cprint("Enter identification name",clr,attrs=[attr])
				id=input('\t\t\t: ')
				path=f'{path_dir}/{id}'
				encrypter.encrypt_password(raw_password,self.private_key,path)
				cprint(f"\nSaving Done {id} at {path_dir}",'yellow',attrs=['bold'])
				sleep(1.638)

			except ValueError as e:
				error=str(e)
				if 'invalid literal' in error:
					cprint("\nOperation cancelled\nInvalid Literal Found: Entered value doesn't seems correct. Try to enter initializer<space>max_range\n\t\t\teg: -r 20, will generate a 20 bit long password",'red','on_grey',attrs=['bold'])
					cprint('press Enter to continue','yellow')
					input()
					
				else:
					cprint("\nSomething went wrong, please try again",'red')
					cprint('press Enter to continue','yellow')
					input()

			except Exception:
				cprint("\nSomething went wrong, please try again",'red')
				cprint('press Enter to continue','yellow')
				input()

		elif name=='master_password_screen':
			clear()
			cprint(master_password_screen,clr,attrs=[attr])
			cprint('Enter Maser password',clr,attrs=[attr])
			raw_password = password_input('\t\t\t: ')
			decrypted_master_password=KeyProcess().decrypt(raw_password,'lib\ekey.psk')
			if decrypted_master_password==raw_password:return 'proceed_to_login_screen'
			else:
				cprint("Invalid password\nExiting Application",'red',attrs=['bold'])
				sleep(1.638)

		elif name=='home_screen':
			cprint(home_screen_top,color=clr,attrs=[attr])
			cprint(f'\n\t\t\t\t path_dir:- {open("data/path_dir","r").read()}',clr,attrs=[attr])
			cprint(home_screen_text,'yellow',attrs=['bold'])
			cprint(home_screen_bottom,clr,attrs=[attr])

		elif name=='show_screen':
			
			path_dir=open('data/path_dir','r').read()
			path=f'{path_dir}/{option}'
			decrypted_password=KeyProcess().decrypt_password(self.private_key,path)
			raw_encrypted_password=open(f'{path}/password.psl','rb').read()
			raw_encrypted_password=str(raw_encrypted_password)

			if decrypted_password == "********":
				self.encryption_state="Failed    "
				try:notify('Invalid Key',"Entered secret key doesn't seems correct. Restart passlock with right key")
				except:pass
			
			self.bitrate=len(raw_encrypted_password)
			raw_encrypted_password=(raw_encrypted_password.split("|?~p~;")[-2])

			cprint(show_screen(),color=clr,attrs=[attr])
			cprint(f'\tIdentification Name: {option}',clr,attrs=[attr])

			cprint(f'\n\tEncrypted Password : {raw_encrypted_password}\n',clr,attrs=[attr])
			cprint(f'\tSaved path         : {path_dir}/{option}\n',clr,attrs=[attr])
			cprint(f"\tDecrypted Password : {decrypted_password}\n",clr,attrs=[attr])
			cprint("\t-c to copy password to clipboard\n\t-edit to edit password",clr,attrs=[attr])
			KeyProcess().encrypt_password(decrypted_password,self.private_key,path)
			_choice=input('\t\t\t')
			if _choice=='-c':pyperclip.copy(decrypted_password)

			elif _choice=='-edit' and decrypted_password!="********":
				cprint("\n\tEnter new password (-r n to generate random password)",clr,attrs=[attr])
				new_password=input("\t\t\t: ")
				cprint("\tEnter Master password",clr,attrs=[attr])
				raw_password = password_input('\t\t\t: ')
				decrypted_master_password=KeyProcess().decrypt(raw_password,'lib\ekey.psk')

				if '-r' in new_password:
					t=str(new_password)
					r=(t.split(" ")[-1])

					if r =='-r':new_password=generate_random_password()
					else:new_password=generate_random_password(int(r))
				
				if decrypted_master_password==raw_password:
					KeyProcess().encrypt_password(new_password,self.private_key,path)
					cprint("\tWriting new password...",clr,attrs=[attr])
					sleep(1.748)
				else:
					cprint("\tSkipping...\n\tInvalid Password",'red',attrs=[attr])
					sleep(1.748)
			elif not _choice:pass
			else:
				cprint("\tAccess denied",'red',attrs=[attr])
				sleep(1.748)

		elif name=='end_screen':
			clear()
			cprint(end_screen,clr,attrs=[attr])
			


if __name__=="__main__":
	clear()
	aes=AESCipher('key')
	byt=aes.encrypt("password")
	print(byt)
	print(aes.decrypt(byt))
