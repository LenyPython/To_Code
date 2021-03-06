from tkinter import *
from math import *
from tkinter import messagebox

# creating main window
screen = Tk()
screen.title("Calculator")


# dictionary for data
memory = {
        'num1':'',
        'num2':'',
        'op':'',
        'm1':'',
        'm2':'',
        'm3':''
        }


# creating function for numbers input
def input_values(a):
    if not a.isdigit():
        if a == '.':
            if monitor.get() == '':
                monitor.insert(0, '0'+a)
            else:
                if a not in monitor.get():
                    value = monitor.get()
                    monitor.delete(0,END)
                    monitor.insert(0, value + a)
        else:
            if monitor.get() != '':
                if monitor.get()[0].isdigit():
                    value = monitor.get()
                    monitor.delete(0,END)
                    monitor.insert(0, a + value)
                else:
                    pass
    else:
        if monitor.get() != '':
            if monitor.get()[0].isdigit():
                value = monitor.get()
                monitor.delete(0,END)
                monitor.insert(0, value + a)
            else:
                monitor.delete(0,END)
                monitor.insert(0, a)
        else:
            monitor.insert(0, a)


def operation(operator):
    global memory
    if monitor.get() != '':
        if monitor.get()[0].isdigit():
            # save operation to dictionary
            memory.update({'num1':monitor.get(),'op':operator})
            # write operation on the screen
            display = operator + ' ' + monitor.get()
            monitor.delete(0, END)
            monitor.insert(0, display)
        else:
            pass


# equal button function
def equal():
    global memory
    answer = ''
    oper = memory['op']
    try:
       a = float(memory['num1'])
       memory.update({'num2':monitor.get()})
       if memory['num2'] == '' or not monitor.get()[0].isdigit():
            pass
       else:
            b = float(memory['num2'])
            if oper == '+':
                answer = a+b
            elif oper == '-':
                answer = a-b
            elif oper == '*':
                answer = a*b
            elif oper == '/':
                answer = a/b
            elif oper == '**':
                answer = a**b
            elif oper == '%':
                answer = a*b/100
    except OverflowError:
        clear_everything()
        monitor.insert(0, '10')
    except ValueError:
        pass

    monitor.delete(0, END)
    monitor.insert(0, answer)

def instant_operations(oper):
    global memory
    answer = ''
    memory.update({'num1':monitor.get()})
    a = float(memory['num1'])
    if oper == 'sqrt':
        if a>0:
            answer = sqrt(a) 
    elif oper == 'sin':
        answer = sin(a)
    elif oper == 'cos':
        answer = cos(a)
    monitor.delete(0, END)
    monitor.insert(0, answer)


# delete all operation info
def clear_everything():
    monitor.delete(0,END)
    global memory
    memory.update({'num1':'','num2':'','op':''})


# delete memory
def clear_m():
    global memory
    memory.update({'m1':'','m2':'','m3':''})


# write to memory
def memory_write(key):
    global memory
    if memory[key] == '':
        value = ''
        for x in monitor.get():
            if x.isdigit() or x == '.':
                value = value+x
        memory.update({key:value})
    else:
        monitor.delete(0,END)
        monitor.insert(0,memory[key])


# the working screen for digits and operation
monitor = Entry(screen, width=32, bd=2, justify=RIGHT)


# create number buttons
button1 = Button(screen, text='1', height=3, width=3, command=lambda:input_values('1'))
button2 = Button(screen, text='2', height=3, width=3, command=lambda:input_values('2'))
button3 = Button(screen, text='3', height=3, width=3, command=lambda:input_values('3'))

button4 = Button(screen, text='4', height=3, width=3, command=lambda:input_values('4'))
button5 = Button(screen, text='5', height=3, width=3, command=lambda:input_values('5'))
button6 = Button(screen, text='6', height=3, width=3, command=lambda:input_values('6'))

button7 = Button(screen, text='7', height=3, width=3, command=lambda:input_values('7'))
button8 = Button(screen, text='8', height=3, width=3, command=lambda:input_values('8'))
button9 = Button(screen, text='9', height=3, width=3, command=lambda:input_values('9'))
button0 = Button(screen, text='0', height=2, width=9, command=lambda:input_values('0'))


#operation buttons
button_m1 = Button(screen, text='Mem1', height=2, width=3, command=lambda:memory_write('m1'))
button_m2 = Button(screen, text='Mem2', height=2, width=3, command=lambda:memory_write('m2'))
button_m3 = Button(screen, text='Mem3', height=2, width=3, command=lambda:memory_write('m3'))
button_cm = Button(screen, text='CMem', height=2, width=7, command=clear_m)

button_equ = Button(screen, text='=', height=6, width=2, command=equal)

button_add = Button(screen, text='+', height=3, width=2, command=lambda:operation('+'))
button_sub = Button(screen, text='-', height=3, width=2, command=lambda:operation('-'))
button_dot = Button(screen, text='.', height=2, width=3, command=lambda:input_values('.'))
button_mul = Button(screen, text='*', height=3, width=2, command=lambda:operation('*'))
button_div = Button(screen, text='/', height=3, width=2, command=lambda:operation('/'))
button_pow = Button(screen, text='x^', height=2, width=2, command=lambda:operation('**'))

button_per = Button(screen, text='%', height=2, width=2,
        command=lambda:operation('%'))
button_sin = Button(screen, text='sin', height=3, width=2,
        command=lambda:instant_operations('sin'))
button_cos = Button(screen, text='cos', height=3, width=2,
        command=lambda:instant_operations('cos'))
button_sqr = Button(screen, text='sqrt', height=3, width=2,
        command=lambda:instant_operations('sqrt'))

button_c = Button(screen, text='C', height=3, width=2, command=lambda:monitor.delete(0,END))
button_ce = Button(screen, text='CE', height=2, width=2, command=clear_everything)

# insert to calculator grid
monitor.grid(row=0, column=0, columnspan=6)
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)
button0.grid(row=5, column=0, columnspan=2)


# insert operators 
button_m1.grid(row=1, column=0)
button_m2.grid(row=1, column=1)
button_m3.grid(row=1, column=2)
button_per.grid(row=1, column=5)
button_cm.grid(row=1, column=3, columnspan=2)

button_add.grid(row=2, column=3)
button_mul.grid(row=2, column=4)
button_sin.grid(row=2, column=5)

button_sub.grid(row=3, column=3)
button_cos.grid(row=3, column=5)
button_div.grid(row=3, column=4)

button_sqr.grid(row=4, column=5)
button_equ.grid(row=4, column=3, rowspan=2)
button_c.grid(row=4, column=4)

button_ce.grid(row=5, column=4)
button_pow.grid(row=5, column=5)
button_dot.grid(row=5, column=2)


if __name__ == '__main__':

    screen.mainloop()
