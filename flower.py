from graphics import graphics                  
      
def main():       
    myCanvas = graphics(500, 500, "Flower")
      
    # The sky, grass, and stem
    myCanvas.rectangle(0, 400, 500, 100, "green")
    myCanvas.rectangle(0, 000, 500, 400, "light blue")
    myCanvas.line(250, 200, 250, 450, "dark green", 15)
      
    # The left and right flower petals
    myCanvas.triangle(250, 150, 250, 250, 400, 200, "purple")
    myCanvas.triangle(250, 150, 250, 250, 100, 200, "purple")
      
    # The up and down flower petals
    myCanvas.triangle(300, 200, 200, 200, 250, 50, "purple")
    myCanvas.triangle(300, 200, 200, 200, 250, 350, "purple")
      
    # The center of the flower
    myCanvas.ellipse(250, 200, 100, 100, "dark orange")
      
    myCanvas.draw()
      
main()