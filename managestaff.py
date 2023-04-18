from tkinter import *
from tkinter import messagebox
from employee_oop import *
from subprocess import call

ms = Tk()
ms.geometry("960x540")
ms.title("Manage staff")
ms.configure(bg='#3D3D3D')

# create employee object
with open("data/users.txt", "r") as f:
    lines = f.readlines()
    employee_list = []
    for line in lines:
        fields = line.split(",")
        employee = Employee(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8])
        employee_list.append(employee)


# function

def select_staff(event):
    try:
        global selected
        for index in staff_list.curselection():
            with open("data/users.txt") as f:
                lines = f.readlines()
                fields = lines[index].split(",")
                selected = index
            name_entry.delete(0, END)
            name_entry.insert(END, fields[0])
            dob_entry.delete(0, END)
            dob_entry.insert(END, fields[1])
            username_entry.delete(0, END)
            username_entry.insert(END, fields[2])
            password_entry.delete(0, END)
            password_entry.insert(END, fields[3])
            role_entry.delete(0, END)
            role_entry.insert(END, fields[4])
            coesalary_entry.delete(0, END)
            coesalary_entry.insert(END, fields[5])
            worktime_entry.delete(0, END)
            worktime_entry.insert(END, fields[6])
            bonus_entry.delete(0, END)
            bonus_entry.insert(END, fields[7])
            salary_entry.configure(state=NORMAL)
            salary_entry.delete(0, END)
            salary_entry.insert(END, fields[8])
            salary_entry.configure(state=DISABLED)
    except IndexError:
        pass


def clear():
    name_entry.delete(0, END)
    dob_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    role_entry.delete(0, END)
    coesalary_entry.delete(0, END)
    worktime_entry.delete(0, END)
    bonus_entry.delete(0, END)
    salary_entry.configure(state=NORMAL)
    salary_entry.delete(0, END)
    salary_entry.configure(state=DISABLED)


def display():
    staff_list.delete(0, END)
    with open("data/users.txt") as f:
        lines = f.readlines()
        for line in lines:
            fields = line.split(",")
            name = fields[0]
            dob = fields[1]
            username = fields[2]
            password = fields[3]
            role = fields[4]
            coesalary = fields[5]
            worktime = fields[6]
            bonus = fields[7]
            salary = fields[8]
            output = f"Name: {name}, DOB: {dob}, Username: {username}, Password: {password}, Role: {role}, " \
                     f"Coesalary: {coesalary}, Worktime: {worktime}, Bonus: {bonus}, Salary: {salary}"
            staff_list.insert(END, output)


def add_employee():
    name = name_entry.get()
    dob = dob_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    role = role_entry.get()
    coesalary = coesalary_entry.get()
    worktime = worktime_entry.get()
    bonus = bonus_entry.get()
    salary = salary_entry.get()

    if name == "" or dob == "" or username == "" or password == "" or role == "" or coesalary == "" or worktime == "" or bonus == "":
        messagebox.showerror("", "Please include all fields")
        return

    check = True
    try:
        float(coesalary)
        float(worktime)
        float(bonus)
    except ValueError:
        check = False

    if not check:
        messagebox.showerror("", "Please input float type")

    employee_list.append(Employee(name, dob, username, password, role, coesalary, worktime, bonus, salary))
    with open("data/users.txt", "a") as user_write:
        user_write.write(f"{name},{dob},{username},{password},{role},{coesalary},{worktime},{bonus},{salary}\n")

    clear()
    display()


def update():
    # input
    name = name_entry.get()
    dob = dob_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    role = role_entry.get()
    coesalary = coesalary_entry.get()
    worktime = worktime_entry.get()
    bonus = bonus_entry.get()
    salary = salary_entry.get()

    if name == "" or dob == "" or username == "" or password == "" or role == "" or coesalary == "" or worktime == "" or bonus == "":
        messagebox.showerror("", "Please include all fields")
        return

    check = True
    try:
        float(coesalary)
        float(worktime)
        float(bonus)
    except ValueError:
        check = False

    if not check:
        messagebox.showerror("", "Please input float type")

    # update info
    with open("data/users.txt") as f:
        lines = f.readlines()

    lines[selected] = ""
    lines[selected] = f"{name},{dob},{username},{password},{role},{coesalary},{worktime},{bonus},{salary}"

    with open("data/users.txt", "w") as f:
        for line in lines:
            f.write(line)

    display()


