import math
n = int(input())
flag = 0
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        flag = 1
        break
    
if flag == 1 :
    print('It is not a Prime number')
else:
    print('It is a prime number')