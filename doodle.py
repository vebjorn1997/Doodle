import random
from turtle import Turtle, Screen

def draw_rectangle(t: Turtle, startpos: tuple[float, float], width: float, height: float, color: str = "black", fill: bool = False):
    t.teleport(x=startpos[0], y=startpos[1])
    t.color(color)
    if fill:
        t.begin_fill()
    for i in range(4):
        if i % 2 != 0:
            t.forward(height)
        else:
            t.forward(width)
        t.right(90)
    if fill:
        t.end_fill()

def draw_line(t: Turtle, startpos, width, height, color, fill=False):
    t.teleport(x=startpos[0], y=startpos[1])
    t.color(color)
    if fill:
        t.begin_fill()
    for i in range(4):
        if i % 2 != 0:
            t.forward(width)
        else:
            t.forward(height)
        t.right(90)
    if fill:
        t.end_fill()

def draw_norway_flag(t: Turtle, screen: Screen, start_x: int = 0, start_y: int = 0, scale: int = 1):
    fraction_size = 10 * scale

    # White
    draw_line(t, (start_x, start_y), fraction_size, fraction_size * 7, "white", True)
    draw_line(t, (start_x+fraction_size*7-fraction_size, start_y), fraction_size * 7, fraction_size, "white", True)

    draw_line(t, (start_x, start_y+fraction_size*3), fraction_size, fraction_size * 7, "white", True)
    draw_line(t, (start_x+fraction_size*7-fraction_size, start_y+fraction_size*3-fraction_size), -fraction_size * 7, fraction_size, "white", True)

    draw_line(t, (start_x+fraction_size*9, start_y), fraction_size, fraction_size * 13, "white", True)
    draw_line(t, (start_x+fraction_size*9, start_y+fraction_size*3-fraction_size), -fraction_size * 7, fraction_size, "white", True)

    draw_line(t, (start_x+fraction_size*9, start_y+fraction_size*3), fraction_size, fraction_size * 13, "white", True)
    draw_line(t, (start_x+fraction_size*9, start_y), fraction_size*7, fraction_size, "white", True)

    # Red
    draw_rectangle(t, (start_x, start_y+fraction_size*9), fraction_size*6, fraction_size*6, "darkred", True)
    draw_rectangle(t, (start_x, start_y-fraction_size), fraction_size*6, fraction_size*6, "darkred", True) 
    draw_rectangle(t, (start_x+fraction_size*10, start_y+fraction_size*9), fraction_size*12, fraction_size*6, "darkred", True)
    draw_rectangle(t, (start_x+fraction_size*10, start_y-fraction_size), fraction_size*12, fraction_size*6, "darkred", True)

    # Blue
    draw_line(t, (start_x, start_y+fraction_size*2), fraction_size*2, fraction_size*22, "darkblue", True)
    draw_line(t, (start_x+fraction_size*7, start_y-fraction_size*7) , -fraction_size*16, fraction_size*2, "darkblue", True)

    # Border
    draw_rectangle(t, (start_x, start_y+fraction_size*9), fraction_size*22, fraction_size*16)

def configure(t: Turtle, screen: Screen):
    """    Configures the screen settings    """
    screen.setup(1.0, 1.0)
    screen.title("Doodle")
    screen.bgcolor("black")
    t.speed(0)
    t.hideturtle()

def main():
    t = Turtle()
    screen = Screen()
    configure(t, screen)

    user_input = random.randint(1, 3)
    for i in range(user_input):
        rnd_num_1 = random.randint(0, user_input)
        rnd_num_2 = random.randint(0, user_input)
        # print(rnd_num_1, rnd_num_2, user_input)
        draw_norway_flag(t, screen, -screen.window_width()/2, 0)


    screen.mainloop()

if __name__ == "__main__":
    main()
    # use system srguments to