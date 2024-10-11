def getFloorAndCeil(a, n, x):
    low=0
    high=n-1
    floor,ceil=-1,-1

    while low<=high:
        mid = (low+high)//2

        if a[mid]==x:
            return a[mid], a[mid]
        if a[mid]<x:
            low=mid + 1
            floor = a[mid]
        else:
            high=mid-1
            ceil = a[mid]

    return floor,ceil
