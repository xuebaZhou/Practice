





#  lstrip()     语法：变量.lstrip()
# lstrip() 方法会将字符串中左侧空白部分删除。
str = "    hello world     "
# 结果："hello world     "
# 注意：引号内是结果，可以看到左侧空白部分已删除！
print(str.lstrip())



#    rstrip()   语法：变量.rstrip()
# rstrip() 方法会将字符串中右侧空白部分删除。
str = "    hello world     "
# 结果："    hello world"
# 注意：引号内是结果，可以看到右侧空白部分已删除！
print(str.rstrip())




#    strip()        语法：变量.strip()
# strip() 方法会将字符串中左右两侧空白部分删除。
str = "    hello world     "
# 结果："hello world"
print(str.strip())




#    find()         语法：变量.find(指定字符，开始下标，结束下标)
# 开始下标（即 6）与结束下标（即 11）可以默认不写，即从头查到尾
# 只写开始下标，不写结束下标时，就是从哪里开始一直到结尾。
# 如果在字符串(即 str)中找到了指定字符(即 l )，会返回指定字符在字符串中的下标，
# 没找到则返回 -1 ！
str = "hello world"
print(str.find("l", 6, 11))  # 结果为：9
print(str.find("l", 3))  # 结果为：3
print(str.find("l"))  # 结果为：2


#  rfind()     语法：变量.rfind(指定字符，开始下标，结束下标)
#   开始下标（即 3）与结束下标（即 11）可以默认不写，即从头查到尾
#   只写开始下标，不写结束下标时，就是从哪里开始一直到结尾。
#   如果在字符串(即 str)中找到了指定字符(即 l )，会返回指定字符在字符串中的下标，
#   没找到则返回 -1 ！
#   与 find() 方法不同的是，rfind() 方法是从右侧开始查找的！

str = "hello world"
print(str.rfind("l", 6, 11))  # 结果为：9
print(str.rfind("l", 3))  # 结果为：9
print(str.rfind("l"))  # 结果为：9













