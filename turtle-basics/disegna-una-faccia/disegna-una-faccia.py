import turtle;
from turtle import Screen;

screen = Screen()
screen.colormode(255)

t = turtle.Turtle()
t.speed(10)

# faccia
t.up()
t.color("pink")
t.fillcolor("pink")
t.setpos(0,-50)
t.down()
t.begin_fill()
t.circle(120)
t.end_fill()

# bocca
t.up()
t.setpos(0,0)
t.down()
t.color("red")
t.circle(50)

# cancello mezza bocca
t.up()
t.setpos(-50,40)
t.down()
t.color("pink")
t.fillcolor("pink")
t.begin_fill()
t.forward(105)
t.left(90)
t.forward(61)
t.left(90)
t.forward(110)
t.left(90)
t.forward(61)
t.left(90)
t.end_fill()

t.up()
t.setpos(-50,100)
t.down()

# occhio sx
t.color("blue")
t.dot(10)
t.color("black")
t.up()
t.sety(80)
t.down()
t.circle(20)

t.up()
t.setpos(50,100)
t.down()

# occhio dx
t.color("blue")
t.dot(10)
t.color("black")
t.up()
t.sety(80)
t.down()
t.circle(20)

t.ht()

print("Press any key to exit...")
input()
