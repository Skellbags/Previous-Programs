'''
Takes two filenames from the command line, and determines
if the files have the same content.
'''

import sys

def main():
    if len(sys.argv) != 3:
        print('Usage:\n  python diff.py <file1> <file2>')
        sys.exit(1)
    try:
        file1 = open(sys.argv[1], 'r')
        file2 = open(sys.argv[2], 'r')
    except FileNotFoundError:
        print("File doesn't exist:", sys.argv[1])
        sys.exit(1)
        
    for line in file1.readlines():
        line1 = line.rstrip("\n\r")
    for line in file2.readlines():
        line2 = line.rstrip("\n\r")
    if line1 == line2:
        print("Files Same")
    else:
        print("Files Differ")
    
    file1.close()
    file2.close()
        
    

    
if __name__ == '__main__':
    main()
