#   五星红旗绘制

import turtle
import time
import math

turtle.setup(width=1.0, height=1.0, startx=None, starty=None)
turtle.ht()
turtle.tracer(0, 0)
turtle.bgcolor("black")

turtle.pensize(1)

def star(center, angle, length, penc, fillc):# 定义
    turtle.pensize(1) # 设置画笔的大小
    turtle.fillcolor(fillc)
    turtle.pencolor(penc)
    L = length*math.sin(36*math.pi/180)/math.sin(54*math.pi/180)
    turtle.up()
    turtle.goto(center)
    turtle.seth(90+angle)
    turtle.fd(length)
    turtle.seth(180+72+angle)
    turtle.down()
    turtle.begin_fill()
    for _ in range(5):
        turtle.fd(L)
        turtle.right(72)
        turtle.fd(L)
        turtle.left(144)
    turtle.end_fill()

def rectangle(center, length_x, length_y, penc, fillc):
    turtle.pensize(1)
    turtle.fillcolor(fillc)  # 设置填充颜色
    turtle.pencolor(penc)  #  设置画笔颜色
    turtle.up()
    pos=(center[0]-length_x/2, center[1]+length_y/2)
    turtle.goto(pos)
    turtle.begin_fill()
    turtle.down()
    turtle.seth(0)
    turtle.fd(length_x)
    turtle.seth(-90)
    turtle.fd(length_y)
    turtle.seth(180)
    turtle.fd(length_x)
    turtle.seth(90)
    turtle.fd(length_y)
    turtle.end_fill()

W = 1200
H = 800
dW = W/30
dH = H/20

#time.sleep(6)

rectangle((0,0), W, H, 'red', 'red')
C0 = (-dW*10, dH*5)
A0 = 0
L0 = dW*3
star(C0, A0, L0, 'yellow', 'yellow')
C1 = (-dW*5, dH*8)
A1 = 90+math.atan(3/5)*180/math.pi
L1 = dW
star(C1, A1, L1, 'yellow', 'yellow')
C2 = (-dW*3, dH*6)
A2 = 90+math.atan(1/7)*180/math.pi
L2 = dW
star(C2, A2, L2, 'yellow', 'yellow')
C3 = (-dW*3, dH*3)
A3 = 90-math.atan(2/7)*180/math.pi
L3 = dW
star(C3, A3, L3, 'yellow', 'yellow')
C4 = (-dW*5, dH)
A4 = 90-math.atan(4/5)*180/math.pi
L4 = dW
star(C4, A4, L4, 'yellow', 'yellow')

turtle.mainloop()