def isprime(a):
    s=0
    for i in range(1,a+1):
        if(a%i==0):
            s=s+1
    return s

n=int(input())
cnt=0
for i in range(1,n+1):
    if(n%i==0 and isprime(i)!=2):
        cnt=cnt+1
print(cnt)
    