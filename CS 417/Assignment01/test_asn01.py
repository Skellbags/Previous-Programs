import os

'''
Test five programs
'''

def write_numbers(numbers, filename):
    f = open(filename, 'w')
    for n in numbers:
        f.write(str(n) + '\n')
    f.close()

print('----TESTING is_right-----')
write_numbers([3,4,5], 'test_in.txt')
os.system('python is_right.py < test_in.txt')
write_numbers([4,5,2], 'test_in.txt')
os.system('python is_right.py < test_in.txt')
write_numbers([2,3,4], 'test_in.txt')
os.system('python is_right.py < test_in.txt')

print('----TESTING pi_approx-----')
write_numbers([100], 'test_in.txt')
os.system('python pi_approx.py < test_in.txt')

print('----TESTING reduce-----')
write_numbers([24, 36], 'test_in.txt')
os.system('python reduce.py < test_in.txt')
write_numbers([3, 4], 'test_in.txt')
os.system('python reduce.py < test_in.txt')
write_numbers([-4, 8], 'test_in.txt')
os.system('python reduce.py < test_in.txt')

print('----TESTING diff-----')
write_numbers([12, 28, 32, 40], 'test_1.txt')
write_numbers([12, 28, 32, 40], 'test_2.txt')
os.system('python diff.py test_1.txt test_2.txt')
write_numbers([12, 28, 31, 40], 'test_2.txt')
os.system('python diff.py test_1.txt test_2.txt')
write_numbers([12, 28, 31, 40, 0], 'test_1.txt')
os.system('python diff.py test_1.txt test_2.txt')

print('----TESTING stats-----')
write_numbers([3, 1.0, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3],
              'test_in.txt')
os.system('python stats.py test_in.txt')
