#  https://zhuanlan.zhihu.com/p/472053977   pycham的相关的快捷键


#  https://www.w3school.com.cn/python/python_ref_string.asp     python字符串方法
#  https://www.w3school.com.cn/python/ref_string_title.asp#:~:text=txt%20%3D%20%22Welcome%20to%20my%20world%22%20x%20%3D,print%28x%29%20%E8%BF%90%E8%A1%8C%E5%AE%9E%E4%BE%8B%20%E5%AE%9A%E4%B9%89%E5%92%8C%E7%94%A8%E6%B3%95%20title%20%28%29%20%E6%96%B9%E6%B3%95%E8%BF%94%E5%9B%9E%E4%B8%80%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%EF%BC%8C%E5%85%B6%E4%B8%AD%E6%AF%8F%E4%B8%AA%E5%8D%95%E8%AF%8D%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%AD%97%E7%AC%A6%E5%9D%87%E4%B8%BA%E5%A4%A7%E5%86%99%E3%80%82%20%E6%AF%94%E5%A6%82%E6%A0%87%E9%A2%98%E3%80%82%20%E5%A6%82%E6%9E%9C%E5%8D%95%E8%AF%8D%E5%8C%85%E5%90%AB%E6%95%B0%E5%AD%97%E6%88%96%E7%AC%A6%E5%8F%B7%EF%BC%8C%E5%88%99%E5%85%B6%E5%90%8E%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%AD%97%E6%AF%8D%E5%B0%86%E8%BD%AC%E6%8D%A2%E4%B8%BA%E5%A4%A7%E5%86%99%E5%AD%97%E6%AF%8D%E3%80%82

#  https://blog.csdn.net/Jmayday/article/details/102747456
#  print('hello,world!')

# name='Kobe Bryant'
# print(name.title())
# print(name)
# print(name.upper())
# print(name.lower())


# first_name='dauidab'
# last_name="zhiuyi"
# full_name=last_name+first_name
# print(full_name)
# language='python\nJavascript\nt\tRust'
# print(language)
# _blank='  python  '
# print(_blank.rstrip()) #去除右侧空白
# print(_blank.strip()) #去除两侧空白
# print(_blank.lstrip()) #去除左侧空白
# num=3.1415926
# print(int(num))
# print(float(num))


#
# ls1 = [1, 2, 3, 4, 5, 6]
# ls2 = [1, 2, 3, 4, 5, 6]
# ls1.append(12)
#
# # 可以添加列表，字典，元组，集合，字符串等
# ls2.append([1, "a"])  # 添加列表
# ls2.append({2: "a", 3: "hj"})  # 添加字典
# ls2.append((1, "k", 3))  # 添加元组
# ls2.append({"1", "2", "h"})  # 添加集合
# ls2.append("123abc")  # 添加字符串
#
# print(ls1.append(12))  # 无返回值
# print(ls1)  # append()函数的操作对象是原列表。
# print(ls2)


# color=['puple','red' ,'green' , 'yellow' , 'pink']
# num=color[0].upper()
# print(num)
# color[0]='black'
# color.append('orange')
# color.insert(0,'blue')
# print(color)
# del color[0]
# print(color)
# color.pop()
# print(color)
# color.remove('red')
# print(color)


# str4='we all know that \'A\' and \'B\' are two capital letters.'
# str5="we all konw that 'A' and 'B' are two capital letters."
# print(str4)
# print(str5)
# str1="List of name:\
#         HUa Li\
#         Chan Deng"
# print(str1)


# str1="""List of name:
#      Hua Li  # Li Hus
#      Chan Deng  # Deng chan
#      """
# print(str1)                         #三个单引号或者双引号可以一行一个名字的输出    而且三个引号中可以添加注释


# import turtle
# xa = turtle.Pen()
# xa.pencolor('red')
# xa.circle(100)
# xa.right(120)
# xa.pencolor('blue')
# xa.circle(100)
# xa.right(120)
# xa.pencolor('green')
# xa.circle(100)

# txt ="63 is my age ."
# x=txt.title()
# print(x)


# car_list = ['honda','toyota','suzuki','mazda','subaru']  #使用sort后会永久地改变list里面的内容
# print(car_list)
# car_list.sort()
# print(car_list)
# car_list.sort(reverse=True)
# print(car_list)
#
#
# car_list = ['honda','toyota','suzuki','mazda','subaru']    #临时排序  关键字sorted
# print(car_list)
# print(sorted(car_list))
# print(car_list)
# print(sorted(car_list,reverse=True))
# print(car_list)
# car_list.reverse()  #reverse 反序
# print(car_list)
# x=len(car_list)    #列表的长度
# print(x)

