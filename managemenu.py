from tkinter import *
from tkinter import messagebox
from subprocess import call
from dish_oop import *

mm = Tk()
mm.geometry("960x540")
mm.title("Manage menu")
mm.configure(bg='#3D3D3D')

# function


def select_dish(event):
    try:
        global selected
        for index in menu_list.curselection():
            with open("data/menu.txt") as f:
                lines = f.readlines()
                fields = lines[index].split(",")
                selected = index
            category_entry.delete(0, END)
            category_entry.insert(END, fields[0])
            name_entry.delete(0, END)
            name_entry.insert(END, fields[1])
            price_entry.delete(0, END)
            price_entry.insert(END, fields[2])
            sold_entry.delete(0, END)
            sold_entry.insert(END, fields[3])
    except IndexError:
        pass


def clear():
    category_entry.delete(0, END)
    name_entry.delete(0, END)
    price_entry.delete(0, END)
    sold_entry.configure(state=NORMAL)
    sold_entry.delete(0, END)
    sold_entry.configure(state=DISABLED)


def display():
    menu_list.delete(0, END)
    with open("data/menu.txt") as f:
        lines = f.readlines()
        for line in lines:
            fields = line.split(",")
            category = fields[0]
            name = fields[1]
            price = fields[2]
            sold = fields[3]
            output = f"Category: {category}, Name: {name}, Price: {price}, Sold: {sold}"
            menu_list.insert(END, output)


def add_dish():
    category = category_entry.get()
    name = name_entry.get()
    price = price_entry.get()
    sold = sold_entry.get()

    if category == "" or name == "" or price == "":
        messagebox.showerror("", "Please include all fields")
        return

    check = True
    try:
        float(price)
    except ValueError:
        check = False

    if not check:
        messagebox.showerror("", "Please input float type")

    with open("data/menu.txt", "a") as f:
        f.write(f"{category},{name},{price},{sold}\n")
    dish_list.append(Dish(category, name, price, sold))
    clear()
    display()


def update():
    # input
    category = category_entry.get()
    name = name_entry.get()
    price = price_entry.get()
    sold = sold_entry.get()

    if category == "" or name == "" or price == "":
        messagebox.showerror("", "Please include all fields")
        return

    check = True
    try:
        float(price)
    except ValueError:
        check = False

    if not check:
        messagebox.showerror("", "Please input float type")

    # update info
    with open("data/menu.txt") as f:
        lines = f.readlines()

    lines[selected] = ""
    lines[selected] = f"{category},{name},{price},{sold}\n"
    dish_list[selected].set_category(category)
    dish_list[selected].set_name(name)
    dish_list[selected].set_price(price)
    dish_list[selected].set_sold(sold)

    with open("data/menu.txt", "w") as f:
        for line in lines:
            f.write(line)

    display()


def remove():
    with open("data/menu.txt") as f:
        lines = f.readlines()

    del lines[selected]
    with open("data/menu.txt", "w") as f:
        for line in lines:
            f.write(line)
    del dish_list[selected]
    clear()
    display()


def back():
    mm.destroy()
    call(["python", "admin.py"])


backBt = Button(mm, text="BACK", command=back)
backBt.place(x=3, y=3)

# category
category_text = StringVar()
category_label = Label(mm, text='Category', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
category_label.grid(row=0, column=0, sticky=E)
category_entry = Entry(mm, textvariable=category_text)
category_entry.grid(row=0, column=1, sticky=E)
# name
name_text = StringVar()
name_label = Label(mm, text='Name', font=('bold', 14), bg='#3D3D3D', fg='#FFD154')
name_label.grid(row=0, column=2, sticky=E)
name_entry = Entry(mm, textvariable=name_text)
name_entry.grid(row=0, column=3, sticky=E)
# price
price_text = StringVar()
price_label = Label(mm, text='Price', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
price_label.grid(row=1, column=0, sticky=E)
price_entry = Entry(mm, textvariable=price_text)
price_entry.grid(row=1, column=1, sticky=E)
# sold
sold_text = StringVar()
sold_label = Label(mm, text='Sold', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
sold_label.grid(row=1, column=2, sticky=E)
sold_entry = Entry(mm, textvariable=sold_text)
sold_entry.grid(row=1, column=3, sticky=E)
# menu List (Listbox)
menu_list = Listbox(mm, height=21, width=153, border=0)
menu_list.grid(row=3, column=0, columnspan=5, rowspan=15, pady=15, padx=20)

# Bind select
menu_list.bind('<<ListboxSelect>>', select_dish)

# Button
add_btn = Button(mm, text='Add Dish', width=16, command=add_dish)
add_btn.grid(row=2, column=0, pady=15)

remove_btn = Button(mm, text='Remove Dish', width=16, command=remove)
remove_btn.grid(row=2, column=1)

update_btn = Button(mm, text='Update Information', width=16, command=update)
update_btn.grid(row=2, column=2)

clear_btn = Button(mm, text='Clear Input', width=16, command=clear)
clear_btn.grid(row=2, column=3)

display()

# Start program
mm.mainloop()
