

#    split()       语法：变量.split(切割字符，切割次数)
#    split() 方法将字符串（即 str）切割为list类型的数据。
#   在字符串中找到切割字符（即 l）进行切割，切割次数（即 2）可以限制进行切割的次数！
#   默认不写切割次数时切割整个字符串中切割字符出现的次数。

str = "hello world"
print(str.split("l", 2))  # 结果：["he","","o world"]
print(str.split("l"))  # 结果：["he","","o wor","d"]

#   count()          语法：变量.count(指定字符，开始下标，结束下标)
#   count() 方法返回的是指定字符（即 l）在字符串（即 str）中出现的总次数！
#   没有在字符串中找到指定字符时返回 0


str = "hello world"
print(str.count("l", 5, 11))  # 结果为：1
print(str.count("l", 3))  # 结果为：2
print(str.count("l"))  # 结果为：3
print(str.count("c"))  # 结果为：0



#  index()    语法：变量.index(指定字符，开始下标，结束下标)
#  开始下标（即 5）与结束下标（即 11）可以不写，默认为从头到尾查找。
# 有开始下标与结束下标时查找的是这个开始于结束的字符串区间。
# 当在字符串（即 str）中查找到指定字符（即 l）时返回指定字符在字符串中的下标位置。
# 如果没在字符串中查找到指定字符时会报错！！
# substring not found


str = "hello world"
print(str.index("l", 5, 11))  # 结果：9
print(str.index("l", 3))  # 结果为：3
print(str.index("l"))  # 结果为：2
#  print(str.index("c"))  # 结果： 报错！！！


#  rindex()         语法：变量.rindex(指定字符，开始下标，结束下标)
#  从右边开始查找指定字符（即 l）返回指定字符在字符串（即 str）中的下标。
# 开始下标（即 5）与结束下标（即 11）可以不写，默认查找整个字符串。
# 有开始下标与结束下标时查找的是这个开始于结束的字符串区间。
# 当在字符串（即 str）中查找到指定字符（即 l）时返回指定字符在字符串中的下标位置。
# 如果没在字符串中查找到指定字符时会报错！！
# substring not found

str = "hello world"
print(str.rindex("l", 5, 11))  # 结果：9
print(str.rindex("l", 3))  # 结果为：9
print(str.rindex("l"))  # 结果为：9
#  print(str.rindex("c"))  # 结果： 报错！！！

