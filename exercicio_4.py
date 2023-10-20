import turtle
import random

maxon = turtle.Turtle()
colors = ['plum', 'purple', 'blue','aqua']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    maxon.color(color)
    maxon.forward(200)
    maxon.left(120)