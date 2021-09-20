from os import remove
from addons import *
clear()
Master_password=password_input("Enter your secret key: ")
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
	global Master_password
	def __init__(self,raw_key=Master_password):
		clear()
		self.raw_key=raw_key			
		try:
			self.path_dir=open("path_dir","r+").read()
			self.rootb=open("lib\ekey","rb")
			self.rootw=open("lib\ekey","r+")
		except FileNotFoundError:
			
			self.rootw=open("lib\ekey","w+")
			self.rootb=open("lib\ekey","rb")
			self.new_raw_password=password_input("Create a new password: ")
			self.conferm_password=input("Confirm password: ")

			if self.new_raw_password==self.conferm_password:
				new_encrypted_password=AESCipher(self.new_raw_password).encrypt(self.new_raw_password)

				t=str(new_encrypted_password)
				splited_encrypted_password=(t.split("'")[-2])#splitting encrypted key
				self.rootw.write(splited_encrypted_password)#saving encrypted password
				cprint("Password Created\nloading...",'green',attrs=["bold"]);sleep(1)
				os.system("exit()")

					
			else:
				self.rootw.close()
				try:os.remove(f"{self.path_dir}lib\\ekey")
				except PermissionError as error:cprint(f"{error}\nplease manually delete empty 'lib/ekey' otherwise it will cause errors","yellow",attrs=["bold"])
				finally:raise ValueError("Passwords doesnt match")#fire value error 
	
	def encrypt_key(self):
		global Master_password
		clear()
		cprint("Enter your Master password","cyan",attrs=["bold"])
		self.raw_key=password_input("Enter Password: ")
		Master_password=self.raw_key
		aes=AESCipher(self.raw_key)
		#encrypted_key=aes.encrypt(raw_key)
		encrypted_root=self.rootb.read()
		t=str(encrypted_root)
		splitted_encrypted_root=(t.split("'")[-2])#splitting encrypted key


		decryptepted_final_key=aes.decrypt(splitted_encrypted_root)#splitted_encrypted_root


		
		if decryptepted_final_key==self.raw_key:
			reencrypted_key=aes.encrypt(decryptepted_final_key)#reencryption decrypted key for better security
			t=str(reencrypted_key)
			splitted_reencrypted_key=(t.split("'")[-2])#splitting encrypted key
			open("lib/ekey","w").write(splitted_reencrypted_key)#saving the new key
			clear()
			typing("Access granded...","cyan")
			Screen().home_elements()

		else:
			cprint("Access denied\nExiting Application...","red",attrs=["bold"])
			sleep(2)
			clear();os.system("exit()")
			
			
		

	def encrypt_password(self,raw_password):
		aes=AESCipher(self.raw_key)
		raw_encrypted_password=aes.encrypt(raw_password)
		t=str(raw_encrypted_password)
		splitted_encrypted_password=(t.split("'")[-2])#splitting raw_encrypted_password
		return splitted_encrypted_password
		

	def decrypt_password(self,id):
		aes=AESCipher(self.raw_key)
		path=open(f"{self.path_dir}\\{id}\\password")
		#print("path= ",path)
		#nput()
		encrypted_password=path.read()#opening encrypted password from root
		decrypted_password=aes.decrypt(encrypted_password)
		return decrypted_password

	def reencrypt_password(self,id,password):
		aes=AESCipher(self.raw_key)
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
				new_path=input("Enter new path: ")
				path_dir=open("path_dir","w")
				path_dir.write(new_path)
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
				dirs=os.listdir(open('path_dir','r').read())
				listToStr = ' '.join(map(str, dirs))
				print(listToStr.replace(' ', '\n'))
				input()

				
			else:
				cprint("Invalid input","red",attrs=['bold'])
				sleep(2)
				
if __name__=="__main__":
	Screen().home_elements()			
