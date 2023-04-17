from tkinter import *


revenue = Tk()
revenue.title("Restaurant management - Revenue by day")

revenue_list = Listbox(revenue, width=80)
revenue_list.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(revenue)
scrollbar.pack(side=RIGHT, fill=BOTH)

revenue_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=revenue_list.yview)

with open("data/total.txt") as f:
    lines = f.readlines()
    for line in lines:
        fields = line.split(",")
        date = fields[0]
        total = fields[1]
        output = f"Date: {date}, Total: {total}"
        revenue_list.insert(END, output)


revenue.mainloop()
