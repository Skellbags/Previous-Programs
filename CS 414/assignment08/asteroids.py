import time
import turtle
import math
import random

from vector import add, sub, mul, directed
import physics

time_before   = 0

window_width  = 600
window_height = 600
window_left   = -(window_width  / 2)
window_right  =   window_width  / 2
window_bottom = -(window_height / 2)
window_top    =   window_height / 2

'''
    A motion_record is a list with 5 entries:
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

# The ship's motion record
ship  = [[0,0], [0,0], 0,0,0, 10]

# This list will hold all the motion records of all the rocks
rocks = []

# And this list will hold the motion records of the bullets
bullets = []

"""
***********************************************************
You probably don't need to change these functions:
***********************************************************
"""

def move_object(motion, T):
    physics.update_motion(motion, T)

def wrap_around(motion):
    '''
    If an object goes outside the window,
    place it on the other side.
    '''
    if   motion[POS][X] > window_right:
         motion[POS][X] = window_left
    elif motion[POS][X] < window_left:
         motion[POS][X] = window_right
    elif motion[POS][Y] > window_top:
         motion[POS][Y] = window_bottom
    elif motion[POS][Y] < window_bottom:
         motion[POS][Y] = window_top

def move_rocks(T):
    '''
    Advance and turn all the rocks
    '''
    for rock in rocks:
        wrap_around(rock)
        move_object(rock, T)

def draw_rocks():
    '''
    Draw all the rocks
    '''
    for rock in rocks:
        draw_rock(rock)

def draw_bullet(bullet):
    '''
    Draw a bullet (just a dot)
    '''
    turtle.penup()
    turtle.goto(bullet[POS][X], bullet[POS][Y])
    turtle.dot(bullet[SIZE])

    

def draw_ship():

    x     = ship[POS][X]
    y     = ship[POS][Y]
    angle = ship[ANGLE]
    size  = ship[SIZE]

    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.forward(10)
    turtle.pendown()    
    turtle.left(160)
    turtle.forward(size)
    turtle.forward(21)
    turtle.left(117)
    turtle.forward(20)
    turtle.left(117)
    turtle.forward(21)
    turtle.penup()

def accelerate_ship():
    ship_angle = directed(1, ship[ANGLE])
    physics.accelerate(ship[VEL], ship_angle, 10)
    
def decelerate_ship():
    ship_angle = directed(-1, ship[ANGLE])
    physics.accelerate(ship[VEL], ship_angle, 10)
    
    
def move_ship(T):
    move_object(ship, T)
    wrap_around(ship)
    

def move_objects(T):
    '''
    Advance all the objects in the scene
    '''
    move_rocks(T)
    move_bullets(T)
    move_ship(T)
    remove_offscreen_bullets()

def random_motion():
    x = random.randrange(window_left, window_right)
    y = random.randrange(window_bottom, window_top)
    vx = random.random() * 200 - 100
    vy = random.random() * 200 - 100
    size = random.randrange(20,60)
    rotation_rate = random.random() * 200 - 100
    mass = size * size
    return [[x,y], [vx,vy], 0, rotation_rate, size, mass]

def make_rocks():
    global rocks

    rocks = []
    for i in range(5):
        rocks.append(random_motion())

def move_bullets(T):
    for bullet in bullets:
        move_object(bullet, T)

def fire_bullet():
    bullet = [[0,0], [0,0], 0,0,0, 10]

    # Here is a vector of length 1, towards where ship's nose is pointing
    u = directed(1, ship[ANGLE])

    # Bullets are spawned at the tip of the ship's nose
    bullet[POS] = add(ship[POS], mul(u, ship[SIZE]))

    # Bullets travel at 100 pixels/second, whither the ship was pointing
    bullet[VEL] = mul(u, 100)

    bullet[SIZE] = 5

    if len(bullets) >= 10:
        pass
    else:
        bullets.append(bullet)

def draw_bullets():
    for bullet in bullets:
        draw_bullet(bullet)

def update_scene():
    '''
    This gets called repeatedly.
    It:
    - updates the positions of all the objects
    - draws all the objects
    '''

    global time_before
    time_now = time.time()
    time_elapsed = time_now - time_before

    move_objects(time_elapsed)
    check_rock_bullet_hit()
    draw_objects()
    if len(rocks) == 0:
        make_rocks()
    time_before = time_now
    turtle.ontimer(update_scene, 50)


"""
You should change the following functions:

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v
"""

def draw_rock(motion_record):
    '''
    Draw a rock (just a hexagon).  For the bonus, make the rock more interesting.
    '''
    x     = motion_record[POS][X]
    y     = motion_record[POS][Y]
    angle = motion_record[ANGLE]
    size  = motion_record[SIZE]

    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.forward(size)
    turtle.pendown()
    turtle.left(60)
    for side in range(6):
        turtle.left(60)
        turtle.forward(size)

def remove_offscreen_bullets():
    """Check all the bullets.  If a bullet is off-screen, remove it from list."""
    for bullet in bullets:
        if bullet[POS][X] > window_right:
             bullets.remove(bullet)
        elif bullet[POS][X] < window_left:
             bullets.remove(bullet)
        elif bullet[POS][Y] > window_top:
             bullets.remove(bullet)
        elif bullet[POS][Y] < window_bottom:
             bullets.remove(bullet)
    return

def check_rock_bullet_hit():
    """Check every rock agains every bullet.  If they collided, then
    either split the rock, or remove the rock.
    """
    for rock in rocks:
        for bullet in bullets:
            if (physics.collided(rock, bullet) == True) and (rock[SIZE] < 50):
                rocks.remove(rock)
                bullets.remove(bullet)
            elif (physics.collided(rock, bullet) == True) and (rock[SIZE] > 50):
                rocks.remove(rock)
                new_rock = physics.split_up(rock, 180)
                rock1 = new_rock[0]
                rock2 = new_rock[1]
                rocks.append(rock1)
                rocks.append(rock2)
                bullets.remove(bullet)
    return

def turn_ship_left():
    """Add 5 degrees to ship's angle"""
    ship[ANGLE] += 15
    return

def turn_ship_right():
    """Subtract 5 degrees from the ship's angle"""
    ship[ANGLE] -= 15
    return

def draw_objects():
    '''
    Draw all the rocks, and the bullets
    '''
    global ship
    turtle.tracer(False)
    turtle.hideturtle()
    turtle.clear()
    
    draw_ship()
    draw_rocks()
    draw_bullets()


    turtle.penup()
    turtle.goto(0, 250)
    turtle.write('Asteroids!', align='center')
    fails = 0
    lives = 3
    turtle.goto(window_left+50, window_bottom+50)
    turtle.write("Lives:", True)
    turtle.write(lives-fails)
    for rock in rocks:
        if physics.collided(rock, ship) == True:
            turtle.goto(0, 0)
            turtle.write('GAME OVER!', align='center')
            fails += 1
            ship  = [[0,0], [0,0], 0,0,0, 10]
    if lives == 0:
        quit()
        

    turtle.tracer(True)

def main():
    global time_before

    turtle.setup(window_width, window_height, 0,0)
    turtle.Screen()

    turtle.onkey(fire_bullet, ' ')
    turtle.onkey(turn_ship_left, 'a')
    turtle.onkey(turn_ship_right, 'd')
    turtle.onkey(accelerate_ship, 'w')
    turtle.onkey(decelerate_ship, 's')

    turtle.ontimer(update_scene, 50)
    time_before = time.time()

    make_rocks()

    turtle.listen()
    turtle.mainloop()

"""
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
| | | | | | | | | | | | | | | | | | | | | | | |

You should should change the functions above.

YOU SHOULD ALSO ADD SOME FUNCTIONS.
"""


# Leave these two lines in place, at the bottom of this file.
if __name__ == '__main__':
    main()

#RS
