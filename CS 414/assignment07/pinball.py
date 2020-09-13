"""
Bounce the ball into the target
"""

import time
import turtle
import time

import physics

"""
Variables needed by the program
"""

# Dimensions of the turtle window
window_width  = 600
window_height = 600
window_left   = -(window_width  / 2)
window_right  =   window_width  / 2
window_bottom = -(window_height / 2)
window_top    =   window_height / 2

# The 4 sides of the play area
bounds_left   = window_left + 50
bounds_right  = window_right - 50
bounds_top    = window_top - 50
bounds_bottom = window_bottom + 50

# To move an object, we need to know how much time elapsed
# since the previous update.  This variable stores the time of
# the previous update
time_before   = 0

'''
    A motion_record is a list with 6 entries:
    [0]: position (x and y values)
    [1]: velocity (x and y values)
    [2]: angle
    [3]: turn rate (angular velocity)
    [4]: radius
    [5]: mass

   INDEX NAMES:
   These variables give names to the indexes in the above list
'''
POS   = 0
VEL   = POS + 1
ANGLE = VEL + 1
RATE  = ANGLE + 1
SIZE  = RATE + 1
MASS  = SIZE + 1

# And these are index names for the 2 coordinates.
X = 0
Y = 1

# The ball's motion record
ball = [[0, window_top - 100], [50, 0], 0,0,20, 50]

# The motion records of the pins
pins = []

# The target's motion record (actually it doesn't move)
target = [[0,0], [0,0], 0,0,20, 1000000]

"""
Study the following functions, but you don't have to change them.

Scroll down to see the functions that you should change.
"""
def move_object(motion, time_elapsed):
    """Move an object.

    Parameters
    ----------
    motion : list
       The object's motion record
    time_elapsed : float
       the duration of the motion
    """
    physics.update_motion(motion, time_elapsed)

def draw_circle(ball, color):
    """ Draw a circle.

    Parameters
    ----------
    ball : list
        the circle's motion record.  We only use its position and radius
    color : str
        the circle's color
    """
    t = turtle
    t.up()
    # go the center of the circle
    t.goto(ball[POS][X], ball[POS][Y])
    # position the pen at the bottom of the circle.
    t.setheading(90)
    t.back(ball[SIZE])
    t.setheading(0)
    # and now draw the circle
    t.down()
    t.pensize(0)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(ball[SIZE])
    t.end_fill()

def draw_target():
    """Draw the square-shaped target, at the middle of the screen."""

    t = turtle
    t.up()
    t.goto(-target[SIZE], -target[SIZE])
    t.setheading(0)
    t.pensize(2)
    t.down()
    for side in range(4):
        t.fd(target[SIZE] * 2)
        t.left(90)

def draw_objects():
    """Draw all the objects in the scene"""

    # Disable the turtle animation, and erase the scren.
    turtle.tracer(False)
    turtle.hideturtle()
    turtle.clear()

    # Draw all the parts of the scene.
    draw_ball()
    draw_target()
    draw_bounds()
    draw_pins()

    show_status()

    # Now show the screen, after everything has been drawn
    turtle.tracer(True)

def move_objects(time_elapsed):
    """Advance the moving objects in the scene.

    There is only one: the ball
    """
    move_object(ball, time_elapsed)

    # Bounce the ball off the sides, if necessary.
    bounce_off_walls(ball, bounds_left, bounds_right,
                     bounds_top, bounds_bottom)


def draw_ball():
    """Draw the ball at its current position"""

    draw_circle(ball, 'yellow')

def bounce_off_walls(motion, left, right, top, bottom):
    """Check if an object has hit a wall, and make it bounce if it did.

    Parameters
    ----------
    motion: list
        the object's motion record
    left, right, top, bottom : float
        the x and y coords of the walls
    """
    x = motion[POS][X]
    y = motion[POS][Y]
    r = motion[SIZE]

    if x + r >= right:
        motion[VEL][X] *= -1
        motion[POS][X] = right - r - 0.1
    elif x - r <= left:
        motion[VEL][X] *= -1
        motion[POS][X] = left + r + 0.1

    if y + r >= top:
        motion[VEL][Y] *= -1
        motion[POS][Y] = top - r - 0.1
    elif y - r <= bottom:
        motion[VEL][Y] *= -1
        motion[POS][Y] = bottom + r + 0.1

"""
*******************************************************
IMPLEMENT THE FUNCTIONS BELOW
*******************************************************
"""
def draw_bounds():
    """Draw the bounding rectangle."""

    pass

def show_status():
    """Display the score, and the Congratulations."""

    pass

def draw_pins():
    """Draw all the pins."""

    pass

def check_pin_ball_hit(time_elapsed):
    """Check if a ball hit a pin, and make it bounce if it did.

    Parameter
    ---------
    time_elapsed: float
        how long since the previous update
    """

    pass

def check_ball_on_target():
    """Check if ball reached target.
    If it did, the game is won."""

    pass

def add_pin(x, y):
    """Add a pin at the current mouse location.

    Turtle calls this when the user clicks the mouse.

    Parameters:
    -----------
    x, y : int
        the mouse position
    """

    pass

"""
*******************************************************
IMPLEMENT THE FUNCTIONS ABOVE
*******************************************************
"""

def update_scene():
    '''
    This gets called repeatedly.
    It:
    - moves the moving objects
    - draws all the objects
    '''

    global time_before
    time_now = time.time()
    time_elapsed = time_now - time_before

    move_objects(time_elapsed)
    check_pin_ball_hit(time_elapsed)
    check_ball_on_target()
    draw_objects()

    time_before = time_now
    turtle.ontimer(update_scene, 50)

def main():
    global time_before

    turtle.setup(window_width, window_height, 0,0)
    turtle.Screen()

    turtle.ontimer(update_scene, 50)
    turtle.onscreenclick(add_pin)

    time_before = time.time()

    turtle.listen()
    turtle.mainloop()


# Leave these two lines in place, at the bottom of this file.
if __name__ == '__main__':
    main()
