import turtle

board = turtle.Screen()
board.bgcolor("light yellow")
board.title("Turtle Interactive")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_right():
    turtle_instance.right(10)

def rotate_left():
    turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def turtle_base():
    turtle_pen_up()
    turtle_instance.home()
    turtle_pen_down()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()




board.listen()
board.onkey(fun=turtle_forward, key="space")
board.onkey(fun=rotate_right, key="Down")
board.onkey(fun=rotate_left, key="Up")
board.onkey(fun=clear_screen, key="c")
board.onkey(fun=turtle_base, key="m")
board.onkey(fun=turtle_pen_up, key="i")
board.onkey(fun=turtle_pen_down, key="p")

turtle.mainloop()
