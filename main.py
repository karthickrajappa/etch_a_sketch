import turtle

screen = turtle.Screen()
tim = turtle.Turtle()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.back(20)


def c_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=c_clockwise)
screen.onkey(key="d", fun=clockwise)

screen.exitonclick()
