from tkinter import *
from tkinter import Text
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import math


root = Tk()


root.title("Calculator")
root.iconbitmap("calc.ico")

root.resizable(0,0)

large_font = ('Verdana',11)

s = ttk.Style()
s.configure('TButton',width=7,foreground="black",weight = "bold")

e = Text(root,width=26,height=2,borderwidth=5,font=large_font,bg ="#C8F2F2")
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
e.configure(state="disabled")

def button_click(number):
	e.configure(state="normal")
	current = e.get('1.0', "end-1c")
	e.delete('1.0', END)
	if(current =='0.' and number =='.' and (e.compare("end-1c", "==", "1.0"))):
		e.insert('1.0','0.')
	else:
		e.insert('1.0',str(current)+str(number))
	e.configure(state="disabled")

def button_clear():
	e.configure(state="normal")
	e.delete('1.0', END)
	e.configure(state="disabled")	

def button_add():
	e.configure(state="normal")
	first_num = e.get('1.0', "end-1c")
	global f_num
	global operation
	operation = "addition"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0', END)
	e.configure(state="disabled")

def button_sub():
	e.configure(state="normal")
	first_num = e.get('1.0', "end-1c")
	global f_num
	global operation
	operation = "subtraction"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0', END)
	e.configure(state="disabled")

def button_mul():
	e.configure(state="normal")
	first_num = e.get('1.0', "end-1c")
	global f_num
	global operation
	operation = "multiply"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0', END)
	e.configure(state="disabled")

def button_div():
	e.configure(state="normal")
	first_num = e.get('1.0', "end-1c")
	global f_num
	global operation
	operation = "division"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0', END)
	e.configure(state="disabled")

def button_power():
	e.configure(state="normal")
	first_num = e.get('1.0',"end-1c")
	global f_num
	global operation
	operation = "power"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0',END)
	e.configure(state="disabled")

def button_sqrt():
	e.configure(state="normal")
	first_num = e.get('1.0',"end-1c")
	global f_num
	global operation
	operation = "sqrt"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0',END)
	if(f_num<0):
		messagebox.showerror("Error","Square root of only postiive numbers is allowed!")
	else:
		ans = f'{(f_num**0.5):g}'
		e.insert(1.0,ans)
	e.configure(state="disabled")

def button_fact():
	e.configure(state="normal")
	first_num = e.get('1.0',"end-1c")
	global f_num
	global operation
	operation = "fact"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0',END)
	try:
		ans = f'{(math.factorial(f_num)):.18g}'
		e.insert(1.0,ans)
	except ValueError:
		messagebox.showerror("Error","Factorial of only postiive integer is allowed!")
	
	e.configure(state="disabled")

	

def button_neg():
	e.configure(state="normal")
	first_num = e.get('1.0',"end-1c")
	global f_num
	global operation
	operation = "neg"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0',END)
	ans = f'{(f_num)*-1:g}'
	e.insert(1.0,ans)
	e.configure(state="disabled")

def button_10():
	e.configure(state="normal")
	first_num = e.get('1.0',"end-1c")
	global f_num
	global operation
	operation = "10^x"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0',END)
	ans = f'{(10**f_num):g}'
	e.insert(1.0,ans)
	e.configure(state="disabled")

def button_log():
	e.configure(state="normal")
	first_num = e.get('1.0',"end-1c")
	global f_num
	global operation
	operation = "log"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0',END)
	try:
		ans = f'{(math.log10(f_num)):g}'
		e.insert(1.0,ans)
	except ValueError:
		messagebox.showerror("Error","log of only postiive number is allowed!")
	
	e.configure(state="disabled")
		

def button_exp():
	e.configure(state="normal")
	first_num = e.get('1.0',"end-1c")
	global f_num
	global operation
	operation = "exp"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0',END)
	ans = f'{(math.exp(f_num)):g}'
	e.insert(1.0,ans)
	e.configure(state="disabled")

def button_mod():
	e.configure(state="normal")
	first_num = e.get('1.0',"end-1c")
	global f_num
	global operation
	operation = "mod"
	try:
		f_num = float(first_num)
	except ValueError:
		f_num = 0
	e.delete('1.0',END)
	e.configure(state="disabled")

