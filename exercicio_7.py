import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in range(4):
    turtle.left(90)
    turtle.backward(150)

turtle.backward(80)
turtle.backward(170)
turtle.right(90)

for _ in range(3):
  turtle.forward(150)
  turtle.left(90)