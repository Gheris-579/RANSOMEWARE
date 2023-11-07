import pyAesCrypt
import glob
import os


# Encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
# Get current directory
curDir = os.getcwd()
# Prompt user for password to decrypt files
password1 = input("\n[!] Enter password to Encryption: ")

print("\n> Beginning recursive encryption...\n")
# Main loop to decrypt all files in recursively
for x in glob.glob('ff7\\**\*', recursive=True):
    fullpath = os.path.join(curDir, x)
    fullnewf = os.path.join(curDir, x + '.encrypt')

    # Encrypt
    if os.path.isfile(fullpath):
        print('>>> Original: \t' + fullpath + '')
        print('>>> Encrypt: \t' + fullnewf + '\n')
        pyAesCrypt.encryptFile(fullpath, fullnewf, password1, bufferSize)
        # Remove file after encryption
        os.remove(fullpath)