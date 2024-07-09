
#Linear Search: Time Complexity O(n) Linear


def linear_search(alist, target):
    for idx, item in enumerate(alist):
        if item == target:
            return idx
    return 'Target not Found'

stuff = [1,34,56,23,67,89,34]

print(linear_search(stuff, 56))

print(stuff.index(56))

