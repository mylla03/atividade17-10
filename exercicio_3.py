import turtle

maxon = turtle.Turtle()
maxon.shape('triangle')
maxon.pensize(5)


for color in ['black', 'pink', 'blue', 'red']:
    maxon.color(color)
    maxon.forward(150)
    maxon.right(90)
maxon.penup()
maxon.forward(200)
maxon.pendown()
for color in ['black', 'pink', 'blue', 'red']:
    maxon.color(color)
    maxon.forward(150)
    maxon.right(90)