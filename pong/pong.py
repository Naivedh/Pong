#pong
import turtle
import winsound

wn=turtle.Screen()

wn.title("pong by NS")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#paddle A
paddle_a=turtle.Turtle()  
   #module.classname
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  
    #not to draw lines
paddle_a.goto(-350,0)


#paddle B
paddle_b=turtle.Turtle()  
   #module.classname
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  
    #not to draw lines
paddle_b.goto(350,0)

#BALL
ball=turtle.Turtle()  
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()  
ball.goto(0,0)


ball.dx = 0.25
ball.dy = -0.25

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#win
winn =turtle.Turtle()
winn.speed(0)
winn.color("orange")
winn.penup()
winn.hideturtle()
winn.goto(0,0)


#function
def paddle_a_up() :
    y=paddle_a.ycor()
    #ycor method gives y cordinate
    y+=20
    paddle_a.sety(y)


def paddle_a_down() :
    y=paddle_a.ycor()
    
    y-=20
    paddle_a.sety(y)




def paddle_b_up() :
    y=paddle_b.ycor()
    #ycor method gives y cordinate
    y+=20
    paddle_b.sety(y)


def paddle_b_down() :
    y=paddle_b.ycor()
    
    y-=20
    paddle_b.sety(y)


def win(score_a, score_b):
    paddle_a.reset()
    paddle_b.reset()
    ball.dx=0
    ball.dy=0
    ball.hideturtle()
    pen.clear()
    if score_a >score_b:
        
        winn.write("Player A wins with {} points".format(score_a), align="center", font=("Courier", 24, "normal"))
    else:
        
        winn.write("Player B wins with {} points".format(score_b), align="center", font=("Courier", 24, "normal"))


#keyboard binding
wn.listen()
    #listen to keyword
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop

while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290 :
        ball.sety(290)
        #to avoid certin problems
        ball.dy *= -1
        winsound.PlaySound("bounce,wav", winsound.SND_ASYNC)

    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce,wav", winsound.SND_ASYNC)

    if ball.xcor() > 390 :
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        if score_a ==5 :
            win(score_a,score_b)
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        

    if ball.xcor() < -390 :
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        if score_b== 5 :
            win(score_a, score_b)            
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        



    #paddle and ball collisions

    if (ball.xcor() > 340 and ball.xcor() < 350)and((ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor()-40)):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce,wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350)and((ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor()-40)):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce,wav", winsound.SND_ASYNC)
