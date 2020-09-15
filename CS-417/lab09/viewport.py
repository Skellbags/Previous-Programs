'''
A viewport into a larger rectangular ASCII picture
'''
class Viewport:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def set_img(self, width, height):
        """
        STEP 5:
        create self.img_width and self.img_height
        """
        self.x = self.width // 2 - self.width // 2
        self.y = self.height // 2 - self.height // 2

    def move_up(self):
        """
        I've done this one for you.  Compare it to the
        move_up FUNCTION in img_viewer.py: it's very similar!

        Make similar changes in move_up, move_left, and move_right.
        """
        self.y -= self.height // 4
        top = self.y - self.height   # top is a local variable, not part of self
        if top < 0:
            self.y = self.height

    def move_down(self):
        """
        STEP 6:
        Copy move_down from img_viewer.py, and modify it
        to use self.x, self.y, self.width, self.height,
        self.img_width, and self.img_height.

        See move_up(self) method just above.
        """
        self.y += self.height // 4
        bottom = self.y - self.height # Check if we've hit the bottom of the image
        if bottom > 0:
           self.y = self.height

    def move_left(self):
        """
        STEP 6:
        Copy move_left() function here, and adapt it.
        """
        self.x -= self.width // 4
        # but don't move past the left edge
        left = self.x - self.width
        if left < 0:
            self.x = self.width

    def move_right(self):
        """
        STEP 6:
        Copy move_right() function here, and adapt it.
        """
        self.x += self.width // 4
        # and make sure we don't go over the right edge
        if self.x > 0:
            self.x = self.width
        #return (x, y, width, height)

    def display(self, img):
        """
        STEP 7:
        Copy display() function here, and adapt it.
        """
        top = self.y - self.height
        left = self.x - self.width
        bottom = self.y
        right = self.x

        for row in range(top, bottom):
            line = ''
            for pixel in img[row][left : right]:
                if pixel == '0':
                    line += '*'
                else:
                    line += '.'
            print (line)

    """
    Step 8:
    Implement __str__(self) method
    """
    def __str__(self):
        return 'viewport (x y w h)=({} {} {} {})'.format(self.x, self.y,self.width, self.height)
        
