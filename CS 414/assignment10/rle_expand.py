from rle_compress import get_lines

def rle_decode(lines, out_file_name):
    '''
    This is similar to rle_encode, in that you should
    - open the given file for output, and
    - process the given list of lines, while
    - writing values to the output file.

    However, each line now consists of pairs of chars,
    where each pair is a run.
    so you need something like this, to grab pairs:
    for i in range(0, len(line), 2):
        count = line[i]
        value = line[i + 1]
    '''
    
    out_handle = open(out_file_name, 'w')
    for line in lines:
        line = line.rstrip('\n\r')
        for i in range(0, len(line), 2):
            count = line[i]
            value = line[i + 1]
            line_out = ""
            line_out = line_out + (value * int(count))
            out_handle.write(line_out)
        out_handle.write("\n")
            
    out_handle.close()
    
    return

def main():
    in_filename = input('Input file? ')
    out_filename = input('Output file? ')

    lines = get_lines(in_filename)
    rle_decode(lines, out_filename)

if __name__ == '__main__':
    main()
#RS
