
#  https://blog.csdn.net/weifei20001217/category_12149993.html

#  语法：变量.startswith(指定字符，开始下标，结束下标)
#  判断字符串是不是以指定字符为开始，开始下标与结束下标均不写时默认从头开始。
#  当有开始下标时，从开始下标开始进行判断。

str = "hello world"
print(str.startswith("llo", 2, 5))  # 结果为：True
print(str.startswith("llo", 2, 4))  # 结果为：False
print(str.startswith("hello"))  # 结果为：True
print(str.startswith("h"))  # 结果为：True
print(str.startswith("llo"))  # 结果为：False
print(str.startswith("hell",0,10))   # 结果为:True


#语法：变量.endswith(指定字符，开始下标，结束下标)
#判断字符串是不是以指定字符为结尾，开始下标，与结束下标不写时默认从头开始。
#当有结束下标时，从结束下标开始进行判断。
a = "hello world"
print(a.endswith("world"))  # 结果为：True
print(a.endswith("ld"))  # 结果为：True
print(a.endswith("l", 0, 10))  # 结果为：True    这个地方  10取不到，指向下标为9的'l'，就是’l‘
print(a.endswith('r',1,9))      # 结果为: True   不管开始下标是多少，只要小于结束下标，结束下标就是判断的字符
print(a.endswith('d',10,11))    # True
print(a.endswith('d',11,11))    # False





