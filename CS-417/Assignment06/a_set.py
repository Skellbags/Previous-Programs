import copy
from typing import List, Any, Dict

class a_set:
    '''
    An implementation of a set.
    This is a collection of values, with no repetitions
    '''
    def __init__(self, orig=None):
        '''
        Constructor.  If the (optional) orig argument is present,
        copy its values into self._data
        '''
        if orig == None:
            self._data   = [] # empty set
        elif type(orig) == list:
            self._data = []
            for x in orig:
                self.add(x)
        elif type(orig) == type(self):
            self._data = copy.copy(orig._data)

    def copy(self) -> 'a_set':
        '''
        Return a copy of this set.
        '''
        result: 'a_set' = a_set(self)
        return result

    def __iter__(self):
        '''
        Generator that visits all the values in this set
        '''
        next: int = 0
        while next < len(self._data):
            yield self._data[next]
            next += 1

    ############################################################
    # You must implement the following methods:

    def add(self, value: Any) -> None:
        '''
        Add this value to the end of the list.
        If it's already in the list, do nothing.
        '''
        if value in self._data:
            pass
        else:
            self._data.append(value)

    def __contains__(self, value: Any) -> bool:
        '''
        Return True/False if value occurs/doesn't occur in the list
        '''
        if value in self._data:
            return True
        else:
            return False

    def remove(self, value: Any) -> Any:
        '''
        If value is in the list, pop it.
        If not, raise KeyError

        RETURN the value that you just removed.
        '''
        if value in self._data:
            index = self._data.index(value)
            return self._data.pop(index)
        else:
            raise KeyError

    def union(self, other: 'a_set') -> 'a_set':
        '''
        Return a new a_set, which contains elements that
        occur in self, plus elements that occur in other
        '''
        union = a_set()
        for x1 in self._data:
            union.add(x1)
        for x2 in other._data:
            union.add(x2)
        return union

    def intersection(self, other: 'a_set') -> 'a_set':
        '''
        Return a new a_set, which contains all the values
        that occur in BOTH self and other
        '''
        inter = a_set()
        for x in self._data:
            for x in other._data:
                inter.add(x)
        return inter

    def difference(self, other: 'a_set') -> 'a_set':
        '''
        Return a new a_set, which contains all the values
        that occur in self, but do NOT occur in other
        '''
        diff = a_set()
        for x in self._data:
            if x not in other._data:
                diff.add(x)
        return diff

    def issubset(self, other: 'a_set') -> bool:
        '''
        Return True/False if self is/isn't a subset of other.
        A is a subset of B if, for every x in A, x is also in B.
        '''
        if len(self.difference(other)) == 0:
            return True
        else:
            return False

    def __len__(self) -> int:
        '''
        Return number of values (it's a one-liner)
        '''
        return len(self._data)

    def __repr__(self) -> str:
        '''
        Return a string describing the set.
        Example: if self contains {1, 3, 4}, this should
                 return the string 'a_set(1, 3, 4)'
        Notice that the last element has no comma after it!
        '''
        return 'a_set({})'.format(",".join(str(x) for x in self._data))

    def __str__(self) -> str:
        '''
        Return a user-friendly string describing the set.
        Example: if self contains {1, 3, 4}, this should
                 return the string '{1, 3, 4}'
        Notice that each element is followed by a comma, space,
        except for the last element.
        '''
        # REPLACE THE NEXT LINE
        return 'a_set{' + (",".join(str(x) for x in self._data)) + "}"

def main():
    my_set = a_set()
    print( 'Empty set:', my_set )

    print('\nTesting "add()":')

    A = a_set([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    B = a_set([8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2])

    print('\nTesting "__str__":')

    print( '  A =', A )
    print( '  B =', B )

    print('\nTesting "__repr__":')
    print( '  repr(A) =', repr(A) )
    print( '  repr(B) =', repr(B) )


    print('\nTesting "remove":')

    A.remove(3)
    A.remove(9)
    B.remove(8)
    B.remove(7)

    print( '  After deletions:' )
    print( '  A =', A )
    print( '  B =', B )

    try:
        A.remove(99)
        print( '  BAD: No exception raised when deleting absent key!')
    except KeyError:
        print( '  CORRECT: Exception raised when deleting absent key' )

    print( '\nTesting "contains":')

    tf_to_yn = {True:"Y", False:"."}

    print("        ", end = "")
    for x in range(10):
        print("{:>4}".format(x), end="")
    print()
    print("  in A? ", end = "")
    for x in range(10):
        print("{:>4}".format(tf_to_yn[x in A]), end="")
    print()
    print("  in B? ", end = "")
    for x in range(10):
        print("{:>4}".format(tf_to_yn[x in B]), end="")
    print()

    print('\nTesting "union":')

    print( '  A union B =', A.union(B) )

    print('\nTesting "intersection":')

    print( '  A intersect B =', A.intersection(B))

    print('\nTesting "difference":')

    print( '  A minus B =', A.difference(B))
    print( '  B minus A =', B.difference(A))

    print('\nTesting "issubset":')
    print( '  A subset of B?', A.issubset(B))
    print( '  B subset of A?', B.issubset(A))
    print( '  A subset of A?', A.issubset(A))

    print( '\nTesting "__len__":')
    print( '  len(A) =', len(A))
    print( '  len(B) =', len(B))

if __name__ == '__main__':
    main()

