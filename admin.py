from tkinter import *
from subprocess import call


admin = Tk()
admin.geometry("960x540")
admin.title("Restaurant management - Admin")
admin.configure(bg='#3D3D3D')

# Function legion


def managestaff():
    admin.destroy()
    call(["python", "managestaff.py"])


def managemenu():
    admin.destroy()
    call(["python", "managemenu.py"])


def report():
    admin.destroy()
    call(["python", "report.py"])


def sign_out():
    admin.destroy()
    call(["python", "login.py"])


# Widget legion
file = open("data/log.txt")
line = file.read()
fields = line.split(",")
file.close()

title = Label(admin, bg="#3D3D3D", fg="#FFD154", text="Restaurant management", font=('Times New Roman', 35))
title.pack()

bt1 = Button(admin, text="Staff Management", width=18, command=managestaff)
bt1.pack(pady=50)

bt2 = Button(admin, text="Menu Management", width=18, command=managemenu)
bt2.pack(pady=50)

bt3 = Button(admin, text="Report", width=18, command=report)
bt3.pack(pady=50)


label = Label(admin, bg="#3D3D3D", fg="#FFD154", text=f"Hello {fields[0]}")
label.place(relx=1, x=-60, y=4, anchor=NE)

bt4 = Button(admin, text="Sign out", command=sign_out)
bt4.place(relx=1, x=-2, y=2, anchor=NE)


admin.mainloop()
