import turtle
from turtle import *
from turtle import Screen
    
def emptySquare():
      t = turtle.Turtle()
      for i in range(4):
         t.forward(50)
         t.right(90)  

    
def filledSquare():
<<<<<<< HEAD
    s = int(input("Enter the length of the side of the square: ")) 
    col = input("Enter the color name or hex value of color(# RRGGBB): ")
    t = turtle.Turtle()
    t.fillcolor(col)
    t.begin_fill()
    for i in range(4):
        t.forward(s)
        t.right(90)
    # Rotate clockwise by 90 degrees
    t.end_fill()

=======
  pass  # TODO
>>>>>>> b16f6313d33d97fe00334d60d554661e0576a562


def emptyCircle():
    t = turtle.Turtle()
    t.circle(100)

def filledCircle():
    t = turtle.Turtle()
    t.fillcolor('red')
    t.begin_fill()
    t.circle(100)
    t.end_fill()


while True:
    screen = Screen()
    answer = screen.textinput("Next Game","1 - Square:")
    if (answer is None):
        break
    elif (answer == '1'):
        emptySquare()
    elif (answer == '2'):
        filledSquare()
    elif (answer == '3'):
        emptyCircle()
    elif (answer == '4'):
<<<<<<< HEAD
        filledCircle()
=======
        filledCircle()
 
>>>>>>> b16f6313d33d97fe00334d60d554661e0576a562
