from tkinter import *
from subprocess import call
from tkinter import messagebox


order = Tk()
order.title("Order")
order.geometry("960x540")
order.configure(bg="#3D3D3D")


def display_menu():
    menu_list.delete(0, END)
    with open("data/menu.txt") as f:
        lines = f.readlines()
        for line in lines:
            fields = line.split(",")
            category = fields[0]
            name = fields[1]
            price = fields[2]
            output = f"Category: {category}, Name: {name}, Price: {price}"
            menu_list.insert(END, output)


def display_order():
    order_list.delete(0, END)
    total = 0.0
    with open("data/order.txt") as f:
        lines = f.readlines()
        for line in lines:
            fields = line.split(",")
            category = fields[0]
            name = fields[1]
            price = fields[2]
            quantity = fields[3]
            output = f"Name: {name}, Quantity: {quantity}"
            order_list.insert(END, output)

            total_temp = float(total_entry.get())
            total_temp = float(price) * int(quantity)
            total += total_temp
        total_entry.configure(state=NORMAL)
        total_entry.delete(0, END)
        total_entry.insert(END, str(total))
        total_entry.configure(state=DISABLED)


def clear():
    category_entry.configure(state=NORMAL)
    category_entry.delete(0, END)
    category_entry.configure(state=DISABLED)
    name_entry.configure(state=NORMAL)
    name_entry.delete(0, END)
    name_entry.configure(state=DISABLED)
    price_entry.configure(state=NORMAL)
    price_entry.delete(0, END)
    price_entry.configure(state=DISABLED)
    quantity_entry.delete(0, END)


def select_menu(event):
    try:
        global selected_menu
        for index in menu_list.curselection():
            with open("data/menu.txt") as f:
                lines = f.readlines()
                fields = lines[index].split(",")
                selected_menu = index
            category_entry.configure(state=NORMAL)
            category_entry.delete(0, END)
            category_entry.insert(END, fields[0])
            category_entry.configure(state=DISABLED)
            name_entry.configure(state=NORMAL)
            name_entry.delete(0, END)
            name_entry.insert(END, fields[1])
            name_entry.configure(state=DISABLED)
            price_entry.configure(state=NORMAL)
            price_entry.delete(0, END)
            price_entry.insert(END, fields[2])
            price_entry.configure(state=DISABLED)
            quantity_entry.delete(0, END)
    except IndexError:
        pass


def select_order(event):
    try:
        global selected_order
        for index in order_list.curselection():
            with open("data/order.txt") as f:
                selected_order = index
    except IndexError:
        pass


def ato():
    category = category_entry.get()
    name = name_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()

    if quantity == "":
        messagebox.showerror("", "Please include quantity")
        return

    check = True
    try:
        int(quantity)
    except ValueError:
        check = False

    if not check:
        messagebox.showerror("", "Please input integer type")

    with open("data/order.txt", "a") as f:
        f.write(f"{category},{name},{price},{quantity}\n")
    clear()
    display_order()


def remove_order():
    with open("data/order.txt") as f:
        lines = f.readlines()

    del lines[selected_order]
    with open("data/order.txt", "w") as f:
        for line in lines:
            f.write(line)
    display_order()


def bill():

    with open("data/menu.txt") as f1, open("data/order.txt") as f2:
        lines2 = f2.readlines()
        lines1 = f1.readlines()
        for line2 in lines2:
            fields2 = line2.split(",")
            name2 = fields2[1]
            quantity = fields2[3]

            for i, line1 in enumerate(lines1):
                fields1 = line1.split(",")
                category = fields1[0]
                name1 = fields1[1]
                price = fields1[2]
                sold_old = fields1[3]

                if name2 in line1:
                    lines1[i] = f"{category},{name1},{price},{int(sold_old) + int(quantity)}\n"
                    break

    with open("data/menu.txt", "w") as f1:
        for line in lines1:
            f1.write(line)

    call(["python", "bill.py"])
    display_order()


Label(order, text="Order", font=('bold', 14), bg='#3D3D3D', fg='#FFD154').grid(row=0, column=5)

# category
category_text = StringVar()
category_label = Label(order, text='Category', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
category_label.grid(row=0, column=0, sticky=E)
category_entry = Entry(order, textvariable=category_text, state=DISABLED)
category_entry.grid(row=0, column=1, sticky=E)
# name
name_text = StringVar()
name_label = Label(order, text='Name', font=('bold', 14), bg='#3D3D3D', fg='#FFD154')
name_label.grid(row=0, column=2, sticky=E)
name_entry = Entry(order, textvariable=name_text, state=DISABLED)
name_entry.grid(row=0, column=3, sticky=E)
# price
price_text = StringVar()
price_label = Label(order, text='Price', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
price_label.grid(row=1, column=0, sticky=E)
price_entry = Entry(order, textvariable=price_text, state=DISABLED)
price_entry.grid(row=1, column=1, sticky=E)

# quantity
quantity_text = StringVar()
quantity_label = Label(order, text='Quantity', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
quantity_label.grid(row=1, column=2, sticky=E)
quantity_entry = Entry(order, textvariable=quantity_text)
quantity_entry.grid(row=1, column=3, sticky=E)

# total
total_text = StringVar()
total_label = Label(order, text='Total', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
total_label.grid(row=5, column=5, sticky=W, padx=20)
total_entry = Entry(order, textvariable=total_text)
total_entry.insert(0, "0.0")
total_entry.configure(state=DISABLED)
total_entry.grid(row=5, column=5, sticky=E, padx=20)

# menu List (Listbox)
menu_list = Listbox(order, height=18, width=100, border=0)
menu_list.grid(row=2, column=0, columnspan=5, padx=20, pady=20)

# order list (List box)
order_list = Listbox(order, height=25, width=45, border=0)
order_list.grid(row=0, column=5, rowspan=4, padx=20, sticky=S)

# Bind select
menu_list.bind('<<ListboxSelect>>', select_menu)
display_menu()

order_list.bind('<<ListboxSelect>>', select_order)
display_order()


atoBt = Button(order, text="Add to order", command=ato)
atoBt.grid(row=5, column=2, sticky=W)

removeBt = Button(order, text="Remove", command=remove_order)
removeBt.grid(row=6, column=5, sticky=W, padx=20)

finish_orderBt = Button(order, text="Order", command=bill)
finish_orderBt.grid(row=6, column=5, sticky=E, padx=20)

order.mainloop()
