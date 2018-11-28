#while
numbers = [12,37,5,42,8,3]
even =[]
odd = []
while len(numbers)>0:
    number = numbers.pop()
    if (number % 2 ==0):
        even.append(number)
    else:
        odd.append(number)
# while else
count = 0
while count < 0:
    print(count,"is less then 5")
    count = count + 1
else:
    print(count," is not less than 5")


#for 循环
for index in range(len(even)):
    print(even[index])

for index in range(len(odd)):
    print(odd[index])

fruits = ['apple','banana','mango']
for fruit in fruits:
    print(fruit)

for num in range(10,20):
    for i in range(2,num):
        if num % 1 == 0:
            j=num/i
            print('%d 等于 %d * %d' % (num, i, j))
            break
    else:
        print(num, '是一个质数')

