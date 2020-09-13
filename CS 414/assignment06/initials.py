import turtle


def draw_initials():
    turtle.penup()

    #r
    turtle.color('red')
    turtle.width(1)
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.goto(-200, 0)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(150)
    turtle.forward(100)
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.write("R")
    

    #j
    turtle.color('blue')
    turtle.width(3)
    turtle.goto(-50, 0)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(100)
    turtle.penup()
    turtle.write("J")
    #s
    turtle.color('green')
    turtle.width(5)
    turtle.goto(100, 0)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.write("S")
    
    





    


def main():
    turtle.setup(400,400, 0,0)
    # Don't show the turtle in action.
    turtle.tracer(False)

    draw_initials()

    # Show the results of all the turtle's actions
    turtle.update()

    turtle.mainloop()

if __name__ == '__main__':
    main()

#RS
