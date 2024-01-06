import turtle

t = turtle.Turtle()
n = 20
r = 10
b = 0

for i in range(n,1,-1):
  t.begin_fill()

  if b==0 :
    t.color("Red") 
    b = 1
  elif b==1:
    t.color("Blue")
    b = 2
  else:
    t.color("White")
    b = 0
  
  t.circle(r*i)
  t.end_fill()
  t.up()
  t.sety((n+1)*r - r*i)
  t.down()

print("Press any key to exit...")
input()
