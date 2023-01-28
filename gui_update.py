import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from tkinter import font
from ss import Take
from datetime import datetime
from login_api import Login
from PIL import Image, ImageTk

# Frames logic
# First Frame Class
class FirstFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.e_name = ""
		self.e_id = ""
		self.e_email = ""
		self.time = 5000

		# ----- Background Image settings ----- #
		img = ImageTk.PhotoImage(Image.open("./assets/image_1.png"), Image.ANTIALIAS)
		lbl = tk.Label(self, image=img)
		lbl.img = img  # Keep a reference in case this code put is in a function.
		lbl.place(relx=0.5, rely=0.5, anchor='center') 
		# -------------------------------------- #
		L1 = tk.Label(self, text="Email")
		L1.place(x = 200, y = 200)
		T1 = tk.Entry(self, width = 50)
		T1.place(x = 350, y = 200)

		L2 = tk.Label(self, text="Password")
		L2.place(x = 200, y = 250)
		T2 = tk.Entry(self, width = 50, show = '*')
		T2.place(x = 350, y = 250)

		label = tk.Label(self, text="Enter Credentials")
		label.place(x = 300, y = 350)

		def infinite_loop():
			if condition:
				a = Take(self.e_name, self.e_id)
				a.main()
				# after(miliseconds, function)
				self.after(self.time, infinite_loop) # 5000 : 5 Secs
			else:
				self.after(self.time, infinite_loop)

		def verify():
			l = Login(T1.get(), T2.get())
			r = l.login()
			if r['status'] == 200:
				global condition, u_name, id
				condition = True
				u_name = T1.get()
				id = r['data']['id']
				self.e_id = r['data']['id']
				self.e_name = r['data']['employeeName']
				self.e_email = r['data']['email']
				self.time = int(r['data']['time']) * 1000
				controller.show_frame(SecondFrame)
				infinite_loop()
				t = datetime.now()
				FirstFrame.hide_window()
			else:
				messagebox.showinfo("Error", "Wrong Credentials")

		b1 = tk.Button(self,
		 		text="Start",
				command=verify)
		b1.place(x = 625, y = 400)

		def quit():
			t = datetime.now()
			app.destroy()
		b2 = tk.Button(self, text="Exit", command=quit)
		b2.place(x = 625, y = 450)

	def hide_window():
		app.iconify()

# Second Frame Class
class SecondFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		# ----- Background Image settings ----- #
		img = ImageTk.PhotoImage(Image.open("./assets/image_1.png"), Image.ANTIALIAS)
		lbl = tk.Label(self, image=img)
		lbl.img = img  # Keep a reference in case this code put is in a function.
		lbl.place(relx=0.5, rely=0.5, anchor='center') 
		# -------------------------------------- #

		label = tk.Label(self, text=f"Welcome")
		label.place(x = 250, y = 170)

		label = tk.Label(self, text=f"Now you can start your work")
		label.place(x = 230, y = 230)

		def quit():
			t = datetime.now()
			print(f"Exit time : {t}")
			app.destroy()
		b2 = tk.Button(self,
						text="Exit",
						command=quit)
		b2.place(x = 650, y = 450)
	def show_me():
		app.update()

# Main Class
class Application(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		window = tk.Frame(self)
		window.pack()

		window.grid_rowconfigure(0, minsize = 500)
		window.grid_columnconfigure(0, minsize = 800)

		self.frames	= {}
		for F in (FirstFrame, SecondFrame):
			frame = F(window, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew")

		self.show_frame(FirstFrame)

	def show_frame(self, page):
		frame = self.frames[page]
		frame.tkraise()

app = Application()
app.title("Application")
app.geometry("700x500")
app.resizable(0, 0)
app.protocol('WM_DELETE_WINDOW', FirstFrame.hide_window)
app.mainloop()
