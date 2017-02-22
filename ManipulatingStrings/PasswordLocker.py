#! python3
# PasswordLocker.py : An insecure password locker program

''' 
    It’s best to use password manager software on your computer that uses one master password to unlock the password manager. 
    Then you can copy any account password to the clipboard and paste it into the website’s Password field.

    The password manager program you’ll create in this example isn’t secure, 
    but it offers a basic demonstration of how such programs work. 
'''

# 1. Use dictionnary to store password
PASSWORDS = {
    'wang_yuw': 'aaa', 
    'yuwei.wang': 'bbb',  
    'yuwei': 'ccc',
    'wang' : 'ddd'
    }

# 2. Handle sys.argv
import sys
if len(sys.argv) < 2:
    print("you should input your account to get the password!")
    sys.exit()
# first argument of argv is always the filename
account = sys.argv[1]

# 3. Copy correct password
import pyperclip
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for" + account + "has been copied to clipboard.")
else:
    print("There is no account named" + account)





