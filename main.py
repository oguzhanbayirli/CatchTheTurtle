import random
import turtle
import time
drawing_board = turtle.Screen()
drawing_board.title("Catch The Turtle")
drawing_board.bgcolor("light blue")

score = 0

turtle1 = turtle.Turtle()
turtle1.hideturtle()
turtle1.color("blue")
turtle1.teleport(0,285)

turtle2 = turtle.Turtle()
turtle2.hideturtle()
turtle2.teleport(0,245)

turtle3 = turtle.Turtle()
turtle3.shape("turtle")
turtle3.color("green")

my_time = 20
def click(x,y):
    global score
    score += 1
    print(turtle3.pos())
while my_time:
    turtle1.write(f"Score: {score}", False, "center", ("Arial", 20, "normal"))
    turtle2.write(f"Time: {my_time}", False, "center", ("Arial", 20, "normal"))
    time.sleep(1)
    my_time -= 1
    if my_time == 1:
        turtle2.clear()
        turtle2.write("Game Over!", False, "center", ("Arial", 20, "normal"))
        break
    turtle3.teleport(random.randint(-350,350),random.randint(-250,250))
    turtle1.clear()
    turtle2.clear()
    turtle3.onclick(click)
drawing_board.listen()
drawing_board.onkey(fun=lambda:drawing_board.bye(),key="space")
drawing_board.mainloop()