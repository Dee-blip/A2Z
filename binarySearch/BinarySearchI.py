i=0
j=n-1

while i<=j:
    mid=i+(j-i)//2
    if nums[mid]==target:
        return mid
    elif nums[mid] >target:
        j=mid-1
    else:
        i=mid+1
return -1
