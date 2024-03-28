#  https://blog.csdn.net/qq_29831163/article/details/89713032

import numpy as np
from matplotlib.pyplot import plot, show, rc, legend, subplot
from scipy.optimize import curve_fit

# rc('font',siza=15);rc('font',family='SimHei');
# t0 = np.arange(1, 7)
# x0 = np.array([2.081, 4.611, 5.1177, 9.3775, 11.0574, 11.0524])
# xt = np.polyfit(t0, x0, 1);
# xh1 = np.polyval(xt, t0)  # 计算预测值
# # 使用最小二乘法拟合一条一次多项式，其中t0是自变量的数组，x0是因变量的数组。
# # 拟合后的多项式系数存储在xt中。然后使用拟合的多项式在t0上计算xh1的值。
# deltal = abs((xh1 - x0)) / x0  # 计算相对误差
# x1 = np.cumsum(x0)  # cumsum的作用主要就是计算轴向的累加和
# #  https://blog.csdn.net/l_dsj/article/details/110421471
# xh2 = lambda t, a, b, c: a * np.exp(b * t) + c
# para, cov = curve_fit(xh2, t0, x1)
# xh21 = xh2(t0, *para)
# xh22 = np.r_[xh21[0], np.diff(xh21)]
# delta2 = np.abs((xh22 - x0) / x0)
# print("拟合的参数值为：", para);
# subplot(121)
# plot(t0, x0, 's');
# plot(t0, xh1, '*-')
# legend(("原始数据点", '线性拟合'), loc='upper left')
# subplot(122);
# plot(t0, x1, 'o');
# plot(t0, xh21, 'p-')
# legend(('累加数据点', '累加后拟合'));
# show()
#


import sympy as sp
# depth,width=sp.symols('depth,width')        #声明符号变量海水深度depth和覆盖宽度width
# 情况一：在中心点的左侧
# AF,AH,EF,BE,EG,EC=sp.symbols("AF,AH,EF,BE,EG,EC")
# def cal(alpha,theta,D):
#     #由几何关系得到
#     AH=D/2
#     con1=[sp.Eq((AF/sp.sin(sp.pi/2)),AH/sp.sin(sp.pi/2-theta/2))]      #三角形AFH中由正弦定理得
#     AF_result=sp.solve(con1,AF)
#     EF=AF_result.pop(AF)
#     con2=[sp.Eq((EF/sp.sin(sp.pi/2-theta/2-alpha)),BE/sp.sin(theta))]  #三角形BEF中由正弦定理得
#     BE_result=sp.solve(con2,BE)
#     EG=AF_result.pop(AF)
#     con3=[sp.Eq((EG/sp.sin(sp.pi/2-theta/2+alpha)),(EC/sp.sin(theta)))] #三角形CEG中由正弦定理得
#     EC_result=sp.solve(con3,EC)
#     BC=BE_result.pop(BE)+EC_result.pop(EC)
#     return BC
# print(cal(sp.pi*(1.5/180),sp.pi*(120/180),70))


# import numpy as np
# import matplotlib.pyplot as plt
#
# # 距离，角度，深度数据的输入
# distance = np.array([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1])
# angle = np.array([0, 45, 90, 135, 180, 225, 270, 315])
# depth = np.array([
#     [415.69, 415.69, 415.69, 415.69, 415.69, 415.69, 415.69, 415.69],
#     [415.69, 451.33, 486.97, 522.60, 558.24, 593.88, 629.52, 665.15],
#     [416.69, 467.21, 517.73, 568.25, 618.77, 669.29, 719.81, 770.33],
#     [415.69, 451.33, 486.97, 522.60, 558.24, 593.88, 629.52, 665.15],
#     [415.69, 415.69, 415.69, 415.69, 415.69, 415.69, 415.69, 415.69],
#     [415.69, 380.05, 344.42, 308.78, 273.14, 237.51, 201.87, 166.23],
#     [416.69, 366.17, 315.65, 265.13, 214.61, 164.09, 113.57, 63.05],
#     [415.69, 380.05, 344.42, 308.78, 273.14, 237.51, 201.87, 166.23]
# ]).T
# # 绘图
# fig = plt.figure(figsize=(10, 10))  # 设置图像的宽和高
# fig_as = fig.add_subplot(111, projection='3d')  # 添加一个3D子图
# x, y = np.meshgrid(angle, distance)
# fig_as.plot_surface(x, y, depth, cmap="viridis")  # 绘制三维曲面图
# # 设置
# fig_as.set_xlabel('Angle (°)')
# fig_as.set_ylabel('Distance (nautical miles)')
# fig_as.set_zlabel('Depth (m)')
# fig_as.set_title('Depth & Distance and Angle')
# plt.show()

