from tkinter import *

def submit(*args):
    print("The temperature value is " + str(scale.get()) + "degrees celcius")

window = Tk()

scale = Scale(window,
              from_=0, to=100,
              activebackground="black",
              length=600,
              font=('arial',25),
              tickinterval=10,
              resolution= 5,
              troughcolor="#69EAFF",
              fg="yellow",
              bg="black",
              command=submit,
              )

scale.set(((scale['from'] - scale['to']) / 2) + scale["to"] )
scale.pack()

window.mainloop()