def button_equal():
	e.configure(state="normal")
	try:
		second_num = e.get('1.0', "end-1c")
		e.delete('1.0', END)

		if(operation == "addition"):
			ans = f'{(f_num+float(second_num)):g}'
			e.insert(1.0,ans)

		if(operation == "subtraction"):
			ans = f'{(f_num-float(second_num)):g}'
			e.insert(1.0,ans)

		if(operation == "multiply"):
			ans = f'{(f_num*float(second_num)):g}'
			e.insert(1.0,ans)

		if(operation == "division"):
			try:
				ans = f'{(f_num/float(second_num)):g}'
				e.insert(1.0,ans)
			except ZeroDivisionError:
				messagebox.showerror("Error","Divide by zero! Not allowed.")
				
			
		if(operation == "power"):
			ans = f'{(f_num**float(second_num)):g}'
			e.insert(1.0,ans)

		if(operation == "mod"):
			ans = f'{(f_num % float(second_num)):g}'
			e.insert(1.0,ans)
	
	except NameError:
		return
	e.configure(state="disabled")
	

#define button

button_1 = ttk.Button(root,text="1",command= lambda:button_click(1))
button_2 = ttk.Button(root,text="2",command= lambda:button_click(2))
button_3 = ttk.Button(root,text="3",command= lambda:button_click(3))
button_4 = ttk.Button(root,text="4",command= lambda:button_click(4))
button_5 = ttk.Button(root,text="5",command= lambda:button_click(5))
button_6 = ttk.Button(root,text="6",command= lambda:button_click(6))
button_7 = ttk.Button(root,text="7",command= lambda:button_click(7))
button_8 = ttk.Button(root,text="8",command= lambda:button_click(8))
button_9 = ttk.Button(root,text="9",command= lambda:button_click(9))
button_0 = ttk.Button(root,text="0",command= lambda:button_click(0))

button_add = ttk.Button(root,text="+",command= button_add)
button_mul = ttk.Button(root,text="x",command= button_mul)
button_div = ttk.Button(root,text="/",command= button_div)
button_sub = ttk.Button(root,text="-",command= button_sub)

button_equal= ttk.Button(root,text="=",command= button_equal)
button_clear = ttk.Button(root,text="Clear",command= button_clear)

button_power = ttk.Button(root,text="x^y",command = button_power)
button_sqrt = ttk.Button(root,text=u'\u221A',command = button_sqrt)
button_fact = ttk.Button(root,text="x!",command = button_fact)
button_neg = ttk.Button(root,text='\u00b1',command = button_neg) 

button_10 = ttk.Button(root,text="10^x",command =  button_10)
button_log = ttk.Button(root,text="log",command = button_log)
button_exp = ttk.Button(root,text="e^x",command = button_exp)
button_point = ttk.Button(root,text=".",command = lambda:button_click('.'))
button_mod = ttk.Button(root,text="MOD",command = button_mod)

#put button on screen

button_1.grid(row=4,column=1)
button_2.grid(row=4,column=2)
button_3.grid(row=4,column=3)

button_4.grid(row=3,column=1)
button_5.grid(row=3,column=2)
button_6.grid(row=3,column=3)

button_7.grid(row=2,column=1)
button_8.grid(row=2,column=2)
button_9.grid(row=2,column=3)

button_0.grid(row=5,column=1,pady=(0,5))

button_add.grid(row=5,column=4,padx=(0,5),pady=(0,5))
button_sub.grid(row=4,column=4,padx=(0,5))
button_mul.grid(row=3,column=4,padx=(0,5))
button_div.grid(row=2,column=4,padx=(0,5))
button_mod.grid(row=1,column=4,padx=(0,5))

button_equal.grid(row=5,column=3,pady=(0,5))
button_point.grid(row=5,column=2,pady=(0,5))

button_clear.grid(row=1,column=0,padx=(5,0))
button_power.grid(row=2,column=0,padx=(5,0))
button_sqrt.grid(row=3,column=0,padx=(5,0))
button_fact.grid(row=4,column=0,padx=(5,0))
button_neg.grid(row=5,column=0,padx=(5,0),pady=(0,5))

button_10.grid(row=1,column=1)
button_log.grid(row=1,column=2)
button_exp.grid(row=1,column=3)



root.mainloop()