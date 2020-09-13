'''
----------------------------------------------------------
Exercise 1:
This code determines whether the list contains a 3.
Modify it to determine whether the list contains a string.
'''

list1 = [1, 2, 'apple', 3, 'banana']
found_a_str = False
for value in list1:
    if value != int:
        found_a_str = True

if found_a_str:
    print ('list1 has a string')
else:
    print ('list1 has no strings')

'''
----------------------------------------------------------
Exercise 2:
This code counts the ones in the list.
Modify it to count the odd values.
'''

list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
odds_count = 0
for value in list2:
    if value % 2 != 0:
        odds_count += 1

print ('list2 has', odds_count, 'odd numbers')

'''
----------------------------------------------------------
Exercise 3:
Below, copy the code you wrote for exercise 2.
Modify it to count the EVEN values.
'''

# copy the code here, between the triple-quoted comments!
evens_count = 0
for value in list2:
    if value % 2 == 0:
        evens_count += 1

print ('list2 has', evens_count, 'even numbers')


'''
----------------------------------------------------------
Exercise 4:
This code determines if the list has two consecutive equal values.
Modify it to determine HOW MANY TIMES it has two consecutive equal values.
'''

list4 = [12, 32, 34, 34, 23, 23, 12, 12]
previous_value = list4[0]
two_in_a_row = 0
# Start at the SECOND value in the list:
for value in list4[1:] :
    if value == previous_value:
        two_in_a_row += 1
    previous_value = value

print ('list4 has', two_in_a_row,' consecutive equal values')



'''
----------------------------------------------------------
Exercise 5:
This code adds up all the values in a list.
Modify it to add up only the ODD values.
'''

list5 = [12, 32, 33, 35, 23, 23, 12, 12]
total = 0
for value in list5:
    if value % 2 != 0:
        total += value
    else:
        pass

print ('sum:', total)

'''
----------------------------------------------------------
Exercise 6:
Below, copy the code you wrote for exercise 5.
Modify it to get the AVERAGE of the odd values.
'''
