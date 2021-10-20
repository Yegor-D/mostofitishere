import turtle
shelly = turtle.Turtle()


win_width, win_height, bg_color = 2000, 2000, 'grey'

turtle.setup()
turtle.screensize(win_width, win_height, bg_color)


def square(s):
  for i in range(4):
    shelly.forward(s)
    shelly.left(90)

square(100)
shelly.forward(100)
square(200)
shelly.forward(100)
square(300)