n = int(input())
l = 1
r = n/2
res = -1
while(l <= r):
    mid = int(l + ( r - l)/2)
    
    if mid * mid == n:
        res = mid
        break
    elif mid*mid < n:
        res = mid
        l = mid+1
        
    else:
        r = mid-1
        
print(f'SqureRoot of {n} is ',res)