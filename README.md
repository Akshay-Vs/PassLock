<h1 align="center">:closed_lock_with_key:Pass Lock (2.0 Early Access)<br>AES-encrypted-password-manager
 </h1>
<h3 align="center">A medium security python password manager that encrypt passwords using  Advanced Encryption Standard (AES)</h3>

______

<pr><br>
PassLock is a password manager and password generator that encrypts passwords using AES and save them securely on your local machine.
The password is encrypted and decrypted with a 32-bit (upto 220bit) key defined by user and will get updated with each use.
So extending the length of the master password will steadily improve the overall security and key length.
PassLock also generates a 40-bit long password that contains lowercase, uppercase letters, numbers, and symbols.
Passlock's 220bit AES encryption and infinitely long password generator make your passwords nearly impossible to break.
Passlock also has a console user interface that will definitely help to enhance your experience.
</pr>
<br>

<h2 align="left"><u><b>Features</b></u></h2>
  &bull;  AES Encryption<br>
  &bull; User defined key<br>
  &bull; Unlimited length random password generator<br>
  &bull; Auto Copy<br>
  &bull; Custom path<br>
  &bull; Console Animations<br>
  
 <h2 align='left'><u><b>Language</b></u></h2>
 &bull; python3
 <br>
 
 <h2 align='left'><u><b>Installation</b></u></h2>
 <p>Install using git bash 
 <code>$git clone https://github.com/Akshay-Vs/AES-encrypted-password-manager.git</code>
  <br>or click <a href="https://github.com/Akshay-Vs/AES-Encrypted-Password-Manager/archive/refs/heads/main.zip">download</a>
 
 <h2 align='left'><u><b>Requerments</b></u></h2>
 &bull; PassLock requered python 3.7 and above<br>
 &bull; PassLock requeres 3 third party modules, and it will automatically install while running<br>

   
| requermets | requered version |
| ---------  | ---------------- |
| Python     | 3.7+             |
| Crypto     | 1.4+             |
| termcolor  | 1.1+             |
| pyperclip  | 1.8+             |

<h2 align='left'><u><b>Development</b></u></h2>
&bull; Version 1.6.2<br>
&bull; Major Update History:
<tab>

| version | release date |features|
|---------|--------------|--------|
| 0.4     | 18-8-2021    |Release
| 1.0     | 21-8-2021    |Enhanced security<br>Bug Fixes<br>Added 40-bit password genetator<br>optimized performance
| 1.1     | 26-8-2021    |Improved encryption<br>Unlimited length random password generator<br>User defined Key (upto 220 bit)
| 1.5     | 01-9-2021    |Improved Startup speed<br>Fixed Random Password generation bug<br>Added seperate key to encrypt password to improve security
| 1.6   | 16-9-2021    |Added new command to change path<br>Improved security<br>Now you can upgrade passowrds upto 62 bit encryption
|1.7      | 16-9-2021    |Security Update:<br>  &nbsp;&nbsp; - Added seperate key to encrypt password to improve security<br>  &nbsp;&nbsp; - Fixed Some Security faults<br>  &nbsp;&nbsp; - Added a Process Manager that constanty monitor all processes(experimental)



&bull; Developer: Akshay Vs<br>
<h4 align="left"><b>Connect with me</b></h4>
<p align="left">
<a href="https://twitter.com/@Akshayv69128812" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="@Akshayv69128812" height="30" width="40" /></a>
<a href="https://stackoverflow.com/users/akshay-vs" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="akshay-vs" height="30" width="40" /></a>
<a href="https://instagram.com/__akshay_v5__" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="__akshay_v5__" height="30" width="40" /></a>
</p>


_____________

<h2 align='left'><u><b>Running</b></u></h2>
&#9724;Extract the Zip file<br>
&#9724;Run PassLock to open Password manager<br>
&#9724;Enter path of a directory to save encrypted password (Recomended: Create a seperate directory to save password)<i> eg: D:\AES-Ecrypted-Password-Manager\data</i><br>
&#9724;Create a master passwors


<h2 align='left'><u><b>Commands</b></u></h2>
<code>new   </code>Create a new password<br>
<code>show  </code>Decrypt and show password<br>
<code>-c    </code>copy password to clipboard<br>
<code>-r    </code>or leaving password blank will generate a random password<br>
<code>-r 40 </code> initialize random password with key length<br>
<code>--help</code>help<br>
<code>--Exit</code>close all files and exit console application<br>


<h2 align='left'><u><b>License and Copyright</b></u></h2>
Lisence: MIT Lisence<br>
&#169; 2021 Akshay Vs

 <h2>Things to do</h2>
 - Final Bugs Fixes
 - Performance optimization
 - Tests
