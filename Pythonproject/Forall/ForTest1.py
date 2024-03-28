
# # 利用for输出列表（包括元素集合）
# A=[1,2,3,4,5]
# for i in A:             # 若元素i在列表A里
#     print(i)
#
# # 利用for输出数字
# for i in range(9,16):  # 若元素i在9-16之内，不等于16
#     print(i)
#
# # 利用for输出字符串
# for i in 'fdhkjh hbj j':  #若字符i在字符串内       此时在打印台输出时  若字符串有空格，这输出时空格占一行
#     print(i)
#
#
# # for 和 else组合使用
# for i in [0,1]:    #若i在【0,1】里
#     print(i)       # 输出 i
# else:              # 否则
#     print(None)     #输出 None


# continue跳过当前的循环，执行下个循环
for i in range(5):
    if i==3:
        continue
    else:
        print("第%d次"%i)
