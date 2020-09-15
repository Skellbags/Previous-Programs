'''
Read a text file, and determine how often each letter
in the alphabet occurs.
'''
import sys
from typing import Dict, List

def get_frequencies(filename: str) -> None:
    '''
    1. Open a text file.
    2. Read all its lines.
    3.    Turn each line to lower case (use .lower() )
    4.    Ignore any letters that are not a-z (use string.ascii_lower)
    5.    Compute the counts for each letter
    6. Go through all the letters,
    6.    Compute the frequency of each letter.
    7.    Print the letter, and its frequency.

    Parameter:
    ---------
    filename: the name of the text file
    '''

    try:
        file = open(filename, 'r')
        lines: List[str] = file.readlines()
    except UnicodeDecodeError as e:
        file = open(filename, 'r', encoding='utf-8')
        lines: List[str] = file.readlines()
    
    all_lines = ""
    for line in lines:
        line = line.lower()
        bad_chars = [';', ':', '!', "*", '"', "'", ".", " ", "\n", "\r", "?", ",", "-", "&"]
        for i in bad_chars: 
            line = line.replace(i, '')
        all_lines += line
    
    all_lines_lst = list(all_lines)
    total = len(all_lines_lst)
    counts = {}
    for x in all_lines_lst:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1
    stats_steeze = {}
    for x in sorted(counts):
        stats_steeze[x] = counts[x]/total
        print(x, stats_steeze[x])
    
    
def main():
    if len(sys.argv) != 2:
        print ('usage: python', sys.argv[0], '<filename>')
        sys.exit(1)

    get_frequencies(sys.argv[1])

if __name__ == '__main__':
    main()

