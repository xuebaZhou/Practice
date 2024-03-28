import geopandas as gpd
import matplotlib.pyplot as plt

# 读取世界地图数据
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


# 定义社会主义国家列表，这里只是举例，你可以根据实际情况修改
socialist_countries = ['China', 'Cuba', 'Vietnam', 'North Korea']

# 将社会主义国家的几何形状提取出来
socialist = world[world['name'].isin(socialist_countries)]

# 绘制世界地图
world.plot()

# 绘制社会主义国家，颜色设置为蓝色
socialist.plot(color='blue')

# 显示图形
plt.show()


# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap
#
# map=Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180)
#
# map.drawcoastlines()
#
# map.drawcountries()
#
# map.drawstates()
#
# map.drawmeridians(range(-180,180,30),labels=[0,0,0,1])
# map.drawparallels(range(-90,90,30),labels=[1,0,0,0])
#
# # 添加标题
# plt.title('World Map')
#
# # 显示地图
# plt.show()
