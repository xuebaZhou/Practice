

#  index      语法：  列表序列.index(数据，开始下标，结束下标)
#默认不写开始下标与结束下标时，查找整个 list 列表。
#如果查找的数据不存在则报错！  返回数据在 list 列表中的下标位置。
list = ["1", "2", "hello", "world", "weifei"]
# 结果：'hello' is not in list , 查找不到会报错！
#print(list.index("hello", 0, 1))
print(list.index("hello", 2))   # 结果：2
print(list.index("hello"))     # 结果：2
print(list.index("1",0,2))      # 0

#  count      语法：列表序列.count(数据)
#count 方法返回数据在 list 列表中存在的总数量。
#注意： 总数量跟下标不同，从1开始，并不是从0，有多少个就是多少个。
list =['1','2',"hello","world",'1','weifei','1']
print(list.count("1"))   #     3
print(list.count('hello'))  #   1
print(list.count("weifei  "))  #  0

# len       语法：len(列表序列)
list=['1','2','hello','world',"1",'weifei','1']
print(len(list))        #  7
list1=['1','2','3']
print(len(list1))       #  3
list2=['A','B','C','D']
print(len(list2))       #  4

#  in 与  not in
#         in ----- 指定数据 in 列表序列
#         not in ------  指定数据 not in 列表序列

list=['1','2','hello','world','1','weifei','1']
print("hello" in list)      #True
print("wei" in list)        #False
print('1' in list)          #True
print('1' not in list)      #False
print('i' not in list)      #True
print("weife" not in list)  #True

#   append      语法：列表序列.append(指定数据)
#   append      方法向列表序列末尾添加指定数据。
#   列表追加数据的时候，直接在原列表里面追加了指定数据，即修改了原列表，故列表为可变数据类型。
#   注意：如果append()追加的数据是一个序列，则追加整个序列到列表。
list = ["2", 2, "hello"]
list.append("world")
# 结果：["2",2,"hello","world"]
print(list)
list.append("weifei")
# 结果：["2",2,"hello","world","weifei"]
print(list)
list.append(["你好", "你说得对，但是原神"])
# 结果：["2",2,"hello","world","weifei",["你好","你说得对，但是原神"]]
print(list)

#  extend()    语法：列表序列.extend(数据)
#  extend 方法在列表末尾添加数据，如果该数据是一个序列，则将这个序列的数据进行逐一添加到列表。
list =['wei','fei']
list.extend('CSDN')
print(list)         #['wei', 'fei', 'C', 'S', 'D', 'N']
list.extend(["CSDN",'666'])
print(list)

# insert()    语法：列表序列.insert(位置下标，数据)
# insert 方法向列表序列指定下标位置添加数据。
list=['1','2','CSDN']
list.insert(1,"weifei")
print(list)             #    ['1', 'weifei', '2', 'CSDN']
list.insert(2,'666')    #    ['1', 'weifei', '666', '2', 'CSDN']
print(list)

#  del   语法 ： del 目标
#  del 可以删除整个数据也可以删除指定数据。
#  删除指定数据时需要在列表序列后面添加需要删除的下标位置。
list = ["weifei", "CSDN", "66666"]
# 结果：["weifei","CSDN","66666"]
print(list)
del list[2]
# 结果：["weifei","CSDN"]
print(list)
del list
print(list)     #     <class 'list'>

list1=['a','b','c','d','e']
# del list1[5]         会报错
# print(list1)          IndexError: list assignment index out of range


#   pop()      语法：列表序列.pop(下标)
#   pop 方法删除指定下标数据，默认为删除最后一个。
list = ["weifei", "CSDN", "66666", "233"]
list.pop()
# 结果：["weifei","CSDN","66666"]
print(list)
list.pop(0)
# 结果：["CSDN","66666"]
print(list)


#   remove()    语法： 列表序列.remove(数据)
#   remove 方法移除列表序列中匹配到的第一个数据项。
list = ["666", "weifei", "CSDN", "666", "233", "666"]
list.remove("666")
# 结果：["weifei","CSDN","666","233","666"]    把第一个'666'移除了
print(list)
#    list.remove('wei')     会报错：ValueError: list.remove(x): x not in list
print(list)


#   clear()    语法：列表序列.clear()
#   clear 方法，清空列表序列中的所有数据，即清空列表。
list = ["666", "weifei", "CSDN", "666", "233", "666"]
list.clear()
# 结果：[]
print(list)


#    修改序列列表指定位置      语法：序列列表[下标] = 数据
#    该方法通过下标来获取到当前数据，并通过 = 重新赋值的方法来达到修改列表指定位置的效果。
list = ["666", "weifei", "CSDN", "666", "233", "666"]
list[0] = "你好"
# 结果：["你好","weifei","CSDN","666","233","666"]
print(list)


#     reverse()       语法：序列列表.reverse()
#     reverse 方法会将列表数据进行逆置，即反转数据。
list = ["1", "2", "3", "4", "5", "6"]
list.reverse()
# 结果： ["6","5","4","3","2","1"]
print(list)


#  sort()      语法：列表序列.sort(key=None,reverse=False)
#   sort 方法会将列表进行排序。  reverse表示排序规则，reverse=True降序，reverse=Flase升序（默认）
list = ["1", "8", "3", "2", "6"]
list.sort()
# 结果：["1","2","3","6","8"]
print(list)
list.sort(reverse=True)
# 结果：['8', '6', '3', '2', '1']
print(list)


#   copy()          语法：序列列表.copy()
#   copy            方法会将列表进行复制并返回一个一模一样的列表。
list1 = ["weifei", "CSDN", "666", "233"]
list2 = list1.copy()
# 结果： ["weifei","CSDN","666","233"]
print(list2)




#     while 和 for 循环 list 序列列表
list = ["CSDN", "weifei", "hello", "world"]
i = 0
while i < len(list):
    print(list[i])
    i += 1

list = ["CSDN", "weifei", "hello", "world"]
for i in list:
    print(i)

b=[7,6,5]
print(b*3)#   输出[7, 6, 5, 7, 6, 5, 7, 6, 5]











































