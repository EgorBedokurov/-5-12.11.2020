import random

some_list = [random.randint(1, 10) for i in range(10)]
print(some_list)
some_list1 = []
for i in some_list:
    if i % 2 ==0:
        some_list1.append(i)
    else:
        some_list1.append(0)

print(some_list1)
print('количество нечетных элементов составляло - ', some_list1.count(0), 'шт.')