# num_list=[1,2,3,4,2,1,3,1,2]
# for i in num_list:
#     print(i,end="   ")
#
# mylist=[1,4,7,8,20]
# newlist=[x for x in mylist if x%2==0]
# print(newlist)
#
# x=len(num_list+mylist)
# y=len(num_list)+len(mylist)
# print(x+y)


# 遗传算法
import numpy as np
from deap import creator, base, tools, algorithms

# 给定的海底城市参数
# center_depth = 110  # 海城中心点的水深 (m)
# slope_angle = 1.5  # 水底斜坡角度 (度)
# beam_width = 120  # 转向器的开角 (度)
# sea_width_miles = 4
# sea_width_meters = sea_width_miles * 1852
#
# # 定义适应度函数
# import numpy as np
# from deap import creator, base, tools, algorithms
#
# # 给定的海底城市参数
# center_depth = 110  # 海城中心点的水深 (m)
# slope_angle = 1.5  # 水底斜坡角度 (度)
# beam_width = 120  # 转向器的开角 (度)
# sea_width_miles = 4
# sea_width_meters = sea_width_miles * 1852
#
#
# # 定义适应度函数
# def evaluate(individual):
#     overlap_ratio = individual[0]
#
#     if overlap_ratio < 0.1 or overlap_ratio > 0.2:
#         return float('inf'),
#
#     W = 2 * center_depth * np.tan(np.deg2rad(beam_width / 2))
#     d = (1 - overlap_ratio) * W
#     num_lines = np.ceil(sea_width_meters / d).astype(int)
#
#     return num_lines,
#
#
# creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
# creator.create("Individual", list, fitness=creator.FitnessMin)
#
# toolbox = base.Toolbox()
# # 遗传算法的参数设置
# toolbox.register("attribute", np.random.uniform, 0.1, 0.2)  # 随机生成重叠率
# toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=2)
# toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# toolbox.register("evaluate", evaluate)
# toolbox.register("mate", tools.cxTwoPoint)  # 交叉操作：两点交叉
# toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.05, indpb=0.1)  # 变异操作：高斯变异
# toolbox.register("select", tools.selTournament, tournsize=3)  # 选择操作：锦标赛选择
# population_size = 50
# crossover_probability = 0.5
# mutation_probability = 0.5
# number_of_generations = 50
#
# population = toolbox.population(n=population_size)
#
# for generation in range(number_of_generations):
#     offspring = algorithms.varAnd(population, toolbox, cxpb=crossover_probability, mutpb=mutation_probability)
#     fits = toolbox.map(toolbox.evaluate, offspring)
#     for fit, ind in zip(fits, offspring):
#         ind.fitness.values = fit
#
#     population = toolbox.select(offspring, k=population_size)
#
# best_individual = tools.selBest(population, k=1)[0]
# best_overlap_ratio = best_individual[0]
#
# W = 2 * center_depth * np.tan(np.deg2rad(beam_width / 2))
# d = (1 - best_overlap_ratio) * W
# num_lines = np.ceil(sea_width_meters / d).astype(int)
#
# line_start_x = np.linspace(-sea_width_meters / 2, sea_width_meters / 2, num_lines)
# line_start_y = np.zeros(num_lines)
# line_direction = np.deg2rad(slope_angle)
#
# print("所需的测线数量: " + str(num_lines))
# print("最佳的重叠率: " + str(best_overlap_ratio))
# print("每条测线的起始点坐标 (x坐标，y坐标): ")
# print(np.column_stack((line_start_x, line_start_y)))
# print("测线方向 (弧度): " + str(line_direction))


# 蒙特卡洛算法
# import numpy as np
#
# # 给定的海底城市参数
# center_depth = 110  # 表示海城中心点的水深 (m)
# slope_angle = 1.5   # 表示水底斜坡角度 (度)
# beam_width = 120    # 表示转向器的开角 (度)
# sea_width_miles = 4  # 表示四海里
# sea_width_meters = sea_width_miles * 1852

