import tkinter as tk

calculation = ""

#Addition Calculation
def add_calculation(symbol):
  global calculation
  calculation += str(symbol)
  text_result.delete(1.0, "end")
  text_result.insert(1.0, calculation)

def evalutate_calculation():
  global calculation
  try: 
    calculation = str(eval(calculation))
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
  except: 
    clear()
    text_result.insert(1.0, "Error")

def clear():
  global calculation
  calculation = ""
  text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("262x262") #Set Dimesions of calculator
root.configure(bg="grey")

text_result = tk.Text(root, height = 2, width = 16, font = ("Times New Roman", 24), bg = 'light green')
text_result.grid(columnspan=5)
#1
btn_1 = tk.Button(root, text = "1", command= lambda: add_calculation(1), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_1.grid(row = 2, column = 1)

#2
btn_2 = tk.Button(root, text = "2", command= lambda: add_calculation(2), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_2.grid(row = 2, column = 2)

#3
btn_3 = tk.Button(root, text = "3", command= lambda: add_calculation(3), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_3.grid(row = 2, column = 3)

#4
btn_4 = tk.Button(root, text = "4", command= lambda: add_calculation(4), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_4.grid(row = 3, column = 1)

#5
btn_5 = tk.Button(root, text = "5", command= lambda: add_calculation(5), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_5.grid(row = 3, column = 2)

#6
btn_6 = tk.Button(root, text = "6", command= lambda: add_calculation(6), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_6.grid(row = 3, column = 3)

#7
btn_7 = tk.Button(root, text = "7", command= lambda: add_calculation(7), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_7.grid(row = 4, column = 1)

#8
btn_8 = tk.Button(root, text = "8", command= lambda: add_calculation(8), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_8.grid(row = 4, column = 2)

#9
btn_9 = tk.Button(root, text = "9", command= lambda: add_calculation(9), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_9.grid(row = 4, column = 3)

#0
btn_0 = tk.Button(root, text = "0", command= lambda: add_calculation(0), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_0.grid(row = 5, column = 2)

#+
btn_plus = tk.Button(root, text = "+", command= lambda: add_calculation("+"), width = 5, font = ("Times New Roman", 14), bg = 'orange', activebackground='grey')
btn_plus.grid(row = 2, column = 4)

#-
btn_min = tk.Button(root, text = "-", command= lambda: add_calculation("-"), width = 5, font = ("Times New Roman", 14), bg = 'orange', activebackground='grey')
btn_min.grid(row = 3, column = 4)

#*
btn_mult = tk.Button(root, text = "*", command= lambda: add_calculation("*"), width = 5, font = ("Times New Roman", 14), bg = 'orange', activebackground='grey')
btn_mult.grid(row = 4, column = 4)

#/
btn_div = tk.Button(root, text = "/", command= lambda: add_calculation("/"), width = 5, font = ("Times New Roman", 14, ), bg = 'orange', activebackground='grey')
btn_div.grid(row = 5, column = 4)

#(
btn_openp = tk.Button(root, text = "(", command= lambda: add_calculation("("), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_openp.grid(row = 5, column = 1)

#)
btn_closep = tk.Button(root, text = ")", command= lambda: add_calculation(")"), width = 5, font = ("Times New Roman", 14), activebackground='grey')
btn_closep.grid(row = 5, column = 3)

#Clear
btn_clr = tk.Button(root, text = "Clr", command=clear, width = 11, font = ("Times New Roman", 14), activebackground='grey')
btn_clr.grid(row = 6, column = 1, columnspan = 2)

#=
btn_eqs = tk.Button(root, text = "=", command= evalutate_calculation, width = 11, font = ("Times New Roman", 14), activebackground='grey')
btn_eqs.grid(row = 6, column = 3, columnspan = 2)


root.mainloop()