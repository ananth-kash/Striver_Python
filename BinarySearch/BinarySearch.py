import random
a=[54,33,55,42,323,3]
random.shuffle(a)

def binarysearch(arr,ele):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if(ele<arr[mid]):
            end=mid-1
        elif(ele>arr[mid]):
            start=mid+1
        else:
            return mid
    return -1

a.sort()
print(binarysearch(a,42))