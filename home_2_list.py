import numpy as np
import random
#home_2_list
#1.4 Вариант 4
#Найдите произведение элементов списка с нечетными номерами.
#Найдите наибольший элемент списка, затем удалите его и выведите новый список.
n = input('Введите длину списка: ')
A = []
m = 1
for i in range(int(n)):
    a = random.randint(0, 10)
    A.append(a)
print("Массив А: ")
for i in range(len(A)):
    print(A[i], end=' ')
for i in range(len(A)):
    if i % 2 != 0:
        m *= A[i]
print("\nПроизведение элементов списка с нечетными номерами: " + str(m))
max = max(A)
A.remove(max)
print ('Максимальный эдемент в списке: ' + str(max))
print ('Список после удаления макс элемента: ')
[print(i, end=' ') for i in A]

#2.3 3.	Даны две квадратных таблицы чисел.
# Требуется построить третью, каждый элемент которой равен сумме элементов,
# стоящих на том же месте в 1-й и 2-й таблицах.

A = np.array([[1, 2 , 3],[4, 5, 6],[7, 8, 9]])
B = np.array([[-1, 2 , -3],[4, -5, 6],[-7, 8, -9]])
C = A + B
print("\n")
print(C)