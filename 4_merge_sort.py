

#Break lists in half recursively, base case (arrive at single element lists)
#Left and right half, both need to be broken
#break down left side first, once you manage then left deal with the right,

#Managing

#Merge the two lists merge-algo

#-- compare elements of each list, gradually draining both, until one is empty
#-- empty the list that still has elements

from re import L


def merge_sort(arr,key='title'): # Time Complexity O(n logn) Linear Logrithmic
    if len(arr) > 1:
        print(arr)
        mid = len(arr) // 2
        left_side = arr[:mid]
        print(left_side)
        right_side = arr[mid:]
        print(right_side)


        merge_sort(left_side)
        merge_sort(right_side)
        print(f'Merging {left_side} and {right_side}')

        #Merge Algorithm

        i = 0 # main
        j = 0 # left half
        k = 0 # right

        while j < len(left_side) and k < len(right_side):
            if left_side[j][key].lower() < right_side[k][key].lower():
                arr[i] = left_side[j]
                i += 1
                j += 1
            else:
                arr[i] = right_side[k]
                i += 1
                k += 1

        while j < len(left_side):
            arr[i] = left_side[j]
            i += 1
            j += 1
        
        while k < len(right_side):
            arr[i] = right_side[k]
            i += 1
            k += 1

        print(f'MERGED {arr}')
    else:
        print('BASE CASE')

alist = [3,1,5,2]

playlist = [
    {"title": "Terrible", "duration": 180, "upload_date": "2022-01-01"},
    {"title": "awful", "duration": 240, "upload_date": "2021-12-15"},
    {"title": "Pretty Rank", "duration": 200, "upload_date": "2022-01-10"},
]

# merge_sort(alist)
# print(alist)

merge_sort(playlist)
print('-'*50)
print(playlist)


    

