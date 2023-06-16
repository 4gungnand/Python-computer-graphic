import turtle
import time

# create a Turtle object
t = turtle.Turtle()

# set the speed of the turtle
t.speed(0)

# define the start position and length of the line
start_pos = (-200, 0)
line_length = 400

# define the gradient of the line
gradient = 0.5

# define the time delay in seconds
delay = 2

# move the turtle to the start position
t.penup()
t.goto(start_pos)
t.pendown()

# set the color of the line
t.color("black")

# draw the line
for i in range(line_length):
    # calculate the color of the line based on the gradient
    r = int(255 * (1 - gradient * i / line_length))
    g = int(255 * gradient * i / line_length)
    b = 0
    t.pencolor(r, g, b)
    
    # move the turtle forward one step
    t.forward(1)
    
    # pause the program for the time delay
    time.sleep(delay / line_length)

# exit the program when the user clicks the screen
turtle.exitonclick()