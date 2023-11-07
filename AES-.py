from Crypto.Cipher import AES
import hashlib

pas = input("Enter your password: ").encode('utf-8')
msg = input("Enter your msg: ").encode('utf-8')


def padding(msg):
    while len(msg) % 16 !=0:
        msg = msg + b' '
    return msg

key = hashlib.sha384(pas).digest()
cipher = AES.new(key, AES.MODE_CBC)
msg_pad = padding(msg)

encrypted_msg = cipher.encrypt(msg_pad)
with open("theykey.key", 'wb') as wen:
    wen.write(cipher.iv)
    wen.write(encrypted_msg)