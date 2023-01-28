"""

>> Developer details: <<
>>>> Smit Panchal
>>>> Python Developer, ML Developer, Django Developer

"""

# ------------ IMPORTING LIBRARIES ------------- #
import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from ss import Take
from login_api import Login
from tkinter import messagebox
import json
# ----------------------------------------------- #


root = Tk()

# ------------ Widgets ------------- #
img = ImageTk.PhotoImage(Image.open("./assets/image_1.png"), Image.ANTIALIAS)
lbl = tk.Label( image=img)
lbl.img = img  # Keep a reference in case this code put is in a function.
lbl.place(relx=0.5, rely=0.5, anchor='center')

L1 = tk.Label(text="Email")
L1.place(x = 200, y = 200)
T1 = tk.Entry(width = 50)
T1.place(x = 350, y = 200)

L2 = tk.Label(text="Password")
L2.place(x = 200, y = 250)
T2 = tk.Entry(width = 50, show = '*')
T2.place(x = 350, y = 250)

label = tk.Label(text="Enter Credentials")
label.place(x = 300, y = 350)
# ----------------------------------- #



# ------------ Functions ------------- #
def infinite_loop():
    if condition:
        a = Take(e_name, e_id)
        a.main()
        # after(miliseconds, function)
        root.after(time, infinite_loop) # 5000 : 5 Secs
    else:
        root.after(time, infinite_loop)

def verify():
    if os.path.exists(os.path.join(os.getcwd(), 'cred.json')):
        with open('cred.json', 'r') as openfile:
            json_object = json.load(openfile)
        username = json_object['username']
        passwd   = json_object['password']
    else:
        username, passwd = T1.get(), T2.get()
    l = Login(username, passwd)
    r = l.login()
    if r['status'] == 200:
        global condition, u_name, id, e_name, e_id, time, e_email
        condition = True
        u_name = username
        id = r['data']['id']
        e_id = r['data']['id']
        e_name = r['data']['employeeName']
        e_email = r['data']['email']
        time = int(r['data']['time']) * 1000
        b2.destroy()
        L1.destroy()
        T1.destroy()
        L2.destroy()
        T2.destroy()
        label.configure(text="Go on with your work.")
        b1.place_forget()
        infinite_loop()
        hide_window()
    else:
        messagebox.showinfo("Error", "Wrong Credentials")

def hide_window():
	root.withdraw()

def quit():
    root.destroy()
# ----------------------------------- #



# ------------ Buttons ------------- #
b1 = tk.Button(
        text="Start",
        command=verify)
b1.place(x = 625, y = 400)

b2 = tk.Button( text="Exit", command=quit)
b2.place(x = 625, y = 450)
# ----------------------------------- #


if os.path.exists(os.path.join(os.getcwd(), 'cred.json')):
    b2.destroy()
    L1.destroy()
    T1.destroy()
    L2.destroy()
    T2.destroy()
    label.configure(text="Go on with your work.")
    b1.place_forget()
    b1.invoke()



# ------------ Application Configuration ------------- #
root.title("Innovexxia Technologies")
root.geometry("700x500")
root.resizable(0, 0)
root.protocol('WM_DELETE_WINDOW', hide_window)
root.iconbitmap(os.path.join(os.getcwd(), 'Asset_4.ico'))
root.mainloop()
# ----------------------------------------------------- #