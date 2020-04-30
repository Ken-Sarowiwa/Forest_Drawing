import math
import turtle



my_turtle = turtle.Turtle()

def draw_triangle(centre_x=0, centre_y=0, width=100, height=120, pen_color='black', fill_color='red'):
    """

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
    my_turtle.up()
    my_turtle.goto(centre_x,centre_y)
    my_turtle.down()

    my_turtle.forward(width) # base

    my_turtle.left(height)
    my_turtle.forward(width)
    
    my_turtle.left(height)
    my_turtle.forward(width)
    
    save_state()




# draw rectangle
def draw_rectangle(centre_x=-400, centre_y=-400, width=700, height=700, pen_color='black', fill_color='red'):
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
    my_turtle.up()
    my_turtle.goto(centre_x,centre_y)
    my_turtle.down()

    for i in range(2):
        my_turtle.forward(width) #Forward turtle by width units
        my_turtle.left(90) #Turn turtle by 90 degree
        my_turtle.forward(height) #Forward turtle by height units
        my_turtle.left(90) 

    save_state()
    


# draw circle
def draw_circle(centre_x=0, centre_y=0, radius=10, pen_color='black', fill_color='red'):
    """

    :param centre_x:
    :param centre_y:
    :param radius:
    :param pen_color:
    :param fill_color:
    """
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    
    my_turtle.pencolor(pen_color)
    my_turtle.up()
    my_turtle.goto(centre_x,centre_y)
    my_turtle.down()
    my_turtle.circle(radius)

    save_state()


# stamp_turtle
def stamp_turtle(centre_x, centre_y, color):
    """

    :param centre_x:
    :param centre_y:
    :param color:
    """
    
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    my_turtle.pencolor(color)
    my_turtle.up()
    my_turtle.goto(centre_x,centre_y)
    my_turtle.down()
    
    my_turtle.stamp()
    
    save_state()



def distance(x1, y1, x2, y2):
    """
    Find cartesian distance between two points (x1,y1) and (x2,y2)
    """
    point_1 = [x1, y1]
    point_2 = [x2, y2]
    distance = math.sqrt( ((point_1[0]-point_2[0])**2)+((point_1[1]-point_2[1])**2) )

    return distance

def save_state(centre_X=0, centre_y=0, pen_color=0, fill_color=0):
    """
    :param centre_X:
    :param centre_y:
    :param pen_color:
    :param fill_color:
    save 
    position, pen color, fill color) in global variables

    """
    pass


# restore_state
def restore_state():
    """
    Reload turtle state

    """
    