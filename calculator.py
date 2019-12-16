from tkinter import *
from math import *

# creating main window 'screen'
screen = Tk()
screen.title("Calculator")
screen.geometry('320x300')

# creating function for numbers input
def in_num():
    pass

# the working screen for digits and operation
monitor = Entry(screen, bd=2, justify=RIGHT)


# create number buttons
button1 = Button(screen, text='1', height=3, width=3, command=in_num)
button2 = Button(screen, text='2', height=3, width=3, command=in_num)
button3 = Button(screen, text='3', height=3, width=3, command=in_num)

button4 = Button(screen, text='4', height=3, width=3, command=in_num)
button5 = Button(screen, text='5', height=3, width=3, command=in_num)
button6 = Button(screen, text='6', height=3, width=3, command=in_num)

button7 = Button(screen, text='7', height=3, width=3, command=in_num)
button8 = Button(screen, text='8', height=3, width=3, command=in_num)
button9 = Button(screen, text='9', height=3, width=3, command=in_num)
button0 = Button(screen, text='0', height=3, width=9, command=in_num)


#operation buttons
button_add = Button(screen, text='+', height=3, width=2, command=in_num)
button_sub = Button(screen, text='-', height=3, width=2, command=in_num)
button_equ = Button(screen, text='=', height=3, width=8, command=in_num)
button_mul = Button(screen, text='*', height=3, width=2, command=in_num)
button_div = Button(screen, text='/', height=3, width=2, command=in_num)
button_sqr = Button(screen, text='sqrt', height=3, width=2, command=in_num)
button_per = Button(screen, text='%', height=3, width=2, command=in_num)
button_pow = Button(screen, text='**', height=3, width=2, command=in_num)
button_sin = Button(screen, text='sin', height=3, width=2, command=in_num)
button_cos = Button(screen, text='cos', height=3, width=2, command=in_num)

# insert to calculator grid
monitor.grid(row=0, column=0, columnspan=6)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=0, columnspan=2)


# insert operators 
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_equ.grid(row=4, column=2, columnspan=2)
button_mul.grid(row=1, column=4)
button_div.grid(row=2, column=4)
button_sqr.grid(row=3, column=4)
button_per.grid(row=3, column=3)
button_pow.grid(row=4, column=4)
button_sin.grid(row=1, column=5)
button_cos.grid(row=2, column=5)


if __name__ == '__main__':

    screen.mainloop()
