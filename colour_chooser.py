from tkinter import *
from tkinter import colorchooser


def colour():
    colour = colorchooser.askcolor()
    print(colour)
    colourHex = colour[1]
    print(colourHex)
    window.configure(background=colourHex)
    
window = Tk()

window.geometry("600x600")
change_colour = Button(text='choose colour!', command=colour)
change_colour.pack()

window.mainloop()