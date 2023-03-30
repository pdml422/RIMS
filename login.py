from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Button
import tkinter
from subprocess import call


def verify_login(t: Tk):
    entered_user = username_entry.get()
    entered_pass = password_entry.get()
    try:
        with open("users.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                fields = line.split(",")
                if fields[0] == entered_user and fields[1] == entered_pass:
                    if fields[2] == "admin\n":
                        messagebox.showinfo("", "Logged in as admin")
                        t.destroy()
                        call(["python", "admin.py"])

                    elif fields[2] == "staff\n":
                        messagebox.showinfo("", "Logged in as staff")
                        t.destroy()
                        call(["python", "staff.py"])

    except Exception:
        pass

    messagebox.showerror("", "Invalid user or password")



login = Tk()
login.geometry("960x540")
login.title("Restaurant management - Login")
login.configure(bg='#3D3D3D')

Frame = tkinter.Frame(bg='#3D3D3D')
Frame.place(relx=0.47, rely=0.47, anchor="center")

# label of username
username_label = Label(Frame, bg='#3D3D3D', fg='#FFD154', text="Username:")
username_label.grid(row=2, column=0)
username_entry = Entry(Frame)
username_entry.grid(row=2, column=1)

# label of password
password_label = Label(Frame, bg='#3D3D3D', fg='#FFD154', text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(Frame, show='*')
password_entry.grid(row=3, column=1)

label1 = Label(login, bg='#3D3D3D', fg='#FFD154', text="Restaurant management", font=('Times New Roman', 35))
label1.pack()

label2 = Label(login, bg='#3D3D3D', fg='#FFD154', text="Login form", font=('Times New Roman', 25))
label2.pack(pady=70)

label3 = Label(Frame, bg='#3D3D3D', text=" ")
label3.grid(row=4, column=1)

label4 = Label(Frame, bg='#3D3D3D', text=" ")
label4.grid(row=6, column=1)

bt = Button(Frame, text="Login", command=lambda: verify_login(login))
bt.grid(row=7, column=1)


def show_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
    else:
        password_entry.config(show='*')


check_button = Checkbutton(Frame, text="Show password", command=show_password)
check_button.grid(row=5, column=1)

login.mainloop()