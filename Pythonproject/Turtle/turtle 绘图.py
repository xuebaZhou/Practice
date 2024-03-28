

#  https://www.cnblogs.com/nowgood/p/turtle.html

import turtle
#  设置画布大小
#  语法 turtle.screensize(canvwidth=None, canvheight=None, bg=None)
# 参数分别为画布的宽(单位像素), 高, 背景颜色
turtle.screensize(800,600,'yellow')


#  语法 ：turtle.setup(width=0.5, height=0.75, startx=None, starty=None)
#  参数:
# width, height: 输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例
# (startx, starty): 这一坐标表示 矩形窗口左上角顶点的位置, 如果为空,则窗口位于屏幕中心
turtle.setup(width=0.6,height=0.6,startx=0,starty=0)   # 此时窗口位于屏幕左上角的位置





#  设置画笔
#  画笔状态
turtle.pensize(10)
turtle.pencolor('brown')
turtle.forward(100)
turtle.pencolor('blue')
turtle.backward(12)
turtle.right(30)
turtle.forward(100)
turtle.goto(0,0)
# turtle.penup()
turtle.color('red')
turtle.left(30)
turtle.speed(10)
#turtle.pendown()
turtle.forward(100)
turtle.speed(10)
turtle.circle(100)
turtle.begin_fill()
turtle.color('blue','red')
turtle.circle(-100)
turtle.end_fill()








turtle.mainloop()
#    turtle.done()
#    turtle.exitonclick()   这种方法当用户点击界面之后就会退出