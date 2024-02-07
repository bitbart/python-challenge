import turtle

screen = turtle.Screen()
screen.colormode(255)

t = turtle.Turtle()

def rotateRight():
  t.right(5)

def rotateLeft():
  t.left(5)
  
screen.onkey(rotateLeft, "Left")
screen.onkey(rotateRight, "Right")

screen.listen()

t.speed(20)
t.up()
t.setpos(-200,-200)
t.down()
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)

t.up()
t.setpos(0,0)
t.down()
t.speed(1)

b = True
score = 0

while b:
  t.forward(1)
  score = score + 1
  (x,y) = t.position()
  # print(x,y)
  if x<-200 or x>200 or y<-200 or y>200:
    b = False

turtle.color("Red")
turtle.write("Game over", align="center", font=("Courier", 32))
turtle.setposition(0, -50)
turtle.write("Score =" + str(score), align="center", font=("Courier", 8))
print("Final score: " + str(score))

print("Click mouse to exit...")
turtle.exitonclick()
