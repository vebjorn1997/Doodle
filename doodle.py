from turtle import Turtle, Screen
import random
import argparse
import os
import docker
import docker.errors


def draw_rectangle(
    t: Turtle,
    startpos: tuple[float, float],
    width: float,
    height: float,
    color: tuple[int, int, int] = (0, 0, 0),
    fill: bool = False,
):
    """
    Draws a rectangle with the given parameters
    :param t: Turtle object
    :param startpos: Tuple with the x and y coordinates of the starting position
    :param width: Width of the rectangle
    :param height: Height of the rectangle
    :param color: Color of the rectangle
    :param fill: If the rectangle should be filled or not
    """
    t.teleport(x=startpos[0], y=startpos[1])
    t.color((color))
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


def draw_circle(
    t: Turtle,
    startpos: tuple[float, float],
    radius: float,
    color: tuple[int, int, int] = (0, 0, 0),
    fill: bool = False,
):
    """
    Draws a circle with the given parameters
    :param t: Turtle object
    :param startpos: Tuple with the x and y coordinates of the starting position
    :param radius: Radius of the circle
    :param color: Color of the circle
    :param fill: If the circle should be filled or not
    """
    t.teleport(x=startpos[0], y=startpos[1])
    t.color((color))
    if fill:
        t.begin_fill()
    t.dot(radius)
    if fill:
        t.end_fill()


def draw_norway_flag(
    t: Turtle, start_x: int = 0, start_y: int = 0, fraction_size: int = 10
):
    """
    Draws the Norwegian flag with the given parameters
    :param t: Turtle object
    :param start_x: Starting x position
    :param start_y: Starting y position
    :param fraction_size: Size of the fractions
    """
    # White
    draw_rectangle(
        t,
        (start_x, start_y),
        fraction_size * 16,
        fraction_size * 22,
        (255, 255, 255),
        True,
    )

    # Red
    draw_rectangle(
        t, (start_x, start_y), fraction_size * 6, fraction_size * 6, (186, 12, 47), True
    )
    draw_rectangle(
        t,
        (start_x, start_y - fraction_size * 10),
        fraction_size * 6,
        fraction_size * 6,
        (186, 12, 47),
        True,
    )
    draw_rectangle(
        t,
        (start_x + fraction_size * 10, start_y),
        fraction_size * 6,
        fraction_size * 12,
        (186, 12, 47),
        True,
    )
    draw_rectangle(
        t,
        (start_x + fraction_size * 10, start_y - fraction_size * 10),
        fraction_size * 6,
        fraction_size * 12,
        (186, 12, 47),
        True,
    )

    # Blue
    draw_rectangle(
        t,
        (start_x, start_y - fraction_size * 7),
        fraction_size * 2,
        fraction_size * 22,
        (0, 32, 91),
        True,
    )
    draw_rectangle(
        t,
        (start_x + fraction_size * 7, start_y),
        fraction_size * 16,
        fraction_size * 2,
        (0, 32, 91),
        True,
    )

    # Border
    draw_rectangle(t, (start_x, start_y), fraction_size * 16, fraction_size * 22)


def draw_sweden_flag(
    t: Turtle, start_x: int = 0, start_y: int = 0, fraction_size: int = 10
):
    """
    Draws the Danish flag with the given parameters
    :param t: Turtle object
    :param start_x: Starting x position
    :param start_y: Starting y position
    :param fraction_size: Size of the fractions
    """
    # Yellow
    draw_rectangle(
        t,
        (start_x, start_y),
        fraction_size * 10,
        fraction_size * 16,
        (254, 204, 2),
        True,
    )

    # Blue
    draw_rectangle(
        t, (start_x, start_y), fraction_size * 4, fraction_size * 5, (0, 82, 147), True
    )
    draw_rectangle(
        t,
        (start_x, start_y - fraction_size * 6),
        fraction_size * 4,
        fraction_size * 5,
        (0, 82, 147),
        True,
    )
    draw_rectangle(
        t,
        (start_x + fraction_size * 7, start_y),
        fraction_size * 4,
        fraction_size * 9,
        (0, 82, 147),
        True,
    )
    draw_rectangle(
        t,
        (start_x + fraction_size * 7, start_y - fraction_size * 6),
        fraction_size * 4,
        fraction_size * 9,
        (0, 82, 147),
        True,
    )

    # Border
    draw_rectangle(t, (start_x, start_y), fraction_size * 10, fraction_size * 16)


