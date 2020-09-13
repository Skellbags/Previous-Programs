import random
import string

def replace_text(text, index, new_letter):
    '''
    Replace one entry in a string
    '''
    text_letters = list(text)
    text_letters[index] = new_letter
    text = "".join(text_letters)
    return text

def vowel_shift_mapping():
    '''
    Creates a mapping of the alphabet onto itself.
    All letters are mapped to themselves,
    except the vowels, which are mapped to different vowels
    '''

    alphabet = string.ascii_lowercase
    # Create a mapping of each letter onto itself
    mapping = dict()
    for letter in alphabet:
        mapping[letter] = letter

    # Now, change it so the vowels map to other vowels
    mapping['a'] = 'e'
    mapping['e'] = 'i'
    mapping['i'] = 'o'
    mapping['o'] = 'u'
    mapping['u'] = 'a'
    mapping[' '] = ' '
    return mapping

def replace_all(text, mapping):
    '''
    Apply the mapping to every letter in the text.
    Return the modified text.
    '''
    text_letters = list(text)
    for index, original_letter in enumerate(text_letters):
        if original_letter in mapping:
            replacement = mapping[original_letter]
        else:
            replacement = original_letter
        text_letters[index] = replacement
    text = "".join(text_letters)
    return text

def make_shift_mapping(offset):
    '''
    Create a dictionary that maps each lower-case letter
    to the one 'offset' later in the alphabet.
    Example: if offset is 2, then
    a -> c
    b -> d
    c -> e
    ...
    x -> z
    y -> a
    z -> b
    '''
    alphabet = string.ascii_lowercase
    mapping = dict()
    shifted_alphabet =  alphabet[offset:] + alphabet[:offset]

    for index, original_letter in enumerate(alphabet):
        replacement_letter = shifted_alphabet[index]
        mapping[original_letter] = replacement_letter
        
    

    return mapping

def invert(mapping):
    '''
    Given a mapping, create its inverse.
    For each (key, value) pair in mapping,
    set inverse[value] = key
    '''
    inverse = dict()
    for key, value in mapping.items():
        inverse[value] = key

    return inverse

def scrambled(text):
    '''
    Return a scrambled version of a string.
    Create a list,
    call scramble(<list name>)
    then join the scrambled letter
    and RETURN the result
    '''
    text_letters = list(text)
    random.shuffle(text_letters)
    text = "".join(text_letters)
    return text

def shift_encipher(text, offset):
    '''
    Create a shift mapping, and apply it to the text.
    Return the result
    '''
    mapping = make_shift_mapping(offset)
    new_text = replace_all(text, mapping)
    
    return new_text

def shift_decipher(text, offset):
    '''
    Create a shift mapping, get the inverse, then apply that to the text.
    Return the result.
    '''
    mapping = make_shift_mapping(offset)
    mapping = invert(mapping)
    new_text = replace_all(text, mapping)

    return new_text
def main():
    print( "----ostrich with u---------------------")
    print( replace_text('ostrich', 4, 'u') )

    print( "----vowel shifted----------------------")
    vowel_shifter = vowel_shift_mapping()
    print( replace_all('enemy troops in north sector', vowel_shifter) )

    print( "----enciphered-------------------------")
    print( shift_encipher('enemy troops in north sector', 5) )

    print( "----deciphered-------------------------")
    print( shift_decipher('ivh jvuzaypjavy', 7) )

    print( "----scrambled--------------------------")
    print( scrambled('ecdyasist') )

if __name__ == '__main__':
    main()

#RS
