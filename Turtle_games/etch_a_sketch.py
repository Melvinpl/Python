import turtle as turtle_module

tim = turtle_module.Turtle()
screen = turtle_module.Screen()


def forward():
    tim.forward(10)
    
def backward():
    tim.backward(10)
    
def clockwise():
    tim.right(20)

def counter_clcokwise():
    tim.left(20)
    
def clear():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clcokwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()