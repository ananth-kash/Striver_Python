a=[]
for i in range(0,40,8):
    a.append(i)

def upperbound(arr: [int], ele: int):
    start=0
    end=len(arr)-1
    uppbound=len(arr)
    while(start<=end):
        mid=(start+end)//2
        if(ele<=arr[mid]):
            uppbound=mid
            end = mid - 1
        else:
            start = mid + 1
    return uppbound


print(a)
print(upperbound(a,12))