from turtle import *

#we want to paint a house

#step 1 : draw a square
speed(30)

width (7)
color ("purple")
forward (200)
left (90)
forward (200)
left (90)
forward(200)
left (90)
forward (200)
#end of square


#drawing a door

left(90)
forward(70)
color ("yellow")
begin_fill()
left(90)
forward (120) #height of the door
right (90)
forward (60)
right(90)
forward (120)
end_fill()

# end of door

penup()
goto (200,200)
pendown()

# drawing a roof

color ("red")
begin_fill ()
right(150)
forward (200)
left (120)
forward (200)
end_fill()

#drawing windows

penup()
goto (0,100)
color ("blue")
begin_fill ()
pendown()
left(120)
forward (40)
left (90)
forward (70)
left (90)
forward (40)
end_fill()

penup()
goto(200,100)
begin_fill()
pendown()
forward(40)
right(90)
forward(70)
right (90)
forward (40)
end_fill ()


exitonclick()