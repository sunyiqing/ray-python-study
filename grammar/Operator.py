#算术运算符
a = 12
b = 10
c = 0

c = a + b
print ("c的值",c)
c = a - b
print ("c的值",c)
c = a * b
print ("c的值",c)
c = a/b
print ("c的值",c)
c = a%b
print ("c的值",c)
a = 2
b = 3
c = a**b
print ("c的值",c)

a = 10
b = 5
c = a//b
print ("c的值",c)

# 成员运算符
b = 20
a = 10
list = [1,2,3,4,5]
if a in list:
    print("在")
else:
    print("不在")

if b not in list:
    print("不在")
else:
    print("在")

#身份运算符
a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (a is not b):
    print("2 - a 和 b 没有相同的标识")

else:
    print("2 - a 和 b 有相同的标识")


# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")


if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

