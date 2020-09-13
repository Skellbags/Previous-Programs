'''
A module for 2D vector math.
'''
import math  # need this for math.sin, math.cos, and math.sqrt

def assign(v1, v2):
    '''
    Copy one vector into another.
    Copies v2 into v1.
    This seems silly, but it replaces the entries in v1,
    and avoids making a copy of v2.
    '''
    v1[0] = v2[0]
    v1[1] = v2[1]

def add(v1, v2):
    '''
    Add two vectors, return their sum.
    Simply add the X and Y parts separately.
    '''
    x = v1[0] + v2[0]
    y = v1[1] + v2[1]
    return [x, y]

def sub(v1, v2):
    '''
    Subtract two vectors, return their difference.
    Simply subtract the X and Y parts separately.
    '''
    x = v1[0] - v2[0]
    y = v1[1] - v2[1]
    return [x, y]

def mul(v, num):
    '''
    Multiply a vector by a number.
    Simply multiply both parts.
    '''
    x = v[0] * num
    y = v[1] * num
    return [x, y]

def directed(length, angle):
    '''
    A vector with a given length and angle.
    Uses some trigonometry, which you don't have to understand if you don't
    want to ;-)
    '''
    # Convert angle to radians
    angle = math.pi * angle / 180
    # Do some trig
    x = length * math.cos(angle)
    y = length * math.sin(angle)
    return [x, y]

def turned_90_ccw(vec):
    '''
    Return vector, turned counter-clockwise by 90 degrees
    '''
    return [-vec[1], vec[0]]

def turned_90_cw(vec):
    '''
    Return vector, turned clockwise by 90 degrees
    '''
    return [vec[1], -vec[0]]

def length(vec):
    '''
    Return length of vector (distance to origin)
    '''
    return math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])

def distance(v1, v2):
    '''
    Return distance between two vectors
    '''
    diff = sub(v1, v2)
    return length(diff)

def dot(v1, v2):
    '''
    Dot product of two vectors.
    It is zero if the vectors are at right angles.
    '''
    return v1[0] * v2[0] + v1[1] * v2[1]

def normalized(v):
    l = length(v)
    if l == 0:
        l = 1
    return mul(v, 1 / l)

#
# This last part can be a bit confusing, so read carefully:
#
# It's because of the magic variable __name__.
#
# If we
#   import vector
# then python will set __name__ = 'vector'
#
# But if we run the vector file,
# then python will set __name__ = '__main__'
#
# So, at the bottom of this file, it reads
# if __name__ == '__main__':
#
# What happens?
# If we import vector, it's False, so nothing happens.
## But if we run the vector file, then it's True,
# and we call the main() function.
#
def main():
    '''
    This is the main() function.
    All modules should have one.
    It usually contains code that runs some tests
    to see if the functions in the module were
    implemented correctly.
    '''
    print('[1,1] + [2,3]=', add([1,1], [2,3]))
    print(' 5 * [2,3]=', mul([2,3], 5))
    print('directed(10, 90)=', directed(10, 90))
    print('[2,1] ccw 90=', turned_90_ccw([2,1]))
    print('[2,1] cw 90=', turned_90_cw([2,1]))
    print('len([3,4])=', length([3,4]))
    print('dist([0,0] to [3,4])=', distance([0,0], [3,4]))
    print('dot([3,4], perp([3,4]))=', dot([3,4], turned_90_ccw([3,4])))
    print('normalized([3,4])=', normalized([3,4]))
    v1 = [3,4]
    assign(v1, [2,3])
    print('after assign(v1,[2,3]), v1=', v1)


if __name__ == '__main__':
    main()



