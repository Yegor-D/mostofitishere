import turtle 

shelly = turtle.Turtle()

# exercises
shelly.forward(100) # moves shelly forward 100 steps
shelly.right(90) # turns shelly right 90 degrees
shelly.left(60) # turns shelly left 60 degrees
shelly.backward(100) # moves shelly backward 100 steps
shelly.color('red') # makes shelly draw in red
shelly.circle(10) # makes shelly draw in a circle of size 10
shelly.penup() # makes shelly lift pen
shelly.pendown() # makes shelly put the pen down to draw
shelly.reset() # clears screen and goest back to start position
shelly.goto(35,80) # move to x coordinate 35, y coordinate 80
shelly.hideturtle() # makes shelly not visible on the screen
shelly.shape('turtle') # changes shelly's shape to a turtleprint(shelly.xcor(), shely.ycor())
shelly.showturtle() # shows shelly again
print(shelly.xcor(), shelly.ycor()) # prints the x and y coordinates of shelly
turtle.screensize() #tells us our screen size