import turtle
t = turtle
t.penup()
#lolipop
t.setheading(0)
t.goto(100, 100)
t.fillcolor('red')
t.begin_fill()
t.pendown()
t.circle(50)
t.pensize()
t.end_fill()
t.right(90)
t.color('gray')
t.pensize(10)
t.forward(100)
t.penup()
#pinetree
t.setheading(0)
t.goto(-100, -100)
t.fillcolor('green')
t.begin_fill()
t.pendown()
t.pensize(1)
t.right(45)
t.forward(40)
t.setheading(180)
t.forward(20)
t.setheading(0)
t.right(45)
t.forward(20)
t.setheading(0)
t.setheading(180)
t.forward(20)
t.setheading(0)
t.right(45)
t.forward(20)
t.setheading(180)
t.forward(34)
t.end_fill()
t.setheading(0)
t.fillcolor("#654321")
t.begin_fill
t.forward(8.5)
t.right(90)
t.forward(10)
t.left(90)
t.forward(17)
t.left(90)
t.forward(10)
t.left(90)
t.forward(25.5)
t.end_fill()
t.penup()
t.goto(-100, -100)
t.fillcolor('green')
t.begin_fill()
t.pendown()
t.left(45)
t.forward(40)
t.setheading(0)
t.forward(20)
t.setheading(180)
t.left(45)
t.forward(20)
t.setheading(180)
t.setheading(0)
t.forward(20)
t.setheading(180)
t.left(45)
t.forward(20)
t.setheading(180)
t.end_fill()
t.penup()

#star
t.setheading(0)
t.goto(50, -100)
t.pendown()
t.color('blue')
t.pensize(1)
for i in range(5):
  t.forward(150)
  t.right(144)
t.end_fill()
t.penup()

#hs
t.setheading(90)
t.goto(-150, 100)
t.pendown()
t.forward(100)
t.setheading(270)
t.forward(50)
t.setheading(0)
t.forward(30)
t.setheading(270)
t.forward(50)
t.setheading(90)
t.forward(100)
t.penup()

def draw_square(x, y, size, color):
  t.goto(x, y)       
  t.down()           
  t.setheading(0)    
  t.fillcolor(color) 
  t.begin_fill()     
  for side in range(4):  
      t.forward(size)    
      t.left(90)         
  t.end_fill()



for side in range(10):
  x = -100
  y = 100+(side*10)
  draw_square(x, y, 10, "yellow")

for side in range(5):
  x = -100+(side*10)
  y = 150
  draw_square(x, y, 10, "yellow")
t.penup()

for side in range(10):
  x = -50
  y = 100+(side*10)
  draw_square(x, y, 10, "yellow")
  
    

  
