import turtle
 
my_turtle = turtle.Turtle()

def draw_triangle(centre_x, centre_y, width, height, pen_color, fill_color):
    """

    :param centre_x:
    :param centre_y:
    :param width:
    :param height:
    :param pen_color:
    :param fill_color:
    """




# draw rectangle
def draw_rectangle(centre_x=0, centre_y=0, width=0, height=0, pen_color='black', fill_color='red'):
    """
    drawing boundary
    :param centre_x:
    :param centre_y:
    :param width:
    :param height:
    :param pen_color:
    :param fill_color:
    """

    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.pencolor(pen_color)

    for i in range(2):
        my_turtle.forward(width) #Forward turtle by width units
        my_turtle.left(90) #Turn turtle by 90 degree
        my_turtle.forward(height) #Forward turtle by height units
        my_turtle.left(90) 
    save_state()
    


# draw circle
def draw_circle(centre_x, centre_y, radius, pen_color, fill_color):
    """

    :param centre_x:
    :param centre_y:
    :param radius:
    :param pen_color:
    :param fill_color:
    """
    pass


# stamp_turtle
def stamp_turtle(centre_x, centre_y, color):
    """

    :param centre_x:
    :param centre_y:
    :param color:
    """
    pass



def distance(x1, y1, x2, y2):
    pass

def save_state(centre_X=0, centre_y=0, pen_color=0, fill_color=0):
    """
    :param centre_X:
    :param centre_y:
    :param pen_color:
    :param fill_color:

    """
    turtle.getscreen()._root.mainloop()  # <-- run the Tkinter main loop


# restore_state
def restore_state():
    """

    """
