

#       lower()     语法：变量.lower()
#       lower() 方法会将字符串中所有的大写字母转为小写。即大写转小写
str1 = "HELLO WORLD"
str2 = "My Name Is WeiFei"
print(str1.lower())  # 结果：hello world
print(str2.lower())  # 结果：my name is weifei


#      upper()      语法：变量.upper()
#      upper方法会将字符串的所有的字母字符转为小写。即小写转大写
str1 = "hello world"
str2 = "my name is weifei"
print(str1.upper())  # 结果：HELLO WORLD
print(str2.upper())  # 结果：MY NAME IS WEIFEI



#   join()    语法：指定字符.join(序列)
#  将序列（也就是字符串、元组、列表、字典）中的元素以指定的字符连接生成一个新的字符串.
str1 = "wei"
str2 = "666"
new_str = str2.join(str1)
new_str2=str1.join(str2)
print(new_str2)
print(new_str)  # 结果：6wei6wei6
str3 = ["I", "love", "you"]     #  w666e666i
print("-".join(str3))   #   结果：I-love-you
print("=0".join(str1))  #   w=0e=0i
print("*".join(str3))   #   结果：I*love*you



#  ljust()    语法：变量.ljust(长度，填充字符)
#  ljust 左对齐。
#  长度（即 15）如果大于字符串（即str）总长度时，缺少的字符由填充字符（即 -）进行向右填充
#  长度如果小于字符串总长度时，输出原来的字符串，更不会进行填充。
str = "hello world"
print(str.ljust(15, "-"))  # 结果：hello world----
print(str.ljust(8, "-"))  # 结果：hello world
# 结果：报错 The fill character must be exactly one character long
# 即  填充字符长度必须正好为一个字符
#   print(str.ljust(15, "**"))


#   rjust()         语法：变量.rjust(长度，填充字符)
#   rjust 右对齐。
#   长度（即 15）如果大于字符串（即str）总长度时，缺少的字符由填充字符（即 -）进行向左填充
#   长度如果小于字符串总长度时，输出原来的字符串，更不会进行填充。
str = "hello world"
print(str.rjust(15, "-"))  # 结果：----hello world
print(str.rjust(8, "-"))  # 结果：hello world
# 结果：报错 The fill character must be exactly one character long
# 即  填充字符长度必须正好为一个字符
#  print(str.rjust(15, "**"))


#   center()        语法：变量.center(长度，填充字符)
#   center 居中对齐。
#   长度（即 15）如果大于字符串（即str）总长度时，缺少的字符由填充字符（即 -）进行向左右两侧向内填充
#   长度如果小于字符串总长度时，输出原来的字符串，更不会进行填充。
str = "hello world"
print(str.center(15, "-"))  # 结果：--hello world--
print(str.center(8, "-"))  # 结果：hello world
# 结果：报错 The fill character must be exactly one character long
# 即  填充字符长度必须正好为一个字符
#   print(str.center(15, "**"))





