'''
A module for 2D physics
'''

import copy

from vector import dot, normalized, add, sub, mul, assign, distance, \
    turned_90_cw, turned_90_ccw

'''
    A motion_record is a list with 5 entries:
    [0]: position (x and y values)
    [1]: velocity (x and y values)
    [2]: angle
    [3]: turn rate (angular velocity)
    [4]: radius

   INDEX NAMES:
   These variables give names to the indexes in the above list
'''
POS   = 0
VEL   = POS + 1
ANGLE = VEL + 1
RATE  = ANGLE + 1
SIZE  = RATE + 1
MASS  = SIZE + 1

def update_motion(motion_record, time_step):
    '''
    Update the position and angle of an object that
    is moving at constant velocity, and turning
    at constant rate
    '''
    advance(motion_record[POS], motion_record[VEL], time_step)
    motion_record[ANGLE] += motion_record[RATE] * time_step

def advance(position, velocity, time_step):
    '''
    Update the position of an object moving at constant velocity
    '''
    assign(position, add(position, mul(velocity, time_step)))

def accelerate(velocity, acceleration, time_step):
    '''
    Update the velocity of an object under constant acceleration
    '''
    assign(velocity, add(velocity, mul(acceleration, time_step)))

def collided(motion1, motion2):
    '''
    Detects whether two circles are currently overlapping.
    '''
    # Get the distance between their centers
    centers_distance = distance(motion1[POS], motion2[POS])
    # Check if centers are close enough
    if centers_distance < (motion1[SIZE] + motion2[SIZE]):
        return True
    else:
        return False

def resolve_collision(motionA, motionB, time_step):
    '''
    Two spheres collided.  Change their velocities

    Math from www.myphysicslab.com/engine2D/collision-en.html
    '''

    pA = motionA[POS]
    pB = motionB[POS]
    vA = motionA[VEL]
    vB = motionB[VEL]
    mA = motionA[MASS]
    mB = motionB[MASS]

    # Get the direction from sphere B to sphere A
    n = normalized(sub(pA, pB))

    # Relative velocity
    vAB = sub(vA, vB)

    # Impulse, ignoring rotational contributions
    J = -2 * dot(vAB, n) / (1 / mA + 1 / mB)

    # New velocities
    vA = add(vA, mul(n,  J / mA))
    vB = add(vB, mul(n, -J / mB))

    motionA[VEL] = vA
    motionB[VEL] = vB

    # Move the spheres slightly away from each other,
    # to make sure they're no longer colliding

    for step in range(2):
        advance(pA, vA, time_step)
        advance(pB, vB, time_step)

def split_up(motion, impulse):
    '''
    Split a moving object.
    motion: an object's position and velocity.
    impulse: the splitting velocity.

    returns:
      a list with two motion records, one for each of
      the two fragments that resulted from the split.
    '''
    v = motion[VEL]
    unit = normalized(v)
    perp1 = turned_90_cw(unit)
    perp2 = turned_90_ccw(unit)
    v1 = add(v, mul(perp1, impulse))
    v2 = add(v, mul(perp2, impulse))
    pos1 = copy.copy(motion[POS])
    pos2 = copy.copy(motion[POS])
    motion1 = [pos1, v1, motion[ANGLE], motion[RATE], motion[SIZE]/2]
    motion2 = [pos2, v2, motion[ANGLE], -motion[RATE], motion[SIZE]/2]
    return [motion1, motion2]

def main():
    p1 = [-2, 0]
    v1 = [1,1]
    p2 = [2, 0]
    v2 = [-1,1]
    motion1 = (p1, v1)
    motion2 = (p2, v2)
    print('Before collision: p1=', p1, 'p2=', p2, 'v1=',v1, 'v2=', v2)
    resolve_collision(motion1, motion2, 0.1)
    print('After collision: p1=', p1, 'p2=', p2, 'v1=',v1, 'v2=', v2)

    motion = [[0,0], [-1,-1], 0, 0, 10]
    (rock1, rock2) = split_up(motion, 0.1)
    print ('rocklet 1:', rock1)
    print ('rocklet 2:', rock2)


if __name__ == '__main__':
    main()

