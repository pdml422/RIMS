from tkinter import *
import time

bill = Tk()
bill.title("Bill")
bill.geometry("960x540")
bill.configure(bg="#3D3D3D")

Label(bill, bg='#3D3D3D', fg='#FFD154', text="\tRestaurant 13\t", font=('Times New Roman', 30)).grid(row=0, column=1)


bill_time = time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime())
Label(bill, bg='#3D3D3D', fg='#FFD154', text=f"\t{bill_time}\t\t").grid(row=1, column=0)

Label(bill, bg='#3D3D3D', fg='#FFD154', text="           ORDER SUMMARY", font=40).grid(row=2, column=1)
Label(bill, bg='#3D3D3D').grid(row=3, column=1)
Label(bill, bg='#3D3D3D', fg='#FFD154', text="================================================================================", font=19).place(x=0, y=100)

Label(bill, bg='#3D3D3D', fg='#FFD154', text="NAME").grid(row=4, column=0, padx=20)
Label(bill, bg='#3D3D3D', fg='#FFD154', text="PRICE").grid(row=4, column=1, padx=20)
Label(bill, bg='#3D3D3D', fg='#FFD154', text="QUANTITY").grid(row=4, column=2, padx=20)

total = 0.0
with open("data/order.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        fields = line.split(",")
        name = fields[1]
        price = fields[2]
        quantity = fields[3]
        Label(bill, bg='#3D3D3D', fg='#FFD154', text=name).grid(row=5 + i, column=0, padx=20)
        Label(bill, bg='#3D3D3D', fg='#FFD154', text=price).grid(row=5 + i, column=1, padx=20)
        Label(bill, bg='#3D3D3D', fg='#FFD154', text=quantity).grid(row=5 + i, column=2, padx=20)
        total += float(price) * int(quantity)

Label(bill, bg='#3D3D3D', fg='#FFD154', text=f"TOTAL: {total}").place(x=800, y=500)
f = open("data/order.txt", "w")
f.close()

bill.mainloop()
