'''
Print three numbers, in sorted order
'''
def sort_three(a, b, c):

    if a > b and b > c:
        print(c,b,a)
    elif a > c and c > b:
        print(b,c,a)
    elif c > a and a > b:
        print(b,a,c)
    elif b > a and a > c:
        print(c,a,b)
    elif b > c and c > a:
        print(a,c,b)
    elif c > b and b > a:
        print(a,b,c)
        


'''
Return list with a given item deleted
'''
def delete_at(alist, k):
    blist = alist[:k] + alist[k+1:]
    return blist
    

'''
Return list with an element inserted
'''
def insert_at(alist, i, x):
    blist = alist[:i] + [x] + alist[i:]
    return blist

'''
Return biggest difference from numbers on two lists
'''
def max_difference(list1, list2):
    biggest_difference = 0
    for x in list1:
        for y in list2:
            if abs(x-y) > biggest_difference:
                biggest_difference = abs(x-y)
            else:
                pass

    return biggest_difference
'''
Main program to test the above functions.
Don't change this code.
'''
def main():
    sort_three(1,2,3)
    sort_three(1,3,2)
    sort_three(2,1,3)
    sort_three(2,3,1)
    sort_three(3,2,1)
    sort_three(3,1,2)
    print()

    print (delete_at(['one', 'two', 'three', 'four'], 0))
    print (delete_at(['one', 'two', 'three', 'four'], 1))
    print (delete_at(['one', 'two', 'three', 'four'], 2))
    print (delete_at(['one', 'two', 'three', 'four'], 3))
    print ()

    print (insert_at(['one', 'two', 'three'], 0, 'and'))
    print (insert_at(['one', 'two', 'three'], 1, 'and'))
    print (insert_at(['one', 'two', 'three'], 2, 'and'))
    print (insert_at(['one', 'two', 'three'], 3, 'and'))
    print ()

    print (max_difference([1, 2, 3], [4, 5, 6]))
    print (max_difference([-6, -5, -4], [-3, -2, -1]))


'''
Call main() when the module is run
'''
if __name__ == '__main__':
    main()

