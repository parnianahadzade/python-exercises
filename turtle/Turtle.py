import turtle

x = turtle.Turtle()
x.color('blue')
x.speed(0)

# square
# x.shape('square')
x.forward(50)
x.left(90)
x.forward(50)
x.left(90)
x.forward(50)
x.left(90)
x.forward(50)

x.penup()
x.forward(100)
x.pendown()

# rectangle
# x.begin_fill()
x.forward(50)
x.left(90)
x.forward(100)
x.left(90)
x.forward(50)
x.left(90)
x.forward(100)
# x.end_fill()

x.penup()
x.forward(100)
x.pendown()

#diamond
# x.speed(1)
x.left(30)
x.forward(50)
x.left(120)
x.forward(50)
x.left(60)
x.forward(50)
x.left(120)
x.forward(50)


turtle.done()

