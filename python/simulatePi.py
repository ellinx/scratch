import turtle
import random

def draw(t, x, y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.dot(2, 'red')

turtle.getscreen().delay(0)
t = turtle.Pen()
r = 100
t.circle(r)
t.goto(r, 0)
t.goto(r, 2*r)
t.goto(-r, 2*r)
t.goto(-r, 0)
t.goto(0,0)
m, n = 0, 0
while n<100:
  x, y = random.random()*2*r-r, random.random()*2*r
  draw(t, x, y)
  if x**2+(y-r)**2<r**2:
    m += 1
  n += 1

print(f"pi is {m/n*4}")


turtle.done()
