from graphics import graphics    

def mouse_left(c, x, y): 
   c.ellipse(x, y, 100, 100, "orange")



def main():
    canvas = graphics(500, 350, 'ball drop')
    
    canvas.set_left_click_action(mouse_left)
    y = -100
    # x = 100
    while True:
        canvas.clear()
        canvas.rectangle(0, 0, 500, 350, 'Orange')
        canvas.ellipse(259, y, 75, 75, 'red')
        y+=5
        # x-=5
        #canvas.ellipse(canvas.mouse_x, canvas.mouse_y, 75, 75, 'blue')
        canvas.update_frame(24)

    

main()