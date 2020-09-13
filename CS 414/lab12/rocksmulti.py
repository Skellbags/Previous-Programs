'''
Animated Moving Rocks
'''
import time
import turtle
import math
import random
import vector
import physics

# When we update the rock positions, we need to know the time before,
# so we know how much time has passed

time_before   = 0  

window_width  = 600
window_height = 600
window_left   = -(window_width  / 2)
window_right  =   window_width  / 2
window_bottom = -(window_height / 2)
window_top    =   window_height / 2

# This list describes the motion of the rock:
# 6 values: [x,y], [vx,vy], angle, turn_rate, size, mass
# These 6 values are a "MOTION RECORD"
rock_motions = []

# STEP 6 HERE

def move_object(motion_record, T):
    '''
    Update object's motion values.
    T : the time that has elapsed since the last update
    '''
    physics.advance(motion_record[0], motion_record[1], T)
    rate = motion_record[3]
    motion_record[2] += rate * T

def random_motion():
    '''
    Create a motion record, using random values
    '''
    # x and y are somewhere inside the window
    x = random.randrange(window_left, window_right)
    y = random.randrange(window_bottom, window_top)
    # velocity components are between -100 and +100
    vx = random.randrange(-100, 100)
    vy = random.randrange(-100, 100)
    # rotation rate is between -100 and +100
    rotation_rate = random.randrange(-100, 100)
    # size is 20
    # STEP 4 HERE
    # STEP 7 HERE
    size = random.randrange(1,50)
    mass = size * size

    # Finally, put these in a motion record, and return it.
    return [[x, y], [vx, vy], 0, rotation_rate, size, mass]

def initialize_rocks():
    '''
    Create the motion record(s) for the rock(s)
    '''
    # We will change rock_motion, so we must declare it to be global
    global rock_motions
    # STEP 1 HERE
    # STEP 2 HERE
    # STEP 3 HERE
    # STEP 6 HERE
    for i in range(4):
        rock_motions.append(random_motion())

def wrap_around(motion):
    '''
    If an object goes out one side of the window,
    make it change direction
    '''
    pos = motion[0]
    if pos[0] > window_right:
        pos[0] = window_left
    elif pos[0] < window_left:
        pos[0] = window_right
    pos = motion[0]
    if pos[1] > window_top:
        pos[1] = window_bottom
    elif pos[1] < window_bottom:
        pos[1] = window_top
    return

def move_rocks(T):
    '''
    Update the motion(s) of the rocks(s)
    '''
    global rock_motions
    # STEP 6 HERE
    # STEP 5 HERE
    for i in rock_motions:
        move_object(i, T)
        wrap_around(i)
    

def draw_rock(motion_record):
    '''
    Given a motion record, use its
    position, angle, and size, to draw
    a hexagonal shape.
    '''
    # Get the position, angle, and size
    pos = motion_record[0]
    angle = motion_record[2]
    size  = motion_record[4]
    turtle.speed(0)
    # Go to the center of the rock (which is a hexagon)
    turtle.penup()
    turtle.goto(pos[0], pos[1])
    # Turn the pen
    turtle.setheading(angle)
    # Go out to the edge of the hexagon
    # STEP 4 HERE
    turtle.forward(size)
    turtle.pendown()
    # Point along the first side of the hexagon
    turtle.left(60)
    for side in range(6):
        turtle.left(60)
        # STEP 4 HERE
        turtle.forward(size)

def draw_rocks():
    '''
    Draw the rock(s)
    '''
    for i in rock_motions:
        draw_rock(i)
    # STEP 6 HERE

def collided(motion1, motion2):
    '''
    Detects whether two objects are currently overlapping.
    '''
    return physics.collided(motion1, motion2)

def move_objects(T):
    '''
    Moves all the objects in the scene
    '''
    move_rocks(T)
    for rock1 in rock_motions:
        for rock2 in rock_motions:
            if rock1 != rock2:
                if physics.collided(rock1, rock2):
                    physics.resolve_collision(rock1, rock2, T)
                #pass
    return
    # STEP 8 HERE

def draw_objects():
    '''
    Draw all the objects
    '''
    turtle.tracer(False)
    turtle.hideturtle()
    turtle.clear()

    draw_rocks()
    turtle.tracer(True)

def update_scene():
    '''
    This gets called 20 times per second.
    It updates the motion of all the objects
    '''
    # Will change time_before, so declare it global
    global time_before
    # What time is it now?
    time_now = time.time()
    # How much time passed since last update?
    time_elapsed = time_now - time_before

    # Move the objects,
    move_objects(time_elapsed)
    # and draw them in their new positions
    draw_objects()

    # save the current time
    time_before = time_now
    # and ask turtle to call this function again in 1/20 second
    turtle.ontimer(update_scene, 50)

def main():
    '''
    Main program.
    NO NEED TO CHANGE THIS
    '''
    global time_before

    turtle.setup(window_width, window_height, 0,0)
    turtle.Screen()

    turtle.ontimer(update_scene, 50)
    time_before = time.time()

    initialize_rocks()

    turtle.listen()
    turtle.mainloop()

if __name__ == '__main__':
    main()

#RS
