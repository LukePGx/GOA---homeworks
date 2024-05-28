from turtle import *

shape("arrow")
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door



forward(70)
color("yellow")
left(90)

forward(120)              #height of the door frfr
right(90)

forward(60)
right(90)

forward(120)


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("brown")
penup()
goto(60, 140)
pendown()
left(120)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
penup()
goto(140, 140)
pendown()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

exitonclick()