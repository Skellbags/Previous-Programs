from typing import List

def print_picture(picture: List[List[str]]) -> None:
    """Print the whole 2D array of pixels."""

    # for each row, print("".join(picture[row]))
    for row in picture:
        print("".join(row))
    

def put_pixel(x: int, y: int, c: str, picture: List[List[str]]) -> None:
    """Set one pixel in the picture"""
    picture[y][x] = c

def h_line(x1: int, x2: int, y: int, symbol: str,
           picture: List[List[str]]) -> None:
    """Draw a horizontal line made up of symbols."""

    # You need a for x loop that ranges from x1 through x2
    # At each x,y, call put_pixel
    for x in range(x1, x2+1):
        put_pixel(x, y, symbol, picture)
    

def v_line(x: int, y1: int, y2: int, symbol: str,
           picture: List[List[str]]) -> None:
    """Draw a vertical line made up of symbols."""

    # Very similar to h_line, but for y instead of for x.
    for y in range(y1, y2+1):
        put_pixel(x, y, symbol, picture)
    

def draw_line(x1: int, y1: int, x2: int, y2: int, symbol: str,
              picture: List[List[str]]) -> None:
    """Draw a line between two endpoints.  See the instructions."""
    x, y = x1, y1
    dx, dy = x2 - x1, y2 - y1
    if dx > 0:
        sign_x = 1
    else:
        sign_x = -1
    if dy > 0:
        sign_y = 1
    else:
        sign_y = -1
    if abs(dx) > abs(dy):
        step_x = sign_x
        step_y = sign_x * (dx // dy)
        num_steps = abs(dx)
    else:
        step_y = sign_y
        step_x = sign_y * (dx // dy)
        num_steps = abs(dy)
    for step in range(num_steps):
        put_pixel(x+step, y-step, symbol, picture)
        
    

def block(x1: int, y1: int, w: int, h: int, symbol: str,
          picture: List[List[str]]) -> None:
    """Draw a block of symbols.  See the instructions."""
    for y in range(y1, y1+h-1):
        for x in range(x1, x1+w):
            put_pixel(x, y, symbol, picture)
    

def draw_sprite(x1: int, y1: int, sprite: List[str],
                picture: List[List[str]]) -> None:
    """Draw a block of sprite pixels.  See the instructions."""
    w, h = len(sprite[0]), len(sprite)
    for y in range(y1, y1+h):
        for x in range(x1, x1+w):
            symbol = sprite[y-y1][x-x1]
            put_pixel(x, y, symbol, picture)
    

def main() -> None:
    with open('scene.txt', 'r') as handle:
        lines = handle.readlines()

    w: int
    h: int
    [w, h] = [int(x) for x in lines[0].split()]

    picture: List[List[str]] = []
    x : int
    y : int
    for y in range(h):
        row: List[str] = []
        for x in range(w):
            row.append('.')
        picture.append(row)

    line: str
    for line in lines[1:] :
        fields: List[str] = line.rstrip('\n\r').split()
        x1: int
        x2: int
        y1: int
        y2: int
        symbol: str
        if fields[0] == 'h':
            x1 = int(fields[1])
            x2 = int(fields[2])
            y  = int(fields[3])
            symbol = fields[4]
            h_line(x1, x2, y, symbol, picture)
        elif fields[0] == 'v':
            x  = int(fields[1])
            y1 = int(fields[2])
            y2 = int(fields[3])
            symbol = fields[4]
            v_line(x, y1, y2, symbol, picture)
        elif fields[0] == 'l':
            x1 = int(fields[1])
            y1 = int(fields[2])
            x2 = int(fields[3])
            y2 = int(fields[4])
            symbol = fields[5]
            draw_line(x1, y1, x2, y2, symbol, picture)
        elif fields[0] == 'b':
            x = int(fields[1])
            y = int(fields[2])
            w = int(fields[3])
            h = int(fields[4])
            symbol = fields[5]
            block(x, y, w, h, symbol, picture)
        elif fields[0] == 's':
            x = int(fields[1])
            y = int(fields[2])
            sprite: List[str] = fields[3:]
            draw_sprite(x, y, sprite, picture)

        print_picture(picture)
        print ('After', line)

if __name__ == '__main__':
    main()



