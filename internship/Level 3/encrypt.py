#Encrypt files
#Uses both Caesar Cipher and Fernet encryption

from cryptography.fernet import Fernet
import os
import random
import hashlib
import base64
import getpass

def passkey(passcode: str) -> bytes:
    return hashlib.sha256(passcode.encode()).digest()

def caeser_encrypt(filename):
    
    #Shift is random and anonymous
    shift = random.randint(0,50000)
    name = str(filename+'.txt')
    shifted_text = ''
    data = ''
    keeper = str(filename+'_gate.txt')

    with open(name, 'r') as new_file:
        for file_info in new_file:
            data += file_info
    
    for x in data:
        shifted_text += chr(ord(x) + shift)
    
    with open(name, 'w') as e_file:
        e_file.write(shifted_text)
    
    shift = str(shift)
    
    #Stores important information in separate file with encryption data 
    with open(keeper, 'w') as s_file:
        s_file.write(shift)
    
    print('\nInitial encryption successful\n')

def caeser_decrypt(filename):
    #gets shift from encrypted gatekeeper file to be accessed with password
    shift = 0
    rev_shift = ''
    coded_info = ''
    coded_file = str(filename+'.txt')
    keeper = str(filename+'_gate.txt')

    with open(keeper, 'r') as gate:
        for code in gate:
            shift = int(code)

    with open(coded_file, 'r') as encrypt:
        for x in encrypt:
            coded_info += x
    
    for y in coded_info:
        rev_shift += chr(ord(y) - shift)
    
    with open(coded_file, 'w') as decrypt:
        decrypt.write(rev_shift)
    
    print('\nSecondary decryption complete. File Decrypted\n')

def fernet_encrypt(filename, key):
    
    content = ''
    name = str(filename+'.txt')
    keeper = str(filename+'_gate.txt')

    try:
        with open(name, 'rb') as new:
            content = new.read()
    except FileNotFoundError:
        print('\nFile is not found\n')

    f_encrypted = key.encrypt(content)

    #s_key = str(filename)+'_secret.key'

    #with open(s_key, "wb") as k_file:
        #k_file.write(code)
    
    #Encrypt the caeser shift code

    with open(keeper, 'rb') as i_data:
        f_data = i_data.read()
    
    p_encrypted = key.encrypt(f_data)

    with open(keeper, 'wb') as k_data:
        k_data.write(p_encrypted)
    
    #f_encrypted = str(f_encrypted)
    with open(name, "wb") as s_file:
        s_file.write(f_encrypted)

    print('\nSecondary encryption complete. File Encrypted\n')


def fernet_decrypt(main_filename, password):

    filename = str(main_filename+'.txt')
    keeper = str(main_filename+'_gate.txt')
    #s_key = str(main_filename)+'_secret.key'

    #Read secret key
    #with open(s_key, "rb") as k_file:
        #code = k_file.read()
    
    de_code = passkey(password)
    f_encrypt = Fernet(base64.urlsafe_b64encode(de_code))

    #Read encrypted file
    try:
        with open(filename, 'rb') as new:
            encrypted_content = new.read()
    except FileNotFoundError:
        print('\nFile is not found\n')
    
    with open(keeper, 'rb') as s_code:
        shifter = s_code.read()
    
    try:
        original_content = f_encrypt.decrypt(encrypted_content)
        e_shift = f_encrypt.decrypt(shifter)
    except:
        print('\n Invalid password \n')

    #Overwrite original file
    with open(filename, "wb") as s_file:
        s_file.write(original_content)
    
    with open(keeper, 'wb') as x_file:
        x_file.write(e_shift)
    
    print('\nInitial decryption successful.\n')
    #Delete key incase for new enryption
    #os.remove(s_key)

def encrypting(filename):
    n_pass = getpass.getpass("\nEnter NEW password for file encryption:\n-> ")
    c_pass = getpass.getpass("\nConfirm password:\n-> ")

    if n_pass!=c_pass:
        print('\nPasswords do no match. Encrption cancelled\n')
        return
    
    else:
        print(f'\nSave your password somewhere safe. Password: {n_pass}\n')
        code_key = passkey(n_pass)
        f_encrypt = Fernet(base64.urlsafe_b64encode(code_key))
        caeser_encrypt(filename)
        fernet_encrypt(filename, f_encrypt)   

def decrypting(filename, password):
    keeper = str(filename+'_gate.txt')
    fernet_decrypt(filename, password)
    caeser_decrypt(filename) 
    os.remove(keeper)

#---------------------------------------------------------------------------
#Main interphase

while True:
    print('\nWelcome to File Encrytption, enter file name you want to encrypt')
    print('Or Decrypt existing')
    choice = input('\n1. Encrpyt a file\n2. Decrypt a file\n3. Exit\n-> ')

    if choice == '1':
        print("\nEnter file name to ENCRYPT \n(E.g abc.txt) filename -> abc")
        file_input = input(str('Enter file name\nfilename -> '))

        #Check for file exist
        file_input_2 = file_input+'.txt'

        try:
            with open(file_input_2, 'r') as check:
                check.read()
            
            engage = encrypting(file_input)

        except FileNotFoundError:
            print('\nFile not found\n')
    
    elif choice == '2':
        print("\nEnter file name to DECRYPT\n(E.g abc.txt) filename -> abc")
        file_input = str(input('\nEnter file name\nfilename -> '))

        #Check for file exist
        file_input_2 = file_input+'.txt'

        try:
            with open(file_input_2, 'r') as check:
                check.read()
            
            password_1 = str(input('Enter decryption password\nPassword-> '))
            disengage = decrypting(file_input, password_1)

        except FileNotFoundError:
            print('\nFile not found\n')
    
    elif choice == '3':
        print('\nHave a good day :)\n')
        break

    else:
        print('\nInvalid choice. Enter option 1 - 3\n')
