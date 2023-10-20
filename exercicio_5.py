import turtle

maxon = turtle.Turtle()
maxon.shape('arrow')
maxon.color('blue')

for _ in [1, 2, 3]:
    maxon.forward(90)
    maxon.right(120)

maxon = turtle.Turtle()
maxon.shape('turtle')
maxon.color('pink')

for _ in [1, 2, 3, 4]:
  maxon.forward(130)
  maxon.right(90)