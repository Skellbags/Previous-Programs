import sys

def print_file(filename):
    handle = open(filename, 'r')
    lines = handle.readlines()
    handle.close()
    return print(lines)
    
def print_lines(filename):
    handle = open(filename, 'r')
    lines = handle.readlines()
    for line in lines:
        line = line.rstrip('\n\r')
        print(line)
    handle.close()
    return line

def print_splits(filename):
    handle = open(filename, 'r')
    lines = handle.readlines()
    for line in lines:
        line = line.rstrip('\n\r')
        words_in_line = line.split()
        print(words_in_line)
    handle.close()
    return words_in_line

def print_words(filename):
    handle = open(filename, 'r')
    lines = handle.readlines()
    for line in lines:
        line = line.rstrip('\n\r')
        words_in_line = line.split()
        for word in words_in_line:
            print(word, end=" ")
    handle.close()
    print()
    return line

def words_length(filename):
    handle = open(filename, 'r')
    lines = handle.readlines()
    for line in lines:
        line = line.rstrip('\n\r')
        words_in_line = line.split()
        line_length = 0
        for word in words_in_line:
            line_length += len(word) + 1
        print(line_length)
    handle.close()
    print(line_length)
    return line

def print_reflowed(filename, width):
    handle = open(filename, 'r')
    lines = handle.readlines()
    for line in lines:
        line = line.rstrip('\n\r')
        words_in_line = line.split()
        line_length = 0
        for word in words_in_line:
            line_length += len(word) + 1
            if (line_length + 1 + len(word)) > width:
                line_length = 0
                print( )
            print(word, end=" ")
    handle.close()
    return line

def print_right_aligned(filename, width):
    handle = open(filename, 'r')
    lines = handle.readlines()
    for line in lines:
        line = line.rstrip('\n\r')
        words_in_line = line.split()
        line_length = 0
        words = []
        for word in words_in_line:
            line_length += len(word) + 1
            words.append(word)
            if (line_length + 1 + len(word)) > width:
                spaces = width - line_length
                print(" "*spaces, end="")
                for word in words:
                    print(word, end=" ")
                print()
                line_length = 0
                words = []
        
    handle.close()
    return 

def print_justified(filename, width):
    handle = open(filename, 'r')
    lines = handle.readlines()
    for line in lines:
        line = line.rstrip('\n\r')
        words_in_line = line.split()
        line_length = 0
        words = []
        for word in words_in_line:
            line_length += len(word) + 1
            words.append(word)
            if (line_length + 1 + len(word)) > width:
                spaces = width - line_length
                for word in words:
                    print(word, end=" ")
                    if spaces > 5:
                        print(" "*2, end="")
                        spaces -= 2
                    elif spaces > 3:
                        print(" "*1, end="")
                        spaces -= 1
                    else:
                        pass
                print()
                line_length = 0
                words = []
        
    handle.close()

def main():
    filename = 'independence.txt'
    width = 40
    print("print file:")
    print("--------------------")
    print_file(filename)
    print("print lines:")
    print("--------------------")
    print_lines(filename)
    print("print splits:")
    print("--------------------")
    print_splits(filename)
    print("print words:")
    print("--------------------")
    print_words(filename)
    print("words length:")
    print("--------------------")
    words_length(filename)
    print("print reflowed:")
    print("--------------------")
    print_reflowed(filename, width)
    print("print right_aligned:")
    print("--------------------")
    print_right_aligned(filename, width)
    print("print justified:")
    print("--------------------")
    print_justified(filename, width)

if __name__ == '__main__':
    main()
