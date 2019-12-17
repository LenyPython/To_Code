from tkinter import *
from math import *

######################################
# 
#ADD A CLEAR BUTTON :/ AND DO THE MATH
#
######################################


# creating main window 'screen'
screen = Tk()
screen.title("Calculator")


# creating function for numbers input
def in_num(a):
    if monitor.get() == '':
        monitor.insert(0, a)
    elif not monitor.get()[0].isdigit():
        monitor.delete(0, END)
        monitor.insert(0, a)
    else:
        number = monitor.get() + a
        monitor.delete(0, END)
        monitor.insert(0, number)


def operation(operator):
    operation = {}
    # save operation to dictionary
    if operator == '+':
        operation['num1'] = float(monitor.get())
        operation['op'] = operator
    elif operator == '-':
        operation['num1'] = float(monitor.get())
        operation['op'] = operator
    elif operator == '*':
        operation['num1'] = float(monitor.get())
        operation['op'] = operator
    elif operator == '/':
        operation['num1'] = float(monitor.get())
        operation['op'] = operator
    elif operator == 'sqrt':
        operation['num1'] = float(monitor.get())
        operation['op'] = operator
    elif operator == '**':
        operation['num1'] = float(monitor.get())
        operation['op'] = operator
    elif operator == 'sin':
        operation['num1'] = float(monitor.get())
        operation['op'] = operator
    elif operator == 'cos':
        operation['num1'] = float(monitor.get())
        operation['op'] = operator
       
    # write operation on the screen
    operation = operator + ' ' + monitor.get()
    monitor.delete(0, END)
    monitor.insert(0, operation)
    #return dictionary
    return operation

#clear function
def clear():
    monitor.delete(0,END)


def clear_everything():
    monitor.delete(0,END)
    


# the working screen for digits and operation
monitor = Entry(screen, width=32, bd=2, justify=RIGHT)


# create number buttons
button1 = Button(screen, text='1', height=3, width=3, command=lambda:in_num('1'))
button2 = Button(screen, text='2', height=3, width=3, command=lambda:in_num('2'))
button3 = Button(screen, text='3', height=3, width=3, command=lambda:in_num('3'))

button4 = Button(screen, text='4', height=3, width=3, command=lambda:in_num('4'))
button5 = Button(screen, text='5', height=3, width=3, command=lambda:in_num('5'))
button6 = Button(screen, text='6', height=3, width=3, command=lambda:in_num('6'))

button7 = Button(screen, text='7', height=3, width=3, command=lambda:in_num('7'))
button8 = Button(screen, text='8', height=3, width=3, command=lambda:in_num('8'))
button9 = Button(screen, text='9', height=3, width=3, command=lambda:in_num('9'))
button0 = Button(screen, text='0', height=2, width=9, command=lambda:in_num('0'))


#operation buttons
button_add = Button(screen, text='+', height=3, width=2, command=lambda:operation('+'))
button_sub = Button(screen, text='-', height=3, width=2, command=lambda:operation('-'))
button_dot = Button(screen, text='.', height=2, width=3, command=lambda:in_num('.'))
button_mul = Button(screen, text='*', height=3, width=2, command=lambda:operation('*'))
button_div = Button(screen, text='/', height=3, width=2, command=lambda:operation('/'))
button_sqr = Button(screen, text='sqrt', height=3, width=2,
        command=lambda:operation('sqrt'))
button_equ = Button(screen, text='=', height=6, width=2, command=lambda:operation('='))
button_pow = Button(screen, text='**', height=2, width=2, command=lambda:operation('**'))
button_sin = Button(screen, text='sin', height=3, width=2,
        command=lambda:operation('sin'))
button_cos = Button(screen, text='cos', height=3, width=2,
        command=lambda:operation('cos'))
button_c = Button(screen, text='C', height=3, width=2, command=clear)
button_ce = Button(screen, text='CE', height=2, width=2, command=clear_everything)

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
button_mul.grid(row=1, column=4)
button_sin.grid(row=1, column=5)
button_sub.grid(row=2, column=3)
button_cos.grid(row=2, column=5)
button_div.grid(row=2, column=4)
button_sqr.grid(row=3, column=5)
button_equ.grid(row=3, column=3, rowspan=2)
button_c.grid(row=3, column=4)
button_ce.grid(row=4, column=4)
button_pow.grid(row=4, column=5)
button_dot.grid(row=4, column=2)


if __name__ == '__main__':

    screen.mainloop()
