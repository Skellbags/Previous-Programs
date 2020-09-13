''' Checks a 4-letter word for palindromicity '''

word = input('Hello, and welcome to my palindrome tester, please enter a 4-letter word: ')

if word[0] == word[-1] and word[1] == word[1]:
    print(True)
else:
    print(False)

#RS
