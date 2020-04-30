import turtle

from utilities import (distance, draw_circle, draw_rectangle, draw_triangle,
                       restore_state, save_state, stamp_turtle)


turtle.setup(800, 800)

def main():
    draw_rectangle() # house drawing area
    draw_triangle()
    
    #  two circles 
    # draw_circle(centre_x=0, centre_y=370) # tree circle
    # draw_circle(centre_x=100, centre_y=370) # Bird circle

    draw_circle(centre_x=20, centre_y=320) # tree circle for testing
    draw_circle(centre_x=80, centre_y=320) # Bird circle for testing

    # Tkinter main loop.
    turtle.getscreen()._root.mainloop() 


# turtle.onscreenclick()


def handle_click(x, y):
    print('detected a click at', x, y)


# create a listener function which is called automatically on button
def left_keypress():
    print('left key detected')


# in main function, declare left_keypress as the listener function
turtle.listen()
turtle.onkey(left_keypress, 'Left')

turtle.register_shape('bird',
                      ((-22, -39), (-20, -7), (-7, 3), (-11, 7), (-12, 9), (-11, 10), (-9, 10), (-3, 7),
                       (10, 24), (30, 16), (13, 18), (4, 0), (14, -6), (6, -13), (0, -4), (-14, -13), (-22, -
                      39)))

turtle.shape('bird')

# turtle.tiltangle(new_tilt_value)

if __name__ == "__main__":
    main()