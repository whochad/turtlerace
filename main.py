
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'black', 'blue', 'green', 'yellow', 'purple']
all_turtles = []

user_bet = screen.textinput(title='Make  your bet', prompt='Which turtle will win the race? Enter a color:\n'
                                                           '(red, black, blue, green, yellow, purple)')
y_positions = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You\'ve won! The {winning_color} turtle has won the race')

            else:
                print(f'You\'ve Lost! The {winning_color} turtle has won the race')
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
