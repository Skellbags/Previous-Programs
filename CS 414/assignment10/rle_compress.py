def get_lines(input_file_name):
    '''
    Open the file, and read all its lines into a list.
    Then, return the list
    '''
    in_handle = open(input_file_name, 'r')
    lines = in_handle.readlines()
    in_handle.close()
    return lines

def rle_encode(lines, out_file_name):
    '''
    Compress the lines, using run-length encoding.

    Open the given file for output.
    For each line,
      - trim the trailing \n
      - find runs of repeated chars
      - if a run is longer than 9, finish it and start a new run.
      - write() each run to the file, as two chars
      - remember the last run in the line!
      - at the end of the line, write() a \n
    Close the file
    '''
    out_handle = open(out_file_name, 'w')
    for line in lines:
        line = line.rstrip('\n\r')
        previous = line[0]
        count = 1
        for char in line[1:]:
            if char == previous:
                if count == 9:
                    out_handle.write(str(count))
                    out_handle.write(previous)
                    count = 1
                else:
                    count += 1
            else:
                out_handle.write(str(count))
                out_handle.write(previous)
                count = 1
            previous = char
        out_handle.write(str(count))
        out_handle.write(previous)
        out_handle.write("\n")
            
    out_handle.close()

    return

def main():
    in_filename = input('Input file? ')
    out_filename = input('Output file? ')

    lines = get_lines(in_filename)
    rle_encode(lines, out_filename)

if __name__ == '__main__':
    main()
#RS
