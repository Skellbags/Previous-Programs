import turtle
import math

t = turtle
t.penup()
t.speed(0)
def draw_octagon(size, x, y):
    t.goto(x, y)
    t.setheading(0)
    for side in range(8):
        t.pendown()
        t.forward(size)
        t.right(45)
        t.penup()

def draw_square(size, x, y):
    t.goto(x, y)
    t.setheading(45)
    for side in range(4): 
        t.pendown()
        t.forward(size)
        t.right(90)
        t.penup()
def main():
    turtle.setup(400,400, 0,0)
    turtle.tracer(False)

    # Depending on the size of your tile,
    # You may need more rows and columns,
    # or fewer.
    for row in range(6):
        for col in range(6):
            x = -150+(row*60)
            y = -150+(col*60)
            t.color('black')
            t.fillcolor('green')
            t.begin_fill()
            draw_octagon(25, x, y)
            t.end_fill()
    for row in range(5):
        for col in range(5):
            x = -150+(row*60)+26
            y = -150+(col*60)
            t.color('black')
            t.fillcolor('yellow')
            t.begin_fill()
            draw_square(25, x, y)
            t.end_fill()
    turtle.update()

    turtle.mainloop()

if __name__ == '__main__':
    main()

#RS
