import tkinter 
import customtkinter
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as mbox
import os
import AES
import RSA



def start_fun():
    root_tk.destroy()

def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select file")
    entry.delete("0", "end")
    entry.insert(tkinter.END, filename)




def encrypt_fun():
    global filename
    AES.encrypt(filename,"public_key")
    tkinter.messagebox.showinfo(title=None, message='Encryption Done\t\t\t')


def decrypt_fun():
    AES.decrypt(filename+'.enc', "AES_key.enc", "private_key")

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("dark")

root_tk = customtkinter.CTk()
root_tk.geometry("350x500")
root_tk.title("Video Encryption Decryption")

image_size =40

#logo image
logo_image = ImageTk.PhotoImage(Image.open(PATH + "/images/logo.png").resize((200, 200), Image.ANTIALIAS))
key = ImageTk.PhotoImage(Image.open(PATH + "/images/key.png").resize((image_size, image_size), Image.ANTIALIAS))
start = ImageTk.PhotoImage(Image.open(PATH + "/images/start.png").resize((image_size,image_size), Image.ANTIALIAS))

frame_1 = customtkinter.CTkFrame(master=root_tk, corner_radius=15)
frame_1.pack(pady=60, padx=50, fill="both", expand=True)

img = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT,image=logo_image)
img.pack(pady=1)

button_1= customtkinter.CTkButton(master=frame_1, image=start, text="Start",command=start_fun,text_font=("Raleway",14),corner_radius=10, width=190, compound="right",  fg_color="#42a5f5", hover_color="#D35B58")
button_1.pack(padx=10, pady=20)

button_2= customtkinter.CTkButton(master=frame_1, image=key, text="Generate Key",command=RSA.generate_key,text_font=("Raleway",14),corner_radius=10, width=20, compound="right", fg_color="#42a5f5", hover_color="#D35B58")
button_2.pack(padx=10, pady=10)

root_tk.mainloop()

#second window
PATH = os.path.dirname(os.path.realpath(__file__))


customtkinter.set_appearance_mode("dark")
root_tk = customtkinter.CTk()
root_tk.geometry("350x500")
root_tk.title("Video Encryption Decryption")


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
            root_tk.destroy()



frame_1 = customtkinter.CTkFrame(master=root_tk, corner_radius=15)
frame_1.pack(pady=30, padx=35, expand=True)

#logo image
logo_image = ImageTk.PhotoImage(Image.open(PATH + "/images/logo.png").resize((180, 180), Image.ANTIALIAS))
img = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT,image=logo_image)
img.pack(pady=1)

entry = customtkinter.CTkEntry(master=frame_1, width=200,  placeholder_text="Selected Video")
entry.pack(pady=1,padx=10, fill="both", expand=True)

frame_2= customtkinter.CTkFrame(master=frame_1, width=200, height=50, corner_radius=15)
frame_2.pack(pady=30, padx=10, fill="both", expand=True)

#row and columns cnfiguration
frame_2.grid_columnconfigure(0, weight=1)
frame_2.grid_columnconfigure(1, weight=1)
frame_2.grid_rowconfigure(0, minsize=2)

button_1 = customtkinter.CTkButton(master=frame_2, text="Encrypt Video",command =encrypt_fun,text_font=("Raleway",11), height=50,fg_color="#2196f3", hover_color="#D35B58")
button_1.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="ew")

button_2 = customtkinter.CTkButton(master=frame_2, text="Decrypt Video",command =decrypt_fun, text_font=("Raleway",11), height=50,fg_color="#2196f3", hover_color="#D35B58")
button_2.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="ew")

button_3= customtkinter.CTkButton(master=frame_2, text="Select",command =open_file, text_font=("Raleway",11), height=50,fg_color="#2196f3", hover_color="#D35B58")
button_3.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="ew")

button_4 = customtkinter.CTkButton(master=frame_2, text="Exit",command =exit_win,text_font=("Raleway",11), height=50,fg_color="#2196f3", hover_color="#D35B58")
button_4.grid(row=2, column=1, columnspan=1, padx=10, pady=10, sticky="ew")

root_tk.mainloop()





