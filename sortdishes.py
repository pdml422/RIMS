from tkinter import *
from dish_oop import *


sort = Tk()
sort.title("Sort dishes by number of sold")

sorted_list = Listbox(sort, width=80)
sorted_list.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(sort)
scrollbar.pack(side=RIGHT, fill=BOTH)

sorted_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=sorted_list.yview)

change_menu()
dish_list_sorted = sorted(dish_list, key=lambda x: x._get_sold())[::-1]

for dish in dish_list_sorted:
    idx = dish_list_sorted.index(dish)
    category = dish_list_sorted[idx]._get_category()
    name = dish_list_sorted[idx]._get_name()
    price = dish_list_sorted[idx]._get_price()
    sold = dish_list_sorted[idx]._get_sold()
    output = f"Category: {category}, Name: {name}, Price: {price}, Sold: {sold}"
    sorted_list.insert(END, output)


sort.mainloop()
