import turtle
import time
#  https://blog.csdn.net/zengxiantao1994/article/details/76588580     Python绘图Turtle库详解

#   https://blog.csdn.net/huacha__/article/details/83274920           Python标准库详解——turtle、random、time
turtle.pensize(5) #设置画笔的宽度
turtle.pencolor("yellow")  #没有参数传入，返回当前画笔颜色，传入参数设置画笔颜色，可以是字符串如"green", "red",也可以是RGB 3元组。
turtle.fillcolor("red") # 绘制图形的填充颜色  这里设置为红色

turtle.begin_fill()  #准备开始填充图形
for _ in  range(5):
    turtle.forward(200)      #   turtle.forward(distance)        向当前画笔方向移动distance像素长度
    turtle.right(144)       #turtle.right(degree)                顺时针移动degree°
turtle.end_fill()           #填充完成
time.sleep(2)

turtle.penup()
turtle.goto(-150,-120)
turtle.color("violet")
turtle.write("Done",font=('Arial',40,'normal'))

turtle.mainloop()