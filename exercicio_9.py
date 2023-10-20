import turtle
import random

maxon = turtle.Turtle()
colors = ['cyan','blue','yellow','green','pink','purple','red','orange']

for c in range(180):
    color = random.choice(colors)
    maxon.color(color)
    maxon.forward(2)
    maxon.right(2)