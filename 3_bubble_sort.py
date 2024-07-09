

def bubble_sort(arr): #O(n^2)
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #swapping values from current to next and vice-versa
    return arr

lst = [12,45,3,24,78,45,67,2]

bubble_sort(lst)