# 定义适应度函数
# def evaluate(individual):
#     overlap_ratio = individual  # 定义覆盖率并赋值
#
#     if overlap_ratio < 0.1 or overlap_ratio > 0.2: # 覆盖率需落在题中所给条件
#         return float('inf')
#
#     W = 2 * center_depth * np.tan(np.deg2rad(beam_width / 2)) # 表示覆盖宽度
#     d = (1 - overlap_ratio) * W  # 表示求两测线之间的距离
#     num_lines = np.ceil(sea_width_meters / d).astype(int) # 求出测线的条数，在整数范围内向上取整
#
#     return num_lines
#
# # 蒙特卡洛搜索
# population_size = 100
# number_of_iterations = 1000
#
# best_overlap_ratio = None
# best_num_lines = None
#
# for _ in range(number_of_iterations):
#     individual = np.random.uniform(0.1, 0.2)
#     #  生成一个随机浮点数，范围在0.1到0.2之间（包括0.1，但不包括0.2）
#     num_lines = evaluate(individual)
#
#     if best_num_lines is None or num_lines < best_num_lines:
#         # 找出最短路径
#         best_num_lines = num_lines
#         best_overlap_ratio = individual
#
# line_start_x = np.linspace(-sea_width_meters / 2, sea_width_meters / 2, best_num_lines)
# line_start_y = np.zeros(best_num_lines)
# line_direction = np.deg2rad(slope_angle)
#
# print("所需的测线数量: " + str(best_num_lines))
# print("最佳的重叠率: " + str(best_overlap_ratio))
# print("每条测线的起始点坐标 (x坐标，y坐标): ")
# print(np.column_stack((line_start_x, line_start_y)))
# print("测线方向 (弧度): " + str(line_direction))


# import matplotlib.pyplot as plt
# # Python脚本中动态设置matplotlibrc,这样也可以避免由于更改配置文件而造成的麻烦
# from pylab import *
# # 设置显示中文字体
# mpl.rcParams["font.sans-serif"] = ["SimHei"]
# # 解决负数坐标显示问题
# plt.rcParams['axes.unicode_minus'] = False
# # 生成数据
# x = [0, 0.15,0.3,0.45,0.6,0.75,0.9,1.05,1.2,1.35,1.5]
# y = [0, 0.005,0.008,0.013,0.012,0.016,0.020,0.017,0.011,0.015, 0]
# # 绘制曲线图
# plt.plot(x, y, color='black', alpha=0.6, linewidth=2, marker='8', markeredgecolor='b', markersize=5, markeredgewidth=2)
# plt.axhline(0)
# # 添加网格
# plt.grid(True)
# # 设置图表标题和坐标轴标签
# plt.title("表1 电压表的校正曲线")
# plt.xlabel("I/(V)")
# plt.ylabel("ΔI/(V)")
# # 显示图表
# plt.show()


# import matplotlib.pyplot as plt
# from pylab import mpl
#
# """一元线性拟合
# 采用的拟合数据为xi=1,2,3,4,5,6,7
# 对应的相应函数值yi=0.5,2.5,2,4,3.5,6,5.5
# """
#
# x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5];
# y = [0,0.04,0.02,0.06,0.05,0.03,0.03,0.04,0.02,0.05,0]
#
# """完成拟合曲线参数计算"""
#
#
# def liner_fitting(data_x, data_y):
#     size = len(data_x);
#     i = 0
#     sum_xy = 0
#     sum_y = 0
#     sum_x = 0
#     sum_sqare_x = 0
#     average_x = 0;
#     average_y = 0;
#     while i < size:
#         sum_xy += data_x[i] * data_y[i];
#         sum_y += data_y[i]
#         sum_x += data_x[i]
#         sum_sqare_x += data_x[i] * data_x[i]
#         i += 1
#     average_x = sum_x / size
#     average_y = sum_y / size
#     return_k = (size * sum_xy - sum_x * sum_y) / (size * sum_sqare_x - sum_x * sum_x)
#     return_b = average_y - average_x * return_k
#     return [return_k, return_b]
#
#
# """完成完后曲线上相应的函数值的计算"""
#
#
# def calculate(data_x, k, b):
#     datay = []
#     for x in data_x:
#         datay.append(k * x + b)
#     return datay
#
#
# """完成函数的绘制"""
#
#
# def draw(data_x, data_y_new, data_y_old):
#     plt.plot(data_x, data_y_new, label="拟合曲线", color="black")
#     plt.scatter(data_x, data_y_old, label="离散数据")
#     mpl.rcParams['font.sans-serif'] = ['SimHei']
#     mpl.rcParams['axes.unicode_minus'] = False
#     plt.title("电流表的修正曲线")
#     plt.xlabel("I/(mA)")
#     plt.ylabel("Δ/(mA)")
#     plt.legend(loc="upper left")
#     plt.show()
#
#
# parameter = liner_fitting(x, y)
# draw_data = calculate(x, parameter[0], parameter[1])
# draw(x, draw_data, y)

