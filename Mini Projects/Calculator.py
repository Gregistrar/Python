import tkinter as tk
import tkinter.font
import math


class PyCalc:
    def __init__(self, master):
        self.gui = master
        self.gui.title("Python Calculator")
        self.gui.configure(background="light blue")
        self.expression = ""
        self.equation = tk.StringVar()
        self.equation.set('Enter your expression')

        self.screen = tk.Entry(self.gui, textvariable=self.equation, width=50, background='light green')
        self.screen.grid(row=0, column=0, columnspan=4, ipadx=5, pady=5)
        self.screen.configure(state='normal')
        self.gui.geometry("420x420")
        self.custom_font = tkinter.font.Font(family="Helvetica", weight='bold', size=9)

        # Top Row Buttons
        clearbut = tk.Button(self.gui, text='Clear', fg='white', bg='black',
                             command=self.clear, height=2, width=10, font=self.custom_font)
        clearbut.grid(row=2, column=2)

        backspace = tk.Button(self.gui, text='Back', fg='white', bg='black',
                              command=lambda: self.press(7), height=2, width=10, font=self.custom_font)
        backspace.grid(row=2, column=3)

        # 2nd Row Buttons
        fraction = tk.Button(self.gui, text=' 1/x ', fg='white', bg='black',
                             command=lambda: self.special_functions("fraction"), height=2, width=10,
                             font=self.custom_font)
        fraction.grid(row=3, column=0)

        power = tk.Button(self.gui, text=' x^2 ', fg='white', bg='black',
                          command=lambda: self.special_functions("power"), height=2, width=10, font=self.custom_font)
        power.grid(row=3, column=1)

        square = tk.Button(self.gui, text=' SqRt ', fg='white', bg='black',
                           command=lambda: self.special_functions("sqroot"), height=2, width=10, font=self.custom_font)
        square.grid(row=3, column=2)

        divide = tk.Button(self.gui, text=' / ', fg='white', bg='black',
                           command=lambda: self.press("/"), height=2, width=10, font=self.custom_font)
        divide.grid(row=3, column=3)

        # 3rd Row Buttons
        button7 = tk.Button(self.gui, text=' 7 ', fg='white', bg='black',
                            command=lambda: self.press(7), height=2, width=10, font=self.custom_font)
        button7.grid(row=4, column=0)

        button8 = tk.Button(self.gui, text=' 8 ', fg='white', bg='black',
                            command=lambda: self.press(8), height=2, width=10, font=self.custom_font)
        button8.grid(row=4, column=1)

        button9 = tk.Button(self.gui, text=' 9 ', fg='white', bg='black',
                            command=lambda: self.press(9), height=2, width=10, font=self.custom_font)
        button9.grid(row=4, column=2)

        multiply = tk.Button(self.gui, text=' * ', fg='white', bg='black',
                             command=lambda: self.press("*"), height=2, width=10, font=self.custom_font)
        multiply.grid(row=4, column=3)

        # 4th Row Buttons
        button4 = tk.Button(self.gui, text=' 4 ', fg='white', bg='black',
                            command=lambda: self.press(4), height=2, width=10, font=self.custom_font)
        button4.grid(row=5, column=0)

        button5 = tk.Button(self.gui, text=' 5 ', fg='white', bg='black',
                            command=lambda: self.press(5), height=2, width=10, font=self.custom_font)
        button5.grid(row=5, column=1)

        button6 = tk.Button(self.gui, text=' 6 ', fg='white', bg='black',
                            command=lambda: self.press(6), height=2, width=10, font=self.custom_font)
        button6.grid(row=5, column=2)

        minus = tk.Button(self.gui, text=' - ', fg='white', bg='black',
                          command=lambda: self.press("-"), height=2, width=10, font=self.custom_font)
        minus.grid(row=5, column=3)

        # 5th Row Buttons
        button1 = tk.Button(self.gui, text=' 1 ', fg='white', bg='black',
                            command=lambda: self.press(1), height=2, width=10, font=self.custom_font)
        button1.grid(row=6, column=0)

        button2 = tk.Button(self.gui, text=' 2 ', fg='white', bg='black',
                            command=lambda: self.press(2), height=2, width=10, font=self.custom_font)
        button2.grid(row=6, column=1)

        button3 = tk.Button(self.gui, text=' 3 ', fg='white', bg='black',
                            command=lambda: self.press(3), height=2, width=10, font=self.custom_font)
        button3.grid(row=6, column=2)

        plus = tk.Button(self.gui, text=' + ', fg='white', bg='black',
                         command=lambda: self.press("+"), height=2, width=10, font=self.custom_font)
        plus.grid(row=6, column=3)

        # 6th Row Buttons
        negate = tk.Button(self.gui, text=' +/- ', fg='white', bg='black',
                           command=self.plusminus, height=2, width=10, font=self.custom_font)
        negate.grid(row=7, column=0)

        button0 = tk.Button(self.gui, text=' 0 ', fg='white', bg='black',
                            command=lambda: self.press(0), height=2, width=10, font=self.custom_font)
        button0.grid(row=7, column=1)

        decimal = tk.Button(self.gui, text=' . ', fg='white', bg='black',
                            command=lambda: self.press('.'), height=2, width=10, font=self.custom_font)
        decimal.grid(row=7, column=2)

        equal = tk.Button(self.gui, text=' = ', fg='white', bg='black',
                          command=self.equalpress, height=2, width=10, font=self.custom_font)
        equal.grid(row=7, column=3)

    def clear(self):
        self.expression = ""
        self.equation.set("")

    def press(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except:
            self.equation.set(" error ")
            self.expression = ""

    def special_functions(self, special_func):
        if special_func == 'sqroot':
            self.expression = math.sqrt(float(self.expression))
            self.equation.set(self.expression)
        elif special_func == 'power':
            self.expression =  math.pow(float(self.expression), 2)
            self.equation.set(self.expression)
        elif special_func == 'fraction':
            self.expression = (1 / int(self.expression))
            self.equation.set(self.expression)

    def plusminus(self):
        if self.expression.startswith('-'):
            self.expression = abs(int(self.expression))
        else:
            self.expression = '-' + self.expression
            self.equation.set(self.expression)


root = tk.Tk()
my_gui = PyCalc(root)
root.mainloop()


# Functions to create
pct_calc = 0
clear_entry = 0
pi_calc = 0
squared_calc = 0
sqrt_calc = 0



# Attempting to loop button creation
# button_list = {'%': pct_calc, 'CE': clear_entry, 'Clear': clear, 'Back': backspace,
#                'Pi': pi_calc, 'x^2': squared_calc, 'SqRt': sqrt_calc, '/': press('/'),
#                '7': press('7'), '8': press('8'), '9': press('9'), 'X': press('*'),
#                '4': press('4'), '5': press('5'), '6': press('6'), '-': press('-'),
#                '1': press('1'), '2': press('2'), '3': press('3'), '+': press('+'),
#                '+/-': plusminus, '0': press('0'), '.': press('.'), '=': equalpress()}
# buttons = []
# for key, val in button_list.items():
#     button = tk.Button(gui, text=key, fg='white', bg='black', command=val)
#     buttons.append(button)









