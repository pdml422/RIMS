from tkinter import *
import time
from tkinter import Tk, Button
from subprocess import call

staff = Tk()
staff.geometry("960x540")
staff.title("Staff Page")
staff.configure(bg="#3D3D3D")


def order():
    call(["python", "order.py"])


def sign_out():
    staff.destroy()
    call(["python", "login.py"])


def checkin():
    bt1["state"] = DISABLED
    bt2["state"] = NORMAL
    time_string = time.localtime()
    time_start = time.strftime("%d/%m/%Y, %H:%M:%S", time_string)
    label1 = Label(staff, bg="#3D3D3D", fg="#FFD154", text=f"Checked in {time_start}")
    label1.pack()
    global time1
    time1 = time_string.tm_sec + time_string.tm_min * 60 + time_string.tm_hour * 3600
    with open(f"worktime/{fields[0]}.txt", "a") as f:
        f.write(f"Check in:{time_start}\n")


def checkout():
    bt2["state"] = DISABLED
    time_string = time.localtime()
    time_end = time.strftime("%d/%m/%Y, %H:%M:%S", time_string)
    label1 = Label(staff, bg="#3D3D3D", fg="#FFD154", text=f"Checked out {time_end}")
    label1.pack()
    time2 = time_string.tm_sec + time_string.tm_min * 60 + time_string.tm_hour * 3600
    count = time2 - time1
    seconds = count % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    count1 = "%d:%02d:%02d" % (hour, minutes, seconds)
    label2 = Label(staff, bg="#3D3D3D", fg="#FFD154", text=f"You have work for {count1}")
    label2.pack()
    with open(f"worktime/{fields[0]}.txt", "a") as f:
        f.write(f"Check out:{time_end}\n")
        f.write(f"Worked for:{count1}\n")


file = open("data/log.txt")
line = file.read()
fields = line.split(",")
file.close()

title = Label(staff, bg="#3D3D3D", fg="#FFD154", text="Restaurant management", font=('Times New Roman', 35))
title.pack()

bt1 = Button(staff, text="Check in", width=12, command=checkin)
bt1.pack(pady=50)

bt2 = Button(staff, text="Check out", width=12, command=checkout, state=DISABLED)
bt2.pack(pady=50)

label = Label(staff, bg="#3D3D3D", fg="#FFD154", text=f"Hello {fields[0]}")
label.place(relx=1, x=-60, y=4, anchor=NE)

bt3 = Button(staff, text="Order", width=12, command=order)
bt3.pack(pady=50)

bt4 = Button(staff, text="Sign out", command=sign_out)
bt4.place(relx=1, x=-2, y=2, anchor=NE)


staff.mainloop()
