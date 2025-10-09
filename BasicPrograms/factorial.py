n = int(input())
sum = 1
for i in range(n):
    sum*=i+1
    
print(f'Fact of {n} is', sum)