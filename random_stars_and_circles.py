"""Purpose:Write a program that loops at random
numbers to draw about  ten crescents in random colors,
of random sizes and at random positions on the canvas.
Date: 4/9/19. author: Gideon Agyemang Prempeh."""

from turtle import * 
import random

tracer(-1)

#stars
#================================================================

def stars(x, y, size, star_color):
    
    fillcolor(star_color)

    penup()
    goto(x, y)
    pendown()
    
    begin_fill()
    for i in range(5):
        forward(size)
        left(145)
    end_fill()
    penup()

#crescents
#=================================================================

def crescent(x, y, size, crescent_color):


    fillcolor(crescent_color)
    
    penup()
    goto(x, y)
    pendown()

    crescent_length = size
    crescent_length_friday = crescent_length + (crescent_length/10)

    begin_fill()
    circle(crescent_length, extent = 180)
    right(25)
    circle(crescent_length_friday, extent = -130)
    end_fill()
    penup()
    
colormode(255)
#loops for star and cresecents
for count in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 150)
    size = random.randint(10, 70)
    
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    star_color = (R, G, B)
    
    stars(x, y, size, star_color)

for count in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 150)
    size = random.randint(10, 70)
    
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    crescent_color = (R, G, B)

    crescent(x, y, size, crescent_color)

penup()
goto(-70, 225)
pencolor( (0,0,0) ) 

pendown()
write("Gideon Agyemang Prempeh", font = ("Arial", "24", "normal"))

getcanvas().postscript( file = "random_stars_and_circles.eps")
