"""

author SubashPalvel

"""

# 1 import statements

import turtle
import time

# 2 Setting properties of the screen

screen = turtle.Screen()  # turtle screen
screen.bgcolor("white")  # background of the screen
screen.setup(width=600, height=600)  # geometry of the GUI
screen.title("Clock by Subash")  # title of the GUI
screen.tracer(0)  # tracer for the GUI

# 3 Setting properties of timing

Timing = turtle.Turtle()  # the turtle
Timing.hideturtle()  # make the turtle invisible
Timing.speed(0)  # setting the speed to 0
Timing

# 4 defining Clock function


def Clock(Hour, Minute, Second, Timing):  # function with 4 parameters

    Timing.up()  # not ready to draw
    Timing.goto(0, 210)  # positioning the turtle
    Timing.setheading(180)  # setting the heading to 180
    Timing.color("red")  # setting the color of the pen to red
    Timing.pendown()  # starting to draw
    Timing.circle(210)  # a circle with the radius 210

    Timing.up()  # not ready to draw
    Timing.goto(0, 0)  # positioning the turtle
    Timing.setheading(90)  # setting the heading to 90 in newer version

    for z in range(12):  # loop
        Timing.fd(190)  # moving forward at 190 units
        Timing.pendown()  # starting to draw
        Timing.fd(20)  # forward at 20
        Timing.penup()  # not ready to draw
        Timing.goto(0, 0)  # positioning the turtle
        Timing.rt(30)  # right at an angle of 30 degrees

    hands = [
        ("black", 80, 12),
        ("black", 150, 60),
        ("black", 110, 60),
    ]  # the color and the hands set
    time_set = (Hour, Minute, Second)  # setting the time

    for hand in hands:  # loop
        time_part = time_set[
            hands.index(hand)
        ]  # time part in the hand index in hands of time_Set
        angle = (time_part / hand[2]) * 360  # setting the angle for the clock
        Timing.penup()  # not ready to draw
        Timing.goto(0, 0)  # positioning the turtle
        Timing.color(hand[0])  # setting the color of the hand
        Timing.setheading(90)  # same as seth(90)
        Timing.rt(angle)  # right at an angle of "right"
        Timing.pendown()  # ready to draw
        Timing.fd(hand[1])  # forward at a unit of 1st index of the hand var


# 5 Running Clock function

while True:
    Hour = int(time.strftime("%I"))  # setting the hour from the time module
    Minute = int(time.strftime("%M"))  # setting the minute from the time module
    Second = int(time.strftime("%S"))  # setting the second as above

    Clock(
        Hour, Minute, Second, Timing
    )  # calling the ghanta_bana() function with the given parameters
    screen.update()  # updating the scren
    time.sleep(1)  # making the code sleep for a second with the time module
    Timing.clear()  # clearing the pen