# 遗传算法
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
#
# # 定义适应度函数
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

# # 考虑测量船大致在南北方向的航行
# import numpy as np
#
# # 给定的海底相关参数
# depth_center = 110  # 海城中心点的水深 (m)
# alpha = 1.5  # 水底斜坡角度 (度)
# theta = 120  # 转向器的开角 (度)
# width_miles = 4 # 表示东西宽四海里
# width_meters = width_miles * 1852 # 将海里单位制转换为米
#
# # 定义生成随机重叠率的函数
# def generate_random_overlap_rate():
#     overlap_rate = np.random.uniform(0.1, 0.2)
#     # 使重叠率在0.1到0.2随机取值
#     return overlap_rate
#
# # 定义计算测线数量的函数
# def cal_num_lines(overlap_rate):
#     W = 2 * depth_center * np.tan(np.deg2rad(theta / 2))
#     d = (1 - overlap_rate) * W
#     # 记录每条测线之间的距离
#     num_lines = np.ceil(width_meters / d).astype(int)
#     # 求出测线的条数，并在整数范围内向上取整
#     return num_lines
#
#
# while(1):
#     # 循环次数为手动输入，可以通过调整循环次数来得到不同的结果。
#     N=int (input("please input a number:"))
#
#     # 定义一个空列表，用来存储重叠率和测线数量
#     results = []
#
#     # 循环N次
#     for i in range(N):
#         # 生成一个随机重叠率
#         overlap_rate = generate_random_overlap_rate()
#         # 计算对应的测线数量
#         num_lines = cal_num_lines(overlap_rate)
#         # 将重叠率和测线数量存入列表中
#         results.append((overlap_rate, num_lines))
#
#     # 从列表中找出测线数量最小的那一对重叠率和测线数量
#     best_result = min(results, key=lambda x: x[1])
#     best_overlap_rate = best_result[0]
#     best_num_lines = best_result[1]
#
#     line_start_x = np.linspace(-width_meters / 2, width_meters / 2, num_lines)
#     line_start_y = np.zeros(num_lines)
#     line_direction = np.deg2rad(alpha)
#
#     print("所需的测线数量: " + str(best_num_lines))
#     print("最佳的重叠率: " + str(best_overlap_rate))
#     print("每条测线的起始点坐标 (x坐标，y坐标): ")
#     print(np.column_stack((line_start_x, line_start_y)))
#     print("测线方向 (弧度): " + str(line_direction))


