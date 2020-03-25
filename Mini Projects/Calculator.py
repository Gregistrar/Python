import tkinter as tk
import tkinter.font

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def plusminus():
    global expression
    if expression.startswith('-'):
        expression
    else:
        equation.set('-' + expression)


def clear():
    global expression
    expression = ""
    equation.set("")


gui = tk.Tk()
gui.configure(background="light blue")
gui.title("Python Calculator")
custom_font = tkinter.font.Font(family="Helvetica", weight='bold', size=10)
gui.geometry("420x420")
equation = tk.StringVar()
expression_field = tk.Entry(gui, textvariable=equation, width=32)
expression_field.grid(columnspan=4, ipadx=60)
equation.set('Enter your expression')







# Top Row Buttons
divide = tk.Button(gui, text=' / ', fg='white', bg='black',
                command=lambda: press("/"), height=2, width=10, font=custom_font)
divide.grid(row=2, column=2)

clear = tk.Button(gui, text='Clear', fg='white', bg='black',
               command=clear, height=2, width=10, font=custom_font)
clear.grid(row=2, column=3)

# 2nd Row Buttons
button7 = tk.Button(gui, text=' 7 ', fg='white', bg='black',
                 command=lambda: press(7), height=2, width=10)
button7.grid(row=3, column=0)

button8 = tk.Button(gui, text=' 8 ', fg='white', bg='black',
                 command=lambda: press(8), height=2, width=10)
button8.grid(row=3, column=1)

button9 = tk.Button(gui, text=' 9 ', fg='white', bg='black',
                 command=lambda: press(9), height=2, width=10)
button9.grid(row=3, column=2)

multiply = tk.Button(gui, text=' * ', fg='white', bg='black',
                  command=lambda: press("*"), height=2, width=10)
multiply.grid(row=3, column=3)

# 3rd Row Buttons
button4 = tk.Button(gui, text=' 4 ', fg='white', bg='black',
                 command=lambda: press(4), height=2, width=10)
button4.grid(row=4, column=0)

button5 = tk.Button(gui, text=' 5 ', fg='white', bg='black',
                 command=lambda: press(5), height=2, width=10)
button5.grid(row=4, column=1)

button6 = tk.Button(gui, text=' 6 ', fg='white', bg='black',
                 command=lambda: press(6), height=2, width=10)
button6.grid(row=4, column=2)

minus = tk.Button(gui, text=' - ', fg='white', bg='black',
               command=lambda: press("-"), height=2, width=10)
minus.grid(row=4, column=3)

# 4th Row Buttons
button1 = tk.Button(gui, text=' 1 ', fg='white', bg='black',
                 command=lambda: press(1), height=2, width=10)
button1.grid(row=5, column=0)

button2 = tk.Button(gui, text=' 2 ', fg='white', bg='black',
                 command=lambda: press(2), height=2, width=10)
button2.grid(row=5, column=1)

button3 = tk.Button(gui, text=' 3 ', fg='white', bg='black',
                 command=lambda: press(3), height=2, width=10)
button3.grid(row=5, column=2)

plus = tk.Button(gui, text=' + ', fg='white', bg='black',
              command=lambda: press("+"), height=2, width=10)
plus.grid(row=5, column=3)

# 5th Row Buttons
negate = tk.Button(gui, text=' +/- ', fg='white', bg='black',
                command=plusminus, height=2, width=10)
negate.grid(row=6, column=0)

button0 = tk.Button(gui, text=' 0 ', fg='white', bg='black',
                 command=lambda: press(0), height=2, width=10)
button0.grid(row=6, column=1)

equal = tk.Button(gui, text=' = ', fg='white', bg='black',
               command=equalpress, height=2, width=10)
equal.grid(row=6, column=3)




gui.mainloop()




