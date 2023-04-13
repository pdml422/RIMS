from tkinter import *
from subprocess import call


table = Tk()
table.geometry("960x540")
table.configure(bg="#3D3D3D")


def menu():
    table.destroy()
    call(["python", "order.py"])


table1 = Button(bg="#3D3D3D", text="Table 1", width=10, command=menu)
table1.place(x=340, y=45)

table2 = Button(bg="#3D3D3D", text="Table 2", width=10, command=menu)
table2.place(x=540, y=45)

table3 = Button(bg="#3D3D3D", text="Table 3", width=10, command=menu)
table3.place(x=340, y=95)

table4 = Button(bg="#3D3D3D", text="Table 4", width=10, command=menu)
table4.place(x=540, y=95)

table5 = Button(bg="#3D3D3D", text="Table 5", width=10, command=menu)
table5.place(x=340, y=145)

table6 = Button(bg="#3D3D3D", text="Table 6", width=10, command=menu)
table6.place(x=540, y=145)

table7 = Button(bg="#3D3D3D", text="Table 7", width=10, command=menu)
table7.place(x=340, y=195)

table8 = Button(bg="#3D3D3D", text="Table 8", width=10, command=menu)
table8.place(x=540, y=195)

table9 = Button(bg="#3D3D3D", text="Table 9", width=10, command=menu)
table9.place(x=340, y=245)

table10 = Button(bg="#3D3D3D", text="Table 10", width=10, command=menu)
table10.place(x=540, y=245)


table.mainloop()
