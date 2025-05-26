def binar(arr,targ):
    left, right = 0, len(arr)-1 
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == targ:
            return mid
        elif arr[mid] < targ:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    
arr = [2,3,5,6,7,8,10]

targ = 11

print(binar(arr,targ))
