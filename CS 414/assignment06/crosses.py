import turtle
import math
t = turtle
t.speed(0)
turtle.penup()
t.goto(-400,-200)

def draw_cross(x, y):
    turtle.penup()

    turtle.color('black')
    turtle.goto(x, y)
    turtle.pendown()
    t.setheading(0)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.lt(90)
    t.fd(25)
    t.lt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.lt(90)
    t.fd(25)
    t.lt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.lt(90)
    t.fd(25)
    t.lt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.lt(90)
    t.fd(25)
    t.lt(90)
    t.fd(25)
    t.up()
    

def main():
    turtle.setup(400,400, 0,0)
    turtle.tracer(False)
    x = 0
    y = 0
    px = -200
    py = -200
# Depending on the size of your cross, you may need
# more than 20 or fewer than 20 rows and columns
    for row in range(20):
        x, y = turtle.pos()
        px = x
        py = y
        for col in range(20):
            x += 25
            y += 50
            draw_cross(x, y)
        px += 50
        py -= 25
            
        t.goto(px, py)
    
    turtle.update()

    turtle.mainloop()

if __name__ == '__main__':
    main()

#RS
