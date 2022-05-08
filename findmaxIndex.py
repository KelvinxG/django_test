
lists=[1,2,1,3,5,6,4]



__max=lists[0]

for x in lists:
    if x>__max:
        __max=x
print("the highest value(index):",lists.index(__max))