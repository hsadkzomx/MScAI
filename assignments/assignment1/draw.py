# I/we declare that this file represents our own work, and that we
# have not seen any work on this assignment done by others, and that
# we have not shown our work to any others.

# Student name(s): James McDermott
# Student ID(s): 00001234

# Do not change the formatting above. For multiple names/IDs, use
# commas to separate.


import math

def distance(x0, y0, x1, y1):
    # Euclidean distance between (x0, y0) and (x1, y1).
    # Don't change this.
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

def render(canvas):
    # This function takes in a canvas which has already been drawn on,
    # and prints it. Don't change this.
    for row in canvas:
        print(' '.join(row))

def draw(shapes, width, height):
    '''Draw a simple picture on a grid.

    A picture is specified as a list of shapes. Each shape is either a
    `disc` or a `rect`.

    `draw` creates the grid as a list of lists and draws the shapes.

    A second function, `render`, takes care of some details of
    printing correctly.

    The coordinate system starts at the top-left of the image.

    Here we draw a rectangle, using the 'colour' #,
    with top-left (0, 0), with width 2 and height 3,
    in a grid of width 10 and height 5
    >>> render(draw([['rect', '#', 0, 0, 2, 3]], 10, 5))
    # # . . . . . . . .
    # # . . . . . . . .
    # # . . . . . . . .
    . . . . . . . . . .
    . . . . . . . . . .

    >>> render(draw([['disc', '#', 2, 2, 2]], 5, 5))
    . . . . .
    . # # # .
    . # # # .
    . # # # .
    . . . . .

    If a shape goes beyond the grid, we just draw the part that
    is inside the grid:
    >>> render(draw([['rect', '#', 3, 3, 9, 9]], 5, 5))
    . . . . .
    . . . . .
    . . . . .
    . . . # #
    . . . # #

    If one shape overlaps another, the later overwrites the earlier:
    >>> render(draw([['disc', '#', 10, 10, 5], ['rect', '=', 5, 5, 3, 5]], 20, 20))
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . = = = . . . . . . . . . . . .
    . . . . . = = = # # # # # . . . . . . .
    . . . . . = = = # # # # # # . . . . . .
    . . . . . = = = # # # # # # # . . . . .
    . . . . . = = = # # # # # # # . . . . .
    . . . . . . # # # # # # # # # . . . . .
    . . . . . . # # # # # # # # # . . . . .
    . . . . . . # # # # # # # # # . . . . .
    . . . . . . . # # # # # # # . . . . . .
    . . . . . . . . # # # # # . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . .

    '''
    
    canvas = [['.' for _ in range(width)] for _ in range(height)]

    ## YOUR CODE HERE
    return canvas



def owl():
    '''

    This function is a test. No need to change anything.

    >>> owl()
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . # # # # # . . . . .
    . . . . . . . . . . . . . . . . . . . # # # . . . . . . . .
    . . . . . . . . . . . . . . . . . . # # # . . . . . . . . .
    . . . . . . . . . . . . . . . . . . # # # . . . . . . . . .
    . . . . . . . . . . . . . . . . . . # # # . . . . . . . . .
    . . . . . . . . . . . . . . . . . . # # # . . . . . . . . .
    . . . . . . . . . . . . . . . . . . # # # . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . # # # . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . # # # # # . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . = = . . . . . . = = . . . . . . . . . . . . . . .
    . . . . . = = . . . . . . = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . =       = =       = . . . . . . . . . . . . . . .
    . . . . . =       = =       = . . . . . . . . . . . . . . .
    . . . . . =       = =       = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    . . . . . = = = = = = = = = = . . . . . . . . . . . . . . .
    
    '''
    shapes = [
        ['disc', '#', 22, 8, 5],
        ['disc', '.', 24, 8, 4],
        ['rect', '=', 5, 18, 10, 12],
        ['rect', ' ', 6, 22, 3, 3],
        ['rect', ' ', 11, 22, 3, 3],
        ['rect', '.', 7, 18, 6, 2],
        ]
        
    render(draw(shapes, 30, 30))

def my_drawing():
    
    # Draw a picture of whatever you like. 

    # No doctests needed for this function.

    # For this function, run it using $ python draw.py

    # Set width, height as you like.
    height, width = 30, 30
    
    shapes = [
        ## YOUR CODE HERE
    ]
    render(draw(shapes, height, width))

    
if __name__ == '__main__':
    my_drawing()