def remove():
    with open("data/users.txt") as f:
        lines = f.readlines()

    del lines[selected]
    with open("data/users.txt", "w") as f:
        for line in lines:
            f.write(line)

    clear()
    display()


def calc_salary():
    coesalary = float(coesalary_entry.get())
    worktime = float(worktime_entry.get())
    bonus = float(bonus_entry.get())
    salary = coesalary * worktime + bonus
    salary = str(salary)
    salary_entry.configure(state=NORMAL)
    salary_entry.insert(0, salary)
    salary_entry.configure(state=DISABLED)


def back():
    ms.destroy()
    call(["python", "admin.py"])


backBt = Button(ms, text="BACK", command=back)
backBt.place(x=3, y=3)

# staff
name_text = StringVar()
name_label = Label(ms, text='Name', font=('bold', 14), bg='#3D3D3D', fg='#FFD154')
name_label.grid(row=0, column=0, sticky=E)
name_entry = Entry(ms, textvariable=name_text)
name_entry.grid(row=0, column=1)
# Username
username_text = StringVar()
username_label = Label(ms, text='Username', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
username_label.grid(row=1, column=0, sticky=E)
username_entry = Entry(ms, textvariable=username_text)
username_entry.grid(row=1, column=1)
# dob
dob_text = StringVar()
dob_label = Label(ms, text='DOB', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
dob_label.grid(row=0, column=3, sticky=E)
dob_entry = Entry(ms, textvariable=dob_text)
dob_entry.grid(row=0, column=4)
# Role
role_text = StringVar()
role_label = Label(ms, text='Role', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
role_label.grid(row=2, column=0, sticky=E)
role_entry = Entry(ms, textvariable=role_text)
role_entry.grid(row=2, column=1)
# Password
password_text = StringVar()
password_label = Label(ms, text='Password', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
password_label.grid(row=1, column=3, sticky=E)
password_entry = Entry(ms)
password_entry.grid(row=1, column=4)
# Coesalary
coesalary_text = StringVar()
coesalary_label = Label(ms, text='Coefficients salary', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
coesalary_label.grid(row=2, column=3, sticky=E)
coesalary_entry = Entry(ms)
coesalary_entry.grid(row=2, column=4)
# Bonus
bonus_text = StringVar()
bonus_label = Label(ms, text='Bonus', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
bonus_label.grid(row=3, column=3, sticky=E)
bonus_entry = Entry(ms)
bonus_entry.grid(row=3, column=4)
# salary
salary_text = StringVar()
salary_label = Label(ms, text='Salary', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
salary_label.grid(row=4, column=1, sticky=E)
salary_entry = Entry(ms, textvariable=salary_text, state=DISABLED)
salary_entry.grid(row=4, column=2, sticky=E)
# work time
worktime_text = StringVar()
worktime_label = Label(ms, text='Working time', font=('bold', 14), pady=15, bg='#3D3D3D', fg='#FFD154')
worktime_label.grid(row=3, column=0, sticky=E)
worktime_entry = Entry(ms, textvariable=worktime_text)
worktime_entry.grid(row=3, column=1)
# staff List (Listbox)
staff_list = Listbox(ms, height=8, width=153, border=0)
staff_list.grid(row=6, column=0, columnspan=5, rowspan=6, pady=15, padx=20, sticky=S)

# Bind select
staff_list.bind('<<ListboxSelect>>', select_staff)

# Button
add_btn = Button(ms, text='Add Staff', width=16, command=add_employee)
add_btn.grid(row=5, column=0, pady=15)

remove_btn = Button(ms, text='Remove Staff', width=16, command=remove)
remove_btn.grid(row=5, column=1)

update_btn = Button(ms, text='Update Information', width=16, command=update)
update_btn.grid(row=5, column=2)

calc_btn = Button(ms, text="Calculate Salary", width=16, command=calc_salary)
calc_btn.grid(row=5, column=3)

clear_btn = Button(ms, text='Clear Input', width=16, command=clear)
clear_btn.grid(row=5, column=4)

display()

# Start program
ms.mainloop()
