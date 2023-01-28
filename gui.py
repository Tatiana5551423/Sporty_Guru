
"""

>> Developer details: <<
>>>> Smit Panchal
>>>> Python Developer, ML Developer, Django Developer

"""

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
import os
import json
from ss import Take
from login_api import Login
import shutil

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# ----------- Script to copy file into STARTUP ----------- #
# STARTUP_FOLDER = "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
# TEMP = STARTUP_FOLDER / Path("./Inn.exe")
# is_app_in_startup = os.path.exists(TEMP)
# if not is_app_in_startup:
#     FILE = Path(__file__).parent / Path("./Inn.exe")
#     shutil.copyfile(FILE, STARTUP_FOLDER)
# --------------------------------------------------------- #

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1100x700")
window.configure(bg = "#FFFFFF")


# ------------ FUNCTIONS ------------- #
def infinite_loop():
    if condition:
        a = Take(e_name, e_id)
        a.main()
        # after(miliseconds, function)
        window.after(time, infinite_loop) # 5000 : 5 Secs
    else:
        window.after(time, infinite_loop)

def verify():
    if os.path.exists(os.path.join(os.getcwd(), 'cred.json')):
        with open('cred.json', 'r') as openfile:
            json_object = json.load(openfile)
        username = json_object['username']
        passwd   = json_object['password']
    else:
        username, passwd = entry_1.get(), entry_2.get()
    if username == "" or passwd == "":
        messagebox.showinfo("Error", "Wrong Credentials")

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
        entry_1.destroy()
        entry_2.destroy()
        canvas.delete(email_label)
        canvas.delete(pass_label)
        canvas.delete(entry_bg_1)
        canvas.delete(entry_bg_2)
        pass_label2 = canvas.create_text(
                                        604.0,
                                        328.0,
                                        anchor="nw",
                                        text="Keep coding and I will never disturb you.",
                                        fill="#000000",
                                        font=("Times", 24 * -1)
                                    )
        button_1.destroy()
        infinite_loop()
        hide_window()
    else:
        messagebox.showinfo("Error", "Wrong Credentials")

def hide_window():
    window.withdraw()

def quit():
    window.destroy()
# ----------------------------------- #


# ---------- DESIGNING UI ---------- #
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Background Image
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=os.path.join(os.getcwd(), "./assets/image_1.png")
    )
image_1 = canvas.create_image(
    500.0,
    350.0,
    image=image_image_1
)

# Copyright text
canvas.create_text(
    0.0,
    686.0,
    anchor="nw",
    text="Copyright @Smit_Panchal",
    fill="#000000",
    font=("Times 10")
)

# Login Button
button_image_1 = PhotoImage(
    file=os.path.join(os.getcwd(), "./assets/button_1.png")
    )
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=verify,
    relief="flat"
)
button_1.place(
    x=722.0,
    y=424.0,
    width=158.0,
    height=53.0
)

# Email Label
email_label = canvas.create_text(
    604.0,
    211.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("Times 24")
)

# Password label
pass_label = canvas.create_text(
    604.0,
    328.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Times 24")
)

image_image_2 = PhotoImage(
    file=os.path.join(os.getcwd(), "./assets/image_2.png")
    )
image_2 = canvas.create_image(
    165.0,
    297.0,
    image=image_image_2
)

# Email-ID Entry
entry_image_1 = PhotoImage(
    file=os.path.join(os.getcwd(), "./assets/entry_1.png")
    )
entry_bg_1 = canvas.create_image(
    870.5,
    225.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#4B96A5",
    highlightthickness=0,
    font=('Times 18')
)
entry_1.place(
    x=737.0,
    y=193.0,
    width=267.0,
    height=62.0
)

# Password Entry
entry_image_2 = PhotoImage(
    file= os.path.join(os.getcwd(), "./assets/entry_2.png")
    )
entry_bg_2 = canvas.create_image(
    870.5,
    350.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#4B96A5",
    highlightthickness=0,
    font=('Times 18'),
    show = '*'
)
entry_2.place(
    x=737.0,
    y=318.0,
    width=267.0,
    height=62.0
)
def hide():
    window.iconify()


if os.path.exists(os.path.join(os.getcwd(), 'cred.json')):
    entry_1.destroy()
    entry_2.destroy()
    canvas.delete(email_label)
    canvas.delete(pass_label)
    canvas.delete(entry_bg_1)
    canvas.delete(entry_bg_2)
    pass_label2 = canvas.create_text(
                                    604.0,
                                    328.0,
                                    anchor="nw",
                                    text="Keep coding and I will never disturb you.",
                                    fill="#000000",
                                    font=("Times", 24 * -1)
                                )
    button_1.invoke()

window.resizable(False, False)
window.title("Innovexxia Technologies")
window.protocol('WM_DELETE_WINDOW', hide)
window.iconbitmap(os.path.join(os.getcwd(), 'Asset_4.ico'))
window.mainloop()