import tkinter as tk
from tkinter import ttk


class Calculator():
    def __init__(self,root):
        # Window properties
        self.root = root
        self.root.title("Calculator")
        self.root.geometry('180x200+100+150')
        self.root.resizable(True, True)

        # Set the theme of the window
        self.root.config(bg='black')
        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TEntry", fieldbackground="black")
       
        Titlelabel = tk.Label(root, fg = '#ff6700', bg='black' , font = 'none 10 bold underline' ,text = 'Python Calculator', compound="center")
        Titlelabel.place(relx=0.5, rely=0.1, anchor='center',)
        Titlelabel.grid(row=1, columnspan=5)
        
        self.history = []
        self.calculator_entry_var = tk.StringVar()
    
        # calculator entry and results label
        self.calculator_entry = ttk.Entry(root, textvariable=self.calculator_entry_var,foreground='yellow')
        self.calculator_entry.place(relx=0.5, rely=0.2, anchor='center',)
        self.calculator_entry.grid(row=2, columnspan=5)

        # Button 7
        button_seven_button = tk.Button(self.root, text="7", bg='grey', fg='white', command=self.button_seven)
        button_seven_button.grid(row=3, column=1, padx=5, pady=5)

        # Button 8
        button_eight_button = tk.Button(self.root, text="8", bg='grey', fg='white', command=self.button_eight)
        button_eight_button.grid(row=3, column=2, padx=5, pady=5)

        # Button 9
        button_nine_button = tk.Button(self.root, text="9", bg='grey', fg='white', command=self.button_nine)
        button_nine_button.grid(row=3, column=3, padx=5, pady=5)

        # Button /
        button_divide_button = tk.Button(self.root, text="/", bg='green', fg='white', command=self.button_divide)
        button_divide_button.grid(row=3, column=4, padx=10, pady=5)

        # Button 4
        button_four_button = tk.Button(self.root, text="4", bg='grey', fg='white', command=self.button_four)
        button_four_button.grid(row=4, column=1, padx=10, pady=5)

        # Button 5
        button_five_button = tk.Button(self.root, text="5", bg='grey', fg='white', command=self.button_five)
        button_five_button.grid(row=4, column=2, padx=10, pady=5)

        # Button 6
        button_six_button = tk.Button(self.root, text="6", bg='grey', fg='white', command=self.button_six)
        button_six_button.grid(row=4, column=3, padx=10, pady=5)

        # Button *
        button_multiply_button = tk.Button(self.root, text="*", bg='green', fg='yellow', command=self.button_multiply)
        button_multiply_button.grid(row=4, column=4, padx=10, pady=5)

        # Button 1
        button_one_button = tk.Button(self.root, text="1", bg='grey', fg='white', command=self.button_one)
        button_one_button.grid(row=5, column=1, padx=10, pady=5)

        # Button 2
        button_two_button = tk.Button(self.root, text="2", bg='grey', fg='white', command=self.button_two)
        button_two_button.grid(row=5, column=2, padx=10, pady=5)

        # Button 3
        button_three_button = tk.Button(self.root, text="3", bg='grey', fg='white', command=self.button_three)
        button_three_button.grid(row=5, column=3, padx=10, pady=5)

        # Button -
        button_minus_button = tk.Button(self.root, text="-", bg='green', fg='white', command=self.button_minus)
        button_minus_button.grid(row=5, column=4, padx=10, pady=5)

        # Button clear
        button_clear_button = tk.Button(self.root, text="C", bg='red', fg='white', command=self.button_clear)
        button_clear_button.grid(row=6, column=1, padx=10, pady=5)

        # Button 0
        button_zero_button = tk.Button(self.root, text="0", bg='grey', fg='white', command=self.button_zero)
        button_zero_button.grid(row=6, column=2, padx=10, pady=5)

        # Button +
        button_plus_button = tk.Button(self.root, text="+", bg='green', fg='white', command=self.button_plus)
        button_plus_button.grid(row=6, column=3, padx=10, pady=5)

        # Button =
        button_equal_button = tk.Button(self.root, text="=", bg='red', fg='white', command=self.button_equal)
        button_equal_button.grid(row=6, column=4, padx=10, pady=5)

        # Button press 0
    def button_zero(self):
        self.calculator_entry.insert("", "0")
         
        # Button press 1
    def button_one(self):
        self.calculator_entry.insert("", "1")

        # Button press 2
    def button_two(self):
        self.calculator_entry.insert("", "2")

        # Button press 3
    def button_three(self):
        self.calculator_entry.insert("", "3")

        # Button press 4
    def button_four(self):
        self.calculator_entry.insert("", "4") 

        # Button press 5
    def button_five(self):
        self.calculator_entry.insert("", "5")

        # Button press 6
    def button_six(self):
        self.calculator_entry.insert("", "6")

        # Button press 7
    def button_seven(self):
        self.calculator_entry.insert("", "7")

        # Button press 8
    def button_eight(self):
        self.calculator_entry.insert("", "8")

        # Button press 9
    def button_nine(self):
        self.calculator_entry.insert("", "9")

        # Button press '+'
    def button_plus(self):
        self.calculator_entry.insert("", "+")

        # Button press '-'
    def button_minus(self):
        self.calculator_entry.insert("", "-")
        
        # Button press '*'
    def button_multiply(self):
        self.calculator_entry.insert("", "*")

        # Button press '/'
    def button_divide(self):
        self.calculator_entry.insert("", "/")

        # Button press 'Clear'
    def button_clear(self):
        self.calculator_entry.delete(0,99)

        # Button press '='
    def button_equal(self):
        try:
            value = self.calculator_entry_var.get()
            print(value)
            total = eval(value)
            print(total)
            self.calculator_entry.delete(0, "end")
            self.calculator_entry.insert("end", total)
            self.history.append(total)

        except Exception as e:
            print(f"there's an error: {e}")
            self.calculator_entry.delete(0, "end")
            e = 'error: ' + str(e)
            self.calculator_entry.insert("end", e)

    
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)

    # Configure row and column weights for dynamic sizing
    for i in range(7):  # Assuming you have 6 rows
        root.grid_rowconfigure(i, weight=1)
    for i in range(5):  # Assuming you have 5 columns
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()