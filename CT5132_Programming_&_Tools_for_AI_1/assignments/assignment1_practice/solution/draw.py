# I/we declare that this file represents our own work, and that we
# have not seen any work on this assignment done by others, and that
# we have not shown our work to any others.

# Student name(s): Jiarong Li
# Student ID(s): 20230033

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
    
    # We use i to represent the number of row of the grid, and j to represent the number of colonm of the grid.
    for shape in shapes: # shapes is a list
        
        if shape[0] == 'rect': # if we need to draw a *rect*
            
            starting_point_j = shape[2] # The position of colonm of starting point
            starting_point_i = shape[3] # The position of row of starting point
            rect_width = shape[4] # The width of *rect*
            rect_height = shape[5] # The height of *rect*
            
            drawing_height = distance(starting_point_j, starting_point_i, 
                                      starting_point_j, starting_point_i+rect_height-1) # The height of picture.
            
            drawing_width = distance(starting_point_j, starting_point_i, 
                                     starting_point_j+rect_width-1, starting_point_i) # The width of picture.
            
            dis_start_right = distance(starting_point_j, starting_point_i,
                                      width-1, starting_point_i) # We calculate the distance from starting point to right hand side of the grid.
            
            dis_start_bottom = distance(starting_point_j, starting_point_i,
                                       starting_point_j, height-1) # We calculate the distance from starting point to bottom of the grid.
            
            if drawing_height > dis_start_bottom: # If the height of the picture is greater than the distance we can use,
                drawing_height = dis_start_bottom # we save the shorter one as the height of picture.
            if drawing_width > dis_start_right: 
                drawing_width = dis_start_right
                
            for i in range(starting_point_i, int(starting_point_i+drawing_height+1)): 
                for j in range(starting_point_j, int(starting_point_j+drawing_width+1)): 
                    canvas[i][j] = shape[1]
                
        
        elif shape[0] == 'disc': # if we need to draw a *disc*
            
            centra_j = shape[2]
            centra_i = shape[3]
            radius = shape[4]
            
            if radius % 2 == 0: # I found when radius is even, the length of outter line of each direction equals to radius + 1.
                outline = radius + 1 # The length of outter line for each direction.
                
                # I found that there is always a *rect* inside the *disc*.
                # We hence first draw the basic *rect* of the *disc*, then draw the rest part of *disc*.
                
                # We calculate the position of the points we need on the grid.
                left_most_width = centra_j - radius + 1 # The position of left side of the *rect*. j represents the row number.                
                right_most_width = centra_j + radius - 1 # The position of right side of the *rect*. j represents the row number. 
                
                top_most_height_basic_rect = centra_i-radius/2 # The position of top line of the basic *rect*. i represents the colonm number.
                bottom_most_height_basic_rect = centra_i+radius/2 # The position of top line of the basic *rect*. i represents the colonm number.
                
                top_most_height = centra_i - radius + 1 # The top position of the *disc*.
                bottom_most_height = centra_i + radius - 1 # The bottom position of the *disc*.
                
                len_basic_rect_width = right_most_width - left_most_width + 1 # The width of basic *rect*.
                
                # We first draw the basic rect inside the disc.
                for i in range(int(top_most_height_basic_rect), int(bottom_most_height_basic_rect)+1):
                    for j in range(left_most_width, right_most_width+1):
                        canvas[i][j] = shape[1]
                
                # The length of outter line of each direction should be the same and equals to *outline*. 
                while len_basic_rect_width != outline:
                    # draw rest of the disc
                    for j in range(left_most_width+1, right_most_width):
                        canvas[int(top_most_height_basic_rect-1)][j] = shape[1]
                        canvas[int(bottom_most_height_basic_rect+1)][j] = shape[1]
                    len_basic_rect_width = len_basic_rect_width - 2
                    left_most_width += 1 
                    right_most_width -= 1
                    top_most_height_basic_rect -= 1
                    bottom_most_height_basic_rect += 1
                            
            else: # I found when radius is odd, the length of outter line of each direction equals to radius.
                outline = radius
                                
                # We first draw the basic rect of the disc.
                left_most_width = centra_j - radius + 1 # j
                right_most_width = centra_j + radius - 1 # j
                
                top_most_height_basic_rect = centra_i-(radius-1)/2 # i
                bottom_most_height_basic_rect = centra_i+(radius-1)/2 # i
                
                top_most_height = centra_i - radius + 1 
                bottom_most_height = centra_i + radius - 1 
                
                len_basic_rect_width = right_most_width - left_most_width + 1
                
                # basic rect inside the disc
                for i in range(int(top_most_height_basic_rect), int(bottom_most_height_basic_rect)+1):
                    for j in range(left_most_width, right_most_width+1):
                        canvas[i][j] = shape[1]
                        
                while len_basic_rect_width != outline:
                    # draw rest of the disc
                    for j in range(left_most_width+1, right_most_width):
                        canvas[int(top_most_height_basic_rect-1)][j] = shape[1]
                        canvas[int(bottom_most_height_basic_rect+1)][j] = shape[1]
                    len_basic_rect_width = len_basic_rect_width - 2
                    left_most_width += 1 
                    right_most_width -= 1
                    top_most_height_basic_rect -= 1
                    bottom_most_height_basic_rect += 1


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
        ['disc', 'o', 9, 8, 5],
        ['disc', '(', 9, 21, 9],
        ['rect', '=', 2, 3, 15, 2],
        ['rect', '=', 5, 0, 9, 3],
        ['rect', ' ', 6, 7, 2, 2],
        ['rect', ' ', 11, 7, 2, 2],
        ['rect', '#', 8, 12, 3, 7],
        ['rect', '=', 13, 14, 8, 3],
        ['rect', '|', 19, 7, 3, 8],
        ['disc', '@', 4, 20, 5],
        ['disc', '@', 20, 4, 3]
    ]
    render(draw(shapes, height, width))

    
if __name__ == '__main__':
    my_drawing()
