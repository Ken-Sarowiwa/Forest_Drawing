import turtle
from utilities import draw_triangle
from utilities import draw_circle
from utilities import draw_rectangle
from utilities import stamp_turtle
from utilities import distance
from utilities import save_state
from utilities import restore_state


def main():
    import turtle
    draw_triangle()
    draw_circle()
    draw_rectangle()
    stamp_turtle()
    distance()
    save_state()
    restore_state()
    turtle.setup(window_width, window_height)
    turtle.listen(handle_click())


turtle.onscreenclick()


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

turtle.tiltangle(new_tilt_value)

main()
