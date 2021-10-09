import math
num=int(input("请输入边："))
num1=int(input("请输入另一个边："))
num2=int(input("请输入最后一个边："))
num3=(num+num2+num1)/2
num4=math.sqrt(num3*(num3-num)*(num3-num1)*(num3-num2))
if num+num1>num2 and num1+num2>num and num+num2>num1:
    print("三角形的周长是："+str(num+num1+num2))
    print("三角形的面积是："+str(num4))
else:
    print("无法构建三角形")