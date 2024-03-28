

# 语法: 变量.isalpha()
#  判断字符串中是不是只有字母。     是则返回True 否则返回False
str1='hello world'
str2="123"
str3="weifei123"
str4='KobeBryant'
print(str1.isalpha())   #False   中间有一个空格
print(str2.isalpha())   #False
print(str3.isalpha())   #False
print(str4.isalpha())   #True


# 语法: 变量.isdigit()
# 判断字符串中是不是只有数字。    是则返回True 否则返回False

str1='hello world'
str2="123"
str3="weifei123"
print(str1.isdigit())   #False
print(str2.isdigit())   #True
print(str3.isdigit())   #False


#  语法:  变量.isalnum()
#  判断字符串中是不是只有数字或字母或数字与字母的组合。  是则返回True 否则返回False.
str1="Jordan23"
str2="Kobe 24"
str3="James 23"
str4="123+456"
str5="congratulation!"
print(str1.isalnum())   #True
print(str2.isalnum())   #False
print(str3.isalnum())   #False
print(str4.isalnum())   #False
print(str5.isalnum())   #False


# 语法:   变量.isspace()
#  判断字符串中是不是只有空格。   是则返回True 否则返回False
str1 = "hello world"
str2 = "          "
str3 = "my name is weifei"
print(str1.isspace())  # 结果为：False
print(str2.isspace())  # 结果为：True
print(str3.isspace())  # 结果为：False



















