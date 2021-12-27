from tkinter import *

root = Tk()
root.title("Calculator")
root.config(bg='#D3D3D3')

root.wm_iconbitmap("Calculator.ico")

e = Entry(root, font="lucida 20 bold")
e.grid(row = 0, column= 0, columnspan=3, padx=10, pady=10)



"""function for calculator functioning """
def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear1():
    e.delete(0,END)

def button_addition():
    fst_number = e.get()
    global fst_num
    global math
    math = "addition"
    fst_num = int(fst_number)
    e.delete(0,END)

def button_subtract():
    fst_number=e.get()
    global fst_num
    global math
    math="subtract"
    fst_num=int(fst_number)
    e.delete(0,END)

def button_multiply():
    fst_number=e.get()
    global fst_num
    global math
    math="multiply"
    fst_num=int(fst_number)
    e.delete(0,END)

def button_division():
    fst_number=e.get()
    global fst_num
    global math
    math="division"
    fst_num=int(fst_number)
    e.delete(0,END)

def button_equal():
    sec_number = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0, fst_num + int(sec_number))
    if math == "subtract":
        e.insert(0, fst_num - int(sec_number))
    if math == "multiply":
        e.insert(0, fst_num * int(sec_number))
    if math == "division":
        e.insert(0, fst_num / int(sec_number))



"""Defining Buttons """
button_1 = Button(root, text="1", bg='#A9A9A9', padx=50, pady=20, command=lambda : button_add(1))
button_2 = Button(root, text="2", bg='#A9A9A9', padx=50, pady=20, command=lambda : button_add(2))
button_3 = Button(root, text="3", bg='#A9A9A9', padx=50, pady=20, command=lambda : button_add(3))
button_4 = Button(root, text="4", bg='#A9A9A9', padx=50, pady=20, command=lambda : button_add(4))
button_5 = Button(root, text="5", bg='#A9A9A9', padx=50, pady=20, command=lambda : button_add(5))
button_6 = Button(root, text="6", bg='#A9A9A9', padx=50, pady=20, command=lambda : button_add(6))
button_7 = Button(root, text="7", bg='#A9A9A9', padx=50, pady=20, command=lambda : button_add(7))
button_8 = Button(root, text="8", bg='#A9A9A9', padx=50, pady=20, command=lambda : button_add(8))
button_9 = Button(root, text="9", bg='#A9A9A9', padx=50, pady=20, command=lambda : button_add(9))
button_0 = Button(root, text="0", bg='#A9A9A9', padx=50, pady=20, command=lambda : button_add(0))
button_sum = Button(root, text="+", bg='#C0C0C0', padx=50, pady=20, command=button_addition)
button_sub = Button(root, text="-", bg='#C0C0C0', padx=50, pady=20, command=button_subtract)
button_mul = Button(root, text="*", bg='#C0C0C0', padx=50, pady=20, command=button_multiply)
button_div = Button(root, text="/", bg='#C0C0C0', padx=50, pady=20, command=button_division)
button_eq = Button(root, text="=", bg='#C0C0C0', padx=50, pady=20, command=button_equal)
button_clear = Button(root, text="C", bg='#C0C0C0', padx=50, pady=20, command=button_clear1)

"""Putting the buttons on the screen"""
button_1.grid(row=1, column=0, padx=10, pady=10)
button_2.grid(row=1, column=1, padx=10, pady=10)
button_3.grid(row=1, column=2, padx=10, pady=10)

button_4.grid(row=2, column=0, padx=10, pady=10)
button_5.grid(row=2, column=1, padx=10, pady=10)
button_6.grid(row=2, column=2, padx=10, pady=10)

button_7.grid(row=3, column=0, padx=10, pady=10)
button_8.grid(row=3, column=1, padx=10, pady=10)
button_9.grid(row=3, column=2, padx=10, pady=10)

button_sum.grid(row=4,column=0, padx=10, pady=10)
button_0.grid(row=4, column=1, padx=10, pady=10)
button_sub.grid(row=4,column=2, padx=10, pady=10)

button_mul.grid(row=5,column=0, padx=10, pady=10)
button_div.grid(row=5,column=1, padx=10, pady=10)
button_eq.grid(row=5,column=2, padx=10, pady=10)
button_clear.grid(row=6,column=1, padx=10, pady=10)

root. mainloop()
