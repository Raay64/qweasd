#coding: cp1251

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

my_list = [5, 2, 7, 1, 9]
sorted_list = bubble_sort(my_list)
print(sorted_list)

