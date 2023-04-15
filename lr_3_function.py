# 2. Функция для сортировки пузырьком bubble:
nums = [1, 2, 6, 4, 7, 5, 3,9]
def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
BubbleSort(nums)
print("Bubble:")
print(nums)

# 4. Функция сортировки выбором select:

nums = [1, 2, 6, 4, 7, 5, 3, 9]
def SelectSort(A):
    for i in range(len(A)-1):
        m = i
        for j in range(i, len(A)):
            if A[j] < A[m]:
               A[m], A[j] = A[j], A[m]
SelectSort(nums)
print("Select:")
print(nums)

#2. Функция сортировки вставками insert:
nums = [1, 2, 6, 4, 7, 5, 3, 9]
def InsertSort(A):
    for i in range(1, len(A), 1):
        t = A[i]
        j = i
        for j in range(j, 0, -1):
            if A[j-1] > t:
                A[j] = A[j - 1]
                j -= 1
            else:
                break
        A[j] = t
InsertSort(nums)
print("Insert:")
print(nums)

# Задача на рекурсию
# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
# на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

y = int(input("Length: "))
x = int(input("Width: "))

def recur(x, y, n):
    if y == x:
        print("It is the last square with the length")
        print(y)
        n += 1
        print("count:")
        print(n)
        return
    if x > y:
        print("square with length:")
        print(y)
        n += 1
        print("count:")
        print(n)
        return recur(x-y, y, n)
    else:
        print("square with length:")
        print(x)
        n += 1
        print("count:")
        print(n)
        return recur(x, y-x, n)

recur(x, y, 0)