import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    timmy = turtle.Turtle()
    timmy.pendown()
    timmy.speed(0)
    inf = 100
    timmy.pensize(10)
    for i in range(inf + 1):
        inf = i
        for j in range(360):
            timmy.forward(1)
            timmy.left(1)
        color = simpledialog.askstring(title="Color Picker (super)",prompt="What color would you like to use? (red) (blue) (green) (random)")
        if color == "red":
            timmy.pencolor(color)
        elif color == "blue":
            timmy.pencolor(color)
        elif color == "green":
            timmy.pencolor(color)
        elif color == "super":
            for k in range(360):
                timmy.pencolor(get_random_color())
                timmy.forward(1)
                timmy.left(1)
        else:
            timmy.pencolor(get_random_color())
    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
