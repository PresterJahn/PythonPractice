import turtle
import math

# predefine the diamond side length
SIDE_LENGTH = 100

# predefine the fill color
FILL_COLOR = "blue"

# setup the turtle window
turtle.setup(500, 600)

# setup the turtle
turtle.hideturtle()
turtle.fillcolor(FILL_COLOR)
turtle.speed(0)

# calculate the half-diagonal so both diamonds meet at a single point in the center
half_diagonal = SIDE_LENGTH / math.sqrt(2)

# draw the left-side diamond first using the predefined SIDE_LENGTH
turtle.penup()
turtle.goto(-half_diagonal, -half_diagonal)
turtle.setheading(45)
turtle.pendown()

turtle.begin_fill()
for _ in range(4):
    turtle.forward(SIDE_LENGTH)
    turtle.left(90)
turtle.end_fill()

# draw the right-side diamond next
turtle.penup()
turtle.goto(half_diagonal, -half_diagonal)
turtle.setheading(45)
turtle.pendown()

turtle.begin_fill()
for _ in range(4):
    turtle.forward(SIDE_LENGTH)
    turtle.left(90)
turtle.end_fill()

turtle.done()