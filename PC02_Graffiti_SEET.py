
#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Wilson Seet
September 4, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

t= Turtle()
t.color("green")
t.pensize(20)
t.forward(120)
t.up()


t.goto(50,-50)
t.pensize(5)
t.color("pink")
t.down()
t.forward(200)

t.up()
t.goto(100,-100)
t.pensize(65)
t.color("blue")
t.down()
t.backward(100)

t.up()
t.goto(200,200)
t.pensize(10)
t.color("red")
t.down()
t.circle(15)
t.up()

t.goto(150,150)
t.color("blue")
t.down()
t.begin_fill()
t.circle(25)
t.end_fill()

t.up()
t.goto(200,-200)
t.color("brown")
t.pensize(15)

t.up()
t.goto(-300,-100)
t.down()
t.pensize(5)
t.forward(50)
t.right(15)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(85)
t.forward(83)
t.right(55)
t.forward(8)