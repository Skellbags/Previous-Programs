"""In this module, the input generator processes lines from stdin,
   with a few extra features:
   1. Line echoing can be turned on/off
   2. Generator ends on stdin EOF.
"""

def console(prompt):
    echo = False
    while True:
        try:
            line = input(prompt)
        except EOFError:
            # EOF, stop reading.
            break

        if echo:
            # Echo line to stdout
            print(line.rstrip('\n\r'))

        if len(line) == 0:
            # Empty line
            yield ""
            continue

        # Look for "@echo on" or "@echo off"
        tokens = line.rstrip('\n\r').split()
        if len(tokens) < 2:
            # It can't be @echo anything.
            yield line.rstrip('\n\r')
            continue

        # Got 2 or more tokens.
        if tokens[0].lower() == '@echo':
            echo = tokens[1].lower() == 'on'
            # Don't yield the @echo line
            continue
        else:
            # Ordinary input
            yield line.rstrip('\r\n')

def main():
    # Test the above function
    for line in console('> '):
        print('line: "' + line + '"')

if __name__ == '__main__':
    main()

