from linked_list import Linked_List

class Enhanced_List(Linked_List):

    '''
    Constructor.  Notice how we call the constructor
    of the parent class.
    '''
    def __init__(self, orig = None):
        Linked_List.__init__(self, orig)

    '''
    Add up values in the list, and return the total
    '''
    def sum(self):
        current = self._head
        sum_nodes = 0
        while current is not None:
            sum_nodes += current._value
            current = current._next
        return sum_nodes


    '''
    Get the average of the values in the list
    '''
    def average(self):
        return (self.sum()) / (self.size())

    '''
    Make and return a new list, with values in reverse order.
    '''
    def reversed(self):
        current = self._head
        rev = Linked_List()
        while current is not None:
            rev.add_head(current._value)
            current = current._next
        return rev

    '''
    Return the index where the value occurs in the list.
    Return -1 if value does not occur in list.
    '''
    def index_of(self, value):
        current = self._head
        n_nodes = 0
        while current is not None:
            if current._value == value:
                return n_nodes
            else:
                n_nodes += 1
                current = current._next
        return -1
    

    '''
    Return the value at the given index.
    Return None if index is out of bounds.
    '''
    def at_index(self, index):
        if index >= self.size() or index < 0:
            return None
        n_nodes = 0
        current = self._head
        while True:
            if n_nodes == index:
                return current._value
            else:
                n_nodes += 1
                current = current._next

def main():
    a_list = Enhanced_List([3, 1, 4, 1, 5, 9])
    print ('a_list          :', a_list)
    print ('sum(a_list)     :', a_list.sum())
    print ('avg(a_list)     :', a_list.average())
    print ('a_list reversed :', a_list.reversed())
    print ('index_of(5)     :', a_list.index_of(5))
    print ('index_of(0)     :', a_list.index_of(0))
    print ('at_index(1)     :', a_list.at_index(1))
    print ('at_index(-1)    :', a_list.at_index(-1))

if __name__ == '__main__':
    main()

