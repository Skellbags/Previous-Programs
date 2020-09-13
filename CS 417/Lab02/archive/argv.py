import sys

def print_block(width, height, symbol):
    print(((symbol) * (int(width))),("\n"+(symbol) * (int(width)) )* (int(height)-1))

def print_args():
    for arg in sys.argv[1:]:           
        print(arg)          

def print_names():
    for arg in sys.argv[1:] :
        if arg[0] == '-':
            print (arg[1:])     

def parse_arguments():
    index = 1
    while index < len(sys.argv):
        arg = sys.argv[index] 
        if arg == "-width":
            width = sys.argv[index+1]
        if arg == "-height":
            height = sys.argv[index+1]
        symbol = sys.argv[1]
        index += 1
    
    return (width, height, symbol)

def main():
    print ('-----print_args----------------')
    print_args()

    print ('-----print_names--------')
    print_names()

    print ('-----parse_arguments-----------')
    (width, height, symbol) = parse_arguments()
    print_block(width, height, symbol)

if __name__ == '__main__':
    main()

