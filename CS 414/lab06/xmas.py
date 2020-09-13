gifts = ['partridge in a pear tree',
         'turtle doves',
         'french hens',
         'colly birds',
         'gold rings',
         'geese a-laying',
         'swans a-swimming',
         'maids a-milking',
         'ladies dancing',
         'lords a-leaping',
         'pipers piping',
         'drummers drumming']

ordinals = ['first', 'second', 'third', 'fourth',
            'fifth', 'sixth', 'seventh', 'eighth',
            'ninth', 'tenth', 'eleventh', 'twelvth']

numerals = ['a', 'two', 'three', 'four', 'five', 'six', 'seven',
            'eight', 'nine', 'ten', 'eleven', 'twelve']

first_verse = 'On the X day of Christmas my true love sent to me'

# Your work begins here.
# RULES:
#   1. Your program must use the variables declared above
#   2. Your program may only use these string literals:
#      "."    ","   "and"   ""
#      All other strings must be obtained from the variables above.

day = 0
how_many_days = 12
while day < how_many_days:
    print(first_verse.replace("X", ordinals[day]))
    start_index = day
    day += 1
    end_index = -1
    gift_index = start_index
    while gift_index > end_index:
        print(numerals[gift_index].title(),gifts[gift_index], end = "")
        if gift_index > 1:
            print(",")
        elif gift_index == 1:
            print(", and")
        else:
            print(".")
        gift_index -= 1
    print()

#RS
