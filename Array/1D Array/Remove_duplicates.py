a=[10,20,22,33,33,33,55,55,3053]
print(a)

def rem_duplicate(arr: [int]):
    i=0
    for j in range(1,len(arr)):
        if (arr[i]!=arr[j]):
            i+=1
            a[i]=a[j]
    return i+1

k=rem_duplicate(a)
b=[]
for i in range(k):
    b.append(a[i])


print(b)



