b=[20,14,22,4,33,5]

def selectionsort(a):
    for i in range(len(a)):
        min_index=i
        for j in range(i+1,len(a)):
            if a[j] < a[min_index]:
                min_index=j
            a[i],a[min_index]=a[min_index],a[i]
    return a

print(selectionsort(b))
