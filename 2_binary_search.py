
def binary_search(alist, target): #requires that the list is sorted
    low = 0
    high = len(alist) - 1

    while low <= high:
        mid = (low + high) // 2
        if alist[mid] == target:
            return f'Found my target at index:{mid}'
        elif alist[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return 'Target not found'

stuff = [1,34,56,23,67,89,34]
stuff.sort()
print(stuff)

print(binary_search(stuff, 56))

#Time complexity O(logn) Logrithmic