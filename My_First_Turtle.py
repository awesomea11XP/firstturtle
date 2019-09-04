import turtle



turtle.shape("turtle")
turtle.bgcolor("black")
turtle.color("yellow")
turtle.speed(100)

def square():
    for i in range (4):
        turtle.forward(300)
        turtle.right(90)


def spirel():
    for i in range (75):
        square()
        turtle.right(5)

def spirel2():
    for i in range (20):
        square()
        turtle.right(5)


spirel()





turtle.exitonclick()