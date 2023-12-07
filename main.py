# Import Turtle
import turtle as trtl

# Declare Turtles.
# ONLY USE THE lines TURTLE!!!!
box = trtl.Turtle()
lines = trtl.Turtle()
wn = trtl.Screen()


# Setup Screen
def setupScreen():
    global wn
    wn.setup(1000, 700)


# Create the box on the screen
def setupBox():
    box.speed(0)
    box.penup()
    box.goto(-490, -300)
    box.pendown()
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.left(90)
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.hideturtle()



# Code for 80 point version goes here
def v80():
    lines.speed(0)
    lines.showturtle()
    lines.penup()
    lines.goto(-490, -300)
    lines.pendown()
    lines.goto(490, -250)
    startx = -490
    starty = -300
    endx = 490
    endy = -300

    for x in range(50):
        lines.goto(startx, starty)
        lines.goto(endx, endy)
        startx += 30
        endy += 20
        lines.goto(startx, starty)



# Code for the 90 point version goes here
def v90():
    # Calling the 80 point function - don't copy-paste from earlier method!!
    v80()
    lines.speed(0)
    lines.showturtle()
    lines.penup()
    lines.goto(490, -300)
    lines.pendown()
    lines.goto(490, -250)
    startx = 490
    starty = -300
    endx = -490
    endy = -300
    for x in range(50):
        lines.goto(startx, starty)
        lines.goto(endx, endy)
        startx += 30
        endy += 20
        lines.goto(startx, starty)


# Code for the 100 point version here
def v100():
    # Calling the 90 point function - don't copy-paste from earlier method!!
    v90()


# Code for the 110 point version here
def v110():
    # Calling the 100 point function - don't copy-paste from earlier method!!
    v100()


setupScreen()
setupBox()
v110()

wn.mainloop()
