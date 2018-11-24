#字符串
str = 'Hello world'
print(str)
print(str[1:2])
print(str[0])
print(str[2:])
print(str * 2)
print(str + "TEST")

print('---------------------------')
#可变列表
list = ['runoob',123,2.23,'john',70.2]
tinyList = [123,'111']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinyList*2)
print(list+tinyList)

print("-------------------")
#不可变列表
tuple = ('runboo',8789,2.2)
tinyTuple =(123,'join')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinyTuple * 2)
print(tuple + tinyTuple)

'''
测试列表可变性以及元组的不可变性
'''
list[2] = 'syq'
# TypeError: 'tuple' object does not support item assignment
tuple[2] = '121'

#字典
dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"

tinyDict = {'name':'john','code':6734}
print(dict)
print(dict[2])
print(dict['one'])
print(tinyDict)
print(tinyDict['name'])
print(tinyDict.keys())
print(tinyDict.values())