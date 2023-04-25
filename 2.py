from random import randint
list_1 = list(randint(1,10) for i in range (int(input('Введите количество кустов: '))) )
print(list_1)
a = int(input('Введите номер куста: '))
sum=0
if a ==1:
    sum =list_1[-1]+list_1[0]+list_1[1]
elif a == len(list_1):
    sum= list_1[-2]+list_1[-1]+list_1[0]
else:
    sum = list_1[a-2]+list_1[a-1]+list_1[a]
print(f'{sum} ягод')