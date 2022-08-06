import turtle
from turtle import Turtle ,Screen
screen=Screen()
screen.screensize(600,600)
screen.title("Pong Game")
def wall(a,b,c):
    wall=Turtle()
    wall.shape("square")
    wall.shapesize(1,2)
    wall.penup()
    wall.setheading(c)
    wall.goto(a,b)
for x in range(-300,300,20):
    screen.tracer(0)
    wall(x,340,0)
    wall(x,-340,0)
    screen.update()
for x in range(-300,320,60):
    screen.tracer(0)
    wall(0,x,90)
    screen.update()
bat1=[]
def bat(a):
    slide=Turtle()
    slide.shape("square")
    slide.shapesize(1,3)
    slide.setheading(90)
    slide.penup()
    slide.goto(a,0)
    bat1.append(slide)
class ball(Turtle):
    def _init_(self):
        super()._init_ () 

        self.shape("circle")
        self.penup()
        self.x_move=1
        self.y_move=1
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.speed(2)
        self.goto(new_x,new_y)
    def bounce(self):
        self.y_move=self.y_move*-1
    def bounceup(self):
        i=i*0.5
        self.x_move=self.y_move*-1*i
        self.y_move=self.y_move*-1*i
    def bouncedown(self):
        i=i*0.5
        self.x_move=self.y_move*-1*i
        self.y_move=self.y_move*1*i
    def ret(self):
        return self.y_move

bat(-300)
bat(300)


        

screen.update()
def up():
    if bat1[0].ycor()<300:
        bat1[0].speed(9)
        bat1[0].fd(20)
        screen.update()

        
def down():
    if  bat1[0].ycor()>-300 :
        bat1[0].speed(9)
        bat1[0].backward(20)
        screen.update()
        
def up1():
    if bat1[1].ycor()<300:
        bat1[1].speed(9)
        bat1[1].fd(20)
        screen.update()
        
def down1():
    if  bat1[1].ycor()>-300:
        bat1[1].speed(9)
        bat1[1].backward(20)
        screen.update()
ball1=ball()
def best(a):
        a1=bat1[a].xcor()
        a2=bat1[a].ycor()
        ballx=ball1.xcor()
        bally=ball1.ycor()
        m=ball1.ret()
        n=(ballx-a1)
        if bat1[a].distance(ball1)<20:
            for i in range (-40,40,10):
                if i>0:
                    if n<=i and n>=i-10  and m<0:
                        ball1.bounceup(i)
                    elif n<=i and n>=i-10 and m>0:
                        ball1.bouncedown(i)
                elif i<=0:
                    if n>=i and n<=i+10 and m<0:
                        i=i*-1
                        ball1.bouncedown(i)
                    elif n>=i and n<=i+10 and m>0:
                        i=i*-1
                        ball1.bounceup(i)        

screen.listen()
for i in range(10000):
        screen.update()
        screen.onkey(key="w",fun=up)
        screen.onkey(key="s",fun=down)
        screen.onkey(key="8",fun=up1)
        screen.onkey(key="2",fun=down1)
        ball1.move()
        if ball1.ycor()>320 or ball1.ycor()<-320:
            ball1.bounce()
        best(0)
        best(1)
''' a1=bat1[1].xcor()
        a2=bat1[1].ycor()
        ballx=ball1.xcor()
        bally=ball1.ycor()
        m=ball1.ret()
        if bat1[1].distance(ball1)<20:
            if (ballx-a1)>10 and m<0:
                ball1.bounceup()
            elif (ballx-a1)>10 and m>0:
                ball1.bouncedown()
            elif(ballx-a1)<10 and m<0:
                ball1.bouncedown()
            elif(ballx-a1)<10 and m>0:
                ball1.bounceup()'''




                


turtle.exitonclick()