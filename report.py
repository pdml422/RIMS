from tkinter import *
from subprocess import call


report = Tk()
report.geometry("960x540")
report.title("Restaurant management - Report")
report.configure(bg='#3D3D3D')

# Function legion


def revenue():
    call(["python", "revenue.py"])


def sort_dishes():
    call(["python", "sortdishes.py"])


def back():
    report.destroy()
    call(["python", "admin.py"])


backBt = Button(report, text="BACK", command=back)
backBt.place(x=3, y=3)


title = Label(report, bg="#3D3D3D", fg="#FFD154", text="Restaurant management", font=('Times New Roman', 35))
title.pack()

bt1 = Button(report, text="Calculate revenue", width=18, command=revenue)
bt1.pack(pady=50)

bt2 = Button(report, text="Sort dishes by sold", width=18, command=sort_dishes)
bt2.pack(pady=50)


report.mainloop()
