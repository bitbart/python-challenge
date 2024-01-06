import turtle, random
screen = turtle.Screen()
screen.colormode(255)

t = turtle.Turtle()

border_left = -250
border_right = 250
border_up = 200
border_down = -200

def keyLeft():
  global dx
  if dx>0: 
    dx = dx-0.1
  else:
    dx = dx+0.1

def keyRight():
  global dx
  if dx>0: 
    dx = dx+0.1
  else:
    dx = dx-0.1

def keyUp():
  global dy
  if dy>0: 
    dy = dy+0.1
  else:
    dy = dy-0.1
  
def keyDown():
  global dy
  if dy>0: 
    dy = dy-0.1
  else:
    dy = dy+0.1
  
def changeColor():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  ball.color(r,g,b)

screen.onkey(keyLeft, "Left")
screen.onkey(keyRight, "Right")
screen.onkey(keyUp, "Up")
screen.onkey(keyDown, "Down")
screen.listen()

# draw external box
t.speed(20)
t.up()
t.setpos(border_left,border_down)
t.down()
t.forward(border_right-border_left)
t.left(90)
t.forward(border_up-border_down)
t.left(90)
t.forward(border_right-border_left)
t.left(90)
t.forward(border_up-border_down)

r = 20
b = True

# set ball initial position
ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("Red")
ball.setposition(0,0)
ball_radius = 10 # approximated!!

dx = 1
dy = 1

while True:
  (x,y) = ball.position()
  
  if x<border_left+ball_radius or x>border_right-ball_radius: 
    dx = -dx
    changeColor()
  
  if y<border_down+ball_radius or y>border_up-ball_radius: 
    dy = -dy
    changeColor()

  ball.setposition(x+dx,y+dy)

# turtle.mainloop()
