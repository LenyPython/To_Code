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

# function for '.' dot sign, creating float values
def dot():
	global memory

	if memory['op']=='':
		if memory['num1']=='':
			memory.update({'num1':'0.'})
			monitor.delete(0,END)
			monitor.insert(0, memory['num1'])
		elif '.' not in memory['num1']:
			memory.update({'num1':memory.get('num1') + '.'})
			monitor.delete(0,END)
			monitor.insert(0, memory['num1'])
	else:
		if memory['num2']=='':
			memory.update({'num2':'0.'})
			monitor.delete(0,END)
			monitor.insert(0, memory['num2'])
		elif '.' not in memory['num2']:
			memory.update({'num2':memory.get('num2') + '.'})
			monitor.delete(0,END)
			monitor.insert(0, memory['num2'])

# creating function for calculator buttons input
def input_values(calInput):
	global memory

	if memory['op'] == '':
		num = 'num1'
		memory.update({num:memory.get(num, '') + calInput})
		monitor.delete(0,END)
		monitor.insert(0, memory[num])
	else:
		num = 'num2'
		memory.update({num:memory.get(num, '') + calInput})
		monitor.delete(0,END)
		monitor.insert(0, memory[num])


# change that it wont have any minus bugs
def operation(operator):
	global memory
	# save operation to dictionary
	memory.update({'op':operator})
	# write operation on the screen
	display = operator + ' ' + memory['num1']
	monitor.delete(0, END)
	monitor.insert(0, display)

#write a minus sign function
def minussign():
	global memory
	#check if first number should have minus sign
	if memory['num1'] == '':
		memory.update({'num1':'-'})
		monitor.delete(0, END)
		monitor.insert(0, memory['num1'])
	#delete minus sign in first num if needed
	elif memory['num1'] == '-':
		memory.update({'num1':''})
		monitor.delete(0, END)
	#make minus sign an operator
	elif memory['op'] == '':
		memory.update({'op':'-'})
		monitor.delete(0, END)
		monitor.insert(0, memory['op'] + ' ' + memory['num1'])
	#check for second num to have minus sign
	elif memory['op'] != '' and memory['num2'] == '':
		memory.update({'num2':'-'})
		monitor.delete(0, END)
		monitor.insert(0, memory['num2'])
	#delete minus sign from second num if needed
	elif memory['num2'] == '-':
		memory.update({'num2':''})
		monitor.delete(0, END)


# equal button function
def equal():
	global memory
	answer = ''
	oper = memory['op']
	try:
		a = float(memory['num1'])
		if memory['num2'] == '': 
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
		messagebox.showerror("Over Flow","Too big number, can't count")
	except ZeroDivisionError:
		messagebox.showwarning("Zero Division", "Can't divide by zero!")        
	except ValueError:
		messagebox.showwarning("Value Error", "Wrong input, try again!")

	monitor.delete(0, END)
	monitor.insert(0, answer)
	memory.update({'num1':monitor.get()})


# single number operations sin, cos, sqrt
def instant_operations(oper):
	global memory
	answer = ''
	memory.update({'num1':monitor.get()})
	try:
		a = float(memory['num1'])
		if oper == 'sqrt':
			if a>0:
				answer = sqrt(a) 
			else:
				messagebox.showerror("Wrong Value", "Can't count sqrt from minus value")
		elif oper == 'sin':
			answer = sin(a/180*3.14)
		elif oper == 'cos':
			answer = cos(a/180*3.14)
		monitor.delete(0, END)
		monitor.insert(0, answer)
	except ValueError:
		messagebox.showerror("No number", "You didn't give a number")


# delete all operation info
def clear_everything():
	monitor.delete(0,END)
	global memory
	memory.update({'num1':'','num2':'','op':''})


# delete memory
def clear_m():
	global memory
	memory.update({'m1':'','m2':'','m3':''})


# clear last input function
def clear():
	global memory
	if memory['num2'] != '':
		monitor.delete(0,END)
		monitor.insert(0, '{} {}'.format(memory['op'], memory['num1']))
		memory.update({'num2':''})
	elif memory['op'] != '':
		monitor.delete(0,END)
		monitor.insert(0, memory['num1'])
		memory.update({'op':''})
	else:
		monitor.delete(0,END)
		memory.update({'num1':''})


# write to memory
def memory_write(key):
	global memory
	value = ''
	if memory[key] == '':
		for x in monitor.get():
			if x.isdigit() or x == '.':
				value = value+x
		memory.update({key:value})
	else:
		monitor.delete(0,END)
		monitor.insert(0,memory[key])
		if memory['num1'] == '':
			memory.update({'num1':memory[key]})
		else:
			memory.update({'num2':memory[key]})


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
button_sub = Button(screen, text='-', height=3, width=2, command=minussign)
button_dot = Button(screen, text='.', height=2, width=3, command=dot)
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

button_c = Button(screen, text='C', height=3, width=2, command=clear)
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
