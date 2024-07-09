
alist = [3,2,756,23,46]

print(id(alist))

print(alist.sort()) #in-place modifying the original list

print(id(alist))
print('CLIST BELOW')


blist = [3,2,756,23,46]

print(blist)

clist = sorted(blist) #out-of-place not changing original values

print(blist)
print(clist)
