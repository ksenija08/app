# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

a = [int(s) for s in input('Введите список целых чисел через пробел: ').split()]

def minimum(arr):
    min_arr = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_arr:
            min_arr = arr[i]
    return min_arr

def maximum(arr):
    max_arr = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_arr:
            max_arr = arr[i]
    return max_arr

print(f"{a} -> max = {maximum(a)}, min = {minimum(a)} ")