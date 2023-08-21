from graphics import graphics

def plus(canvas, x, y, w, h, color, thickness):
    '''     
    The plus function draw a plus sign centered at x, y.
    Parameter information:
       * canvas: the graphics object to draw the plus on. 
       * x and y: The coordinates for the center of the plus.
       * w and h: Width and height.
       * color: The fill color.
       * thickness: How thick the plus should be. 
    '''     
    canvas.line(x-(w/2), y, x+(w/2), y, color, thickness)
    canvas.line(x, y-(h/2), x, y+(h/2), color, thickness)

def main():  
    gui = graphics(500, 500, 'plusses') 
    gui.rectangle(0, 0, 500, 500, 'white')
    plus(gui, 250, 250, 400, 400, 'green', 50)
    plus(gui, 100, 100, 50, 50, 'blue', 10)
    gui.draw()

main()