def draw_bangladesh_flag(
    t: Turtle, start_x: int = 0, start_y: int = 0, fraction_size: int = 10
):
    """
    Draws the Bangladeshi flag with the given parameters
    :param t: Turtle object
    :param start_x: Starting x position
    :param start_y: Starting y position
    :param fraction_size: Size of the fractions
    """
    # Green
    draw_rectangle(
        t,
        (start_x, start_y),
        fraction_size * 12,
        fraction_size * 20,
        (0, 106, 78),
        True,
    )

    # Dot
    draw_circle(
        t,
        (start_x + fraction_size * 9, start_y - fraction_size * 6),
        fraction_size * 8,
        (244, 42, 65),
        True,
    )

    # Border
    draw_rectangle(t, (start_x, start_y), fraction_size * 12, fraction_size * 20)


def draw(screen: Screen, t: Turtle, args: argparse.Namespace):
    for _ in range(random.randint(1, 5)):
        fraction_size = random.randint(1, 5) * 10
        start_x = random.randint(
            int(-screen.window_width() / 2),
            int(screen.window_width() / 2 - fraction_size * 22),
        )
        start_y = random.randint(
            int(-screen.window_height() / 2 + fraction_size * 16),
            int(screen.window_height() / 2),
        )

        if args.user_input == 1:
            draw_norway_flag(t, start_x, start_y, fraction_size)
        elif args.user_input == 2:
            draw_bangladesh_flag(t, start_x, start_y, fraction_size)
        else:
            draw_sweden_flag(t, start_x, start_y, fraction_size)



def configure(t: Turtle, screen: Screen):
    """Configures the screen settings"""
    screen.setup(1.0, 1.0)
    screen.title("Doodle")
    screen.bgcolor("black")
    screen.colormode(255)
    t.speed(0)
    t.hideturtle()


def build_image(client: docker.DockerClient):
    """Builds the image using the Dockerfile"""
    docker_name = "doodle-converter"
    try:
        print("Building image...")
        if len(client.images.list(name=docker_name)) > 0:
            print("Image already exists")
        else:
            client.images.build(path=".", forcerm=True, tag=docker_name)
    except docker.errors.BuildError as e:
        print(e)


def convert_to_png(client: docker.DockerClient, args):
    """Converts the PS file to PNG using the container"""
    cwd = os.getcwd()
    try:
        print("Converting to PNG...")
        client.containers.run(
            "doodle-converter",
            command=f"{args.output_file}.ps {args.output_file}.png",
            volumes={f"{cwd}": {"bind": "/app", "mode": "rw"}},
            auto_remove=True,
        )
    except docker.errors.ContainerError or docker.errors.APIError as e:
        print(e)


def main():
    t = Turtle()
    screen = Screen()
    client = docker.from_env()
    configure(t, screen)

    # Argument parser
    parser = argparse.ArgumentParser(
        description="Draw a number of flags depending on the input value given. The program requires a running version of Docker."
    )
    parser.add_argument(
        "user_input",
        type=int,
        choices=[1, 2, 3],
        help="Define which flag is created; 1 for Norway, 2 for Bangladesh, 3 for Sweden",
    )
    parser.add_argument("output_file", type=str, help="File to store the flag data")
    args = parser.parse_args()

    build_image(client)
    draw(screen, t, args)

    # Save as PS
    t.getscreen().getcanvas().postscript(file=f"{args.output_file}.ps")

    # Convert to PNG
    convert_to_png(client, args)


if __name__ == "__main__":
    main()
