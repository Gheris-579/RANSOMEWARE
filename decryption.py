import pyAesCrypt
import os
import glob
import getpass

username = getpass.getuser()

# Encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
# Get current directory
curDir = os.getcwd()
# Prompt user for password to decrypt files
password1 = input("\n[!] Enter password to decrypt: ")

print("\n> Beginning recursive decryption...\n")
# Main loop to decrypt all files in recursively
for x in glob.glob(f'C:\\Users\\{username}\\Desktop\\**', recursive=True):
    fullpath = os.path.join(curDir, x)
    fullnewf = os.path.join(curDir, os.path.splitext(x)[0])
    # Decrypt
    if os.path.isfile(fullpath):
        print('>>> Encrypted: \t' + fullpath + '')
        try:
            pyAesCrypt.decryptFile(fullpath, fullnewf, password1, bufferSize)
            print('>>> Decrypted: \t' + fullnewf + '')
            os.remove(fullpath)         # Remove encrypted file after decrypt
        except ValueError:
            print('>>> Error - Wrong password!\n' )
