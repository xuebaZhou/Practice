#https://blog.csdn.net/qq_45856289/article/details/107631343?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168803492816800184156968%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168803492816800184156968&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-107631343-null-null.142^v88^control,239^v2^insert_chatgpt&utm_term=%E5%85%83%E7%BB%84&spm=1018.2226.3001.4187
# 元组的相关定义


#   元组与列表最大的区别就是元组不再是一种可变类型的数据结构

# singleton=1,    # 逗号表明该对象是一个元组
# ().a()       #   表示空元组
# b1=(9,)      #   表示b1为只有一个元素9的元组
# b2=(9)       #   表示b2为整数9

#  通过下标查找数据
tuple_data = (10, 20, 30)
# 结果：10
print(tuple_data[0])
# 结果：30
print(tuple_data[2])



#     index()
#     语法: 元祖数据.index(数据)
#     index方法在元祖中也是一样的查找数据并返回下标。  没有查找到数据时报错
tuple_data = (10, 20, 30)
# 结果：1
print(tuple_data.index(20))
# 结果：报错
# print(tuple_data.index(40))




#   count()
#   语法: 元祖数据.count(数据)
#   count方法返回数组在元祖中出现的总次数。
tuple_data = (10, 20, 30, 20, 20)
# 结果：3
print(tuple_data.count(20))
# 结果：1
print(tuple_data.count(10))



#  len()
#  语法 len(元组数据)
#  len 统计元祖中数据存在的个数
tuple_data = (10, 20, 30, 20, 20)
# 结果：5
print(len(tuple_data))

#    注意！！！   tuple元祖的数据不支持修改！


tuple_data = (10, 20, 30, ["weifei", "CSDN", "666"])
tuple_data[3][0] = "hello"
# 结果：(10,20,30,["hello","CSDN","666"])
print(tuple_data)
#  tuple_data[0] = 40
# 结果： 报错！ 'tuple' object does not support item assignment
# print(tuple_data)

#   PS   虽然元组数据不支持修改，但是元组中的列表数据是可以修改的。












#     https://blog.csdn.net/laobai1015/article/details/85160715
#     Python中字典（dict）的用法详解
#  dict字典
#  1、构造字典对象需要使用大括号表示，即{}.每一个字典元素都是以键值对的形式存在，即  key:value
#  2、键在字典中是唯一的，不能重复，对于字符型的键需要用引号引起来。
#  3、字典不再是序列，无法通过位置索引完成元素值的获取，只能通过键索引实现
#  4、字典是可变类型的数据结构
d={'name':"james",'age':33,"children":{'son':"kobe",'girl':"jordan"}}  #构造字典
print(d)
print(d['age'])
d['age']=35
print(d)
d['address']="常德"  #   新增元素
print(d)
d.pop("children")  # 删除元素
print(d)





#   set 集合
#  注意：  创建一个空集合必须使用set()而不是{},{}用来创建一个空字典的
#   在创建集合时如果有重复元素，Python会自动的删除重复元素的
#  集合的规范操作
a=set('abcde')  #  把字符串转为集合
print(a)      #  每次的输出是不一样的
b={1,2,2,2,3,5,6,6,'d'}
c=set(b)     #  转化为集合，去掉重复元素
print(list(c))  #  显示去掉重复元素列表
#print(a.difference(b))#   返回的集合元素包含在第一个集合中，但不包含在第二个集合中
#print(a.difference_update(b))   #  会出现None这一结果,
#   difference() 方法返回一个移除相同元素的新集合，这个有返回值的d
#   而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。导致需要先执行
#    a.difference_update(b)这一语句，才能用print打印到输出台上面去
#a.difference_update(b)
#print(a)

print(a.intersection(b))  #返回两个或者更多的集合中的相同的元素
#   https://zhuanlan.zhihu.com/p/141755563    Python集合17个方法详解
print(a.update(c))  #  会打印出None   a.update(c)没有返回值的，需要用变量来接收
#https://blog.csdn.net/Chihwei_Hsu/article/details/81416818     Python set 交集、并集、差集

x='12+23+34'
a=eval(x)
print(a)   #   eval函数会把字符串的内容作为对应的Python语句来执行


str1="I am a student"   #    默认以空格作为分隔符
list1=str1.split()
print(list1)
str2="1,2,3,4"          #   逗号作为分隔符
List2=str2.split(',')
print(List2)


List=['I','am','a','techer']
print(' '.join(List))
















































