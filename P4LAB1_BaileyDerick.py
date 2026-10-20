# Name: Your Name
# Date: 10/20/2026
# Assignment: P4LAB1 - Turtle House

# Pseudocode:
# 1. Import the turtle library.
# 2. Create a turtle drawing window.
# 3. Change the background color.
# 4. Create a turtle and change its color and speed.
# 5. Use a for loop to draw a square for the house.
# 6. Move the turtle to the top of the square.
# 7. Use a while loop to draw a triangle for the roof.
# 8. Finish the drawing and keep the window open.

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("My Turtle House")

# Create the turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("darkgreen")
pen.pensize(4)
pen.speed(5)

# Draw the square (house) using a for loop
for side in range(4):
    pen.forward(150)
    pen.left(90)

# Move to the top-left corner of the square
pen.left(90)
pen.forward(150)
pen.right(90)

# Draw the triangle (roof) using a while loop
count = 0

while count < 3:
    pen.forward(150)
    pen.left(120)
    count += 1

# Hide the turtle and keep the window open
pen.hideturtle()
turtle.done()