#
# # 考虑测量船大致在南北方向的航行
# import numpy as np
# import xlwt
# # 给定的海底相关参数
# depth_center = 110
# theta = np.pi*(120/180)
# alpha=np.pi*(1.5/180)
# width_miles = 4
# width_meters = width_miles * 1852 # 将海里单位制转换为米
#
# # 定义生成随机重叠率的函数
# def random_overlap_rate():
#     overlap_rate = np.random.uniform(0.1, 0.2)
#     # 使重叠率在0.1到0.2随机取值
#     return overlap_rate
#
# # 定义计算测线数量的函数
# def cal_num_lines(overlap_rate):
#     W = 2 * depth_center * np.tan((theta / 2))
#     d = W*(1 - overlap_rate)
#     # 记录每条测线之间的距离
#     num_lines = int(np.ceil(width_meters / d))
#     # 求出测线的条数，并在整数范围内向上取整
#     return num_lines
#
#
# while(1):
#     # 循环次数为手动输入，可以通过调整循环次数来得到不同的结果。
#     N=int (input("please input a number:"))
#
#     # 定义一个空列表，用来存储重叠率和测线数量
#     results = []
#
#     # 循环N次
#     for i in range(N):
#         # 生成一个随机重叠率
#         overlap_rate = random_overlap_rate()
#         # 计算对应的测线数量
#         num_lines = cal_num_lines(overlap_rate)
#         # 将重叠率和测线数量存入列表中
#         results.append((overlap_rate, num_lines))
#
#     # 从列表中找出测线数量最小的那一对重叠率和测线数量
#     min_result = min(results, key=lambda x: x[1])
#     min_overlap_rate = min_result[0]
#     min_num_lines = min_result[1]
#
#     start_x = np.linspace(-width_meters / 2, width_meters / 2, min_num_lines)
#     start_y = np.zeros(min_num_lines)
#     line_direction =alpha
#
#
#     print("所需的测线数量: " + str(min_num_lines))
#     print("最佳的重叠率: " + str(min_overlap_rate))
#     print("每条测线的起始点坐标 (x坐标，y坐标): ")
#     print(np.column_stack((start_x, start_y)))
#     print("测线方向 (弧度): " + str(line_direction))

# import sympy as sp
# #设置初始条件
# alpha=sp.pi*(1.5/180)
# theta=sp.pi*(120/180)
# d=sp.symbols('d')
# D=110
# count=0
# # AS=110+d*sp.tan(alpha)
# AF,AH,EF,BE,EG,EC=sp.symbols("AF,AH,EF,BE,EG,EC")
# def cal_left(alpha,theta,D,d):
#     x=D+d*sp.tan(alpha)
#     width=(sp.sin(theta)/sp.sin(sp.pi/2-theta/2-alpha))*((sp.sin(sp.pi/2)*(x/2))/sp.sin(sp.pi/2-theta/2))
#     result=[x,width]
#     return result
# def cal_full_plus(alpha,theta,D,d):
#     x=D+d*sp.tan(alpha)
#     width=(sp.sin(theta)/sp.sin(sp.pi/2-theta/2+alpha))*((sp.sin(sp.pi/2)*(x/2))/sp.sin(sp.pi/2-theta/2))+(sp.sin(theta)/sp.sin(sp.pi/2-theta/2-alpha))*((sp.sin(sp.pi/2)*(x/2))/sp.sin(sp.pi/2-theta/2))
#     result=[x,width]
#     return result
#
# def cal_full_mius(alpha,theta,D,d):
#     x=D-d*sp.tan(alpha)
#     width=(sp.sin(theta)/sp.sin(sp.pi/2-theta/2+alpha))*((sp.sin(sp.pi/2)*(x/2))/sp.sin(sp.pi/2-theta/2))+(sp.sin(theta)/sp.sin(sp.pi/2-theta/2-alpha))*((sp.sin(sp.pi/2)*(x/2))/sp.sin(sp.pi/2-theta/2))
#     result=[x,width]
#     return result
# def cal_center(alpha,theta,D):
#     #由几何关系得到
#     AH=D/2
#     con1=[sp.Eq((AF/sp.sin(sp.pi/2)),AH/sp.sin(sp.pi/2-theta/2))]      #三角形AFH中由正弦定理得
#     AF_result=sp.solve(con1,AF)
#     EF=AF_result[AF]
#     con2=[sp.Eq((EF/sp.sin(sp.pi/2-theta/2-alpha)),BE/sp.sin(theta))]  #三角形BEF中由正弦定理得
#     BE_result=sp.solve(con2,BE)
#     EG=AF_result[AF]
#     con3=[sp.Eq((EG/sp.sin(sp.pi/2-theta/2+alpha)),(EC/sp.sin(theta)))] #三角形CEG中由正弦定理得
#     EC_result=sp.solve(con3,EC)
#     BC=BE_result[BE]+EC_result[EC]                                      #求得中心处覆盖宽度
#     return BC
#
# #确定最远边界时的条件
# result=cal_left(alpha,theta,D,d)
# con=[sp.Eq(result[1]*sp.cos(alpha)+d,2*1852)]
# result_d=sp.solve(con,d)
# print(result_d[d])
# x_far=result_d[d]
# result=cal_full_plus(alpha,theta,D,result_d[d])
# depth_now=result[0].evalf()
# print(depth_now)
# count+=1
# e=sp.symbols('e')
# width_full_big=result[1]
# depth_new=D+(x_far-e)*sp.tan(alpha)
# width_full_small=(sp.sin(theta)/sp.sin(sp.pi/2-theta/2+alpha))*((sp.sin(sp.pi/2)*(depth_new/2))/sp.sin(sp.pi/2-theta/2))+(sp.sin(theta)/sp.sin(sp.pi/2-theta/2-alpha))*((sp.sin(sp.pi/2)*(depth_new/2))/sp.sin(sp.pi/2-theta/2))
# # result=cal_full_mius(alpha,theta,depth_now,d)
# # width_full_small=cal_center(alpha,theta,depth_new)
# # width_full_small=result[1]
# # #模型假设：重叠率为百分之十
# con=sp.Eq(1-2*e/((width_full_small+width_full_big)*sp.cos(alpha)),0.11)
# result_d=sp.solve(con,e)
# count+=1
# print(result_d[e])


