a=[20,14,22,4,33,5]
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]

print(a)