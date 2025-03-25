a=[10,20,33,44,55,60]

def ins_pos(arr: [int],ele):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]>=ele:
            lb=mid
            end=mid-1
        else:
            start=mid+1
    return lb

print(ins_pos(a,12))
print(ins_pos(a,22))

