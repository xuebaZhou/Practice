

#    replace()          语法：变量.replace(旧字符，新字符，替换次数)
#   该方法为替换，将字符串（即 str）中的旧字符（即 l）替换为新字符（即 h）。
#   替换次数（即 2）为替换多少次，替换次数小于旧字符在字符串中出现的次数时多余字符的不会进行替换！
#   替换次数大于旧字符在字符串中出现的次数时也是全部替换。
#   替换次数默认不写时替换全部。
str = "hello world"
print(str.replace("l", "h", 2))  # 结果：hehho world
print(str.replace("l", "h"))  # 结果：hehho worhd
print(str.replace("c", "h"))  # 结果：hello world




#    capitalize()    语法: 变量.capitalize()
# capitalize() 方法将字符串首字符大写，其他字符全部小写。
str1 = "hello World nihao james"
print(str1.capitalize())  # 结果：Hello world nihao james
str2 = "HELLO WORLD NIHAO JAMES"
print(str2.capitalize())  # 结果：Hello world nihao james



#     title() 语法：变量.title()
#     title() 方法会将字符串中的每一个单词首字母大写，其余字母小写。
str1 = "hello world"
str2 = "my name is weifei"
str3 = "hEllO wORld"
print(str1.title())  # 结果：Hello World
print(str2.title())  # 结果：My Name Is Weifei
print(str3.title())  # 结果：Hello World



