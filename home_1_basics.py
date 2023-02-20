import numpy
import random
#1.10 Число делится на 3 тогда, когда сумма его цифр делится на 3.
#Проверить этот признак на примере заданного трехзначного числа.
#number from 100 to 999
n = input("Введите трехзначное число: ")
#из стоки извлекаем значения
a = int(n[0])
b = int(n[1])
c = int(n[2])
#проверяем равен ли остаток от деления на 3 нулю
if ((a + b + c) % 3 == 0):
    print("Вы ввели " + n + "\nЧисло делится на 3, так как \n" +
          "Сумма цифр числа " + n + " делится на 3")
else:
    print("Число " + n + " не делится на три")

#2.7 Составить алгоритм решения ребуса КОТ + КОТ = ТОК
#(различные буквы означают различные цифры, старшая буква ‒ не 0).

k=1
o=0
t=0
for k in range(1,10):
    for o in range(0,10):
        for t in range(0,10):
            if ((k*100+o*10+t) + (k*100+o*10+t)) == (t*100+o*10+k):
                print('\nЧисла:')
                print('k = ' + str(k))
                print('o = ' + str(o))
                print('t = ' + str(t))
                break
else:
    print('\nНет решения')


#3.15 Удалить элементы, индексы которых кратны 3.

n = input('Введите длину списка: ')
A = []
B = []
for i in range(int(n)):
    a = random.randint(0, 100)
    A.append(a)
print("Массив А: ")
for i in range(len(A)):
    print(A[i])
for i in range(len(A)):
    if i % 3 != 0:
        B.append(A[i])

print("Массив B: ")
for i in range(len(B)):
    print(B[i])