#第四问经过划分成四个区域之后，每个区域使用问题三中所讨论的模型求解
import sympy as sp
import numpy as np
#初始数据的赋值
theta = np.pi * (120 / 180)
def initiate(D1_high,D1_low,D2_high,D2_low,full_width,ns_width):
    alpha = sp.symbols('alpha')
    d1 = D1_high - D1_low
    d2 = D2_high - D2_low
    d_average = (d1 + d2) / 2
    d = full_width * 1852
    # low_average = (D1_low + D2_low) / 2
    high_average = (D1_high + D2_high) / 2
    con = sp.Eq(sp.tan(alpha), d_average / d)
    result = sp.solve(con, alpha)

    alpha = np.deg2rad(float(result[0]))
    depth_center = high_average - ((full_width / 2) * 1852) * np.tan(alpha)
    result=[depth_center,ns_width,alpha,full_width]
    return result

def cal_above(alpha,theta,D,d):
    x=D-d*sp.tan(alpha)
    width=(sp.sin(theta)/sp.sin(sp.pi/2-theta/2+alpha))*((sp.sin(sp.pi/2)*(x/2))/sp.sin(sp.pi/2-theta/2))+(sp.sin(theta)/sp.sin(sp.pi/2-theta/2-alpha))*((sp.sin(sp.pi/2)*(x/2))/sp.sin(sp.pi/2-theta/2))
    result=[x,width]
    return result
def cal_down(alpha,theta,D,d):
    x=D+d*sp.tan(alpha)
    width=(sp.sin(theta)/sp.sin(sp.pi/2-theta/2+alpha))*((sp.sin(sp.pi/2)*(x/2))/sp.sin(sp.pi/2-theta/2))+(sp.sin(theta)/sp.sin(sp.pi/2-theta/2-alpha))*((sp.sin(sp.pi/2)*(x/2))/sp.sin(sp.pi/2-theta/2))
    result=[x,width]
    return result
# 定义生成随机重叠率的函数
def random_overlap_rate():
    overlap_rate = np.random.uniform(0.1, 0.2)
    # 使重叠率在0.1到0.2随机取值
    return overlap_rate
