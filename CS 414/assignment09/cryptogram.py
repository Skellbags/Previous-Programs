import random
import string

def print_wrapped(text):
    '''
    Input:
       text:  list of single characters
    Action:
       Assemble text into a single string, and print it using
       wrapping if the printed line gets too long.
    Method:
       1. create a single string: quote = "".join(text)
       2. break string into words: words = quote.split()
       3. initialize line_length = 0
       4. visit each word:
            if new line length would be > 72,
                print()
                reset line length to 0
            print the word using ,end=" "
            update line length
    '''
    quote = "".join(text)
    words = quote.split(" ")
    line_length = 0
    for word in words:
        line_length += len(word)
        print(word, end=" ")
        if line_length >= 72:
            print("")
            line_length = 0    
    
    return

def choose_quote():
    '''
    Return:
      A single line from a file
    Method:
      open the file: handle = open('quotes.txt')
      read all its lines: lines = handle.readlines()
      generate a random index between 0 and len(lines)-1
      return that random line
    '''
    quotesdoc = open("quotes.txt", "r")
    quotes = quotesdoc.readlines()
    quote = random.choice(quotes)
    
    
    return quote

def encrypt(text):
    '''
    Input:
       text: a list of single characters
    Action:
       encrypt the list, using a substitution cipher
    Method:
       1. Get the alphabet = list(string.lowercase)
       2. Get a shuffled alphabet:
          cipher = list(string.lowercase)
          random.shuffle(cipher)
       3. Make a dictionary: substitution = dict()
       4. For each letter in the alphabet, find its cipher_letter, and set
          substitution[letter] = cipher_letter
       3. Go through text, and replace each letter with its substitution
    '''

    alphabet = list(string.ascii_lowercase)
    shifted_alphabet = random.sample(alphabet, len(alphabet))
    global substitution
    global substitution_caps
    substitution = dict()
    substitution_caps = dict()

    for letter, original_letter in enumerate(alphabet):
        replacement_letter = shifted_alphabet[letter]
        substitution[original_letter] = replacement_letter
    for letter, original_letter in enumerate(alphabet):
        replacement_letter = shifted_alphabet[letter]
        substitution_caps[original_letter.upper()] = replacement_letter.upper()
        
    text_letters = list(text)
    for index, original_letter in enumerate(text_letters):
        if original_letter.isupper() == True:
            if original_letter in substitution_caps:
                replacement = substitution_caps[original_letter]
            else:
                replacement = original_letter
        else:
            if original_letter in substitution:
                replacement = substitution[original_letter]
            else:
                replacement = original_letter
            
        text_letters[index] = replacement
        
    text = "".join(text_letters)
    
    return text


def exchange(text, first, second):
    '''
    Input:
       text: a list of single characters
       x: a character
       y: another character
    Go through all the entries in text:
       if an entry == x, replace it with y,
       and vice versa.  Handle upper-case versions of
       the letters too.

    '''
    text = list(text)
    for n, i in enumerate(text):
        if i ==  str(first):
            text[n] = str(second)
        if i ==  str(second):
            text[n] =  str(first)
    text = "".join(text)
    return text

def show_frequencies(text):
    '''
    Input:
       text: a list of single characters
    Action:
       Count how many times each character occurs, and
       print the counts.
    Method:
       1. create a dictionary of counts.
       2. go through all letters in text:
            if its count doesn't exist, set its count to 1
            otherwise, increment its count
    '''
    text = list(text.lower())
    alphabet = list(string.ascii_lowercase)
    frequencies = 0
    for letter in alphabet:
        frequencies = text.count(letter)
        print(letter.upper(),":", frequencies," | ", end = "")
    print("")
    return

def main():
    quote = choose_quote()
    print(quote)
    plaintext = list(quote)
    ciphertext = encrypt(plaintext)
    while True:
        print_wrapped(ciphertext)
        show_frequencies(ciphertext)
        crypt_letter = input('Letter to replace: ')
        plain_letter = input('Swap with:         ')
        ciphertext = exchange(ciphertext, crypt_letter, plain_letter)
        if ciphertext == plaintext:
            print_wrapped(ciphertext)
            print ('You did it!')
            break

if __name__ == '__main__':
    main()

#RS
