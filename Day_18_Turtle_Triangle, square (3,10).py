from turtle import Turtle, Screen
import random
timmy = Turtle()
screen = Screen()
colors = ['red','green','blue','deep pink','orange red','deep sky blue','purple','black']

def draw_shape(num_sides):
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(360/num_sides)

for _ in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(_)


screen.exitonclick()