# import tkinter as tk
# import calendar
# import time
# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# class CalendarApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Calendar App")
#         self.geometry("300x400")
#         self.current_datetime = time.strftime("%Y-%m-%d %H:%M:%S %A")
#         self.datetime_label = tk.Label(self, text=self.current_datetime, font=("Helvetica", 14))
#         self.datetime_label.pack(pady=10)
#         self.calendar_label = tk.Label(self, text="", font=("Helvetica", 12))
#         self.calendar_label.pack(pady=10)
#         self.year_entry = tk.Entry(self)
#         self.year_entry.pack(pady=5)
#         self.month_entry = tk.Entry(self)
#         self.month_entry.pack(pady=5)
#         self.show_button = tk.Button(self, text="Show", command=self.show_calendar)
#         self.show_button.pack(pady=5)
#         self.switch_button = tk.Button(self, text="Switch", command=self.switch_datetime)
#         self.switch_button.pack(pady=5)
#         self.update_button = tk.Button(self, text="Update", command=self.update_datetime)
#         self.update_button.pack(pady=5)
#         self.set_button = tk.Button(self, text="Set", command=self.open_set_dialog)
#         self.set_button.pack(pady=5)
#     def update_datetime(self):
#         new_datetime = time.strftime("%Y-%m-%d %H:%M:%S %A")
#         self.current_datetime = new_datetime
#         self.datetime_label.config(text=self.current_datetime)
#     def show_calendar(self):
#         year = int(self.year_entry.get())
#         month = int(self.month_entry.get())
#         cal = calendar.monthcalendar(year, month)
#         header = f"     {calendar.month_name[month]} {year}     \n"
#         weekdays = " Mo  Tu  We  Th  Fr  Sa  Su \n"
#         lines = [weekdays]
#         for week in cal:
#             line = ""
#             for day in week:
#                 if day == 0:
#                     line += "    "
#                 else:
#                     line += f"{day:2d}  "
#             lines.append(line)
#         calendar_str = header + "\n".join(lines)
#         self.calendar_label.config(text=calendar_str)
#     def switch_datetime(self):
#         current_time = datetime.now()
#         new_datetime = current_time + relativedelta(years=1)
#         new_datetime_str = new_datetime.strftime("%Y-%m-%d %H:%M:%S %A")
#         self.current_datetime = new_datetime_str
#         self.datetime_label.config(text=self.current_datetime)
#     def open_set_dialog(self):
#         dialog = SetDialog(self)
#         self.wait_window(dialog)
#         if dialog.result is not None:
#             self.current_datetime = dialog.result
#             self.datetime_label.config(text=self.current_datetime)
# class SetDialog(tk.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.title("Set Date and Time")
#         self.geometry("300x200")
#         self.result = None
#         self.year_entry = tk.Entry(self)
#         self.year_entry.pack(pady=10)
#         self.month_entry = tk.Entry(self)
#         self.month_entry.pack(pady=10)
#         self.day_entry = tk.Entry(self)
#         self.day_entry.pack(pady=10)
#         self.hour_entry = tk.Entry(self)
#         self.hour_entry.pack(pady=10)
#         self.minute_entry = tk.Entry(self)
#         self.minute_entry.pack(pady=10)
#         self.second_entry = tk.Entry(self)
#         self.second_entry.pack(pady=10)
#         self.confirm_button = tk.Button(self, text="Confirm", command=self.set_datetime)
#         self.confirm_button.pack(pady=10)
#     def set_datetime(self):
#         year = self.year_entry.get()
#         month = self.month_entry.get()
#         day = self.day_entry.get()
#         hour = self.hour_entry.get()
#         minute = self.minute_entry.get()
#         second = self.second_entry.get()
#         try:
#             new_datetime = f"{year}-{month}-{day} {hour}:{minute}:{second}"
#             datetime.strptime(new_datetime, "%Y-%m-%d %H:%M:%S")
#             self.result = new_datetime
#             self.destroy()
#         except ValueError:
#             tk.messagebox.showerror("Error", "Invalid date or time format.")
# if __name__ == "__main__":
#     app = CalendarApp()
#     app.mainloop()

