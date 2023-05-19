n=int(input())
a=list(map(int,input().split()))
ev=0
odd=0
for i in range(n):
    if(i%2==0):
        ev=ev+a[i]
    else:
        odd=odd+a[i]
dif=ev-odd
print(dif)