import turtle

def customize_turtle(some_turtle, shape, color, speed):
    some_turtle.shape(shape)
    some_turtle.color(color)
    some_turtle.speed(speed)

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_rectangle(some_turtle):
    some_turtle.right(60)
    for i in range(3):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    brad = turtle.Turtle()
    customize_turtle(brad, "turtle", "green",20)
    for i in range(36):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

'''    angie = turtle.Turtle()
    customize_turtle(angie, "turtle", "yellow", 2)
    angie.circle(100)

    lisa = turtle.Turtle()
    customize_turtle(lisa, "turtle", "green", 2)
    for i in range(10):
        draw_rectangle(lisa)'''
    
    
draw_art()