def cal_num_lines(overlap_rate,alpha,full_width,depth_center,ns_width):
    full_length=(full_width)/np.cos(alpha)
    #假设坡度沿直线延申，可以按最深处和最浅处进行平均值
    result=cal_down(alpha,theta,depth_center,(full_width/2)*1852)
    width_east=result[1]
    result=cal_above(alpha,theta,depth_center,(full_width/2)*1852)
    width_west=result[1]
    width_average=(width_east+width_west)/2
    d = width_average*(1 - overlap_rate)
    #求出测线的条数，并在整数范围内向上取整
    # num_lines = (np.ceil(ns_width*1852/ d))

    num_lines=(ns_width*1852/d)
    print(num_lines)
    return num_lines
# print(cal_num_lines(random_overlap_rate()))

def monteCarlo(ns_width,full_width,alpha,depth_center):
    # #可以自行调整进行测试的次数，这里默认值设为1
    for i in range(1):
        # 循环次数为手动输入，可以通过调整循环次数来得到不同的结果。
        N = int(input("please input a number:"))

        # 定义一个空列表，用来存储重叠率和测线数量
        results = []

        # 循环N次
        for i in range(N):
            # 生成一个随机重叠率
            overlap_rate = random_overlap_rate()
            # 计算对应的测线数量
            num_lines = cal_num_lines(overlap_rate,alpha,full_width,depth_center,ns_width)
            # 将重叠率和测线数量存入列表中
            results.append((overlap_rate, num_lines))

        # 从列表中找出测线数量最小的那一对重叠率和测线数量
        min_result = min(results, key=lambda x: x[1])
        min_overlap_rate = min_result[0]
        min_num_lines = min_result[1]
        # 求出x,y坐标
        start_x = np.linspace(-(ns_width*1852) / 2, 0, min_num_lines)
        start_y = np.zeros(min_num_lines)
        line_direction = 0

        print("所需的测线数量: " + str(min_num_lines))
        print("最佳的重叠率: " + str(min_overlap_rate))
        print("每条测线的起始点坐标 (x坐标，y坐标): ")
        print(np.column_stack((start_x, start_y)))
        print("测线方向 (弧度): " + str(line_direction))

#左下部分
# result=initiate(91.77,24.40,65.89,55.41,2.72,3.8)
# depth_center=result[0]
# ns_width=result[1]
# alpha=result[2]
# full_width=result[3]
# overlap_rate=random_overlap_rate()
# num_lines=cal_num_lines(overlap_rate,alpha,full_width,depth_center,ns_width)
# # print(num_lines)
# monteCarlo(ns_width,full_width,alpha,depth_center)

#右下部分
# result=initiate(197.20,91.77,82.29,65.89,1.28,3.8)
# depth_center=result[0]
# ns_width=result[1]
# alpha=result[2]
# full_width=result[3]
# overlap_rate=random_overlap_rate()
# num_lines=cal_num_lines(overlap_rate,alpha,full_width,depth_center,ns_width)
# print(num_lines)
# monteCarlo(ns_width,full_width,alpha,depth_center)

#上二部分
# result=initiate(82.29,55.41,71.75,70.21,4,0.66)
# depth_center=result[0]
# ns_width=result[1]
# alpha=result[2]
# full_width=result[3]
# overlap_rate=random_overlap_rate()
# num_lines=cal_num_lines(overlap_rate,alpha,full_width,depth_center,ns_width)
# print(num_lines)
# monteCarlo(ns_width,full_width,alpha,depth_center)

#上一部分
result=initiate(84.40,65.20,71.71,70.21,4,0.54)
depth_center=result[0]
ns_width=result[1]
alpha=result[2]
full_width=result[3]
overlap_rate=random_overlap_rate()
num_lines=cal_num_lines(overlap_rate,alpha,full_width,depth_center,ns_width)
print(num_lines)
# monteCarlo(ns_width,full_width,alpha,depth_center)
